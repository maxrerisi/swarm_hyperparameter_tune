from parameter_file import CHANGING_PARAMS, DEFAULT_HYPERPARAMETERS


def paramsToPos(params) -> tuple:
    out = []
    for par in CHANGING_PARAMS:
        out.append(params[par])
    return tuple(out)


def posToParams(pos) -> dict:
    out = {}
    for a, b in enumerate(pos):
        out[CHANGING_PARAMS[a]] = b
    for a in DEFAULT_HYPERPARAMETERS:
        if a not in out:
            out[a] = DEFAULT_HYPERPARAMETERS[a]
    return out
