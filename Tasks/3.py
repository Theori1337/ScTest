with open("space.txt", mode="r", encoding="utf8") as file, open("space_new.txt", mode="w") as newFile:
    firstLine, data = file.readline(), [x.strip().split("*") for x in file.readlines()]
    ships = []  # массив с именами кораблей
    for i in range(len(data)):
        ships.append(data[i][0])
    while True:
        n = input()
        if n == "stop":
            break
        for i in range(len(data)):
            shipName = data[i][0]
            xd = int(data[i][3].split(" ")[0])  # координата вектора х
            yd = int(data[i][3].split(" ")[1])  # координата вектора y
            planet = data[i][1]  #
            if shipName == n:
                print(f"Корабль {shipName} был отправлен с планеты: {planet} и его направление движения было: {xd, yd}")
        if n not in ships:
            print("error.. er.. ror..")
