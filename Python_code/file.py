import pickle as p
def countrec():
    count = 0
    f = open("STUDENT.DAT","rb")
    while True:
        try:
            t = p.load(f)
            if t[2] > 75:
                count = count + 1
                print(t)
        except EOFError:
            print("End of the file reached. ")
            break
    print("Numbe of the student with greater percentage then 75 are : ",count)

countrec()