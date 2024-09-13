import heapq
from collections import defaultdict

# A node of the Huffman tree
class HuffmanNode:
    def _init_(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Comparator method to make the nodes comparable
    def _lt_(self, other):
        return self.freq < other.freq

# Function to build the Huffman Tree
def build_huffman_tree(frequency):
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0]  # Root of the tree

# Function to generate Huffman codes from the tree
def generate_codes(node, prefix="", codebook={}):
    if node is None:
        return

    if node.char is not None:  # It's a leaf node
        codebook[node.char] = prefix
    generate_codes(node.left, prefix + "0", codebook)
    generate_codes(node.right, prefix + "1", codebook)

    return codebook

# Function to encode text using Huffman coding
def huffman_encoding(text):
    if not text:
        return "", None

    # Step 1: Calculate the frequency of each character
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1

    # Step 2: Build the Huffman tree
    root = build_huffman_tree(frequency)

    # Step 3: Generate the Huffman codes
    huffman_codes = generate_codes(root)

    # Step 4: Encode the text
    encoded_text = ''.join(huffman_codes[char] for char in text)

    return encoded_text, root

# Function to decode the encoded text using the Huffman tree
def huffman_decoding(encoded_text, tree):
    decoded_text = []
    node = tree
    for bit in encoded_text:
        node = node.left if bit == "0" else node.right
        if node.left is None and node.right is None:  # It's a leaf node
            decoded_text.append(node.char)
            node = tree  # Go back to the root

    return ''.join(decoded_text)

# Example usage:
if _name_ == "_main_":
    text = "hello huffman"
    encoded_text, tree = huffman_encoding(text)
    print(f"Encoded text: {encoded_text}")
    
    decoded_text = huffman_decoding(encoded_text, tree)
    print(f"Decoded text: {decoded_text}")