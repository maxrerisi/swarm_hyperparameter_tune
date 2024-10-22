import numpy as np
from main import INT_PARAM, DEFAULT_HYPERPARAMETERS


param_list = DEFAULT_HYPERPARAMETERS


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
