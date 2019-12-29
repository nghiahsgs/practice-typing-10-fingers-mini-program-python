import random as rd
import time
import io
from gtts import gTTS
import os



def text_2_speech(myText):
	#myText="Text to speech conversion using python"

	language='en'

	ouput=gTTS(text=myText,lang=language,slow=False)

	ouput.save("output.mp3")

	os.system('start output.mp3')
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
for i in range(50):
	sentence=generate_random_sentence()
	if(len(sentence)>70):
		continue
	print('-------')
	print(sentence)
	text_2_speech(sentence)
	total_word_test+=len(sentence.split(' '))
	#input('type exactly this sentence: ')
	user_input=input()
	#print(user_input)
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
print('This program will help you break your limit and bring your best out :v')
text_2_speech('This program will help you break your limit and bring your best out :v')

print('total_word_accuracy',total_word_accuracy)
print('total_word_test',total_word_test)
print('accuracy performmance',total_word_accuracy/total_word_test*100.0)
print('total time %s (minutes)'%((time_end-time_start)/60))
print('speed typing %s (word per minute)'%(60*total_word_accuracy/(time_end-time_start)))

