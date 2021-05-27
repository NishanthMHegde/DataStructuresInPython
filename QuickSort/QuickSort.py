def quick_sort(nums, low, high):
	if low>=high:
		return
	pivot = partition(nums, low, high)
	quick_sort(nums, low, pivot-1)
	quick_sort(nums, pivot+1, high)

def partition(nums, low, high):
	middle = int((low+high)/2)
	swap(nums, middle, high)

	i = low
	for j in range(low, high):
		if nums[j] <=nums[high]:
			swap(nums, j, i)
			i = i + 1
	swap(nums, i, high)
	return i


def swap(nums, index1, index2):
	temp = nums[index1]
	nums[index1] = nums[index2]
	nums[index2] = temp


nums = [5,4,3,2,1]
quick_sort(nums, 0, len(nums)-1)
print(nums)