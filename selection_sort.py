def selectionSort(list):
    for index in range(10):
        min_position=index
        for value in range(min_position,10):
            if list[value] < list[min_position]:
                min_position = value


        new = list[index]
        list[index] = list[min_position]
        list[min_position] = new
        print(list)
    






numbers = [76, 72, 100, 92, 88, 71, 81, 45, 70, 42]
selectionSort(numbers)