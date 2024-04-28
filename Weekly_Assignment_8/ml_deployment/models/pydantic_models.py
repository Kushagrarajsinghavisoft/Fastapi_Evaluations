from pydantic import BaseModel

# Define request body model
class InputFeatures(BaseModel):
    Income: float
    Recency: float
    MntWines: float
    MntFruits: float
    MntMeatProducts: float
    MntGoldProds: float
    NumWebPurchases: float
    NumCatalogPurchases: float
    AcceptedCmp3: float
    AcceptedCmp4: float
    AcceptedCmp5: float
    AcceptedCmp1: float
    AcceptedCmp2: float
