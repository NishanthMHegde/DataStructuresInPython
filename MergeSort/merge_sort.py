
def merge_sort(nums):
	if len(nums) ==1:
		return 1
	middle = int(len(nums)/2)
	left_half = nums[:middle]
	right_half = nums[middle:]
	merge_sort(left_half)
	merge_sort(right_half)

	i = 0
	j = 0
	k = 0

	#merge the left and right subarrays based on values
	while i<len(left_half) and j<len(right_half):
		if left_half[i] < right_half[j]:
			nums[k] = left_half[i]
			i = i+1
		else:
			nums[k] = right_half[j]
			j=j+1
		k=k+1 

	#copy the rest of the remaining left out values from the left/right subarrays
	while i<len(left_half):
		nums[k] = left_half[i]
		i=i+1
		k=k+1
	while j<len(right_half):
		nums[k] = right_half[j]
		j=j+1
		k=k+1


nums = [5,4,3,2,1]
merge_sort(nums)
print(nums)