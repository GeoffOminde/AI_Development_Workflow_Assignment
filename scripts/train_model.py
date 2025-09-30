import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from data_preprocessing import preprocess_student_data
import pickle

# ----------------------------
# Paths
# ----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # script directory
DATA_PATH = os.path.join(BASE_DIR, '..', 'data', 'student_data_sample.csv')
MODEL_PATH = os.path.join(BASE_DIR, 'rf_model.pkl')

# ----------------------------
# Load Sample Data
# ----------------------------
df = pd.read_csv(DATA_PATH)

# Features and target
X = df.drop('Dropout', axis=1)
y = df['Dropout']

# ----------------------------
# Preprocess Features
# ----------------------------
X_processed = preprocess_student_data(X)

# ----------------------------
# Train/Test Split
# ----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_processed, y, test_size=0.15, random_state=42
)

# ----------------------------
# Train Random Forest Model
# ----------------------------
rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf.fit(X_train, y_train)

# ----------------------------
# Evaluate Model
# ----------------------------
y_pred = rf.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred))

# ----------------------------
# Save Model
# ----------------------------
with open(MODEL_PATH, 'wb') as f:
    pickle.dump(rf, f)

print(f"Random Forest model saved to {MODEL_PATH}")
