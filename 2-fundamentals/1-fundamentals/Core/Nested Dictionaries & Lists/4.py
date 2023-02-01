# Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(dict):
    for key, val in dict.items():
        # used .upper() to change the key string to uppercase
        print(len(val), key.upper())
        for x in val:
            print(x)
        # add some space after an iteration
        print("")

printInfo(dojo)
