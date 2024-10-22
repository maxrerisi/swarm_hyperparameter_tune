import numpy as np


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
INT_PARAM = ["num_parallel_tree", "max_depth"]


def get_random_params():
    out = {}
    for key, val in param_list.items():
        if isinstance(val, list):
            rand = 0
            while rand == 0:
                rand = np.random.uniform(val[0], val[1])
            if key in INT_PARAM:
                rand = int(rand) + 1
            out[key] = rand
        else:
            out[key] = val

    return out
