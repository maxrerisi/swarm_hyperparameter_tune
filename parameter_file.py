INT_PARAMS = ["num_parallel_tree", "max_depth"]
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
CHANGING_PARAMS = ["max_depth", "eta", "min_child_weight", "alpha",
                   "gamma", "lambda", "scale_pos_weight", "num_parallel_tree"]

NUMBER_OF_ROUNDS = 50
MEMBER_COUNT = 10

BOOSTING_ROUNDS = 75
FOLD_COUNT = 5

RANDOM_MAGNITUDE = 10
SELF_BEST_MAGNITUDE = 5
SWARM_BEST_MAGNITUDE = 7.5

