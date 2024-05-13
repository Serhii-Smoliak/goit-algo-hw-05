def binary_search(input_arr, search_target):
	left = 0
	right = len(input_arr) - 1
	iters = 0

	while left <= right:
		mid = left + (right - left) // 2
		iters += 1

		if input_arr[mid] == search_target:
			return iters, input_arr[mid]
		elif input_arr[mid] < search_target:
			left = mid + 1
		else:
			right = mid - 1

	if left < len(input_arr):
		return iters, input_arr[left]
	else:
		return iters, None


# Приклад використання:
arr = [0.1, 0.3, 0.5, 0.7, 0.9]
target = 0.6
result = binary_search(arr, target)
print(result)
