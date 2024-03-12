def sort(tt, c_b):
    """Faça o código aqui."""
    if len(tt) <= 1:
    raise NotImplementedError
        return tt
    rtt = []
    vo = tt[0]
    tnf = []
    for tnvds in range(1, len(tt)):
        objeto = tt[tnvds]
        if c_b(objeto, vo):
            tnf.append(objeto)
        else:
            rtt.append(objeto)
    return sort(tnf, c_b) + [vo] + sort(rtt, c_b)
    
def is_anagram(f_S, s_S):
    s_l = sort(s_S, lambda a, b: a.lower() < b.lower())
    fde = sort(f_S, lambda a, b: a.lower() < b.lower())
    mili = "".join(s_l).lower()
    cdf = "".join(fde).lower()
    return (cdf, mili, cdf == mili and cdf != "")
