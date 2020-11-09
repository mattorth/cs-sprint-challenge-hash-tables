#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


# inputs: tickets ( source and destination) and length
# output: array of destinations in order
# destination must match following source
# solution should run in linear time



def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    log = {}
    route = [None] * length
    for ticket in tickets:
        log[ticket.source] = ticket.destination

    source = "NONE"
    destination = ""
    idx = 0
    while destination != "NONE":
        route[idx] = log[source]
        source = log[source]
        destination = log[source]
        idx += 1
    route[idx] = destination
    return route
