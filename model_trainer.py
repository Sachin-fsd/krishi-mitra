import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

class YieldPredictor:
    def __init__(self):
        self.model = None
        self.label_encoders = {}
        
    def load_data(self, file_path='./data/crop_yield_train.csv'):
        """Load and preprocess the dataset"""
        try:
            
            df = pd.read_csv(file_path)
            
            
            df.columns = df.columns.str.strip()
            
            
            df = df.dropna()
            
            return df
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return None
    
    def preprocess_data(self, df):
        """Preprocess the data for training"""
        try:
            
            df_processed = df.copy()
            
            
            categorical_cols = ['Crop', 'Season', 'State', 'District']
            for col in categorical_cols:
                if col in df_processed.columns:
                    le = LabelEncoder()
                    df_processed[col] = le.fit_transform(df_processed[col])
                    self.label_encoders[col] = le
            
            return df_processed
        except Exception as e:
            print(f"Error preprocessing data: {str(e)}")
            return None
    
    def train_model(self, df):
        """Train the model"""
        try:
            
            df_processed = self.preprocess_data(df)
            if df_processed is None:
                return False
            
            
            X = df_processed.drop(['Yield'], axis=1)
            y = df_processed['Yield']
            
            
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            
            self.model = RandomForestRegressor(
                n_estimators=100,
                max_depth=10,
                random_state=42
            )
            self.model.fit(X_train, y_train)
            
            
            y_pred = self.model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            
            print(f"Model Evaluation:")
            print(f"Mean Squared Error: {mse:.2f}")
            print(f"R2 Score: {r2:.2f}")
            
            return True
        except Exception as e:
            print(f"Error training model: {str(e)}")
            return False
    
    def save_model(self):
        """Save the model and encoders"""
        try:
            
            joblib.dump(self.model, './models/crop_yield_model.pkl')
            
            
            joblib.dump(self.label_encoders, 'label_encoders.pkl')
            
            print("Model and encoders saved successfully")
            return True
        except Exception as e:
            print(f"Error saving model: {str(e)}")
            return False
    
    def load_model(self):
        """Load the saved model and encoders"""
        try:
            self.model = joblib.load('./models/crop_yield_model.pkl')
            self.label_encoders = joblib.load('./models/label_encoders.pkl')
            return True
        except Exception as e:
            print(f"Error loading model: {str(e)}")
            return False

def main():
    
    predictor = YieldPredictor()
    
    
    df = predictor.load_data()
    if df is None:
        return
    
    
    if predictor.train_model(df):
        
        predictor.save_model()
        print("Model training and saving completed successfully")
    else:
        print("Model training failed")

if __name__ == "__main__":
    main() 
    