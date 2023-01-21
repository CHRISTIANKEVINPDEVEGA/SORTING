def selectionSort(list):
    for index in range(len(list)):
        search_start = index
        for value in range(search_start,len(list)):
            least_value = value
            if least_value < list[search_start]:
                list[search_start]=least_value
                print(list)                









numbers = [76, 72, 100, 92, 88, 71, 81, 45, 70, 42]
print(selectionSort(numbers))