def study_schedule(p_peri, t_tempo):
    if t_tempo is None:
        return None
    inicio = 0
    for entry, exit in p_peri:
        if type(entry) != int or type(exit) != int:
            return None
        if entry <= t_tempo <= exit:
            inicio += 1
    return inicio
