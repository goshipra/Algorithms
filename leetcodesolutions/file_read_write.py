
with open('song.txt','r') as openfile:
    text_content = openfile.read()
    # print(text_content) print all content of a file
    for t in text_content:
        # print(t) reads every characters and prints in each line
        pass

with open('song.txt','r') as openfile:
    line = openfile.readline()
    # print(line) print first line
    for t in line:
        # print(t) print fist line all charactes if not specified
        pass

with open('song.txt','r') as openfile:
    lines = openfile.readlines()
    print(lines)
    for t in lines:
        # print(t) This will print each line from file
        pass

# Reading image
with open('img.png','rb') as image1:
    image = image1.read()
    # print(image)





