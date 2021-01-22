def divideList(lst):
    dct = {}

    for element in lst:
        if len(element) not in dct:
            dct[len(element)] = [element]
        elif len(element) in dct:
            dct[len(element)] += [element]

    res = []
    for key in sorted(dct):
        res.append(dct[key])

    return res


# Driver code
lst = ['The', 'art', 'of', 'programming']
print(divideList(lst))
