class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def build_huffman_tree(data):
    frequency = {}
    for char in data:
        frequency[char] = frequency.get(char, 0) + 1

    nodes = [HuffmanNode(char, freq) for char, freq in frequency.items()]

    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.freq)
        left, right = nodes.pop(0), nodes.pop(0)
        merged_node = HuffmanNode(None, left.freq + right.freq)
        merged_node.left, merged_node.right = left, right
        nodes.append(merged_node)

    return nodes[0]

def huffman_encode(data):
    root = build_huffman_tree(data)
    huffman_codes = {}

    def build_codes(node, code):
        if node.char:
            huffman_codes[node.char] = code
        if node.left:
            build_codes(node.left, code + '0')
        if node.right:
            build_codes(node.right, code + '1')

    build_codes(root, '')

    encoded_data = ''.join(huffman_codes[char] for char in data)
    return encoded_data, huffman_codes

def huffman_decode(encoded_data, huffman_codes):
    reverse_codes = {code: char for char, code in huffman_codes.items()}

    decoded_data = ''
    code = ''
    for bit in encoded_data:
        code += bit
        if code in reverse_codes:
            decoded_data += reverse_codes[code]
            code = ''

    return decoded_data

data = input("Enter input characters: ")
encoded_data, huffman_codes = huffman_encode(data)
decoded_data = huffman_decode(encoded_data, huffman_codes)

print("Original data:", data)
print("Encoded data:", encoded_data)
for char, code in huffman_codes.items():
    print(f"{char}\t\t{code}")
print("Decoded data:", decoded_data)
