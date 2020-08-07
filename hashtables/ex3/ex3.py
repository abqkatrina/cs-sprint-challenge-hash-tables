def intersection(arrays):
    """
    YOUR CODE HERE
    need to find common int in multiple lists
    those lists are contained in an single array

    count # times in cache compared to number of lists?
    doesn't account for duplicates since not checking each list separately


    compare 0 to 1 --> results
    compare >=2 to results, if not found, delete from results?
    too inefficient

    """
    # if not in first list, can't match
    result = []
    cache = {}
    # for each list in arrays...
    for l in arrays:
        # for each element in the list
        for e in l:
            if e not in cache:
                # add to cache at index of e
                cache[e] = 1
            else:
                # add to existing cache value at index of e
                cache[e] += 1

    # need listed items of cache for methods
    temp = list(cache.items())
    # for each item in mid
    for x in temp:
        # if the item in the list is present in each list...
        if x[1] == len(arrays):
            # add that item to the results
            result.append(x[0])

                
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
