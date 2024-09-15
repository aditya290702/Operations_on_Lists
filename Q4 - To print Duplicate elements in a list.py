def dupli(l):
    i = 0
    size = len(l)
    duplicate = []
    print ("the duplicate element/s  is/are")
    for i in range(0, size):
        for j in range(i+1, size):
         if(l[i] == l[j]):

                duplicate.append(l[j])

    print(duplicate)


def main():
    l=[1,2,2,3,3,3,3]
    x=dupli(l)
    print(x)

if __name__=="__main__":
    main()