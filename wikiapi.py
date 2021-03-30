import wikipediaapi as wikiapi #устанавливаю библиотеку по работе с API Википедии
import json #устанавливаю библиотеку для хранения корпуса в джейсоне
import time

wiki = wikiapi.Wikipedia("ru")
page = wiki.page("Ташкент")


links = page.links
linksru = [i for i in sorted(list(links.keys())) if ord(i[0]) >= 1040  # cобираю тексты на русском
            and ord(i[-1]) >= 1040]
linksru = [i for i in linksru if ':' not in i]
linksru = [i for i in linksru if ',' not in i]


data = {}


for i in linksru:
    page = wiki.page(i)
    if page.exists():
        data[i] = page.summary   # Саммэри по основной странице и по всем страницвм, ссылки которых взчли из нее
    time.sleep(1.5)   # ожидание в 2 секунды, иначе сдыхает от количества запросов
    print(i)


with open("tashk.json", "w") as k:
    json.dump(data, k, ensure_ascii=False)  # Записываю свой корпус статей в формате .json

