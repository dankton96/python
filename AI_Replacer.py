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
places2add=[]
for c in text[:-4]:
    pattern=c+text[i+1]+text[i+2]+text[i+3]
    if(pattern[0] in numList):
        if(pattern[-1] in letterList):
            if('<i' not in pattern):
                places2add.append(i)
                #print(pattern+'\n')
    i+=1
i=0
for p in places2add:
    text=text[:p]+'<i>'+text[(p+1):]
    i+=1
    for p in places2add[i:]:
        p+=3
outFile=open("CorrectedSub.srt","w")
outFile.write(text)
file.close()
outFile.close()
