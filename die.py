hit_die = 0     # 1d20
die1 = 0        # 1d6
die2 = 0        # 1d6
crit_die = 0    # 1d6
counter = 0
sum = 0
for hit_die in range(1,21):
    if hit_die >= 10 and hit_die != 20:       # normal hit
        for die1 in range(1, 7):
            for die2 in range(1, 7):
                sum += die1 + die2
                counter += 1
    if hit_die == 20:                         # critical hit
        for die1 in range(1, 7):
            for die2 in range(1, 7):
                for crit_die in range (1, 7):
                    sum += die1 + die2 + crit_die
                    counter += 1
print()
print('2d6 yes crit')
print('counter -', counter)
print('sum -', sum)
print('avg - ', sum/counter)

hit_die = 0     # 1d20
die1 = 0        # 1d12
crit_die = 0    # 1d12
counter = 0
sum = 0
for hit_die in range(1,21):
    if hit_die >= 10 and hit_die != 20:       # normal hit
        for die1 in range(1, 13):
            sum += die1
            counter += 1
    if hit_die == 20:                         # critical hit
        for die1 in range(1, 13):
            for crit_die in range (1, 13):
                sum += die1 + crit_die
                counter += 1
print()
print('1d12 yes crit')
print('counter -', counter)
print('sum -', sum)
print('avg - ', sum/counter)




hit_die = 0     # 1d20
die1 = 0        # 1d6
die2 = 0        # 1d6
crit_die = 0    # 1d6
counter = 0
sum = 0
for hit_die in range(1,21):       # notmal hit
    if hit_die >= 10:
        for die1 in range(1, 7):
            for die2 in range(1, 7):
                sum += die1 + die2
                counter += 1
print()
print('2d6 no crit')
print('counter -', counter)
print('sum -', sum)
print('avg - ', sum/counter)

hit_die = 0     # 1d20
die1 = 0        # 1d12
crit_die = 0    # 1d12
counter = 0
sum = 0
for hit_die in range(1,21):         # notmal hit
    if hit_die >= 10:
        for die1 in range(1, 13):
            sum += die1
            counter += 1
print()
print('1d12 no crit')
print('counter -', counter)
print('sum -', sum)
print('avg - ', sum/counter)
