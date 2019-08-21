def wordpop(msg):
    res = []
    print("input : " + msg)
    for i in msg.split(' '):
        res.append(i[0])
        if any([i[-1] == '!', i[-1] == '?', i[-1] == '~', i[-1] == '.']):
            res.append(i[-1])
    print(res)
    return res
