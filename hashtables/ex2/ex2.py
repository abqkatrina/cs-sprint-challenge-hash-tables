#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    Your function should output an array of strings with the entire route of
    your trip. For the above example, it should look like this:

    ["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]

    Your solution should run in linear time. You can assume that your
    function will always be handed a valid ticket chain as input. 

    * We can hash each ticket such that the starting location is the key and
    the destination is the value. Then, when constructing the entire
    route, the `i`th location in the route can be found by checking the
    hash table for the `i-1`th location.
    
    """
    route = []
    cache = {}
    
    # add tickets to cache: k is source, v is dest
    for t in tickets:
        if t not in cache:
            cache[t.source] = t.destination
    
    # need to establish an index range 
    route.append(cache['NONE'])

    # return each destination
    for i in range(length-1):
        route.append(cache[route[i]])

    return route
