ind = 0
while True:
    tmp = ''
    if (ind < 10):
        tmp = '0' + ind
    else:
        tmp = '' + int

    file = open('art' + tmp +, 'w')