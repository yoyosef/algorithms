import random
def partition(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r, 1):
        if array[j] <= x:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def randomized_partition(array, p, r):
    i = random.randint(p, r)
    array[r], array[i] = array[i], array[r]
    return partition(array, p, r)


def randomized_quicksort(array, p, r):
    if p < r:
        q = randomized_partition(array, p, r)
        randomized_quicksort(array, p, q - 1)
        randomized_quicksort(array, q + 1, r)


def randomized_select(array, p, r, i):
    if p == r:
        return array[p]
    # q is the partition point returned by randomized_partition
    q = randomized_partition(array, p, r)
    # A[q] is the kth smallest element from p to r
    k = q - p + 1

    # Found the ith smallest element
    if i == k:
        return array[q]
    # The ith element is in the left partition
    elif i < k:
        # exclude q because it has been already checked
        # need to find the ith of the left partition
        return randomized_select(array, p, q - 1, i)
    else:
        # since we've 'removed' the left partition, we want to find the (i-k)th element
        # of the right partition
        return randomized_select(array, q + 1, r, i - k)

if __name__ == '__main__':
    arr = [1, 5, 4, 3, 2, 9, -1]
    print(sorted(arr))
    print(randomized_select(arr, 0, len(arr) - 1, 3))