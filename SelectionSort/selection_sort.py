def selection_sort(nums):
	for i in range(len(nums) -1):
		index = i
		for j in range(i+1, len(nums)):
			if nums[j] < nums[index]:
				index = j
		if index != i:
			temp = nums[index]
			nums[index] = nums[i]
			nums[i] = temp

	return nums

nums = [6,5,4,3,2,1]
print(selection_sort(nums))
nums = [-1,-2,-3,-4,-5]
print(selection_sort(nums))
