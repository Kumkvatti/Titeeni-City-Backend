import secrets
import string
import numpy as np

# Generate N random n character codes, and removes duplicates

N = 10000
n = 16

code_list = [[] for _ in range(N)]

for x in range(0,N):
    s =  (''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(n)))
    if s not in code_list:
        code_list[x] = s

with open('lb_codes.txt', 'w') as f:
    for x in code_list:
        f.write(x + '\n')