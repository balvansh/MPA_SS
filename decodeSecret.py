def decodeSecret(shares):
    dKey = []
    dValue = []
    for value in shares:
        try:
            dKey.append((value[0]).encode("utf-8"))
        except:
            dKey.append(int(str(value[0], 'utf-8')))
        try:
            dValue.append((value[1]).encode("utf-8"))
        except:
            dValue.append(int(str(value[1], 'utf-8')))
    result = 1.0
    print("Id of the entered keys: ",dKey)
    print("The secrets entered are: ",dValue)
    sum = 0
    for i in range(len(dValue)):
        result = 1.0
        for j in range(len(dKey)):
            if i != j:
                vard = dKey[j] - dKey[i]
                result = result * ( dKey[j] / vard )
        sum = sum + result * dValue[i]
    print(sum)
    return sum