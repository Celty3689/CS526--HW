def read_input(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        m = int(f.readline().strip())
        A = list(map(int, f.readline().strip().split()))
        B = list(map(int, f.readline().strip().split()))
    return A, B

def longest_alternating_sequence(A, B):
    # 将数组分割为奇数和偶数，并去除重复数字
    A_odd = sorted(set([x for x in A if x % 2 == 1]))    # A中的奇数，去重并排序
    A_even = sorted(set([x for x in A if x % 2 == 0]))   # A中的偶数，去重并排序
    B_odd = sorted(set([x for x in B if x % 2 == 1]))    # B中的奇数，去重并排序
    B_even = sorted(set([x for x in B if x % 2 == 0]))   # B中的偶数，去重并排序

    def find_longest_sequence(odd_arr, even_arr):
        if not odd_arr:
            return 0

        max_len = 0

        # 从odd_arr的每个位置开始
        for i in range(len(odd_arr)):
            length = 1
            last_val = odd_arr[i]
            use_odd = False  # 下一个应该用even_arr

            # 贪心构建序列
            while True:
                found = False
                if use_odd:
                    # 在odd_arr中找大于last_val的最小值
                    best_candidate = float('inf')
                    for k in range(len(odd_arr)):
                        if odd_arr[k] > last_val and odd_arr[k] < best_candidate:
                            best_candidate = odd_arr[k]
                            found = True
                    if found:
                        last_val = best_candidate
                        length += 1
                        use_odd = False
                    else:
                        break
                else:
                    # 在even_arr中找大于last_val的最小值
                    best_candidate = float('inf')
                    for k in range(len(even_arr)):
                        if even_arr[k] > last_val and even_arr[k] < best_candidate:
                            best_candidate = even_arr[k]
                            found = True
                    if found:
                        last_val = best_candidate
                        length += 1
                        use_odd = True
                    else:
                        break

            max_len = max(max_len, length)

        return max_len

    # 两种组合模式
    # 模式1: A奇数 + B偶数
    case1 = find_longest_sequence(A_odd, B_even)
    # 模式2: A偶数 + B奇数
    case2 = find_longest_sequence(A_even, B_odd)

    return max(case1, case2)

def main():
    input_files = ['longest_seq1.txt', 'longest_seq2.txt', 'longest_seq3.txt',
                   'longest_seq4.txt', 'longest_seq5.txt', 'longest_seq6.txt']

    for filename in input_files:
        try:
            A, B = read_input(filename)
            length = longest_alternating_sequence(A, B)
            print(f"{filename}: {length}")
        except FileNotFoundError:
            print(f"{filename}: File not found")

if __name__ == "__main__":
    main()