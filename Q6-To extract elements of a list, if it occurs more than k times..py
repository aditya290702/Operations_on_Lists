def extraction(list,k):
    dict={}
    for i in list:
        val=0
        for j in list:
            if i==j:
                val=val+1
        dict[i]=val
    print(dict)
    for a in dict:
        if dict[a]>k:
            print( a ,end=" ")
def main():
    k=2
    list=[1,2,2,2,3,3]
    extraction(list,k)

if __name__=="__main__":
    main()
