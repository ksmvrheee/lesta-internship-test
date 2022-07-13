def quicksort(ar):
    """Sorts an array in a pretty fast way by dividing it to several other arrays without the memory abuse."""
    if len(ar) > 1:
        return quicksort(list(filter(lambda x: x < ar[0], ar))) + \
            list(filter(lambda x: x == ar[0], ar)) + \
            quicksort(list(filter(lambda x: x > ar[0], ar)))
    else:
        return ar
