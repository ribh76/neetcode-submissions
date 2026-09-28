class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        high = len(nums) - 1
        low = 0 
        self.merge_sort(nums, low, high)
        return nums

    def merge_sort(self, arr: List[int], low: int, high: int) -> None: 
        if low < high:
            mid = (low + high) // 2
            self.merge_sort(arr, low, mid)
            self.merge_sort(arr, mid + 1, high)
            self.merge(arr, low, mid, high)

    def merge(self, arr: List[int], low: int, mid: int, high: int) -> None: 
        arr1 = arr[low:mid + 1]
        arr2 = arr[mid + 1:high + 1]

        arr3 = []
        a, b = 0, 0

        while a < len(arr1) and b < len(arr2): 
            if arr1[a] <= arr2[b]: 
                arr3.append(arr1[a])
                a += 1
            else:
                arr3.append(arr2[b])
                b += 1

        while a < len(arr1):
            arr3.append(arr1[a])
            a += 1
        
        while b < len(arr2):
            arr3.append(arr2[b])
            b += 1
        
        for i in range(len(arr3)):
            arr[low + i] = arr3[i]