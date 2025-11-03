def shopping_cart(filename):
    try:
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]
            n = int(lines[0])
            categories = lines[1].split(',')

            # Use sliding window to find longest subarray with at most 2 distinct categories
            max_items = 0
            left = 0
            category_count = {}

            for right in range(n):
                current_category = categories[right]
                category_count[current_category] = category_count.get(current_category, 0) + 1

                # Shrink window if we have more than 2 unique categories
                while len(category_count) > 2:
                    left_category = categories[left]
                    category_count[left_category] -= 1
                    if category_count[left_category] == 0:
                        del category_count[left_category]
                    left += 1

                # Update maximum items count
                max_items = max(max_items, right - left + 1)

            return max_items

    except Exception as e:
        print(f"Error processing {filename}: {e}")
        return 0

def check_all_shopping_files():
    """Process all shopping cart input files"""
    files = ['sc_input1.txt', 'sc_input2.txt']

    for filename in files:
        result = shopping_cart(filename)
        print(f"{result} items were selected")

if __name__ == "__main__":
    check_all_shopping_files()