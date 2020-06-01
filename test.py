import random
from bisect import bisect_left
import time

def test():
    a = [0.1, 0.2, 0.33, 0.44]
    total = sum(a)
    probabilities = [0]

    for x in a:
        probabilities.append(probabilities[-1] + x / total)
    print(probabilities)
    random.seed(time.time())
    def  rand():
        x = random.random()
        idx = bisect_left(probabilities, x) - 1
        return idx

    cnt = 10000000
    used = [0] * (len(a))
    for i in range(cnt):
        t = rand()
        used[t] += 1
    for i in range(len(used)):
        used[i] /= cnt
    print(used)

test()