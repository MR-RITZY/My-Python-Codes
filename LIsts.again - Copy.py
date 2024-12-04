def ListsToStrings(lists):
    string = ''
    for i in range(len(lists)):
        if len(lists) == 1:
            string = string + lists[i]
        elif i == len(lists) - 1:
            string = string + ' and ' + lists[i]
        elif i == len(lists) - 2:
            string = string + lists[i]
        else:
            string = string + lists[i] + ', '
    print(string)
    return string

ListsToStrings(['Be happy'])



