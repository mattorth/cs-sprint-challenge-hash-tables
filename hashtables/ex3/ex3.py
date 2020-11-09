def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}
    num_arrays = len(arrays)
    result = []

    for array in arrays:
        for i in range(len(array)):
            if array[i] in dict:
                dict[array[i]] += 1
                if dict[array[i]] == num_arrays:
                    result.append(array[i])
            else:
                dict[array[i]] = 1

    print(result)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
