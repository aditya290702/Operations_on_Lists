def extract(l):
        for i in range(len(l)):
            if l[i][0] == "k":
                print(l[i])

def main():
    l = ["Kohli","kaka","messi","sachin","kapoor"]
    extract(l)


if __name__ == "__main__":
    main()
