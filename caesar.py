def caesar(text, rot):
	result = ""
	for i in range(len(text)):
		char = text[i]

		if(char.isupper()):
			result +=chr((ord(char) + rot - 65) % 26 + 65)
		else:
			result += chr((ord(char) + rot - 97) % 26 + 97)
	return result