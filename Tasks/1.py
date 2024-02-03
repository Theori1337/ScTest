with open("space.txt", mode="r", encoding="utf8") as file, open("space_new.txt", mode="w") as newFile:
    firstLine, data = file.readline(), [x.strip().split("*") for x in file.readlines()]  # 1 строчка таблицы и массив с последующими
    for i in range(len(data)):  # Перебор по элементам массива
        shipName = data[i][0]  # имя корабля
        xd = int(data[i][3].split(" ")[0])  # координата вектора х
        yd = int(data[i][3].split(" ")[1])  # координата вектора y
        n = int(data[i][0].split("-")[1][0])  # первая цифра в номере корабля
        t = len(data[i][1])  # кол-во букв в родной планете корабля
        x = 0
        y = 0
        m = int(data[i][0].split("-")[1][1])  # вторая цифра в номере корабля
        if n > 5:
            x = n + xd
        if n <= 5:
            x = -(n + xd) * 4 + t
        if m > 3:
            y = m + t + yd
        if m <= 3:
            y = -(n + yd) * m
        if shipName[3] == "V":
            newFile.write(f"{shipName} - {x, y}" + "\n")
