import pickle

trained_model_path = 'ml_deployment/datafiles/svc_model_file.pkl'
scaler_path = 'ml_deployment/datafiles/scaler_file.pkl'

# Load the trained model from the pickle file
with open(trained_model_path, 'rb') as f:
    model = pickle.load(f)

# Load the scaler from the pickle file
with open(scaler_path, 'rb') as f:
    scaler = pickle.load(f)