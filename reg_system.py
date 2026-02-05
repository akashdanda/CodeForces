n = int(input())
hash_map = {}
for _ in range(n):
    word = input()
    if word in hash_map:
        print(word + str(hash_map[word]))
        hash_map[word] += 1
    else:
        print("OK")
        hash_map[word] = 1
        
