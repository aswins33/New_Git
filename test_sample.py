s1 = "listen"
s2 = "silent"

if len(s1) != len(s2):
    print(False)
else:
    count = {}

    # Count characters in s1
    for ch in s1:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    # Subtract counts using s2
    for ch in s2:
        if ch in count:
            count[ch] -= 1
        else:
            print(False)
            break
    else:
        # Check if all values are zero
        for value in count.values():
            if value != 0:
                print(False)
                break
        else:
            print(True)
            