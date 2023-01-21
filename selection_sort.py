def selectionSort(list):
    for i in range(len(list)):
        for val in list:
            min_val=val
            pos=0
            if min_val < list[pos]:
                min_val=list[pos]
                pos = pos + 1            







numbers = [76, 72, 100, 92, 88, 71, 81, 45, 70, 42]
print(selectionSort(numbers))