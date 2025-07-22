# Time complexity O(logn) | Space complexity O(1)

def search(nums, target):
    left = 0
    right = len(nums)-1
    while (left <= right):
        middle = (left+right)//2
        if nums[middle] == target:
            return middle
        if nums[left] <= nums[middle]:
            # Left part is sorted
            if target >= nums[left] and target < nums[middle]:
                # Explore left part
                right = middle-1
            else:
                left = middle+1
        else:
            # Right part is sorted
            if target <= nums[right] and right > nums[middle]:
                left = middle+1
            else:
                right = middle-1
    return -1
