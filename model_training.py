# model_training.py
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer

# -------------------------------
# Load dataset
# -------------------------------
df = pd.read_csv('Bengaluru_House_Data.csv')

# Drop rows with missing target or total_sqft
df = df.dropna(subset=['total_sqft', 'price'])

# -------------------------------
# Convert total_sqft to numeric
# -------------------------------
def convert_sqft(x):
    try:
        x = str(x)
        if '-' in x:  # range like "1200 - 1500"
            tokens = x.split('-')
            return (float(tokens[0].strip()) + float(tokens[1].strip())) / 2
        if 'Sq. Yards' in x:
            return float(x.replace('Sq. Yards','').strip()) * 9
        if 'Acres' in x:
            return float(x.replace('Acres','').strip()) * 43560
        return float(x)
    except:
        return None

df['total_sqft'] = df['total_sqft'].apply(convert_sqft)
df = df.dropna(subset=['total_sqft'])

# -------------------------------
# Extract BHK from size
# -------------------------------
def extract_bhk(size_str):
    try:
        return int(size_str.split()[0])
    except:
        return 0

df['bhk'] = df['size'].apply(extract_bhk)

# -------------------------------
# Show dataset info
# -------------------------------
print("✅ Bengaluru House dataset loaded and cleaned!")
print("Shape:", df.shape)
print("\n--- First 5 rows ---")
print(df.head())

print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Statistical Summary ---")
print(df.describe())

# -------------------------------
# Features and target
# -------------------------------
X = df.drop(['price', 'size'], axis=1)
y = df['price']

# -------------------------------
# Define numeric and categorical features
# -------------------------------
numerical_features = ['total_sqft', 'bath', 'balcony', 'bhk']
categorical_features = ['area_type', 'availability', 'location', 'society']

# -------------------------------
# Preprocessing pipeline with imputation
# -------------------------------
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='Unknown')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer([
    ('num', numeric_transformer, numerical_features),
    ('cat', categorical_transformer, categorical_features)
])

# -------------------------------
# Full pipeline
# -------------------------------
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', RandomForestRegressor(n_estimators=200, max_depth=20, random_state=42))
])

# -------------------------------
# Train/Test split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -------------------------------
# Train model
# -------------------------------
pipeline.fit(X_train, y_train)

# -------------------------------
# Evaluate
# -------------------------------
r2 = pipeline.score(X_test, y_test)
print(f"\n🎯 Model trained! R² Score: {r2:.3f}")

# -------------------------------
# Save model
# -------------------------------
joblib.dump(pipeline, 'bangalore_house_price_model.pkl')
print("💾 Model saved as 'bangalore_house_price_model.pkl'")
