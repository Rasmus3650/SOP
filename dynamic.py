def dynamic(text, rot, increment):
	result = ""
	inc_int = 0

	for i in range(len(text)):
		char = text[i]
		rot += inc_int
		if(char.isupper() and char != " "):
			result +=chr((ord(char) + rot - 65) % 26 + 65)
		elif (char != " "):
			result += chr((ord(char) + rot - 97) % 26 + 97)
		else:
			result += " "
		inc_int = increment
	return result