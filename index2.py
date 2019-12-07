import random as rd
import time
import io
	
def generate_random_sentence():
	file_name='list_sentences.txt'
	file=io.open(file_name,mode='r',encoding='utf8')
	list_lines=file.read()
	list_lines=list_lines.split('\n')
	
	index_random_sentence=rd.randint(0,len(list_lines)-1)
	random_sentence=list_lines[index_random_sentence]
	file.close()
	
	return random_sentence.lower()

print('You need complete 5 random sentences!')
print('Type correctly one sentence in order to appear next sentence')
print('--------BETTER THAN YESTERDAY------')
total_word_test=0
total_word_accuracy=0

time_start=int(time.time())
for i in range(5):
	sentence=generate_random_sentence()
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
print('total time %s (minutes)'%((time_end-time_start)/60))
print('speed typing %s (word per minute)'%(60*total_word_accuracy/(time_end-time_start)))

