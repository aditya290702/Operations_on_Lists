def iterationofdict(dict):
    for keys,values in dict.items():
        print(keys,values)
def main():
    dict={"ADI": [7, 1], "is": [6, 7], "a Bdb Student": [9, 9]}
    iterationofdict(dict)

if __name__=="__main__":
    main()
