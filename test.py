import random
import os
message = '8d 1012'
luckynumber = ""
if message[0].isnumeric():
    if message[1] =='d':
        ttl=0
        ass = type(luckynumber)
        print(ass)
        luckynumber = ""
        for g in range(int(message[0])):
            randnum = random.randint(1,20)
            luckynumber = luckynumber + str(randnum) + '\n'
            ttl = ttl + randnum
            
        no_leading_num_message = message[2:]
        ass = type(no_leading_num_message.strip())
        print(ass)
        luckynumber = luckynumber + no_leading_num_message.strip() + '\n' + 'ttl: ' + str(ttl) + '\n' + 'avg: ' 
        print(luckynumber)