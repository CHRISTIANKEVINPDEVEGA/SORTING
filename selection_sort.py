'''Main function'''
def selectionSort(list):
    '''This is the first loop, it is the loop that determines the start of the searching'''
    for index in range(10):
        min_position=index
        '''This is the second loop that picks the index position of the value with the lowest value'''
        for value in range(min_position,10):
            if list[value] < list[min_position]:
                min_position = value

        '''This is the code that manually swaps the value of indexes'''
        new = list[index]
        list[index] = list[min_position]
        list[min_position] = new
        print(list)
    






numbers = [76, 72, 100, 92, 88, 71, 81, 45, 70, 42]
selectionSort(numbers)