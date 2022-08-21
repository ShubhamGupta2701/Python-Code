n = int(input("Enter an interger : "))
if n%2 == 0:
    if n in range(2,5):
        print("not weird")
    elif n in range(6,20):
        print("weird")
    else:
        print("Not weird")
else:
    print("weird")