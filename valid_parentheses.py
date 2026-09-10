def valid_parentheses(string):
    if len(string) == 0:
        return "Empty"
    stack = []
    for i in range(len(string)):
        if string[i] == "(" or string[i] == "[" or string[i] == "{":
            stack.append(string[i])
        else:
            if len(stack) == 0:
                return "Invalid"
            if string[i] == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return "Invalid"
            elif string[i] == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return "Invalid"
            elif string[i] == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return "Invalid"
    if len(stack) == 0:
        return "Valid"
    else:
        return "Invalid"

print(valid_parentheses(""))
