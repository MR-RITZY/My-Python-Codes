import random
head = []
tail = []
StreakHead = 0
StreakTail = 0
for i in range(1_000_000):
    h = random.randint(0, 1)
    t = random.randint(0, 1)
    head.append(h)
    tail.append(t)
for j in range(len(head)):
    if head[j] == head[j-1] == head[j-2] == head[j-3] == head[j-4] == head[j-5] == 1:
        StreakHead = StreakHead + 1
for k in range(len(tail)):
    if tail[k] == tail[k-1] == tail[k-2] == tail[k-3] == tail[k-4] == tail[k-5] == 1:
        StreakTail = StreakTail + 1
print(StreakHead, StreakTail)
