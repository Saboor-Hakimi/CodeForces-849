n = int(input())

for _ in range(n):
    m = int(input())

    str = input()


    while True:
        try:
            # print("str", str[0], str[-1])
            if (str[0] == "0" and str[-1] == "1") or (str[0] == "1" and str[-1] == "0"):
                # print("here", str)
                # str is str without the first and last character
                str = str[1:-1]
            else:
                break
        except:
            break
    print(len(str))