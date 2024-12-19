from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd

class StockPredictionModel:
    def __init__(self, data_path):
        self.data_path = data_path
        self.model = RandomForestRegressor()
        self.X_train, self.X_test, self.y_train, self.y_test = None, None, None, None

    def load_data(self):
        data = pd.read_csv(self.data_path)
        # Assuming the last column is the target variable
        X = data.iloc[:, :-1]
        y = data.iloc[:, -1]
        return X, y

    def preprocess_data(self, X, y):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    def train(self):
        self.model.fit(self.X_train, self.y_train)

    def predict(self, X):
        return self.model.predict(X)

    def evaluate(self):
        predictions = self.predict(self.X_test)
        mse = mean_squared_error(self.y_test, predictions)
        return mse

    def run(self):
        X, y = self.load_data()
        self.preprocess_data(X, y)
        self.train()
        mse = self.evaluate()
        print(f'Model Mean Squared Error: {mse}')