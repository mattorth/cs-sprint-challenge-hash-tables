def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # inputs: weights, length, limit
    # outputs: tuple of indices weights that add up to limit
    # return none if no pair exists
    # run with linear time (hash table)
    # edge cases
        # 1 item
        # multiple solutions
    table = {}

    # 1 item
    if (length == 1):
        return None

    for idx in range(length):
        weight = weights[idx]
        if weight in table:
            other_idx = table[weight]
            return (idx, other_idx)
        difference = limit - weight
        table[difference] = idx
    return None
