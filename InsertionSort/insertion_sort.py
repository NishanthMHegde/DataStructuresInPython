def insertion_sort(nums):
	for i in range(1, len(nums)):
		j =i
		while j>0 and nums[j-1] > nums[j]:
			temp = nums[j]
			nums[j] = nums[j-1]
			nums[j-1] = temp
			j = j -1 
	return nums

nums = [6,5,4,3,2,1]
print(insertion_sort(nums))
nums = [-1,-2,-3,-4,-5]
print(insertion_sort(nums))
