def main():
	
	f = open("readaloud.txt","r+")
	w = open("textoutput.txt","w+")
	lines = f.read()
	w.write(lines.replace('\n', ' '))	
	f.close()
	w.close()
	
	#f = open("readaloud.txt","r+")
	#w = open("textoutput.txt","w+")
	#lines = f.readlines()
	#j = int()
	#j = 0
	#for i in lines:
	#	print(i.replace('\n', ' '))	
	#f.close()
	#w.close()
    
	
	#Open the file back and read the contents
    #f=open("guru99.txt", "r")
    #   if f.mode == 'r': 
    #     contents =f.read()
    #     print contents
    #or, readlines reads the individual line into a list
    #fl =f.readlines()
    #for x in fl:
    #print x
if __name__== "__main__":
	main()