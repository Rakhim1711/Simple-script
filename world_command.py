print("Hello World")

def world():
    print('Hi World')

def new_function(string):

    count = 0
    for x in string:
        if x == 'a':
            count += 1
    print(count)

new_function('aaaabbbbbcccc')