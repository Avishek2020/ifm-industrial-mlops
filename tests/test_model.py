
import sys
from pathlib import Path

# Add project root to Python module search path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import numpy as np
from train import train_model


def test_model_training():
    model = train_model()
    assert model is not None


def test_model_prediction():
    model = train_model()

    sample = np.array([[60, 2]])
    prediction = model.predict(sample)

    assert prediction[0] in [0, 1]
