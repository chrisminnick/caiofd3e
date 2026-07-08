with open("limerick.txt", "r") as file:
    for line in file:
        no_newline = line.strip()
        print(no_newline)
