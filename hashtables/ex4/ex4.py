def has_negatives(a):
    """
    YOUR CODE HERE
    need to compare pos and neg -- two lists
    one list neg --> absolute value
    if in list pos --> result
    """
    # need to return result -- lists have .append -- noice
    result = []
    #  need a dict for holding info
    cache = {}

    # enumerate makes an index key with a value
    for k, v in enumerate(a):
        # for every key, add its value to the dict
        cache[v] = v
    
    # need a list of the items in cache for coomparison methods (cache holds original numbers)
    temp = list(cache.items())

    for i in temp:
        # if the item is neg, use absolute value
        if i[1] < 0:
            pos = abs(i[1])
            # if that new number is already in cache, add it to the list of results
            if pos in cache:
                result.append(pos)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
