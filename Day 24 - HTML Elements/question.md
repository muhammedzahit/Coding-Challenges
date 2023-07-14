# Question

Have the function HTMLElements(str) read the str parameter being passed which will be a string of HTML DOM elements and plain text.
The elements that will be used are: b, i, em, div, p. For example: if str is ```<div><b><p>hello world</p></b></div>``` then this string of
DOM elements is nested correctly so your program should return the string true.

If a string is not nested correctly, return the first element encountered where, if changed into a different element, would result in a
properly formatted string. If the string is not formatted properly, then it will only be one element that needs to be changed. For example:
if str is ```<div><i>hello</i>world</b>``` then your program should return the string div because if the first ```<div>``` element were changed into
a ```<b>```, the string would be properly formatted.

Examples

    Input: "<div><div><b></b></div></p>"
    Output: div

    Input: "<div>abc</div><p><em><i>test test test</b></em></p>"
    Output: i

    Input: "<div><i>hello</i>world</b>"
    Output: div

    Input: "<div><b></b></div>"
    Output: "true"

## Solution

```python
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

```

If we encounter a ```<``` character, we switch to adding or removing mode. If we encounter a ```>``` character, we close adding or removing mode.

If we are in adding mode, we add the character to a string. If we are in removing mode, we remove the last element from the stack and compare it to the string. If they are not equal, we return the last element from the stack.

If we reach the end of the string, we check if the stack is empty. If it is, we return ```true```. If it is not, we return the last element from the stack.