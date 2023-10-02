import codecs
import re
with codecs.open("_chat.txt",'r',encoding='utf-8',errors='ignore') as fdata:
    text=fdata.readlines()
    lines = len(text)
    pollcount =0
    for eachline in text:
        if 'POLL' in eachline:
            pollcount=pollcount+1
    print('Total Number of lines:', lines)
    print('Total polls: '+str(pollcount))
    count=0;
    user=input("Enter user's full name to get details(no.of chats,last chat timing,last chat) :")
    usern=user+':'
    for x in text:
        if re.search(usern,x):
            count+=1;
            line=x;
if count!=0:
    print("No of messages               :",count)
    d=line.split(" ")
    print("The date of the last message :",d[0].strip("[,"))
    print("The time of the last message :",d[1].rstrip("]"))
    y=line.split(": ")
    # print("the last message is ",line.lstrip(newuser))0
    print("The last message is          :",y[1])
    
    

else:
    print("no such member is found in the chat")

