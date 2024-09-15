def sumandavg(l):
    sum=0
    count=0
    a=len(l)

    for count in range(0, a):
        sum = sum + l[count]
        avg = sum/a
    print(sum, avg)

def main():
    l=[5, 4, 3, 2, 1]
    x=sumandavg(l)
    return (x)

if __name__=="__main__":
    main()