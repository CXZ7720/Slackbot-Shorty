def wordpop(msg):
    res = []
    print("input : " + msg)

    if msg[0] is '*' and msg[-1] is '*':
        # Bold text
        msg = msg[1:-1]

    elif msg[0] is '_' and msg[-1] is '_':
        # Italics text
        msg = msg[1:-1]

    elif msg[0] is '~' and msg[-1] is '~':
        # Stricked text
        msg = msg[1:-1]

    elif msg[0] is '>':
        # Quote
        msg = msg[1:]

    elif msg[0] is '`' and msg[-1] is '`':
        if msg[1] is '`' and msg[-2] is '`':
            if msg[2] is '`' and msg[-3] is '`':
                # Preformatted text
                msg = msg[3:-3]
            else:
                msg = msg[1:-1]    
        # Code format text
        else:
            msg = msg[1:-1]
    # print(msg)
    for i in msg.split(' '):
        res.append(i[0])
        if any([i[-1] == '!', i[-1] == '?', i[-1] == '~', i[-1] == '.']):
            res.append(i[-1])
    print(res)
    return res
