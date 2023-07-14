def HTMLElements(strParam):

    flag = False
    removeFlag = False
    order = []
    str_ = ""

    for c in strParam:

        # switch to adding or removing mode
        if c == "<":
            flag = True
            continue

        # close adding or removing mode
        if c == '>' and flag:
            if removeFlag:
                end = order.pop()
                if end != str_:
                    return end
            else:
                order.append(str_)

        # switch to removing mode
        if flag and c == "/":
            removeFlag = True
            continue

        # add character to string
        if flag:
            str_ += c


    if len(order) == 0:
        return "true"
    else:
        return order.pop()


