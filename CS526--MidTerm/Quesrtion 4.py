def validate_symbol_puzzle(filename):
    try:
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]
            n = int(lines[0])
            symbols = lines[1].split(',')
            board = []

            # Read the board
            for i in range(2, 2 + n):
                row = lines[i].split(',')
                board.append(row)

            # Validate rows
            for i in range(n):
                row_symbols = [cell for cell in board[i] if cell != '.']
                if len(row_symbols) != len(set(row_symbols)):
                    return False

            # Validate columns
            for j in range(n):
                col_symbols = [board[i][j] for i in range(n) if board[i][j] != '.']
                if len(col_symbols) != len(set(col_symbols)):
                    return False

            # Validate sub-boards
            sub_size = int(n ** 0.5)
            for box_i in range(sub_size):
                for box_j in range(sub_size):
                    sub_symbols = []
                    for i in range(box_i * sub_size, (box_i + 1) * sub_size):
                        for j in range(box_j * sub_size, (box_j + 1) * sub_size):
                            if board[i][j] != '.':
                                sub_symbols.append(board[i][j])
                    if len(sub_symbols) != len(set(sub_symbols)):
                        return False

            return True

    except Exception as e:
        print(f"Error processing {filename}: {e}")
        return False

def check_all_puzzle_files():
    """Process all symbol puzzle input files"""
    files = ['spg_input1.txt', 'spg_input2.txt']

    for filename in files:
        is_valid = validate_symbol_puzzle(filename)
        result = "valid" if is_valid else "invalid"
        print(f"The board is {result}")

if __name__ == "__main__":
    check_all_puzzle_files()