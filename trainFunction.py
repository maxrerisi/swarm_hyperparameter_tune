import pandas as pd
import numpy as np
import xgboost as xgb
import random
import os
from sklearn.metrics import roc_auc_score as auc

BOOSTING_ROUNDS = 25
FOLD_COUNT = 5


def seed_everything(seed):
    """
    Seeds the 3 conceivable randomizers used throughout this repository. Default seed 42 is passed as an argument wherever necessary.
    """
    random.seed(seed)
    os.environ['PYTHONASSEED'] = str(seed)
    np.random.seed(seed)


# seed_everything(42) # TODO i dont think we want this

# TODO do i bother with a k fold?
df = pd.read_csv("processed_data.csv", index_col=0)

# TODO assume that it can be any value but never 0.
param_list = {
    "max_depth": [1, 100],  # TODO must be int
    "eta": [0, 1],
    "subsample": 1,
    "colsample_bytree": 1,
    "colsample_bylevel": 1,
    "min_child_weight": [1, 100],
    "objective": "binary:logistic",
    "eval_metric": "auc",
    "tree_method": "exact",
    "alpha": [0, 100],
    "gamma": [0, 100],
    "lambda": [0, 100],
    "scale_pos_weight": [0, 25],
    "nthread": 8,
    "verbosity": 0,
    "num_parallel_tree": [1, 5],  # TODO must be integer
    "seed": 42
}

hyperparam = {"objective": "binary:logistic",
              "eval_metric": "auc",
              "tree_method": "exact",
              "verbosity": 0}


def train_xgboost(hyperparam):

    X = df.drop("admission", axis=1).to_numpy()
    y = df['admission'].to_numpy()

    p = np.random.permutation(len(y))
    X = X[p]
    y = y[p]

    fold_size = int(len(y) / FOLD_COUNT)

    out = []
    for j in range(FOLD_COUNT):
        start = j * fold_size
        end = (j + 1) * fold_size
        if j == FOLD_COUNT - 1:
            X_train, X_test = X[:start], X[start:]
            y_train, y_test = y[:start], y[start:]
        else:
            X_train, X_test = [*X[:start], *X[end:]], X[start:end]
            y_train, y_test = [*y[:start], *y[end:]], y[start:end]
        sub_out = (X_train, y_train, X_test, y_test)
        out.append(tuple([np.array(a) for a in sub_out]))

    predictions = []
    for fold in out:
        X_train, y_train, X_test, y_test = fold
        dtrain = xgb.DMatrix(X_train, label=y_train)
        dtest = xgb.DMatrix(X_test, label=y_test)
        eval_list = [(dtrain, 'train'), (dtest, 'eval')]

        xgb_model = xgb.train(hyperparam, dtrain, BOOSTING_ROUNDS, eval_list,
                              early_stopping_rounds=1000)
        predictions += list(xgb_model.predict(
            dtest, iteration_range=(0, xgb_model.best_iteration + 1)))

    return auc(y, predictions)


print(train_xgboost(hyperparam))
