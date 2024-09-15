def minmax(dict):
    a=max(dict.values())
    b=min(dict.values())
    print("minimum value is: ",b ," maximum value is :",a)
def main():
    dict={"ADI":7, "is": 6, "a Bdb Student":9}
    minmax(dict)
if __name__=="__main__":
    main()