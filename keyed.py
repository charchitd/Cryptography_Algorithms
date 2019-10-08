def split_len(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]
key = str(input("Enter the Key of your choice: "))
plaintext = str(input("Enter the Plaintext: "))
def encode(key, plaintext):

    order = {
        int(val): num for num, val in enumerate(key)
    }

    ciphertext = ''
    for index in sorted(order.keys()):
        for part in split_len(plaintext, len(key)):
            try:
                ciphertext += part[order[index]]
            except IndexError:
                continue

    return ciphertext

print(encode(key,plaintext))


	
	
	
	
	
