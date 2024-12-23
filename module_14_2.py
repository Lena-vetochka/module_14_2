import sqlite3


connection = sqlite3.connect('not_telegram.db')   #подключаемся к бд
cursor = connection.cursor()                  #курсор

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# добавляем значения
# for i in range(1, 11):
#     cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)',
#                    (f'User{i}', f'example{i}@gmail.com', int(f'{i}' +'0'), 1000))

# # обновляем значения balance у каждой 2ой записи начиная с 1ой на 500
# cursor.execute('UPDATE Users SET balance = ? WHERE id % 2 != 0', (500,))

# # удаляем каждую 3ую запись в таблице начиная с 1ой
# cursor.execute('DELETE FROM Users WHERE id % 3 = 1')

#  Удаление пользователя с id=6
cursor.execute('DELETE FROM Users WHERE id = 6')

cursor.execute('SELECT COUNT(*) FROM Users')  #Подсчёт кол-ва всех пользователей
total_users = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM Users') #Подсчёт суммы всех балансов
all_balances= cursor.fetchone()[0]
print(all_balances/total_users)

#выборка - возраст не равен 60
# cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
# users = cursor.fetchall()
# for i in users:
#     print(f'Имя: {i[0]} | Почта: {i[1]} | Возраст: {i[2]} | Баланс: {i[3]}')

connection.commit()
connection.close()