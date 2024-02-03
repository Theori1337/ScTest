with open("space.txt", mode="r", encoding="utf8") as file, open("space_new.txt", mode="w") as newFile:
    firstLine, data = file.readline(), [x.strip().split("*") for x in file.readlines()]
    ships = []  # массив с числами из имен кораблей
    for i in range(len(data)):
        ships.append(int(data[i][0].split("-")[1]))
    numbers = sorted(ships)[:10]
    numbers.sort()
    for j in range(len(numbers)):
        for i in range(len(data)):
            if numbers[j] == int(data[i][0].split("-")[1]):
                print(data[i][0])
