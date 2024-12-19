def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def preprocess_data(data):
    # Implement preprocessing steps such as handling missing values, normalization, etc.
    return data

def extract_features(data):
    # Implement feature extraction logic
    return data

def split_data(data, target_column, test_size=0.2):
    from sklearn.model_selection import train_test_split
    X = data.drop(columns=[target_column])
    y = data[target_column]
    return train_test_split(X, y, test_size=test_size, random_state=42)

def evaluate_model(model, X_test, y_test):
    from sklearn.metrics import mean_squared_error, r2_score
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    return mse, r2