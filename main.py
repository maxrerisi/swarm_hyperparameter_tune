# TODO create a simple function that takes the params as input and returns auc.


# did that need to do the swarm math with vectors and weighting for n-dim space (num of features but it should be 1d n times)

# get_random_params.py
INT_PARAM = ["num_parallel_tree", "max_depth"]

# paramsToPos.py
CHANGING_PARAMS = ["max_depth", "eta", "min_child_weight", "alpha",
                   # will impact the order in which coordinates are processed
                   "gamma", "lambda", "scale_pos_weight", "num_parallel_tree"]

# default hyperparameters with lists for ranges.
DEFAULT_HYPERPARAMETERS = {
    "max_depth": [1, 100],
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
    "num_parallel_tree": [1, 5],
    "seed": 42
}

# trainFunction.py
BOOSTING_ROUNDS = 25
FOLD_COUNT = 5
