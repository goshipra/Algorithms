# function
# input file - textwrap
# read lines and write  odd lines to another file

def get_odd_lines():
    with open('abc.txt', 'rt') as f:
        num_lines = sum(1 for line in open('abc.txt'))
        for i, line in enumerate(f):
            # print(i, line)
            if i % 2 != 0:
            # for line_num in range(1, num_lines, 2):
                print(i, line)

                #### OR ####
def get_odd_lines_alternative():
    with open('abc.txt', 'rt') as input:
        reading_file = input.readlines()
        print(reading_file)
        for i in range(len(reading_file)):
            if i % 2 != 0:
                print(reading_file[i])

read_file = get_odd_lines()
get_odd_lines_alternative()
#print(read_file)
