import heapq

# Function to generate the Shannon-Fano codes
def shannon_fano_coding(symbols, prefix=""):
    # Base case: If there is only one symbol, return its code
    if len(symbols) == 1:
        return {symbols[0][0]: prefix}

    # Sort symbols by frequency
    symbols = sorted(symbols, key=lambda x: x[1], reverse=True)
    
    # Find the point to split the symbols into two parts with nearly equal total frequency
    total = sum([freq for _, freq in symbols])
    running_sum = 0
    split_point = 0
    for i, (symbol, freq) in enumerate(symbols):
        running_sum += freq
        if running_sum >= total / 2:
            split_point = i + 1
            break

    # Recursively generate codes for each part
    left_codes = shannon_fano_coding(symbols[:split_point], prefix + "0")
    right_codes = shannon_fano_coding(symbols[split_point:], prefix + "1")

    # Combine the codes
    left_codes.update(right_codes)
    return left_codes

# Function to encode a message using Shannon-Fano coding
def shannon_fano_encode(message):
    # Calculate frequency of each symbol
    frequency = {}
    for char in message:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Generate Shannon-Fano codes
    symbols = [(char, freq) for char, freq in frequency.items()]
    codes = shannon_fano_coding(symbols)

    # Encode the message
    encoded_message = ''.join(codes[char] for char in message)
    return encoded_message, codes

# Function to decode a Shannon-Fano encoded message
def shannon_fano_decode(encoded_message, codes):
    # Create a reverse mapping from code to symbol
    reverse_codes = {code: char for char, code in codes.items()}

    # Decode the message
    decoded_message = []
    buffer = ""
    for bit in encoded_message:
        buffer += bit
        if buffer in reverse_codes:
            decoded_message.append(reverse_codes[buffer])
            buffer = ""

    return ''.join(decoded_message)

# Example usage
if _name_ == "_main_":
    message = "shannonfano"
    encoded_message, codes = shannon_fano_encode(message)
    print(f"Original Message: {message}")
    print(f"Encoded Message: {encoded_message}")
    print(f"Shannon-Fano Codes: {codes}")

    decoded_message = shannon_fano_decode(encoded_message, codes)
    print(f"Decoded Message: {decoded_message}")