def bubbleSort(numbers):
    itemCount = len(numbers)
    for index in range(itemCount-1):
        for value in range(itemCount-1):
            if numbers[value] > numbers[value+1]:
                temp = numbers[value], numbers[value+1]
                numbers[value+1], numbers[value] = temp
                






Numbers = [76, 72, 100, 92, 88, 71, 81, 45, 70, 42]
bubbleSort(Numbers)
