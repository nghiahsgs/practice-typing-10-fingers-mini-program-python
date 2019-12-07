import random as rd
import time

list_chars=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#list_chars+=[',','.','/',';']
#list_chars+=[',','.','/',';']
len_list_chars=len(list_chars)
def gen_random_string(length_string):
	kq=''
	for i in range(length_string):
		index_random_char=rd.randint(0,len_list_chars)
		#print(index_random_char)
		#print(list_chars[index_random_char])
		kq+=list_chars[index_random_char]
	return kq
	
def generate_random_sentence(nbs_words):
	new_sentence=''
	length_string=5 #because word is random
	for i in range(nbs_words):
		try:
			new_sentence+=gen_random_string(length_string)+' '
		except:
			pass
	new_sentence=new_sentence[:-1]
	return new_sentence

print('You need complete 10 random sentences!')
print('Type correctly one sentence in order to appear next sentence')
print('--------BETTER THAN YESTERDAY------')
nbs_words=5
total_word_test=0
total_word_accuracy=0

time_start=int(time.time())
for i in range(2):
	sentence=generate_random_sentence(nbs_words)
	print('-------')
	print(sentence)
	total_word_test+=len(sentence.split(' '))
	#input('type exactly this sentence: ')
	user_input=input()
	'''
	if(user_input==sentence):
		print('good')
	else:
		print('try other sentence')
	'''
	#check number type correctly
	for word in user_input.split(' '):
		if word in sentence:
			total_word_accuracy+=1
time_end=int(time.time())

print('--------YOUR RESULT------')
print('total_word_accuracy',total_word_accuracy)
print('total_word_test',total_word_test)
print('accuracy performmance',total_word_accuracy/total_word_test*100.0)
print('total time',time_end-time_start)
print('speed typing %s (word per minute)'%(60*total_word_accuracy/(time_end-time_start)))

