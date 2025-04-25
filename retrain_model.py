import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import pickle
import warnings
warnings.filterwarnings('ignore')


print("Loading dataset...")
df = pd.read_csv('./data/crop_yield_train.csv')


df.columns = df.columns.str.strip()


print("\nAvailable columns in dataset:")
print(df.columns.tolist())


features = ['State', 'District', 'Crop', 'Crop_Year', 'Season', 'Area', 'Production']
target = 'Yield'



numerical_cols = ['Area', 'Production', 'Yield', 'Crop_Year']
for col in numerical_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
    df[col] = df[col].fillna(df[col].median())


categorical_cols = ['State', 'District', 'Crop', 'Season']
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])


label_encoders = {}
for column in categorical_cols:
    label_encoders[column] = LabelEncoder()
    df[column] = label_encoders[column].fit_transform(df[column].astype(str))


df['Calculated_Yield'] = df['Production'] / df['Area']


X = df[features]
y = df[target]  


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


print("\nTraining model...")
model = RandomForestRegressor(
    n_estimators=100,  
    max_depth=15,      
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation Metrics:")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"R-squared (R²) Score: {r2:.2f}")


calculated_yield = X_test['Production'] / X_test['Area']
calculated_mse = mean_squared_error(y_test, calculated_yield)
calculated_rmse = np.sqrt(calculated_mse)
calculated_mae = mean_absolute_error(y_test, calculated_yield)
calculated_r2 = r2_score(y_test, calculated_yield)

print("\nCalculated Yield (Production/Area) Metrics:")
print(f"Mean Squared Error (MSE): {calculated_mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {calculated_rmse:.2f}")
print(f"Mean Absolute Error (MAE): {calculated_mae:.2f}")
print(f"R-squared (R²) Score: {calculated_r2:.2f}")


feature_importance = pd.DataFrame({
    'Feature': features,
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=False)

print("\nFeature Importance:")
print(feature_importance)


print("\nSaving model and encoders...")
with open('./models/crop_yield_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('label_encoders.pkl', 'wb') as f:
    pickle.dump(label_encoders, f)

print("\nModel training completed successfully!")
print(f"Features used: {features}") 