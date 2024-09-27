def add_child(data_dict, child):
    """
         Функція для додавання нового учня у словник.
         Функція повертає к-ть дітей у словнику, яка стала
         після додавання нового учня.
         Параметри
         data_dict - основний словник з даними
         child - кортеж із даними по учню.
         Обмеження
         Не можна додати повторно учня.
         Якщо учень вже є у словнику - має генеруватися виключення ValueError
    """
    data_dict[child] = {}
    return len(data_dict)

def add_child_subjects(data_dict, child, subj_list):
    """
         Функція додавання списку предметів вказаному учню.
         Функція повертає кількість предметів, яка стала
         у вказаного учня (переданого в child) після
         додавання всіх предметів із переліку subj_list.
         Параметри
         data_dict - основний словник з даними
         child - кортеж із даними по учню.
         subj_list - список назв предметів, які треба додати учню.
         Обмеження
         Неможливо додати предмет, який уже є у словнику,
         що відповідає вказаному учню. Якщо предмет уже існує - має
         генеруватися виключення ValueError
    """
    if child not in data_dict.keys():
        add_child(data_dict, child)        
    for el in subj_list:
        data_dict[child][el] = []
    return len(data_dict[child])

def add_child_grades(data_dict, child, subject, grades_list):
    """
         Функція додавання оцінок вказаному учню по вказаному предмету.
         Функція повертає кількість оцінок, яка стала у вказаного
         учня по вказаному предмету після додавання усіх оцінок з
         переліку grades_list.
         Параметри
         data_dict - основний словник з даними
         child - кортеж із даними по учню.
         subject - предмет, по якому додаються оцінки учню.
         grades_list - список оцінок, які треба додати учню
         по вказаному предмету.
         Якщо вказаний предмет не існує, то він додається учню із
         вказаними по ньому оцінками
    """
    if child not in data_dict.keys():
        raise ValueError
    pup = data_dict[child]
    if subject not in pup.keys():
        data_dict[child][subject] = list(grades_list)
    else:
        data_dict[child][subject].extend(grades_list)
    return len(data_dict[child][subject])

def calcucale_avg(data_dict, child, subject):
    """
         Функція обчислює середнє значення по оцінках
         вказаного учня по вказаній дисципліні.
         Параметри
         data_dict - основний словник з даними
         child - кортеж із даними по учню.
         subject - предмет, по якому треба обчислити середній бал.
         Обмеження
         Якщо вказаної дитини немає  - генерується виключення ValueError.
         Якщо предмета немає - функція повертає значення -1.
         Значення середнього балу не може бути більше 12.
    """
    if child not in data_dict.keys():
        raise TypeError
    pup = data_dict[child]
    if subject not in pup.keys():
        return -1
    return sum(data_dict[child][subject])/len(data_dict[child][subject])*2

def class_by_name(data_dict, child_name):
    """
    Функція повертає назву класу, до якого відноситься учень,
    ПІБ якого задано параметром child_name.
    Параметри
    data_dict - основний словник з даними
    child_name - ПІБ учня, клас якого треба знайти. Задається
    рядком.
    Обмеження
    Якщо вказаної дитини немає - генерується виключення ValueError.
    Функція повинна повертати рядок тексту, формат якого наступний:
    перші два або один символи - цифри, далі один дефіс -, потім
    одна велика літера від А до D.
    """
    for el in data_dict.keys():
        if el[1] == child_name:
            return el[0].replace('-','=')
    raise TypeError
    
def calcucale_avg_all(data_dict, child):
    """
    Функція обчислює середнє значення по оцінках
    вказаного учня з усіх предметів. Функція повертає словник,
    у якому ключ - назва дисципліни, значення - середній бал
    по цій дисципліні.
    Параметри
    data_dict - основний словник з даними
    child - кортеж із даними по учню.
    Обмеження
    Якщо вказаної дитини немає- генерується виключення ValueError.
    Якщо по предмету немає оцінок - функція
    повертає значення -1 у словнику по ключу цього предмету
    """
    if child not in data_dict.keys():
        raise TypeError
    pup = data_dict[child]
    res = {}
    for key,val in pup.items():
        if len(pup[key])==0:
            res[key] = -1
        else:
            res[key] = sum(pup[key])/len(pup[key])
    return res

def is_excellent_student(data_dict, child):
    """
    Функція перевіряє, чи є вказаний учень відмінником.
    Якщо середня оцінка учня по кожному з предметів більше або
    дорівнює 10, то функція повертає значення True. Інакше - повертає
    значення False. При наявності хоч одного предмета із пустим списком
    оцінок бо повній відсутності даних по предметах - функція повертає None.
    Параметри
    data_dict - основний словник з даними
    child - кортеж із даними по учню.
    Обмеження
    Якщо вказаної дитини немає у словнику - генерується
    виключення ValueError.
    """
    if child not in data_dict.keys():
        raise TypeError
    pup = data_dict[child]
    for key,val in pup.items():
        if not val:
            return False
    if min([sum(pup[key])/len(pup[key]) for key in pup.keys()])>=10:
        return True
    return None

def subject_max_grade(data_dict, child):
    """
    Функція по заданому учню знаходить предмет із максимальним балом.
    Повертає список предметів, якщо максимальний бал у них однаковий.
    Параметри
    data_dict - основний словник з даними
    child - кортеж із даними по учню.
    Обмеження
    Якщо вказаної дитини немає у словнику - генерується
    виключення ValueError.
    """
    max_grade = -1
    if child not in data_dict.keys():
        raise TypeError
    res = []
    pup = data_dict[child]
    for key,val in pup.items():
        current_max = max(pup[key])
        if max_grade < current_max:
            max_grade = current_max
    for key,val in pup.items():
        if max_grade in pup[key]:
            res.append(key)
    return res

def subject_min_grade(data_dict, child):
    """
    Функція по заданому учню знаходить предмет із мінімальним балом.
    Повертає список предметів, якщо мінімальний бал у них однаковий
    Параметри
    data_dict - основний словник з даними
    child - кортеж із даними по учню.
    Обмеження
    Якщо вказаної дитини немає у словнику - генерується
    виключення ValueError.
    """
    min_grade = 12
    if child not in data_dict.keys():
        raise TypeError
    res = []
    pup = data_dict[child]
    for key,val in pup.items():
        current_min = min(pup[key])
        if min_grade > current_min:
            min_grade = current_min
    for key,val in pup.items():
        if min_grade in pup[key]:
            res.append(key)
    return res

def subject_avg(data_dict, subject):
    """
    Функція повертає середню оцінку по предмету для кожного класу у форматі
    списку рядків, наприклад, ['8-A: 10.5', '5-C: 11'].
    Параметри
    data_dict - основний словник з даними
    subject - назва предмету у вигляді рядка
    Обмеження
    Якщо дані по цьому предмету не внесено - повертається пустий список.
    Кожен рядок списку, який повертається у результаті виконання функції,
    повинен відповідати формату "назва_класу: середній_бал", при цьому
    формат назви класу має вигляд: перші два або один символи - цифри,
    далі один дефіс -, потім одна велика літера від А до D.
    """
    res = []
    avg = 0
    for key in data_dict.keys():
        if subject in data_dict[key].keys():
            if len(data_dict[key][subject])>0:
                avg = sum(data_dict[key][subject])/len(data_dict[key][subject])
        res.append(key[0] + ': '+ str(avg))
    return res

def children_list(data_dict, class_name):
    """
    Функція повертає список учнів заданого класу. Якщо не внесено
    жодного з учнів класу - повертається пустий список
    Параметри
    data_dict - основний словник з даними
    class_name - назва класу у вигляді рядка
    """
    res = []
    for el in data_dict.keys():
        if class_name == el[0]:
            res.append(el[1])
    return res

def subject_best_children(data_dict, subject):
    """
    Функція по заданому предмету знаходить учня з найвищим балом у кожній
    паралелі класів (наприклад, 8і класи, 5і класи, 7і класи і т.д.
    Якщо таких учнів декілька - повертається список їх прізвищ.
    Функція повертає словник, ключами якого є номери паралелей класів (без літери),
    а значеннями - список прізвищ учнів з найвищою оцінкою по заданому предмету.
    Якщо оцінки по заданому предмету відсутні - повертається пустий словник.
    Параметри
    data_dict - основний словник з даними
    subject - назва предмету у вигляді рядка
    """
    res = {}
    max_grade = {}
    for key in data_dict.keys():
        if subject in data_dict[key].keys():
            if len(data_dict[key][subject]) == 0:
                continue
            if key[0][0] not in res.keys():
                res[key[0][0]] = []
                max_grade[key[0][0]] = -1
            if max_grade[key[0][0]] < max(data_dict[key][subject]):
                res[key[0][0]].clear()
                res[key[0][0]].append(key[1])                
                max_grade[key[0][0]] = max(data_dict[key][subject])
            elif max_grade[key[0][0]] == max(data_dict[key][subject]):
                res[key[0][0]].append(key[1])
    return res
