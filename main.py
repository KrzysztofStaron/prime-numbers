num = 1

while True:
    num += 2
    number = [int(x) for x in str(num)]
    sum = 0
    # 2
    # if number[len(number)-1] % 2 == 0:
    #    continue
    # 3
    for x in number:
        sum += x
    if sum % 3 == 0:
        continue
    # 4 nie ma sensu
    # 5
    if number[len(number)-1] % 5 == 0:
        continue

    # 6 nie ma senzu
    # 7 zrobie
    # 8 nie ma senzu
    # 9 nie ma senzu
    # 10 nie ma senzu
    # 11 zrobie kiedys

    failed = False
    for x in range(7, num // 2):
        if num%x == 0:
            failed = True
            break

    if failed:
        continue
    else:
        print (num)
        continue
