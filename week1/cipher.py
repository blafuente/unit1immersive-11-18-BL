# Caesar Cipher
# Given a string, print the Caesar Cipher (or ROT13) of that string. What is Caesar Cipher? http://practicalcryptography.com/ciphers/caesar-cipher/

# Use your solution to decipher the following text: "lbh zhfg hayrnea jung lbh unir yrnearq"

def decrypt_function(encrypted_letter):
	try:
		number = encrypted_list.index(encrypted_letter)
	except ValueError:
		# Do this!
		decrpyted_message.append(encrypted_letter)
	else:
		decrpyted_message.append(decrpyted_list[number])

message = "lbh zhfg hayrnea jung lbh unir yrnearq!"
decrpyted = "abcdefghijklmnopqrstuvwxyz"
encrypted = "nopqrstuvwxyzabcdefghijklm"
message_list =  list(message)
decrpyted_list = list(decrpyted)
encrypted_list = list(encrypted)
decrpyted_message = []

for i in range(0,len(message_list)):
	decrypt_function(message_list[i])

final_decrypted_message = "".join(decrpyted_message)
print (final_decrypted_message)

