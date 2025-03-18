# To solve this we use binary search approach . We check if the mid element is equal to arr[index-1] + 1 . If not we return it.
# Else we change the low or high element accordingly.
#Time Complexity : O(logn)
#Space Complexity : O(1)
class Solution:
    def binary_search(arr):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = low + (high - low ) // 2
            if mid>0 and arr[mid]!=arr[mid-1] + 1:
                return arr[mid]-1
            elif mid < len(arr) -1 and arr[mid]!=arr[mid+1] - 1:
                return arr[mid] + 1

            if arr[mid]==mid +1:
                low = mid + 1
            else:
                high = mid - 1
            
        return -1 

        

