class BubbleSort:
    def bubble_sort(self, arr):
        for i in range(len(arr)):
            swapped = False
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                yield arr, j
            if not swapped:
                break

class InsertionSort:
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1

            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
                yield arr, j
            arr[j + 1] = key

class QuickSort:
    def quick_sort(self, arr: list[int]):
        yield from self._quick_sort_helper(arr, 0, len(arr) - 1)
    
    def _quick_sort_helper(self, arr: list[int], low: int, high: int):
        if low < high:
            pivot_idx = yield from self._partition(arr, low, high)
            yield from self._quick_sort_helper(arr, low, pivot_idx - 1)
            yield from self._quick_sort_helper(arr, pivot_idx + 1, high)
    
    def _partition(self, arr: list[int], low: int, high: int):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                yield arr, j
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        yield arr, i + 1
        return i + 1

class MergeSort:
    def merge_sort(self, arr: list[int]):
        yield from self._merge_sort_helper(arr, 0, len(arr) - 1)
    
    def _merge_sort_helper(self, arr: list[int], left: int, right: int):
        if left < right:
            mid = (right + left) // 2
            yield from self._merge_sort_helper(arr, left, mid)
            yield from self._merge_sort_helper(arr, mid + 1, right)
            yield from self._merge(arr, left, mid, right)

    def _merge(self, arr: list[int], left: int, mid: int, right: int):
        left_part = arr[left:mid + 1]
        right_part=  arr[mid + 1:right + 1]
        i = j = 0
        k = left

        while i < len(left_part) and j < len(right_part):
            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1
            yield arr, k
        
        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1
            yield arr, k
        
        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1
            yield arr, k

class HeapSort:
    def heap_sort(self, arr: list[int]):
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            yield from self.heapify(arr, n, i)
        
        for end in range(n - 1, 0, -1):
            arr[0], arr[end] = arr[end], arr[0]
            yield arr, end
            yield from self.heapify(arr, end, 0)
    
    def heapify(self, arr: list[int], heap_size: int, i: int):
        largest = i
        left = 2*i + 1
        right = 2*i + 2

        if left < heap_size and arr[left] > arr[largest]:
            largest = left
 

        if right < heap_size and arr[right] > arr[largest]:
            largest = right

        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            yield arr, largest
            yield from self.heapify(arr, heap_size, largest)
