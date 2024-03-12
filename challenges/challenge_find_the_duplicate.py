def find_duplicate(fy):
    trt = set()
    for xx in fy:
        if not isinstance(xx, int) or 0 > xx:
            return False
        if xx in trt:
            return xx
        else:
            trt.add(xx)
    return False
