def find_max():
    a = [0, 1, 3, 2]
    max_value = a[0]  # Assume the first element is the maximum

    for i in range(1, len(a)):
        if a[i] > max_value:
            max_value = a[i]

    return max_value

def main():
    x = find_max()
    print(x)

if __name__ == "__main__":
    main()
