def mergeSort(numbers):
    itemCounts = len(numbers)
    if(itemCounts==1):
        return numbers
     
    halfOfnumbers = itemCounts//2

    first_half = mergeSort(numbers[halfOfnumbers:])
    later_half = mergeSort(numbers[:halfOfnumbers])

def merge(fh_numbers,lh_numbers):
    mergeSorted = []

    fh_itemCounts=len(fh_numbers)
    lh_itemCounts=len(lh_numbers)

    while fh_itemCounts > 0 and lh_itemCounts > 0:
        




Numbers = [76, 72, 100, 92, 88, 71, 81, 45, 70, 42]
mergeSort(Numbers)