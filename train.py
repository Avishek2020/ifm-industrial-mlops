
import numpy as np
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_model():
    np.random.seed(42)

    # Simulated industrial sensor data
    temperature = np.random.normal(65, 12, 500)
    vibration = np.random.normal(2.5, 1, 500)

    # 1 = maintenance required
    labels = (
        (temperature > 80) | (vibration > 4)
    ).astype(int)

    X = np.column_stack((temperature, vibration))
    y = labels

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print(f"Model accuracy: {accuracy:.2%}")

    if accuracy < 0.90:
        raise ValueError("Model quality below threshold")

    joblib.dump(model, "model.joblib")
    print("Model saved successfully!")

    return model

if __name__ == "__main__":
    train_model()
