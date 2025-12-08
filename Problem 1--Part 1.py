"""
Huffman Encoder (Huffman Encoder)
Input: Text file or long string
Output: Compressed file
Display: Input set, frequency map, Huffman tree
"""

import heapq
import sys

class HuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char  # Character (leaf node)
        self.freq = freq  # Frequency
        self.left = None  # Left child
        self.right = None  # Right child

    def __lt__(self, other):
        return self.freq < other.freq

def display_char(char):
    """Format special characters for display"""
    if char == '\n': return '\\n'
    elif char == '\t': return '\\t'
    elif char == '\r': return '\\r'
    elif char == ' ': return '[space]'
    else: return char

def build_frequency_map(text):
    """Build frequency map"""
    freq_map = {}
    for char in text:
        freq_map[char] = freq_map.get(char, 0) + 1
    return freq_map

def build_huffman_tree(freq_map):
    """Build Huffman tree"""
    heap = []
    for char, freq in freq_map.items():
        heapq.heappush(heap, HuffmanNode(char, freq))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0] if heap else None

def generate_codes(node, current_code="", code_map=None):
    """Generate Huffman codes"""
    if code_map is None:
        code_map = {}

    if node is None:
        return code_map

    if node.char is not None:
        code_map[node.char] = current_code
    else:
        generate_codes(node.left, current_code + "0", code_map)
        generate_codes(node.right, current_code + "1", code_map)

    return code_map

def encode_text(text, code_map):
    """Encode text"""
    encoded = ""
    for char in text:
        encoded += code_map[char]
    return encoded

def save_compressed_file(encoded_text, filename, freq_map):
    """Save compressed file"""
    # Add padding bits
    padding = 8 - (len(encoded_text) % 8)
    if padding == 8:
        padding = 0

    # Create bit string with padding info
    padded_info = format(padding, '08b')
    padded_text = encoded_text + '0' * padding
    full_bit_string = padded_info + padded_text

    # Write to file
    with open(filename, 'wb') as f:
        # Save frequency map
        for char, freq in freq_map.items():
            f.write(f"{ord(char)}:{freq},".encode('utf-8'))
        f.write(b"\n")  # Separator

        # Save encoded data
        for i in range(0, len(full_bit_string), 8):
            byte = full_bit_string[i:i+8]
            f.write(int(byte, 2).to_bytes(1, 'big'))

    return padding

def print_tree(node, prefix="", is_left=True):
    """Print tree structure"""
    if node is None:
        return

    if node.char is not None:
        char_display = display_char(node.char)
        print(f"{prefix}{'└── ' if is_left else '├── '}'{char_display}':{node.freq}")
    else:
        print(f"{prefix}{'└── ' if is_left else '├── '}Internal:{node.freq}")

    if node.left or node.right:
        new_prefix = prefix + ("    " if is_left else "│   ")
        if node.left:
            print_tree(node.left, new_prefix, False)
        if node.right:
            print_tree(node.right, new_prefix, True)

def main():
    """Main function: Execute Huffman encoding"""
    # Use provided test text
    test_content = """Hello World! This is a test of Huffman coding.
1234567890
Special characters: !@#$%^&*()_+-=[]{}|;:,.<>?
Multiple
lines
with
different
lengths."""

    print("=" * 70)
    print("PART 1: HUFFMAN ENCODING")
    print("=" * 70)

    # 1. Print input set
    print("\n1. INPUT SET:")
    print("-" * 40)
    print(test_content)
    print(f"\nTotal characters: {len(test_content)}")

    # 2. Build and print frequency map
    print("\n2. FREQUENCY MAP:")
    print("-" * 40)
    freq_map = build_frequency_map(test_content)
    sorted_freq = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)

    for char, freq in sorted_freq:
        print(f"'{display_char(char)}' (ASCII {ord(char):3d}): {freq}")
    print(f"Total unique characters: {len(freq_map)}")

    # 3. Build and print Huffman tree
    print("\n3. HUFFMAN TREE:")
    print("-" * 40)
    root = build_huffman_tree(freq_map)

    if root:
        print_tree(root)
    else:
        print("Empty tree (input was empty)")
        return

    # 4. Generate Huffman codes and compress
    code_map = generate_codes(root)
    encoded_text = encode_text(test_content, code_map)

    try:
        padding = save_compressed_file(encoded_text, "compressed.bin", freq_map)
        print("\n" + "-" * 40)
        print(f"✓ Compressed file saved: compressed.bin")
        print(f"✓ Original size: {len(test_content)} characters")
        print(f"✓ Encoded bits: {len(encoded_text)}")
        print(f"✓ Padding bits: {padding}")

        # Show part of encoded result
        print(f"\nFirst 100 encoded bits:")
        if len(encoded_text) > 100:
            print(encoded_text[:100] + "...")
        else:
            print(encoded_text)

    except Exception as e:
        print(f"\n✗ Failed to save compressed file: {e}")
        return

    print("\n" + "=" * 70)
    print("ENCODING COMPLETED SUCCESSFULLY")
    print("=" * 70)

if __name__ == "__main__":
    main()