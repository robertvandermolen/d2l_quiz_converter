#convert the awesome checkit program to a D2L quiz



#prompt user for files
what=input('what bank file to convert: ')
who=input('what name for the file of the quiz: ')
name=input('what do you want to title these type of question: ')


#for testing
#what='bank.txt'
#who='test_dump'
#name='E1'




#open up your bank
bank=open(what, "r")

dump=open(who+'.csv','w')


inQuestion=0

qCounter=0
theQuest=''
for line in bank:
	
	
	try:
		if line.split()[0]=='<div':
			if line.split()[1]=='class="exercise-statement">':
				if inQuestion==0:
					qCounter=qCounter+1
					print("NewQuestion,WR",file=dump)
					print("Title, "+name+"."+str(qCounter),file=dump)
					theQuest='QuestionText, "<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"></script>'
					inQuestion=1
	except:
		pass
	

	
	
	if inQuestion==1:
		if len(line.split())!=0:
			theQuest=theQuest+line
		
	try:
		if inQuestion==1:
			if line.split()[0]=='</div>':
				inQuestion=0
				dump.write(theQuest+'",HTML,')
				print('points,1',file=dump)
	except:
		pass
	
	
	
	
bank.close()
dump.close()


