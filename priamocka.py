from PIL import Image
pic = Image.new("RGB", (250,250), "white")
pixels = pic.load()
pic.save("obrazok.png")
A = (50,10)
B = (50,100)
p1=(B[1]-A[1])
p2=(B[0]-A[0])
if p2 >0:
    k = p1/p2
    q = A[1] - k*A[0]

    for x in range(A[0], B[0]):
        y =  int(k*x + q)
        pixels[x,y] = (0,0,0)
if p2==0:

    for y in range(A[1], B[1]):
        x =  A[0]
        pixels[x,y] = (0,0,0)
if p1==0:
     for x in range(A[0], B[0]):
        y =  A[1]
        pixels[x,y] = (0,0,0)
pic.save("obrazok.png")
