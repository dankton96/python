import datetime
import easygui
numList=['0','1','2','3','4','5','6','7','8','9']
letterList=['a','b','c','d','e','f','g','i','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
FilePath=easygui.fileopenbox("Selecione o arquivo a ser manipulado:")
file=open(FilePath,'r+')
sub=[]
for sc in file:
    sub.append(sc)
text=''
for i in sub:
    text+=str(i)
i=0
places2calc=[]
lines=text.splitlines()
for l in lines:
    if(i!=0):
        if(len(lines[i-1])<=3):
            if(len(lines[i])==29):
                #print(l)
                places2calc.append(i)
    else:
        #print(l)
        places2calc.append(i)
    i+=1
i=0
for p in places2calc:
    if(len(lines[i])!=29):
        del(places2calc[i])
    i+=1
#newline=''
#time diference to correct -00:01:26,647
TimeDifStr='10/10/2000 00:01:26,647'
TimeDif=datetime.datetime.strptime(TimeDifStr, '%d/%m/%Y %H:%M:%S,%f')
for p in places2calc:
        p1Str='10/10/2000 '+lines[p][:12]
        p2Str='10/10/2000 '+lines[p][17:]
        p1=datetime.datetime.strptime(p1Str, '%d/%m/%Y %H:%M:%S,%f')
        p2=datetime.datetime.strptime(p2Str, '%d/%m/%Y %H:%M:%S,%f')
        #print(p1,p2, sep='\n')
        newP1=p1-TimeDif
        newP2=p2-TimeDif
        print(str(newP1),str(newP2),sep='\n')
        
#00:02:26,647 --> 00:02:29,617
numPlaces=[0,1,3,4,6,7,9,10,11,17,18,20,21,23,24,26,27,28]
file.close()
#outFile.close()
