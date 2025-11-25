def radix_sort(arr):
    """Sort numbers by processing individual digits"""
    if not arr:
        return arr

    # Find maximum number to know number of digits
    max_num = max(arr)

    # Do counting sort for every digit
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    return arr

def counting_sort(arr, exp):
    """Counting sort for specific digit place"""
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Store count of occurrences
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Change count to actual position
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy output to original array
    for i in range(n):
        arr[i] = output[i]

def create_test_files():
    """Generate test data files"""
    import random

    # 15 elements
    small_data = [random.randint(1, 50) for _ in range(15)]
    with open('15 elements.txt', 'w') as f:
        f.write(' '.join(map(str, small_data)))

    # 50 elements
    medium_data = [random.randint(1, 100) for _ in range(50)]
    with open('50 elements.txt', 'w') as f:
        f.write(' '.join(map(str, medium_data)))

    # 500 elements
    large_data = [random.randint(1, 1000) for _ in range(500)]
    with open('500 elements.txt', 'w') as f:
        f.write(' '.join(map(str, large_data)))

def test_radix_sort():
    """Test radix sort on all datasets"""
    create_test_files()

    test_files = [
        '15 elements.txt',
        '50 elements.txt',
        '500 elements.txt'
    ]

    for filename in test_files:
        print(f"\nTesting {filename}:")

        with open(filename, 'r') as f:
            data = list(map(int, f.read().strip().split()))

        print(f"Original: {data}")

        sorted_data = radix_sort(data.copy())
        print(f"Radix Sort: {sorted_data}")


if __name__ == "__main__":
    test_radix_sort()