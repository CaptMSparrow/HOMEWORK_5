from collections import Counter


persons = [
    {'name': 'Aria', 'age': 25, 'gender': 'female'},
    {'name': 'Emily', 'age': 12, 'gender': 'female'},
    {'name': 'Zoe', 'age': 33, 'gender': 'female'},
    {'name': 'Grace', 'age': 30, 'gender': 'female'},
    {'name': 'Ellie', 'age': 22, 'gender': 'female'},
    {'name': 'Hannah', 'age': 40, 'gender': 'female'},
    {'name': 'Alex', 'age': 11, 'gender': 'female'},
    {'name': 'Zoe', 'age': 17, 'gender': 'female'},
    {'name': 'Nora', 'age': 18, 'gender': 'female'},
    {'name': 'Hannah', 'age': 8, 'gender': 'female'},
    {'name': 'Elizabeth', 'age': 43, 'gender': 'female'},
    {'name': 'Harper', 'age': 18, 'gender': 'female'},
    {'name': 'Sofia', 'age': 25, 'gender': 'female'},
    {'name': 'Lily', 'age': 31, 'gender': 'female'},
    {'name': 'Emma', 'age': 39, 'gender': 'female'},
    {'name': 'Ryan', 'age': 25, 'gender': 'male'},
    {'name': 'Ethan', 'age': 22, 'gender': 'male'},
    {'name': 'Jacob', 'age': 28, 'gender': 'male'},
    {'name': 'Alex', 'age': 19, 'gender': 'male'},
    {'name': 'Owen', 'age': 10, 'gender': 'male'},
    {'name': 'Jack', 'age': 44, 'gender': 'male'},
    {'name': 'Logan', 'age': 33, 'gender': 'male'},
    {'name': 'Jackson', 'age': 38, 'gender': 'male'},
    {'name': 'Oliver', 'age': 39, 'gender': 'male'},
    {'name': 'James', 'age': 25, 'gender': 'male'},
    {'name': 'Henry', 'age': 7, 'gender': 'male'},
    {'name': 'Luke', 'age': 36, 'gender': 'male'},
    {'name': 'Alex', 'age': 12, 'gender': 'male'},
    {'name': 'Jack', 'age': 27, 'gender': 'male'},
    {'name': 'Daniel', 'age': 30, 'gender': 'male'}
    ]
# количество всех людей
number_of_people = len(persons)
print(f'Количество всех людей: {number_of_people}')
# количество мужчин
count_male = 0
all_m = []
for name_of_p_m in persons:
    if name_of_p_m['gender'] == "male":
        all_m.append(name_of_p_m)       # список с данными для мужчин
        count_male += 1
print(f'Количество мужчин: {count_male}')
# количество женщин
count_female = 0
for name_of_p_f in persons:
    if name_of_p_f['gender'] == "female":
        count_female += 1
print(f'Количество женщин: {count_female}')
# количество совершеннолетних
count_age = 0
for age_of_p in persons:
    if int(age_of_p['age']) >= 18:
        count_age += 1
print(f'Количество совершеннолетних: {count_age}')
# список имен без повторений
# list_of_names = []
# list_of_nam = [nam['name'] for nam in persons]
# for nam in list_of_nam:
#    if nam not in list_of_names:
#        list_of_names.append(nam)
# print(f'Список имен без посторений: {list_of_names}')
# весь список имен
all_list_of_names = [name_of_p['name'] for name_of_p in persons]
print(f'Список всех имен: {all_list_of_names}')
# oтсортированный список всех возрастов без повторений
list_of_all_ages = []
list_of_ages = [ages['age'] for ages in persons]
for age in list_of_ages:
    if age not in list_of_all_ages:
        list_of_all_ages.append(age)
list_of_all_ages.sort()
print(f'Отсортированный список всех возрастов: {list_of_all_ages}')
# самые встречающиеся имена
most_common_names = Counter(all_list_of_names)
print(f'Три самых популярных имени: {most_common_names.most_common(3)}')
# Имена мужчин старше 35, имя которых начинается с L
men_over = [m['name'] for m in all_m if 'L' in m['name'] if m['age'] > 35]
print(f'Список всех мужчин старше 35 и именем на букву L: {men_over}')
