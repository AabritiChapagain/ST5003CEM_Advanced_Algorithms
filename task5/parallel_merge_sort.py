import threading


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def sequential_merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = sequential_merge_sort(arr[:mid])
    right = sequential_merge_sort(arr[mid:])

    return merge(left, right)


def parallel_merge_sort(arr, threads=2):

    if threads <= 1 or len(arr) <= 1:
        return sequential_merge_sort(arr)

    mid = len(arr) // 2

    left_half = arr[:mid]
    right_half = arr[mid:]

    left_result = []
    right_result = []

    def sort_left():
        left_result.extend(
            parallel_merge_sort(left_half, threads // 2)
        )

    def sort_right():
        right_result.extend(
            parallel_merge_sort(right_half, threads // 2)
        )

    t1 = threading.Thread(target=sort_left)
    t2 = threading.Thread(target=sort_right)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    return merge(left_result, right_result)


if __name__ == "__main__":

    numbers = [8, 3, 6, 2, 9, 1, 5, 7, 4]

    print("Original:")
    print(numbers)

    print("\nSequential:")
    print(sequential_merge_sort(numbers))

    print("\nParallel:")
    print(parallel_merge_sort(numbers, threads=4))