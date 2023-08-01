import random

prefix = [135,178,132,134,187]

def get_phone():
    index = random.randint(0,len(prefix) -1)
    phone = str(prefix[index])
    for i in range(0,8):
        phone += str(random.randint(0,9))
    return phone

