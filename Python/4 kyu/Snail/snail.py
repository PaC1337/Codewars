def snail(snail_map):
    trail = []
    while len(snail_map) > 0:
        trail += snail_map[0]
        del snail_map[0]
        if len(snail_map) > 0:
            for i in snail_map:
                trail += [i[-1]]
                del i[-1]
            trail += snail_map[-1][::-1]
            del snail_map[-1]
            for n in reversed(snail_map):
                trail += [n[0]]
                del n[0]
    return trail
