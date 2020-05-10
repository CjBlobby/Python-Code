Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	print(' Want to make a story?')
	noun = input('Type a noun, eg. tree.')
	noun2 = input('Type another noun.')
	adj = input('Type an adjective, eg. fast.')
	adv = input('Type an adverb, eg. quickly.')
	verb = ('Type a verb, eg. run.)
		
SyntaxError: EOL while scanning string literal
>>> 
	      
SyntaxError: EOL while scanning string literal
def main():
	print(' Want to make a story?')
	noun = input('Type a noun, eg. tree.')
	noun2 = input('Type another noun.')
	adj = input('Type an adjective, eg. fast.')
	adv = input('Type an adverb, eg. quickly.')
	verb = ('Type a verb, eg. run.')
	print('It was a very good story')
	print('The ',noun,'was ',adj,' and the ',noun2 ,adv ,verb,' on it.')

main()
                
