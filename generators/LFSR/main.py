# Регистр сдвига с линейной обратной связью
class LFSR:
    def __init__(self, input_values, fpoly=[5, 2]):
        self.input_values = input_values


s = int('0b100', 2)

new = bin(s >> 1)

print(new)
