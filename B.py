n = int(input())

for _ in range(n):
    len = int(input())
    posX = 0
    posY = 0
    targetX = 1
    targetY = 1

    flag = False

    for char in input():
        if char == "U":
            posY += 1
        elif char == "D":
            posY -= 1
        elif char == "L":
            posX -= 1
        elif char == "R":
            posX += 1

        if posX == targetX and posY == targetY:
            print("YES")
            flag = True
            break

    if not flag:
        print("NO")
    

