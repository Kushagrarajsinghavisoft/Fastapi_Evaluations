from fastapi import FastAPI
from mongoengine import connect

from ml_deployment.utils.v1.file_loader import model, scaler
from ml_deployment.models.pydantic_models import InputFeatures
from ml_deployment.config.v1.database_config import mongo_config
from ml_deployment.models.mongo_data import InputFeaturesDocument
from ml_deployment.utils.v1.preprocessing_features import helper_scale_input_features

# Define FastAPI app
app = FastAPI()

# Endpoint to handle predictions
@app.post("/predict/")
async def predict(features: InputFeatures):
    # Convert input features to numpy array
    scaled_inputs = helper_scale_input_features([
        features.Income, features.Recency, features.MntWines, features.MntFruits, features.MntMeatProducts,
        features.MntGoldProds, features.NumWebPurchases, features.NumCatalogPurchases, features.AcceptedCmp3,
        features.AcceptedCmp4, features.AcceptedCmp5, features.AcceptedCmp1, features.AcceptedCmp2
    ], scaler)
    
    
    # Make predictions using the trained model
    prediction = model.predict(scaled_inputs)
    prediction = int(prediction[0])

    if prediction==0:
        prediction = "Offer Denied"
    else:
        prediction = "Offer Accepted"


    # Save input features to MongoDB
    input_features_document = InputFeaturesDocument(
        Income= features.Income,
        Recency= features.Recency,
        MntWines= features.MntWines,
        MntFruits= features.MntFruits,
        MntMeatProducts= features.MntMeatProducts,
        MntGoldProds= features.MntGoldProds,
        NumWebPurchases= features.NumWebPurchases,
        NumCatalogPurchases= features.NumCatalogPurchases,
        AcceptedCmp3= features.AcceptedCmp3,
        AcceptedCmp4= features.AcceptedCmp4,
        AcceptedCmp5= features.AcceptedCmp5,
        AcceptedCmp1= features.AcceptedCmp1,
        AcceptedCmp2= features.AcceptedCmp2,
        prediction = prediction
        
    )
    input_features_document.save()

    return {'prediction': prediction}

@app.get("/health")
async def health():
    return {"status": "ok"}


# Define MongoDB connection settings
port=27017
host="localhost"
db_name="Customer_personality_prediction_db"

# Connect to MongoDB
# connect(db=db_name, host=f'mongodb://{host}:{port}')
connect(db=db_name, host=f'mongodb://{mongo_config.mongo_host}:{port}')
