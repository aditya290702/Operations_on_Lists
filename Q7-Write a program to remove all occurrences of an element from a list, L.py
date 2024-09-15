def remove(element,l):
    for i in l:
        if i == element:
            l.remove(i)
    print(l)
def main():
    element=5
    l=[5, 4, 3, 2, 1, 5,4, 2, 5, 5]
    remove(element,l)

if __name__=="__main__":
    main()