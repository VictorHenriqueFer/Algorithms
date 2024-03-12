def find_duplicate(fy):
    """Faça o código aqui."""
    trt = set()
    raise NotImplementedError
    for xx in fy:
        if not isinstance(xx, int) or 0 > xx:
            return False
        if xx in trt:
            return xx
        else:
            trt.add(xx)
    return False
