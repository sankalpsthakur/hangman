from string import ascii_lowercase
import random
import string
import collections

class hangman:

	def KMPSearch(self, dictw, clean): 
		M = len(dictw) 
		N = len(clean) 
		ans = []

		# create lps[] that will hold the longest prefix suffix  
		# values for pattern 
		lps = [0]*M 

		# Preprocess the pattern (calculate lps[] array) 
		self.computeLPSArray(dictw, M, lps) 

		j = 0 # index for dictw[] 
		i = 0 # index for clean[] 
		
		while i < N: 
			if dictw[j] == clean[i] or clean[i]=='.': 
				i += 1
				j += 1

			if j == M: 
				# print "Found pattern at index " + str(i-j) 
				for k in range(i-j,i):
					if '.' in clean[k]:
						ans.append(i-j)

				

				j = lps[j-1]
				# print(ans) 

			# mismatch after j matches 
			elif i < N and dictw[j] != clean[i] and clean[i]!='.': 
				# Do not match lps[0..lps[j-1]] characters, 
				# they will match anyway 
				if j != 0: 
				    j = lps[j-1] 
				else: 
				    i += 1
		return ans
  
	def computeLPSArray(self, dictw, M, lps): 
	    len = 0 # length of the previous longest prefix suffix 
	  
	    lps[0] # lps[0] is always 0 
	    i = 1
	  
	    # the loop calculates lps[i] for i = 1 to M-1 
	    while i < M: 
	        if dictw[i]== dictw[len]: 
	            len += 1
	            lps[i] = len
	            i += 1
	        else: 
	            # This is tricky. Consider the example. 
	            # AAACAAAA and i = 7. The idea is similar  
	            # to search step. 
	            if len != 0: 
	                len = lps[len-1] 
	  
	                # Also, note that we do not increment i here 
	            else: 
	                lps[i] = 0
	                i += 1

	def __inti__(self):
		c_dictionary = open("words_250000_train.txt","r+")
		current_dictionary = c_dictionary.read().splitlines()
		c_dictionary.close()
		global zclean
		
	
	#matches pattern of alphabets in a word
	def appendable(self,clean,dictw):
		dec=True
		if len(clean)!=len(dictw):
			dec=False
		elif len(clean)==len(dictw):
			for i in range(len(clean)):
				if clean[i]=='.': 
					continue
				if clean[i]!=dictw[i]: 
					dec= False 
					break
		return dec
	        


	
	def guess(self,word):
		
		clean_word = word[::2].replace("_",".")
		
		guessed_letters=['e','c','r','n']
		wrong_guesses=[letter for letter in guessed_letters if letter not in clean_word]
		# print(clean_word)

		c_dictionary = open("words_250000_train.txt","r+")
		current_dictionary = c_dictionary.read().splitlines()
		c_dictionary.close()
		new_dictionary=[]

		len_word = len(clean_word)

		
		for dict_word in current_dictionary: 
			if self.appendable(clean_word,dict_word):
				new_dictionary.append(dict_word)

		# for dict_word in current_dictionary:
		# 	for wg in wrong_guesses:
		# 		if wg in dict_word:
		# 			try: new_dictionary.remove(dict_word)
		# 			except: ValueError
						
		# print(new_dictionary)
	    	
	    
	 #    print(wrong_guesses)

		for letter in wrong_guesses:
			new_dictionary=[word for word in new_dictionary if letter not in word]

		# print(new_dictionary)

		words_containing_letter = []
		for alphabet in ascii_lowercase:
			freq=0
			for word in new_dictionary:  
			    if alphabet in word:
			        freq+=1
			words_containing_letter.append(freq)   

		
		# print(new_dictionary)


		char_list=[i for i in ascii_lowercase]
		sorted_list_wcl = sorted(zip(char_list,words_containing_letter) , key=lambda x:x[1], reverse=True)
		
		final_char_list=[lis[0] for lis in sorted_list_wcl if lis[1]!=0]
		# print(sorted_list_wcl)
		# print(final_char_list)

		guess_letter = '!'
		for letter in final_char_list:
		    if letter not in guessed_letters:
		        guess_letter = letter
		        break
		
		# random.choice(string.ascii_lowercase) not in guessed_letters
		# if guess_letter == '!':
		#     sorted_letter_count = self.full_dictionary_common_letter_sorted
		#     for letter,instance_count in sorted_letter_count:
		#         if letter not in self.guessed_letters:
		#             guess_letter = letter
		#             break

		
		if guess_letter == '!':
			wl=[]
			for word in current_dictionary:
				ar=self.KMPSearch(word,clean_word)
				# print(self.KMPSearch(word,clean_word))
				if ar:	
					for k in range(ar[0],ar[0]+len(word)-1):
						if clean_word[k]=='.':
							wl.append(word[k-ar[0]])

			wl=collections.Counter("".join(wl)).most_common()
			wl=[lis[0] for lis in wl if lis[1]!=0]
			# print(wl)
			for letter in wl:
			    if letter not in guessed_letters:
			        guess_letter = letter
			        break


		if guess_letter == '!':
		    sorted_letter_count = self.full_dictionary_common_letter_sorted
		    for letter,instance_count in sorted_letter_count:
		        if letter not in self.guessed_letters:
		            guess_letter = letter
		            break
		
		# print(guess_letter)


		# if clean[i]=='.':
		# 	lst.append(dict[i])
		        
		guessed_letters.append(guess_letter)

		# print(guessed_letters)
		zclean=clean_word
		
		# print(random.choice(string.ascii_lowercase))

		zguess=guess_letter
		# print(guess_letter)
		return guess_letter



var=hangman()
print(var.guess('_ _ r c _ c e _ e'))







# print(ma.KMPSearch('smur','unsmu.ness'))

# print(ma.guess('u n u _ u _ n e s s '))






# word.count(alphabet)


# for alphabet in ascii_lowercase:
# 	freq=0
# 	char_list=( alphabet,  if alphabet in word for word in new_dictionary)

# print(char_list)
