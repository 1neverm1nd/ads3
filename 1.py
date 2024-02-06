def selection_sort(arr):
    N = len(arr)
    for i in range(N-1):
        m = arr[i]
        p = i
        for j in range(i+1, N):
            if m > arr[j]:
                m = arr[j]
                p = j
        if p != i:
            t = arr[i]
            arr[i] = arr[p]
            arr[p] = t
    return arr

def split_and_merge_list(a):
    N1 = len(a) // 2
    a1 = a[:N1]
    a2 = a[N1:]

    if len(a1) > 1:
        a1 = split_and_merge_list(a1)
    if len(a2) > 1:
        a2 = split_and_merge_list(a2)

    return merge_list(a1, a2)


def merge_list(a, b):
  c = []
  N = len(a)
  M = len(b)
  i , j = 0 , 0
  while i < N and j < M:
      if a[i] <= b[j]:
          c.append(a[i])
          i += 1
      else:
          c.append(b[j])
          j += 1
  c += a[i:] + b[j:]
  return c


def quicksort(arr):
    if len(arr) <= 1 :
        return arr
    else:
        pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quicksort(left) + [pivot] + quicksort(right)

def heapsort(arr):
    n = len(arr)

    for i in range (n // 2-1,-1,-1):
        heapify(arr,n,i)
    for i in range (n-1,0,-1):
        arr[i] , arr[0] = arr[0],arr[i]
        heapify(arr,i,0)
    return arr


def heapify(arr,n,i):
    n = len(arr)
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2

    if left < n and arr[right] > arr[largest]:
        largest = left

    if right < n and arr[left] > arr[largest]:
        largest = right
    if largest != i:
        arr[i] ,arr[largest] = arr[largest] , arr[i]
        heapify(arr,n,largest)





def bubblesort(arr):
    N = len(arr)
    for i in range(0, N-1):
        for j in range(0, N-1-i):
         if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            return arr


a = [9, 5, -3, 4, 7, 8, -8]
b = selection_sort(a[:])

print(a)
print(b)

