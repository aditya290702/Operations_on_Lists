def sumind(dict):
    sum=0
    for i in dict:
        sum=sum+dict[i]
    print(sum)
def main():
    dict={"ADI":7, "is": 6, "a Bdb Student":9}
    sumind(dict)
if __name__=="__main__":
    main()