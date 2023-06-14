from PIL import Image
pic = Image.new("RGB", (250,250), "white")
pixels = pic.load()
pic.save("obrazok.png")
A = (2,2)
B = (100,50)

k = (B[1]-A[1])/(B[0]-A[0])
q = A[1] - k*A[0]

for x in range(A[0], B[0]):
    y =  int(k*x + q)
    pixels[x,y] = (0,0,0)
pic.save("obrazok.png")
