def run():
    string = input().strip()

    s = []

    for ch in string:
        if ch == "(":
            s.append(ch)
        
        else:
            if not s or s[-1] != "(":
                return "No"
            s.pop()

    if s:
        return "No"

    return "Yes"

print(run())