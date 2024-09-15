def even(l):
    count = 0
    a = len(l)
    print ("the even numbers are")
    for count in range(0, a):
        if(l[count] % 2 ==0):
            print(l[count])

def main():
    l=[50, 43, 32, 23, 12,33, 56, 84, 87548, 3485634]
    x=even(l)
    return (x)

if __name__=="__main__":
    main()