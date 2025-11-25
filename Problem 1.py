def insertion_sort(arr):
    """Insert elements one by one into sorted position"""
    array = arr.copy()
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

def merge_sort(arr):
    """Divide and conquer with merging"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays"""
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

def quick_sort(arr):
    """Partition around pivot and recurse"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def create_test_files():
    """Generate test data files"""
    import random

    # 15 elements
    small_data = [random.randint(1, 100) for _ in range(15)]
    with open('15 elements.txt', 'w') as f:
        f.write(' '.join(map(str, small_data)))

    # 50 elements
    medium_data = [random.randint(1, 500) for _ in range(50)]
    with open('50 elements.txt', 'w') as f:
        f.write(' '.join(map(str, medium_data)))

    # 500 elements
    large_data = [random.randint(1, 1000) for _ in range(500)]
    with open('500 elements.txt', 'w') as f:
        f.write(' '.join(map(str, large_data)))

def test_all_algorithms():
    """Test all three sorting algorithms"""
    create_test_files()

    test_files = [
        '15 elements.txt',
        '50 elements.txt',
        '500 elements.txt'
    ]

    algorithms = [
        (insertion_sort, "Insertion Sort"),
        (merge_sort, "Merge Sort"),
        (quick_sort, "Quick Sort")
    ]

    for filename in test_files:
        print(f"\nTesting {filename}:")

        with open(filename, 'r') as f:
            data = list(map(int, f.read().strip().split()))

        print(f"Original: {data}")

        for algorithm, algo_name in algorithms:
            sorted_data = algorithm(data)
            print(f"{algo_name}: {sorted_data}")

if __name__ == "__main__":
    test_all_algorithms()