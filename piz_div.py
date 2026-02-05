
#store map of low and hig
n, st_x, st_y, end_x, end_y = map(int, input().split())
hash_map = {}
x = []
y = []
for i in range(2):
    if i == 0:
        x = list(map(int, input().split()))
    else:
        y = list(map(int, input().split()))

for i in x:
    if i not in hash_map:
        hash_map[i] = [-1, -1]

for i in range(len(y)):
    if hash_map[x[i]] == [-1, -1]:
        hash_map[x[i]] = [y[i], y[i]]
    else:
        if y[i] < hash_map[x[i]][0]:
            hash_map[x[i]][0] = y[i]
        elif y[i] > hash_map[x[i]][1]:
            hash_map[x[i]][1] = y[1]
hash_map[st_x] = [st_y, st_y]
hash_map[end_x] = [end_y, end_y]
sorted_nums = list((hash_map.keys()))
sorted_nums.sort()
#both high and low and get min of both
def recurse(i, cur_y):
    if (i == len(sorted_nums) - 1):
        return 0
    cur_x = sorted_nums[i]
    cur_col = hash_map[cur_x][1] - hash_map[cur_x][0]

    dist_low = (sorted_nums[i + 1] - cur_x) + abs(hash_map[sorted_nums[i + 1]][0]- cur_y)  
    dist_high = (sorted_nums[i + 1] - cur_x) + abs(hash_map[sorted_nums[i + 1]][1]- cur_y)

    return min(cur_col + dist_low + recurse(i + 1, hash_map[sorted_nums[i + 1]][0]), cur_col + dist_high + recurse(i + 1, hash_map[sorted_nums[i + 1]][1])) 
print(recurse(0, st_y))
    #taking the minimum amount of both high and low
#recursive need to implement dp
        