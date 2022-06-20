
with open('song.txt','r') as openfile:
    text_content = openfile.read()
    for t in text_content:
        print(t)

with open('song.txt','r') as openfile:
    line = openfile.readline()
    for t in line:
        print(t)

with open('song.txt','r') as openfile:
    lines = openfile.readlines()
    for t in lines:
        print(t)

# Reading image
with open('image.jpeg','rb') as image1:
    image = image1.read()
    print(image)





