note = {}
print(type(note))
titles = []

print("Приступим к записи!")
note["username"] = input("Введите имя пользователя: ")
note["titles"] = []
for a in range(3):
    title = input(f"Введите заголовок {a + 1}: ")
    note["titles"].append(title)
note["content"] = input("Описание заметки: ")
note["status"] = input("Стаус заметки (например, 'В работе', 'Выполнена'): ")
new_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
end_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")

temp_new_date = new_date[:len(new_date)-5]
temp_end_date = end_date[:len(end_date)-5]

note["new_date"] = temp_new_date
note["end_date"] = temp_end_date

print("\nСобранная информация о заметке:")
for key, value in note.items():
    print(f"{key.capitalize()}: {value}")

