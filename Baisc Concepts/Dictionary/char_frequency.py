def char_frequency(text: str):
    frequency = {}

    for char in text.lower():

        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


char_frequency('sanket')
print(char_frequency('sankets'))
