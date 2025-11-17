def count_vowel_combinations(morse_sequence):
    """
    Count the number of possible vowel sequences that can be derived from a Morse code sequence.
    """
    # Morse code mapping for vowels
    vowel_morse = {'A': '.-','E': '.','I': '..','O': '---','U': '..-'}

    n = len(morse_sequence)
    if n == 0:
        return 0

    #count[i] = number of ways to decode first i characters
    count = [0] * (n + 1)
    count[0] = 1  # empty string

    for i in range(1, n + 1):
        for vowel, code in vowel_morse.items():
            code_len = len(code)
            if i >= code_len and morse_sequence[i - code_len:i] == code:
                count[i] += count[i - code_len]

    return count[n]

# 测试文件内容
files = {
    "vowel_input1.txt": "...-..",
    "vowel_input2.txt": "..---.-..-..-",
    "vowel_input3.txt": "...-.-.---..--......",
    "vowel_input4.txt": ".-..---......-..---.----....---.-....-.-..-.-...---...-.---.-...-....---.------.........---..-....-."
}

for filename, sequence in files.items():
    count = count_vowel_combinations(sequence)
    print(f"File Input: {filename}")
    print(f"The Number of Vowel combinations is: {count}")