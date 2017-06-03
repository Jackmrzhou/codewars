#version python2.7.6
class VigenereCipher (object):
	def __init__(self, key, alphabet):
		self.key = key.decode('utf8')
		self.alphabet = alphabet.decode('utf8')

	def encode(self, string):
		string = string.decode('utf8')
		encoded_str = u""
		for i,c in enumerate(string):
			k = self.key[i % len(self.key)]
			if (self.alphabet.find(c) >= 0):
				encoded_str += self.alphabet[(self.alphabet.find(c)+self.alphabet.find(k))%len(self.alphabet)]
			else:
				encoded_str += c
		return encoded_str.encode('utf8')

	def decode(self, string):
		string = string.decode('utf8')
		decoded_str = u""
		for i,c in enumerate(string):
			k = self.key[i % len(self.key)]
			if (self.alphabet.find(c) >= 0):
				decoded_str += self.alphabet[(self.alphabet.find(c)-self.alphabet.find(k)+len(self.alphabet))\
					%len(self.alphabet)]
			else:
				decoded_str += c
		return decoded_str.encode('utf8')

#Test given is wrong!