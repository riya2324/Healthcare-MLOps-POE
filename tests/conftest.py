import pytest
from train import train_model

@pytest.fixture(scope="session", autouse=True)
def trained_model():
    # Ensure the model files exist before API tests run.
    train_model()
