import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# ✅ Load Dataset
df = pd.read_csv("anemia.csv")

# ✅ Features (X) and Labels (y)
X = df[['Gender', 'Hemoglobin', 'MCH', 'MCHC', 'MCV']]
y = df['Result']

# ✅ Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# ✅ Check accuracy
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("✅ Model Training Complete!")
print("📊 Accuracy:", acc)

# ✅ Save model
joblib.dump(model, "model.pkl")
print("✅ model.pkl saved successfully!")

