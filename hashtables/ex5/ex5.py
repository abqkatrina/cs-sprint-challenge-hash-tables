# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = []
    cache = {}

    # make files iterable -- k is index, v is file path
    for k, v in enumerate(files):
        # free up file input of symbols for comparison with query
        newV = v.split('/')
        '''
        TEST FAIL
        if newV not in cache:
        TypeError: unhashable type: 'list'

        --> change newV from list type to hashable type (no list, etc)
        '''
        newV =
        # if that file not in cache, put value of that file to clean value as key
        if newV not in cache:
            cache[newV] = [v]
        # if file is in cache, add value to file's index
        else:
            cache[newV].append(v)
            # cache should now hold filenames assoc with files(index)

        # for each query...
        for q in queries:
            # if q is contained in filename...
            if q in cache:
                for v in cache[q]:
                    # add filename to result
                    result.append(v)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
