def main():
    import random
    import time
    from datetime import timedelta
    arr = [random.randint(0,1000) for i in range(1000)]
    print("Unsorted array\n", arr)
    bubblearr = list(arr)
    start_time = time.monotonic()
    bubbleSort(bubblearr)
    end_time = time.monotonic() 
    print("Time:",timedelta(seconds=end_time - start_time)) 
    insertionarr = list(arr)
    start_time = time.monotonic()
    insertionSort(insertionarr)
    end_time = time.monotonic() 
    print("Time:",timedelta(seconds=end_time - start_time)) 
    selectionarr = list(arr)
    start_time = time.monotonic()
    selectionSort(selectionarr)
    end_time = time.monotonic() 
    print("Time:",timedelta(seconds=end_time - start_time)) 
    shellarr = list(arr)
    start_time = time.monotonic()
    shellSort(shellarr)
    end_time = time.monotonic() 
    print("Time:",timedelta(seconds=end_time - start_time))
    
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
    print("Bubble Sort:", "Comparisons:", compare, "Swaps:", swap)
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
    print("Insertion Sort:", "Comparisons:", compare, "Swaps:", swap)
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
    print("Selection Sort:", "Comparisons:", compare, "Swaps:", swap)
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
    print("Shell Sort:", "Comparisons:", compare, "Swaps:", swap)
    return arr

main()