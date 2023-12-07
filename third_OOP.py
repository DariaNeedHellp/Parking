#class car():
#    places = ["01_01", "01_02", "01_03", "01_04", "01_05", "02_01", "02_02", "02_03", "02_04", "02_05"]
#    """Описание машины"""
#    def __init__(self, place, number, color, model, fio, day, time):
#        """свойства машины"""
#        self.numPlace = place
#        self.numCar = number
#        self.carColor = color
#        self.carModel = model
#        self.fio = fio
#        self.day = day
#        self.firstTime = time

#    def assembly(self):
#        """собирает строку машины"""
#        for indexCurrentPlace in range(0,len(places)):
#            places[indexCurrentPlace] = str(self.numPlace) + ";" + str(self.numCar) + ";" + self.carColor + ";" + self.carModel + ";" + self.fio + ";" + self.day + ";" + str(self.firstTime)
class CParking():
    __places = []

    def __init__(self):
        pass

    def addPlace(self, place):
        self.__places.append(place)

    def getPlaceByNumber(self, numPlace):
        for numRow in range(0, len(self.__places)):
            if self.__places[numRow].getNumPlace() == numPlace:
                return self.__places[numRow]
        print("Введённый вами номер места парковки не найден")
        return 0
    def ChangeCriteria(self):
        colors = ["белый", "желтый", "коричневый", "ораньжевый", "фиолетовый", "синий", "зеленый", "черный", "серый",
                  "красный", "иной"]
        models = ["mitsubishi", "ford", "volkswagen", "chevrolet", "renault", "kia", "hyundai", "nissan", "toyota",
                  "lada", "bmv", "chery", "mercedes", "honda", "byd", "иной"]
        print("Введите место на котором стоит машина, запись которой нужно изменить")
        numPlaceInput = input()
        print("Введите критерий, на который хотите заменить")
        criteria = input()
        for numRow in range(0,len(self.__places)):
            placeCurrent = self.__places[numRow]
            if placeCurrent.getNumPlace() == numPlaceInput:
                if placeCurrent.getOccupied():
                    carCurrent = placeCurrent.getCar()
                    flag = True
                    for c in range(0,len(colors)):
                        if criteria == colors[c]:
                            carCurrent.setColor(criteria)
                            flag = False
                            break
                    if flag:
                        for m in range(0,len(models)):
                            if criteria == models[m]:
                                carCurrent.setModel(criteria)
                                flag = False
                                break
                    if flag:
                        if carCurrent.numCarCheck(True):
                            carCurrent.setNumCar(criteria)
                            flag = False
                    if flag:
                        print("Введеный вами критерий не найден в базе данных или номер машины неправильного формата")
                    else:
                        print("Парковочное место пусто")

    def searchPlace(self):
        flagKtg = True
        while flagKtg:
            print(" Выберете катигорию по которой хотите произвести поиск:")
            print("    1. По номеру машины")
            print("    2. По цвету машины")
            print("    3. По модели машины")
            print("    4. По дате въезда машины на стоянку")
            print("    5. По времени въезда машины на стоянку")
            print("    6. Завершить поиск")
            z = int(input())
            if z == 1:
                print("Введите номер машины:")
                numCarInput = input()
                for numRow in range(0, len(self.__places)):
                    placeCurrent = self.__places[numRow]
                    strOut = placeCurrent.getNumPlace()
                    if placeCurrent.getOccupied():
                        carCurrent = placeCurrent.getCar()
                        if carCurrent.getNumCar() == numCarInput:
                            strOut += (";" + carCurrent.getNumCar() + ";" + carCurrent.getColor() + ";" + carCurrent.getModel() + ";" + carCurrent.getFio() + ";" + placeCurrent.getDay() + ";" + placeCurrent.getTime())
                            print(strOut)
                            flagKtg = False
            if z == 2:
                print("Введите цвет машины:")
                carColorInput = input()
                for numRow in range(0, len(self.__places)):
                    placeCurrent = self.__places[numRow]
                    strOut = placeCurrent.getNumPlace()
                    if placeCurrent.getOccupied():
                        carCurrent = placeCurrent.getCar()
                        if carCurrent.getColor() == carColorInput:
                            strOut += (";" + carCurrent.getNumCar() + ";" + carCurrent.getColor() + ";" + carCurrent.getModel() + ";" + carCurrent.getFio() + ";" + placeCurrent.getDay() + ";" + placeCurrent.getTime())
                            print(strOut)
                        flagKtg = False

            if z == 3:
                print("Введите марку машины:")
                carModelInput = input()
                for numRow in range(0, len(self.__places)):
                    placeCurrent = self.__places[numRow]
                    strOut = placeCurrent.getNumPlace()
                    if placeCurrent.getOccupied():
                        carCurrent = placeCurrent.getCar()
                        if carCurrent.getModel() == carModelInput:
                            strOut += (";" + carCurrent.getNumCar() + ";" + carCurrent.getColor() + ";" + carCurrent.getModel() + ";" + carCurrent.getFio() + ";" + placeCurrent.getDay() + ";" + placeCurrent.getTime())
                            print(strOut)
                        flagKtg = False

            if z == 4:
                print("Введите дату въезда машины на стоянку:")
                dayInput = input()
                for numRow in range(0, len(self.__places)):
                    placeCurrent = self.__places[numRow]
                    strOut = placeCurrent.getNumPlace()
                    if placeCurrent.getOccupied():
                        carCurrent = placeCurrent.getCar()
                        if placeCurrent.getDay() == dayInput:
                            strOut += (";" + carCurrent.getNumCar() + ";" + carCurrent.getColor() + ";" + carCurrent.getModel() + ";" + carCurrent.getFio() + ";" + placeCurrent.getDay() + ";" + placeCurrent.getTime())
                            print(strOut)
                        flagKtg = False

            if z == 5:
                print("Введите время въезда машины на стоянку:")
                timeInput = input()
                for numRow in range(0, len(self.__places)):
                    placeCurrent = self.__places[numRow]
                    strOut = placeCurrent.getNumPlace()
                    if placeCurrent.getOccupied():
                        carCurrent = placeCurrent.getCar()
                        if placeCurrent.getTime() == timeInput:
                            strOut += (";" + carCurrent.getNumCar() + ";" + carCurrent.getColor() + ";" + carCurrent.getModel() + ";" + carCurrent.getFio() + ";" + placeCurrent.getDay() + ";" + placeCurrent.getTime())
                            print(strOut)
                        flagKtg = False

            elif z == 6:
                flagKtg = False
    def loadPlacesFromBase(self):
        f = open('garage.txt', 'r+')
        mode = 0
        flag = True
        while flag:
            record = f.readline()
            if record == "":
                flag = False
            else:
                str_record = record[:(len(record) - 1)]
                if str_record == "[num_place]":
                    mode = 1
                else:
                    if mode == 1:
                        placeNew = CPlace()
                        items = str_record.split(";")
                        placeNew.setNumPlace(items[0])
                        if len(items) > 1:
                            carNew = CCar()
                            carNew.setNumCar(items[1])
                            carNew.setColor(items[2])
                            carNew.setModel(items[3])
                            carNew.setFio(items[4])
                            placeNew.setCarEntry(carNew, items[5], items[6])
                            placeNew.setOccupied(True)
                        self.addPlace(placeNew)
        f.close()

    def savePlacesToBase(self):
        f = open('garage.txt', 'w+')
        f.seek(0)
        f.write("[num_place]" + "\n")
        for numRow in range(0, len(self.__places)):
            placeCurrent = self.__places[numRow]
            strOut = placeCurrent.getNumPlace()
            if placeCurrent.getOccupied():
                carCurrent = placeCurrent.getCar()
                strOut += (";" + carCurrent.getNumCar() + ";" + carCurrent.getColor() + ";" + carCurrent.getModel() + ";" + carCurrent.getFio() + ";" + placeCurrent.getDay() + ";" + placeCurrent.getTime())
            strOut += "\n"
            f.write(strOut)
        f.close()

    def tableCall(self):
        print("_" * 141)
        print(
            "Номер места| Номер машины | Цвет машины      | Модель машины  | ФИО                                            | Дата въезда | Время въезда |")
        print("_" * 141)
        for numRow in range(0, len(self.__places)):
            record = self.__places[numRow]

            numPlace = record.getNumPlace()
            strOut = numPlace
            if len(numPlace) < 11:
                for i in range(len(numPlace), 10):
                    strOut += " "
            strOut += " | "
            carPlace = record.getCar()
            if carPlace != "":
                numCar = carPlace.getNumCar()
                strOut += numCar
                if len(numCar) < 11:
                    for i in range(len(numCar), 12):
                        strOut += " "
                strOut += " | "
                carColor = carPlace.getColor()
                strOut += carColor
                if len(carColor) < 15:
                    for i in range(len(carColor), 16):
                        strOut += " "
                strOut += " | "
                carModel = carPlace.getModel()
                strOut += carModel
                for i in range(len(carModel), 14):
                    strOut += " "
                strOut += " | "
                fio = carPlace.getFio()
                strOut += fio
                for i in range(len(fio), 46):
                    strOut += " "
                strOut += " | "
                day = record.getDay()
                strOut += day
                if len(day) < 11:
                    for i in range(len(day), 11):
                        strOut += " "
                strOut += " | "
                firstTime = record.getTime()
                strOut += firstTime
                if len(firstTime) < 12:
                    for i in range(len(firstTime), 12):
                        strOut += " "
                strOut += " | "
            else:
                for i in range(0, 12):
                    strOut += " "
                strOut += " | "
                for i in range(0, 16):
                    strOut += " "
                strOut += " | "
                for i in range(0, 14):
                    strOut += " "
                strOut += " | "
                for i in range(0, 46):
                    strOut += " "
                strOut += " | "
                for i in range(0, 11):
                    strOut += " "
                strOut += " | "
                for i in range(0, 12):
                    strOut += " "
                strOut += " | "
            print(strOut)
            print("-" * 141)

class CPlace():
    __numPlace = ""
    __carPlace = ""
    __day = ""
    __firstTime = ""
    __occupied = False

    def __init__(self, numPlace = "", carPlace = "", day = "", firstTime = ""):
        self.__numPlace = numPlace
        self.__carPlace = carPlace
        self.__day = day
        self.__firstTime = firstTime

    def getOccupied(self):
        return self.__occupied

    def setOccupied(self, occupied):
        self.__occupied = occupied

    def getNumPlace(self):
        return self.__numPlace

    def setNumPlace(self, numPlace):
        self.__numPlace = numPlace

    def getCar(self):
        return self.__carPlace

    def setCar(self, carPlace):
        self.__carPlace = carPlace

    def getDay(self):
        return self.__day

    def setDay(self, day):
        self.__day = day

    def getTime(self):
        return self.__firstTime

    def setTime(self, firstTime):
        self.__firstTime = firstTime

    def printCarEntry(self):
        print("На месте №" + self.__numPlace + " автомобиль с номером " + self.__carPlace.getNumCar() + " заехал " + self.__day + " в " + self.__firstTime)

    def setCarEntry(self, carPlace, day, firstTime):
        self.__carPlace = carPlace
        self.__day = day
        self.__firstTime = firstTime
        self.__occupied = True

    def clearCarEntry(self):
        self.__carPlace = ""
        self.__day = ""
        self.__firstTime = ""
        self.__occupied = False

    def timeCheck(self, time):
        hour1 = ["0", "1", "2"]
        hour2 = ["0", "1", "2", "3", "4"]
        minutes1 = ["0", "1", "2", "3", "4", "5", "6"]
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        flagTestingTime = True
        if len(time) != 5:
            flagTestingTime = False
        else:
            if time[:1] not in hour1:
                flagTestingTime = False
            if time[1:2] not in numbers:
                flagTestingTime = False
            if time[:1] == "2" and time[1:2] not in hour2:
                flagTestingTime = False
            if time[2:3] != ":":
                flagTestingTime = False
            if time[3:4] not in minutes1:
                flagTestingTime = False
            if time[4:5] not in numbers:
                flagTestingTime = False

        if flagTestingTime == False:
            print("Вы ввели время неправильно попробуйте снова (в формате 00:00)")
        return flagTestingTime

    def dayCheck(self, day):
        flagTestingDay = True
        if len(day) != 10:
            flagTestingDay = False
        else:
            if int(day[:2]) > 31:
                flagTestingDay = False
            if (day[2:3] and day[5:6]) != ".":
                flagTestingDay = False
            if int(day[3:5]) > 12:
                flagTestingDay = False
            if int(day[6:]) < 2023:
                flagTestingDay = False
        if flagTestingDay == False:
            print("Вы ввели дату неправильно попробуйте снова (в формате 01.01.2000)")
        return flagTestingDay

class CCar():
    __numCar = ""
    __carColor = ""
    __carModel = ""
    __fio = ""

    def __init__(self, numCar = "", carColor = "", carModel = "", fio = ""):
        self.__numCar = numCar
        self.__carColor = carColor
        self.__carModel = carModel
        self.__fio = fio

    def getNumCar(self):
        return self.__numCar

    def setNumCar(self, numCar):
        self.__numCar = numCar

    def numCarCheck(self, numCar):
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        chars = ["А", "В", "Е", "К", "М", "Н", "О", "Р", "С", "Т", "У", "Х", "A", "B", "E", "K", "M", "H", "O", "P", "C", "T", "Y", "X"]

        flagTestingNumCar = True
        if len(numCar) != 6:
            flagTestingNumCar = False
        else:
            if numCar[:1] not in chars:
                flagTestingNumCar = False
            if numCar[1:2] not in numbers:
                flagTestingNumCar = False
            if numCar[2:3] not in numbers:
                flagTestingNumCar = False
            if numCar[3:4] not in numbers:
                flagTestingNumCar = False
            if numCar[4:5] not in chars:
                flagTestingNumCar = False
            if numCar[5:6] not in chars:
                flagTestingNumCar = False

        if flagTestingNumCar == False:
            print("Номер автомобиля введённый вами не соответствует стандарту")

        return flagTestingNumCar

    def getColor(self):
        return self.__carColor

    def setColor(self, carColor):
        self.__carColor = carColor

    def carColorCheck(self, carColor):
        testCarColor = True
        colors = ["белый", "желтый", "коричневый", "ораньжевый", "фиолетовый", "синий", "зеленый", "черный", "серый", "красный", "иной"]
        if carColor not in colors:
            testCarColor = False
        if testCarColor == False:
            print("Данного цвета нет в основном регисте цветов, введите слово << иной >> ")
        return testCarColor

    def getModel(self):
        return self.__carModel

    def setModel(self, carModel):
        self.__carModel = carModel

    def carModelCheck(self, carModel):
        testCarModel = True
        models = ["mitsubishi", "ford", "volkswagen", "chevrolet", "renault", "kia", "hyundai", "nissan", "toyota", "lada", "bmv", "chery", "mercedes", "honda", "byd", "иной"]
        if carModel not in models:
            testCarModel = False
            print("Данной модели нет в основном регисте моделей, введите слово << иной >> ")
        return testCarModel

    def getFio(self):
        return self.__fio

    def setFio(self, fio):
        self.__fio = fio

parkingNew = CParking()
parkingNew.loadPlacesFromBase()

Work = True
while Work:
    print("Меню")
    print("    1. Зарегистрировать машину на стоянке")
    print("    2. Зарегистрировать выезд машины со стоянки")
    print("    3. Вывести основной регистр цветов и моделей")
    print("    4. Найти машины по критериям")
    print("    5. Вывести весь список мест на парковке(занятых и незанятых)")
    print("    6. Записать в базу")
    print("    7. Изменение данных машины")
    print("    8. Выйти из программы")

    x = int(input())
    if x == 1:
        print("1")
        print("Введите номер места парковки")
        numPlace = input()
        print("Введите номер автомобиля (все буквы заглавные)")
        numCar = input()
        print("Введите цвет автомобиля (все буквы строчные, русские, без ё)")
        carColor = input()
        print("Введите марку автомобиля (все буквы строчные английские)")
        carModel = input()
        print("Введите полное ФИО хозяина машины (через пробел)")
        fio = input()
        print("Введите дату въезда машины на стоянку (в формате 01.01.2000)")
        day = input()
        print("Введите время въезда машины на стоянку (в формате 00:00)")
        firstTime = input()

        placeCurrent = parkingNew.getPlaceByNumber(numPlace)
        if placeCurrent != 0:
            if placeCurrent.getOccupied():
                print("Место занято")
            else:
                if placeCurrent.dayCheck(day) and placeCurrent.timeCheck(firstTime):
                    carNew = CCar()
                    if carNew.numCarCheck(numCar) and carNew.carColorCheck(carColor):
                        carNew.setNumCar(numCar)
                        carNew.setColor(carColor)
                        carNew.setModel(carModel)
                        carNew.setFio(fio)
                        placeCurrent.setCarEntry(carNew, day, firstTime)

    if x == 2:
        print("Введите номер места парковки")
        numPlace = input()
        placeCurrent = parkingNew.getPlaceByNumber(numPlace)
        placeCurrent.clearCarEntry()

    if x == 3:
        colors = ["белый", "желтый", "коричневый", "ораньжевый", "фиолетовый", "синий", "зеленый", "черный", "серый", "красный", "иной"]
        models = ["mitsubishi", "ford", "volkswagen", "chevrolet", "renault", "kia", "hyundai", "nissan", "toyota", "lada", "bmv", "chery", "mercedes", "honda", "byd", "иной"]
        print("Цвета из основного регистра: ")
        print(colors)
        print("Модели из основного регистра: ")
        print(models)

    if x == 4:
        parkingNew.searchPlace()

    if x == 5:
        parkingNew.tableCall()

    if x == 6:
        parkingNew.savePlacesToBase()
    if x == 7:
        parkingNew.ChangeCriteria()
    if x == 8:
        Work = False
        print("Спасибо что использовали наше программное обеспечение")


#red = EColors.red
#print(red.value)
#                places.append(str_record)
#placeNew = CPlace()
#numPlace = input()
#placeNew.setNumPlace(numPlace)
#parkingNew.addPlace(placeNew)

#placeSecond = CPlace()
#numPlace = input()
#placeSecond.setNumPlace(numPlace)
#parkingNew.addPlace(placeSecond)

#carNew = CCar()
#numCar = input()
#if carNew.numCarCheck(numCar):
 #   carNew.setNumCar(numCar)
  #  print(carNew.getNumCar())
#day = input()
#firstTime = input()
#if placeNew.dayCheck(day) and placeNew.timeCheck(firstTime):
#    placeNew.setCarEntry(carNew, day, firstTime)
#    placeNew.printCarEntry()
#parkingNew.tableCall()