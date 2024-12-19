# FILE: /stock-prediction-app/stock-prediction-app/src/config.py
# This file holds configuration settings such as file paths, model parameters, and any other constants required for the application.

import os

# File paths
DATA_FILE_PATH = os.path.join('data', 'stock_data.csv')
MODEL_SAVE_PATH = os.path.join('models', 'stock_model.pkl')

# Model parameters
MODEL_TYPE = 'RandomForest'  # Example model type
N_ESTIMATORS = 100  # Number of trees in the forest
RANDOM_STATE = 42  # Seed for reproducibility

# Other constants
TEST_SIZE = 0.2  # Proportion of the dataset to include in the test split
EPOCHS = 50  # Number of epochs for training (if applicable)
BATCH_SIZE = 32  # Batch size for training (if applicable)