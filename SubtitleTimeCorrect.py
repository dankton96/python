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
#time diference to correct -00:01:26,647
TimeDifStr='10/10/2000 00:01:26,647'
TimeDif=datetime.datetime.strptime(TimeDifStr, '%d/%m/%Y %H:%M:%S,%f')
for p in places2calc:
        p1Str='10/10/2000 '+lines[p][:12]
        p2Str='10/10/2000 '+lines[p][17:]
        p1=datetime.datetime.strptime(p1Str, '%d/%m/%Y %H:%M:%S,%f')
        p2=datetime.datetime.strptime(p2Str, '%d/%m/%Y %H:%M:%S,%f')
        newP1=p1-TimeDif
        newP2=p2-TimeDif
        p1Str=str(newP1)
        p2Str=str(newP2)
        newline="{:02d}:{:02d}:{:06.3f}".format(int(p1Str[:1]),int(p1Str[2:4]),float(p1Str[5:]))+' --> '+"{:02d}:{:02d}:{:06.3f}".format(int(p2Str[:1]),int(p2Str[2:4]),float(p2Str[5:]))
        i=0
        newline=newline.replace('.',',')
        lines[p]=newline
places2calc.clear()
for c in lines:
    if(len(c)<=3):
        if(c.isnumeric()):
            places2calc.append(i)
    i+=1
for n in places2calc:
    lines[n]=str((int(lines[n])-33))
#    i=0
#    for c in lines[n]:
#        if(c=='.'):
#            lines[n][i]=','
#        i+=1
file.close()
newFile="CorrectedSub.srt"
file=open(newFile,'w')
for l in lines:
    file.write(l+'\n')
file.close()
