import sys

def find_longest_downhill_path(matrix):
    """
    Find the longest strictly decreasing downhill path.
    """
    if not matrix or not matrix[0]:
        return 0

    m = len(matrix)
    n = len(matrix[0])

    #8 possible directions
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    #DP memoization
    dp = [[-1] * n for _ in range(m)]

    def dfs(i, j):
        """Return the number of nodes in the longest path"""
        if dp[i][j] != -1:
            return dp[i][j]

        max_length = 1

        for dx, dy in directions:
            x, y = i + dx, j + dy

            if 0 <= x < m and 0 <= y < n and matrix[x][y] < matrix[i][j]:
                length = 1 + dfs(x, y)
                max_length = max(max_length, length)

        dp[i][j] = max_length
        return max_length

    #Find maximum path
    max_nodes = 0
    for i in range(m):
        for j in range(n):
            max_nodes = max(max_nodes, dfs(i, j))

    #Convert from node count to edge count
    return max_nodes - 1 if max_nodes > 0 else 0

def main():
    test_files = ['ski_input1.txt', 'ski_input2.txt']

    results = []
    for filename in test_files:
        try:
            with open(filename, 'r') as f:
                lines = f.read().strip().split('\n')

                m = int(lines[0].strip())
                n = int(lines[1].strip())

                matrix = []
                for i in range(2, 2 + m):
                    row = list(map(int, lines[i].strip().split()))
                    matrix.append(row)

                result = find_longest_downhill_path(matrix)
                results.append(result)
                print(f"{filename}: {result}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")
            return

    #For batch processing
    return results

if __name__ == "__main__":
    main()