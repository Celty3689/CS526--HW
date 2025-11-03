Question 1: Snowfall
    File List:snowfall_input1.txt, snowfall_input2.txt, snowfall_input3.txt, snowfall_input4.txt, snowfall_input5.txt

    How to Run:
        1. Ensure all snowfall_input*.txt files are in the same directory as snowfall.py
        2. Run in terminal: Question 1.py

    Input:
        Line 1: number of days n
        Line 2: cumulative snowfall totals

    Output:
        Only YES or NO for each input file

    Algorithm Core:
        1. Convert cumulative snowfall to daily snowfall
        2. Calculate total snowfall
        3. Use sliding window to check if any three consecutive days' sum exceeds half of total snowfall.

    Algorithm Steps:
        1. Convert cumulative snowfall to daily snowfall:
            daily[0] = cumulative[0]
            daily[i] = cumulative[i] - cumulative[i-1] for i > 0

    2. Calculate total snowfall:
        total = cumulative[n-1]

    3. Check all possible 3-day windows:
        For i from 0 to n-3:
        window_sum = daily[i] + daily[i+1] + daily[i+2]
        If window_sum > total/2, return "YES"

    4. If no window satisfies condition, return "NO"

    Time Complexity: O(n)
    Space Complexity: O(n)



Question 2:
    Input File Format:
        Line 1: grid size N
        Subsequent lines: coordinates of initially infected counties

    How to Run:
        1. Place pandemic_input1.txt and pandemic_input2.txt in same directory as pandemic.py
        2. Run: python pandemic.py

    Input:
        Line 1: grid size N
        Subsequent lines: coordinates of initially infected counties

    Output:
        pandemic_input1.txt: There are healthy counties left
        pandemic_input2.txt: There are no healthy counties left

    Algorithm Steps:
        1. Initialize N×N grid with all counties healthy
        2. Mark initially infected counties as infected
        3. Infection Spread Simulation

    4. Check Result:
        Count remaining healthy counties (value = 0)
        If count > 0: "There are healthy counties left"
        Else: "There are no healthy counties left"

    Key Features:
        Boundary-aware: Only considers valid grid coordinates when checking neighbors
        Iterative simulation: Continues until no new infections occur
        4-directional neighborhood: Only horizontal/vertical neighbors considered

    Time Complexity: O(N² × iterations)
    Space Complexity: O(N²)

    Infection Rule:
        A county becomes infected ONLY if it has ≥2 infected neighbors. Single infected neighbor is not sufficient for transmission.



Question 3:
    Goal:
        Find the maximum number of consecutive items you can select.
        This is equivalent to finding the longest contiguous subarray with at most 2 distinct elements.

    Input files:
        sc_input1.txt: 3 categories [dinner, lunch, dinner]
        sc_input2.txt: 5 categories [dinner, lunch, breakfast, lunch, lunch]

    HOW TO RUN:
        1. Place sc_input1.txt and sc_input2.txt in the same directory as shopping_cart.py
        2. Run in terminal: python shopping_cart.py

    ALGORITHM STEPS:
        1. Initialize sliding window [left, right] = [0, 0]
        2. Use dictionary to track category frequencies in current window
        3. Expand window by moving right pointer:
            Add current category to frequency count
        4. While window contains >2 unique categories:
            Remove leftmost category from frequency count
            Move left pointer to shrink window
        5. Update max_items = max(max_items, window_length)
        6. Repeat until right pointer reaches end of array

    TIME COMPLEXITY: O(n)
    SPACE COMPLEXITY: O(1)



Question 4:
    Check three conditions:
        1. Each row contains each symbol at most once
        2. Each column contains each symbol at most once
        3. Each sqrt(n) x sqrt(n) sub-board contains each symbol at most once

    INPUT FILES:
        spg_input1.txt
        spg_input2.txt

    OUTPUT:
        The board is valid
        The board is invalid

    HOW TO RUN:
        1. Place spg_input1.txt and spg_input2.txt in same directory
        2. Run: python symbol_puzzle.py

    ALGORITHM:
        1. Read board size n and symbol list
        2. Read n x n board, dots represent empty cells
        3. Validate rows: check no duplicates in non-empty cells
        4. Validate columns: check no duplicates in non-empty cells  
        5. Validate sub-boards: divide into sqrt(n) x sqrt(n) blocks, check no duplicates
        6. Use set comparison to detect duplicates efficiently

    Time: O(n^2) for n x n board
    Space: O(n) for temporary storage

    KEY FEATURES:
        Handles empty cells (ignored in validation)
        Works for any perfect square n (4, 9, 16, etc.)
        Efficient duplicate detection using sets
