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

NUMBER_OF_ROUNDS = 100000
MEMBER_COUNT = 10

BOOSTING_ROUNDS = 15
FOLD_COUNT = 5 # if 1, assumes a 80:20 split

RANDOM_MAGNITUDE = 5
SELF_BEST_MAGNITUDE = 1
SWARM_BEST_MAGNITUDE = 1

#TODO comment this file
#TODO use other metrics
#TODO net displacement (on average)
#TODO visualizing how they are spaced, bc:
# 7: (47, 1, 69, 23, 24, 88, 16, 5) 0.870335 69.897537
# 8: (38, 1, 67, 20, 49, 24, 9, 5) 0.872823 70.055718
# 9: (66, 1, 15, 22, 41, 30, 10, 4) 0.873344 60.488845
# 10: (78, 0, 23, 16, 23, 85, 15, 5) 0.874490 60.233888
# got those results using 1 for all the magnitudes, they must be far apart, no?
# A way of changing vector weights mid program?
#TODO what about the case where the bootstrap is just lucky and the AUC is actually junk?
#TODO average member best?
#TODO use this in a kaggle comp
    #TODO make a real repo first tho
