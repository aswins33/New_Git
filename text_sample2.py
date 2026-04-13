a1="dusty"
a2="study"

if len(a1) !=len(a2):
    print(False)
else:
    count={}

    for name in a1:
        if name in count:
            count[name] += 1
        else:
            count[name] = 1

    for name in a2:
        if name in count:
            count[name] -=1
        else:
            print(False)
            break
    else:
        for check in count.values():
            if check !=0:
                print(False)
                break
        else:
            print(True)