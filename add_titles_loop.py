titles = []
i = True
n = 0

print ('Для остановки программы введите "stop"')
while i :
    title = input(f'Введите заголовок №{n+1}: ')
    title = title.strip()
    #Решила проверить дважды на случай если пользователь ошибётся
    if title == '' :
        title = input('Вы ввели пустой заголовок. Нажмите Enter повторно если желаете завершить ввод. ')
        if title == '' :
            i = False
    elif title == 'stop' :
        i = False
    else :
        n = n + 1
        titles.append(title)

print (f'Количество заголовоков: {n}. Вот они: ', titles)
