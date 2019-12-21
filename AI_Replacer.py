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
pattern=''
i=0
j2n=False
places2add=[]
############################## PROBLEM HERE (I GUESS) ##########################################
for c in text[:-3]:
    pattern=c+text[i+1]+text[i+2]
    if(pattern=='/i>'):
        j2n=False
    if(pattern[0] in numList):
        if(pattern[-1] in letterList):
            if(('<i>' not in pattern) and ('<' not in pattern) and ('<i' not in pattern) and ('i>' not in pattern) and ('>' not in pattern) ):
                if('\r\n' not in pattern[1:-1]):
                    if(not j2n):
                        places2add.append(i)
                        j2n=True
                        #print(pattern+'\n')
    i+=1
#################################################################################################
for p in places2add:
    text=text[:(p+2)]+'<i>'+text[(p+2):]
outFile=open("CorrectedSub.srt","w")
outFile.write(text)
file.close()
outFile.close()
