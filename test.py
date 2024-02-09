import random
import os
message = 'a b c'
message = message.split(" ", 1)
message = message + message[1].split(" ", 1)
for t in message:
    print(t)