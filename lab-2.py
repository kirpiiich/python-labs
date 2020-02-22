import random
import timeit

def partition(arr, low, high):
  i = (low-1)
  pivot = arr[high]

  for j in range(low, high):
    if arr[j] <= pivot:
      i = i+1
      arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
  return (i+1)

def quickSort(arr, low, high):
  if low < high:
    pi = partition(arr,low,high)
    quickSort(arr, low, pi-1)
    quickSort(arr, pi+1, high)

def quickSortByOrder(arr, order):
  n = len(arr)
  if order:
    quickSort(arr, 0, n-1)
  else:
    for i in range(n):
      arr[i] = -1*arr[i]
    quickSort(arr, 0, n-1)
    for i in range(n):
      arr[i] = -1*arr[i]

def main():
  arr = [random.randint(10, 99) for i in range(40)]
  while(True):
    choice = input("1.Quick sort ascending\n2.Quick sort descending\nPress any key to quit\n")
    if choice == '1':
      print("Unsorted array\n", arr)
      start = timeit.default_timer()
      quickSortByOrder(arr, True)
      print("Sorted array\n", arr)
      stop = timeit.default_timer()
      execution_time = stop - start
      print("Program executed in", "%.8f" % (execution_time*1000), "ms")
    elif choice == '2':
      print("Unsorted array\n", arr)
      start = timeit.default_timer()
      quickSortByOrder(arr, False)
      print("Sorted array\n", arr)
      stop = timeit.default_timer()
      execution_time = stop - start
      print("Program executed in", "%.8f" % (execution_time*1000), "ms")
    else:
      print("До связи...")
      break

main()