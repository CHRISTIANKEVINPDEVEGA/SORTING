def insertionSort(numbers):
    itemCounts = len(numbers)
    for index in range(itemCounts):
        indexposition=index
        while indexposition < 0 and numbers[indexposition-1] > numbers[indexposition]:
            temp = numbers[indexposition], numbers[indexposition-1]
            numbers[indexposition-1], numbers[indexposition] = temp
            indexposition = indexposition - 1





Numbers = [76, 72, 100, 92, 88, 71, 81, 45, 70, 42]
insertionSort(Numbers)