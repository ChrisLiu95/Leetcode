def readfile(s):
    with open(s) as f:
        # for line in f.readlines():  # line 为 file 的每一行
        #     result.append(line)
        result = f.readlines()
    result = sorted(result, key=lambda x: int(x.strip().split(":")[1]))
    print(result)
    new = open("new.txt", "w")
    new.writelines(result)
    return new


print(readfile("text.txt"))
