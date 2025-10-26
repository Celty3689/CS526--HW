def process_file(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        T = int(f.readline().strip())
        arr = list(map(int, f.readline().strip().split()))

    original_arr = arr.copy()  #Save the original array for output.

    #descending sort
    arr.sort(reverse=True)

    total = 0
    count = 0
    for num in arr:
        total += num
        count += 1
        if total > T:
            break

    #print the result
    print(f"File: {filename}")
    print(f"{filename}: Target: {T} Answer: {count}")
    print()


def main():
    files = ['fewest_1.txt', 'fewest_2.txt', 'fewest_3.txt']

    for file in files:
        try:
            process_file(file)
        except FileNotFoundError:
            print(f"File {file} not found, skipping...\n")
        except Exception as e:
            print(f"Error processing {file}: {e}\n")

if __name__ == "__main__":
    main()