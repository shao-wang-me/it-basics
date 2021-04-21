def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


def bubble_sort(nums):
    done = False
    while not done:
        done = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                done = False
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


def insertion_sort(nums):
    for i in range(len(nums)):
        pass
        # TODO


def test():
    sort_functions = [selection_sort, bubble_sort]
    for sort_function in sort_functions:
        print(sort_function.__name__)
        cases = [[7, 2, 5, 2, 87, 9], [45, 1, 1, 2, 5, 6, 7, 44, 23, 4, 6]]
        for case in cases:
            print(sort_function(case))


test()
