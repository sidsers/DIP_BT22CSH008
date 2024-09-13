class ArithmeticCoder:
    def _init_(self, probabilities):
        self.probabilities = probabilities
        self.cumulative_prob = self.__cumulative_probabilities()

    def __cumulative_probabilities(self):
        cumulative = {}
        total = 0.0
        for symbol, prob in self.probabilities.items():
            cumulative[symbol] = (total, total + prob)
            total += prob
        return cumulative

    def encode(self, sequence):
        low, high = 0.0, 1.0

        for symbol in sequence:
            range_width = high - low
            low, high = (low + range_width * self.cumulative_prob[symbol][0],
                         low + range_width * self.cumulative_prob[symbol][1])

        # Return the final interval's lower bound as the code.
        return (low + high) / 2

    def decode(self, code, length):
        sequence = []
        for _ in range(length):
            for symbol, (low, high) in self.cumulative_prob.items():
                if low <= code < high:
                    sequence.append(symbol)
                    range_width = high - low
                    code = (code - low) / range_width
                    break
        return sequence


# Example Usage

# Probabilities of the pixel values (0, 1, 2, 3)
probabilities = {
    0: 0.1,
    1: 0.4,
    2: 0.2,
    3: 0.3
}

# Create an ArithmeticCoder object with the given probabilities
coder = ArithmeticCoder(probabilities)

# Example sequence of pixel values (to be encoded)
sequence = [1, 3, 2, 1]

# Encode the sequence
encoded_value = coder.encode(sequence)
print("Encoded Value:", encoded_value)

# Decode the value back to the original sequence
decoded_sequence = coder.decode(encoded_value, len(sequence))
print("Decoded Sequence:", decoded_sequence)