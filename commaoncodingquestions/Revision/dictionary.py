# 5. Dictionary

# Count the frequency of each word in a given sentence.
def count(sentence):
    word_list = sentence.lower().split()
    # print(word_list)
    Word_dict = {}

    for word in word_list:
        if word in Word_dict:
            Word_dict[word] = Word_dict[word] + 1
        else:
            Word_dict[word] = 1
    print(Word_dict)            


inp =  "Python is fun fun fun"
# my_dict = count(inp)  


# Find the key with the maximum value in a dictionary.
def max_val(my_dict):

    max_key_value = 0
    max_value_key = ""
    for element in my_dict:
        # print(my_dict[element])
        if my_dict[element] > max_key_value:
            max_key_value = my_dict[element]
            max_value_key = element
        else:
            continue 
    print(max_value_key)   
    
my_dict = {"shipra":13,"kamal": 21,"krishiv": 39}
max_val(my_dict)

# Merge two dictionaries.
def merge_dict(dict1,dict2):
    for element in dict2:
        dict1[element]  = dict2[element]
    print(dict1)

dict1 = {"shipra":13,"kamal": 21,"krishiv": 39}
dict2 = {"ashipra":3,"akamal": 1,"akrishiv": 9}
merge_dict(dict1,dict2)



