# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка должна содержать данные о фирме: название, форма собственности, выручка,
# издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста
import json

myList = []
listFirm = []
cont = 0
s = 0
finalList = []
with open('my_file.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    for line in content:
        myList.append(line.strip('\n'))
    profit = {elm.split()[0]: ((int(elm.split()[2])) - int(elm.split()[3])) for elm in myList}
    finalList.append(profit)
    for item in myList:
        if ((int(item.split()[2])) - int(item.split()[3])) > 0:
            cont += 1
            s += (int(item.split()[2])) - int(item.split()[3])
    averageProfit = {'average_profit': s/cont}
    finalList.append(averageProfit)
    print(finalList)
with open('json_file.json', 'w', encoding='utf-8') as f:
    json.dump(finalList, f, ensure_ascii=False, indent=4)
