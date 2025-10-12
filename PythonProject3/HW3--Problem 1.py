def is_palindrome(s):
    """Check if a string is a palindrome."""
    #Remove any whitespace and convert to lowercase for case-insensitive comparison
    s = s.strip().lower()
    return s == s[::-1]


def process_palindromes(input_file):
    """Process the input file and check for palindromes."""
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        palindrome_count = 0
        results = []

        for line in lines:
            #Remove newline characters and check if palindrome
            string = line.strip()
            if string:
                palindrome = is_palindrome(string)
                results.append(str(palindrome).lower())
                if palindrome:
                    palindrome_count += 1

        #Output results
        for result in results:
            print(result)
        print(palindrome_count)


    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return [], 0

#main
if __name__ == "__main__":
    #Replace with your actual file name
    process_palindromes('palendrome_0L.txt')