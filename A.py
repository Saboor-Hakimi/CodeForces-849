str = "codeforces"

n = int(input())

for _ in range(n):
    char = input()
    if char in str:
        print("YES")
    else:
        print("NO")