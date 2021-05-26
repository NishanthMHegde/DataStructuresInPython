def bubble_sort(nums):
	for i in range(len(nums)-1):
		for j in range(len(nums) -1 -i):
			if nums[j] > nums[j+1]:
				temp = nums[j]
				nums[j] = nums[j+1]
				nums[j+1] = temp
	return nums


nums = [6,5,4,3,2,1]
print(bubble_sort(nums)) 

nums = [-1, -2 ,-3, -4, -5, -6]
print(bubble_sort(nums))