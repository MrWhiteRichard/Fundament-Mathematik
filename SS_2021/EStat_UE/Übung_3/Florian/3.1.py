import random

n = 1000
succ = 0


for i in range(n):
    x = [0,0]
    while x[0] <= 8 and x[1] <= 6:
        rand = random.randint(0,1)
        if rand:
            x[0] += 1
        else:
            x[1] += 1
        if x[0] == 8 and x[1] == 6:
            succ += 1

print("P(robot reaches (8,6)) is approximately {}".format(succ/n))

n = 1_000_000
succ = 0
sanity_check = 0

for i in range(n):
    x = [0,0]
    while abs(x[0] - x[1]) < 2:
        if sum(x)%2 == 0:
            rand = random.randint(0,2)
            if rand <= 1:
                x[0] += 1
            else:
                x[1] += 1
        else:
            rand = random.randint(0,3)
            if rand == 0:
                x[0] += 1
            else:
                x[1] += 1
    if x[0] - x[1] == 2:
        succ += 1
    if x[1] - x[0] == 2:
        sanity_check += 1

print("P(robot leaves the corridor at lower end) is approximately {}".format(succ/n))
print("P(robot leaves the corridor at upper end) is approximately {}".format(sanity_check/n))
