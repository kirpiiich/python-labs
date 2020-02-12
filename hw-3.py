def main():
    import random
    import timeit
    arr = [random.randint(10,99) for i in range(40)]
    print("Unsorted array:\n", arr)
    bubblearr = list(arr)
    start = timeit.default_timer() 
    bubbleSort(bubblearr)
    end = timeit.default_timer() 
    print("Execution time:", "%.8f" % (end - start), "sec") 
    insertionarr = list(arr)
    start = timeit.default_timer() 
    insertionSort(insertionarr)
    end = timeit.default_timer()  
    print("Execution time:", "%.8f" % (end - start), "sec") 
    selectionarr = list(arr)
    start = timeit.default_timer() 
    selectionSort(selectionarr)
    end = timeit.default_timer()  
    print("Execution time:", "%.8f" % (end - start), "sec") 
    shellarr = list(arr)
    start = timeit.default_timer() 
    shellSort(shellarr)
    end = timeit.default_timer()  
    print("Execution time:", "%.8f" % (end - start), "sec") 
    
def bubbleSort(arr):
    length = len(arr) - 1
    compare = 0
    swap = 0
    for i in range(length):
        for j in range(length - i):
            compare+=1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap+=1
    print("Bubble Sort:\n", "Comparisons:", compare, "Swaps:", swap)
    return arr

def insertionSort(arr):
    compare = 0
    swap = 0
    for i in range(1, len(arr)):
        key = i
        while key > 0 and arr[key-1] > arr[key]:
            compare+=1
            swap+=1
            arr[key-1], arr[key] = arr[key], arr[key-1]
            key -= 1
    print("Insertion Sort:\n", "Comparisons:", compare, "Swaps:", swap)
    return arr

def selectionSort(arr):
    compare = 0
    swap = 0
    length = len(arr) - 1 
    for i in range(0, length):
        min_ind = i
        for j in range(i, len(arr)):
            compare+=1
            if arr[j] < arr[min_ind]:
                min_ind = j
        compare+=1
        if i != min_ind:
            swap+=1
            arr[i], arr[min_ind] = arr[min_ind], arr[i]
    print("Selection Sort:\n", "Comparisons:", compare, "Swaps:", swap)
    return arr
    
def shellSort(arr):
    compare = 0
    swap = 0
    step = len(arr)//2
    while step > 0:
        for i in range(len(arr)-step):
            j = i
            while j >= 0 and arr[j] > arr[j + step]:
                compare += 1
                arr[j], arr[j + step] = arr[j + step], arr[j]
                swap+=1
                j-=step
        step//=2
    print("Shell Sort:\n", "Comparisons:", compare, "Swaps:", swap)
    return arr

main()