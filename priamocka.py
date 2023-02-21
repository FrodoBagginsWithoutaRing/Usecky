import PIL.ImageColor
from PIL import Image
#na zaciatku budeme mat dva body a nasou ulohou je pixel po pixli vykreslit usečku (a,b)(c,d),,,a<c,   b<d
#doplnit tak aby to fungovalo vzdy !!!!!!
#input dlzku!!!DONE!!
a=input('Zadaj suradnice bodu A: ')
A=[]
temp=''
for i in range(len(a)):

    if a[i]==',':
        A.append(int(temp))
        temp=''
    else:
        temp=temp+a[i]
        if i==(len(a)-1):
            A.append(int(temp))
b=input('Zadaj suradnice bodu B: ')
B=[]
temp=''
for i in range(len(b)):

    if b[i]==',':
        B.append(int(temp))
        temp=''
    else:
        temp=temp+b[i]
        if i==(len(b)-1):
            B.append(int(temp))
if A[0]>B[0] or A[1]>B[1]:
    C=[]
    C=A
    A=B
    B=C
pic=Image.new('RGB',(250,250),'white')
pixels=pic.load()
if (B[0]-A[0]>B[1]-A[1]):
    k = (B[1]-A[1])/(B[0]-A[0])
    q=A[1]-k*A[0]
    for x in range(A[0],B[0]):
        y=(k*x+q)
        pixels[x,y]=(0,0,0)
if (B[0]-A[0]<B[1]-A[1]):
    k = (B[1]-A[1])/(B[0]-A[0])
    q=A[1]-k*A[0]
    for y in range(A[1],B[1]):
        x=int((y-q)/k)
        pixels[x,y]=(0,0,0)
if A[0]==B[0]or A[1]==B[1]:
    if A[0]==B[0]:
        x=A[0]
        for y in range(A[1],B[1]):
            pixels[x,y]=(0,0,0)
    if A[1]==B[1]:
        y=A[1]
        for x in range(A[0],B[0]):
            pixels[x,y]=(0,0,0)
pic.show()
