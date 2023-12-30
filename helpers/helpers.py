def chunkwise(collection, size=2) -> zip:
    it = iter(collection)
    return zip(*[it]*size)


def pairs(collection) -> zip:
    return chunkwise(collection, size=2)
