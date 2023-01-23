def mergeSort(numbers):
    itemCounts = len(numbers)
    if itemCounts==1 :
        return numbers
     
    halfOfnumbers = itemCounts//2

    fh_numbers = mergeSort(numbers[:halfOfnumbers])
    lh_numbers = mergeSort(numbers[halfOfnumbers:])

    return merge(fh_numbers,lh_numbers)

def merge(fh_numbers,lh_numbers):
    mergeSorted = []
    fh_index = 0
    lh_index = 0

    fh_itemCounts=len(fh_numbers)
    lh_itemCounts=len(lh_numbers)

    while fh_itemCounts > fh_index and lh_itemCounts > lh_index:
        if fh_numbers[fh_index] < lh_numbers[lh_index]:
            mergeSorted.append(fh_numbers[fh_index])
            fh_index = fh_index + 1

        else:
            mergeSorted.append(lh_numbers[lh_index])
            lh_index = lh_index + 1



Numbers = [76, 72, 100, 92, 88, 71, 81, 45, 70, 42]
print(mergeSort(Numbers))