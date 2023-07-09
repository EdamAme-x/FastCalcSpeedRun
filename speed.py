import random
import math

suc = 0;
fail = 0;

while True:
    first = 100 * random.random()
    secd = 100 * random.random()

    print(f'{math.floor(first)} + {math.floor(secd)} = ')
    ans = int(input())

    if math.floor(first) + math.floor(secd) == ans:
        print("ok : " + str(suc + 1))
        suc += 1;
    else:
        print("fail : " + str(fail + 1))
        fail += 1;