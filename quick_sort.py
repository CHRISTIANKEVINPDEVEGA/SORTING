def partition(numbers, lower, higher):
    pivot = numbers[higher]

    for index in range(lower, higher):
        if numbers[index] <= pivot:
            numbers[lower], numbers[index] = numbers[index], numbers[lower]
            lower = lower + 1

    numbers[lower], numbers[higher] = numbers[higher], numbers[lower]
    
    return lower


Numbers = [76, 72, 100, 92, 88, 71, 81, 45, 70, 42]
quickSort(Numbers)