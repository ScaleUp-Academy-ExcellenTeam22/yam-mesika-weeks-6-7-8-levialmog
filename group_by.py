def group_by(function, iterable):
    """
    The function gets function and iterable creates a dictionary and enters to it according to:
    The keys are the values returned from the function passed as the first parameter.
    The value corresponding to a particular key is a list of all the organs for which the value
    appearing in the key is repeated.
    :param function: The function that return the keys of the dictionary.
    :param iterable: The values that append to the dictionary.
    :return: Dictionary according to the required.
    """
    dictionary_results = {}
    for item in iterable:
        dictionary_results.setdefault(function(item), []).append(item)

    return dictionary_results


if __name__ == "__main__":
    print(group_by(len, ["hi", "bye", "yo", "try"]))
