import pytest
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from ml.model import train_model, compute_model_metrics
import numpy as np
import pandas as pd

# TODO: implement the first test. Change the function name and input as needed
def test_correct_algorithm():
    """
    Tests to make sure model is implemented as desired
    """
    X = np.array([[0, 1], [1, 0], [1, 1], [0, 0]])
    y = np.array([1, 1, 0, 0])

    model = train_model(X,y)

    assert isinstance(model, LogisticRegression)
    assert model.solver == 'saga'
    assert model.random_state == 42

# TODO: implement the second test. Change the function name and input as needed
def test_compute_metrics():
    """
    Runs compute_model_metrics and checks against expected values
    """
    y = np.array([0, 1, 1, 0])
    preds = np.array([0, 1, 1, 0])

    p, r, f = compute_model_metrics(y, preds)

    assert p == 1.0
    assert r == 1.0
    assert f == 1.0


# TODO: implement the third test. Change the function name and input as needed
def test_train_test_shape():
    """
    confirms train_test_split breaks into correct train/test sizes
    """
    df = pd.DataFrame({"a": range(100), "salary": ["<=50K"] * 100})

    train, test = train_test_split(df, test_size=0.2, shuffle=True, random_state=42)

    assert len(train) == 80
    assert len(test) == 20
