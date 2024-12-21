note = {'status': 'отложено'}
available_status = ['выполнено', 'в процессе', 'отложено'] #Возможные статусы

status_temp = 3 #будущий индекс списка доступных статусов

print('Обновление статуса заметки.')
while status_temp not in [0, 1, 2]:
    status_temp = input('Доступные варианты: 0 - выполнено, 1 - в процессе, 2 - отложено. Ввод: ').strip()
    #Пытаемся обновить статус заметки
    try:
        status_temp = int(status_temp)
        note['status'] = available_status[status_temp]
        print('Статус заметки успешно обновлён:', available_status[status_temp])
    except ValueError:
        print('Ошибка, введено не число! Повторите попытку.')
    except IndexError:
        print('Ошибка, введено неизвестное число, выберите пожалуйста из списка.')

print('Программа успешно завершила работу.')
