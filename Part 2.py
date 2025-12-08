"""
Huffman Decoder (Huffman Decoder)
Input: Compressed file (output of encoder)
Output: Reconstructed document file
Display: Input set
"""

import sys
import heapq  # Import heapq module

class HuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char  # Character (leaf node)
        self.freq = freq  # Frequency
        self.left = None  # Left child
        self.right = None  # Right child

    def __lt__(self, other):
        """Add comparison operator for heap sorting"""
        return self.freq < other.freq

def read_compressed_file(filename):
    """Read compressed file"""
    with open(filename, 'rb') as f:
        # Read frequency map
        freq_data = b""
        while True:
            byte = f.read(1)
            if byte == b'\n' or not byte:
                break
            freq_data += byte

        # Parse frequency map
        freq_map = {}
        if freq_data:
            items = freq_data.decode('utf-8').rstrip(',').split(',')
            for item in items:
                if ':' in item:
                    char_code, freq = item.split(':')
                    freq_map[chr(int(char_code))] = int(freq)

        # Read encoded data
        bit_string = ""
        while True:
            byte = f.read(1)
            if not byte:
                break
            bit_string += format(ord(byte), '08b')

    return freq_map, bit_string

def build_huffman_tree(freq_map):
    """Rebuild Huffman tree from frequency map"""
    heap = []
    for char, freq in freq_map.items():
        node = HuffmanNode(char, freq)
        heapq.heappush(heap, node)  # Push node directly since it has __lt__ method

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0] if heap else None

def decode_text(bit_string, huffman_tree):
    """Decode bit string"""
    # Extract padding information (first 8 bits)
    padding = int(bit_string[:8], 2)

    # Remove padding info bits and padding bits
    encoded_bits = bit_string[8:]
    if padding > 0:
        encoded_bits = encoded_bits[:-padding]

    # Decode
    decoded_text = ""
    current_node = huffman_tree

    for bit in encoded_bits:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = huffman_tree

    return decoded_text

def display_char(char):
    """Format special characters for display"""
    if char == '\n': return '\\n'
    elif char == '\t': return '\\t'
    elif char == '\r': return '\\r'
    elif char == ' ': return '[space]'
    else: return char

def main():
    """Main function: Execute Huffman decoding"""
    print("=" * 70)
    print("PART 2: HUFFMAN DECODING")
    print("=" * 70)

    # 1. Print input set (compressed file information)
    print("\n1. INPUT SET (Compressed File):")
    print("-" * 40)

    try:
        freq_map, bit_string = read_compressed_file("compressed.bin")
        print(f"File: compressed.bin")
        print(f"Total bits read: {len(bit_string)}")
        print(f"Frequency map entries: {len(freq_map)}")

        # Show part of bit string
        print(f"\nFirst 100 bits of encoded data:")
        if len(bit_string) > 100:
            print(bit_string[:100] + "...")
        else:
            print(bit_string)

        # Show part of frequency map
        print(f"\nFirst 10 frequency map entries:")
        sorted_freq = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
        for i, (char, freq) in enumerate(sorted_freq[:10]):
            print(f"  '{display_char(char)}' (ASCII {ord(char):3d}): {freq}")
        if len(sorted_freq) > 10:
            print(f"  ... and {len(sorted_freq)-10} more entries")

    except FileNotFoundError:
        print("Error: compressed.bin not found")
        print("Please run huffman_encoder.py first")
        return

    # 2. Rebuild Huffman tree
    print("\n2. RECONSTRUCTING HUFFMAN TREE...")
    huffman_tree = build_huffman_tree(freq_map)
    if huffman_tree:
        print("✓ Huffman tree reconstructed successfully")
    else:
        print("✗ Failed to reconstruct Huffman tree")
        return

    # 3. Decode
    print("\n3. DECODING TEXT...")
    decoded_text = decode_text(bit_string, huffman_tree)
    print(f"✓ Decoded {len(decoded_text)} characters")

    # 4. Save reconstructed document
    print("\n4. SAVING RECONSTRUCTED DOCUMENT:")
    print("-" * 40)

    try:
        with open("decompressed.txt", 'w', encoding='utf-8') as f:
            f.write(decoded_text)
        print("✓ Reconstructed document saved: decompressed.txt")
    except Exception as e:
        print(f"✗ Failed to save file: {e}")
        return

    # 5. Show first 200 characters of reconstructed document
    print("\n5. RECONSTRUCTED DOCUMENT (first 200 characters):")
    print("-" * 40)
    if len(decoded_text) > 200:
        print(decoded_text[:200] + "...")
    else:
        print(decoded_text)

    print("\n" + "=" * 70)
    print("DECODING COMPLETED SUCCESSFULLY")
    print("=" * 70)

if __name__ == "__main__":
    main()