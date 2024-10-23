import numpy as np
from parameter_file import INT_PARAMS, DEFAULT_HYPERPARAMETERS


def get_random_params():
    out = {}
    for key, val in DEFAULT_HYPERPARAMETERS.items():
        if isinstance(val, list):
            rand = 0
            while rand == 0:
                rand = np.random.uniform(val[0], val[1])
            if key in INT_PARAMS:
                rand = int(rand) + 1
            out[key] = rand
        else:
            out[key] = val

    return out

print(get_random_params())