n, sumTime = map(int, input().split())

minTimes = []
maxTimes = []
sumMinTime = 0
sumMaxTime = 0
for _ in range(n):
    mn, mx = map(int, input().split())
    minTimes.append(mn)
    maxTimes.append(mx)
    sumMinTime += mn
    sumMaxTime += mx

if sumMinTime > sumTime or sumMaxTime < sumTime:
    print("NO")
    exit()

remTime = sumTime - sumMinTime
i = 0 
while remTime > 0 and i < len(minTimes):
    pot_added = maxTimes[i] - minTimes[i]
    if remTime > pot_added:
        remTime -= pot_added
        minTimes[i] = maxTimes[i]
    else:
        minTimes[i] += remTime
        remTime = 0
    i = i + 1
print("YES")
for i in minTimes:
    print(i, end = ' ')