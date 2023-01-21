def mergeSort(numbers):
    itemCounts = len(numbers)
    if(itemCounts==1):
        return numbers
     
    halfOfnumbers = itemCounts//2

    first_half = mergeSort(numbers[halfOfnumbers:])
    later_half = mergeSort(numbers[:halfOfnumbers])



Numbers = [76, 72, 100, 92, 88, 71, 81, 45, 70, 42]
mergeSort(Numbers)