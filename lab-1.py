digits = {
  '0':'',
  '1':'один',
  '2':'два',
  '3':'три',
  '4':'четыре',
  '5':'пять',
  '6':'шесть',
  '7':'семь',
  '8':'восемь',
  '9':'девять'
}

teens = {
  '11':'одиннадцать',
  '12':'двенадцать',
  '13':'тринадцать',
  '14':'четырнадцать',
  '15':'пятнадцать',
  '16':'шестнадцать',
  '17':'семнадцать',
  '18':'восемнадцать',
  '19':'девятнадцать',
}

tens = {
  '0':'',
  '1':'десять',
  '2':'двадцать',
  '3':'тридцать',
  '4':'сорок',
  '5':'пятьдесят',
  '6':'шестьдесят',
  '7':'семьдесят',
  '8':'восемьдесят',
  '9':'девяносто'
}

hundreds = {
  '0':'',
  '1':'сто',
  '2':'двести',
  '3':'триста',
  '4':'четыреста',
  '5':'пятьсот',
  '6':'шестьсот',
  '7':'семьсот',
  '8':'восемьсот',
  '9':'девятьсот'
}

decThousands = ['одна тысяча', 'две тысячи', 'тысячи', 'тысяч']
decMillions = ['миллион', 'миллиона', 'миллионов']
decBillions = ['миллиард', 'миллиарда', 'миллиардов']

def getNumberString(number):
  numberString = []
  hundred = number // 100
  number%=int(100)
  numberString.append(hundreds.get(str(hundred)))
  if (number // 10 == 1) and (number % 10 != 0):
    numberString.append(teens.get(str(number)))
  else:
    numberString.append(tens.get(str(number // 10)))
    numberString.append(digits.get(str(number % 10)))
  return numberString

def convertNumberToString(number):
  numberString = []
  billion = number // 1000000000
  number%=int(1000000000)
  million = number // 1000000
  number%=int(1000000)
  thousand = number // 1000
  number%=int(1000)
  hundred = number
  number%=int(100)
  numberString.extend(getNumberString(billion))
  if (billion % 10 == 1):
    numberString.append(decBillions[0])
  elif (billion % 10 >= 2) and (billion % 10 <= 4):
    numberString.append(decBillions[1])
  elif (billion % 10 >= 5) or (billion % 10 == 0 and billion != 0):
    numberString.append(decBillions[2])
  numberString.extend(getNumberString(million))
  if (million % 10 == 1):
    numberString.append(decMillions[0])
  elif (million % 10 >= 2) and (million % 10 <= 4):
    numberString.append(decMillions[1])
  elif (million % 10 >= 5) or (million % 10 == 0 and million != 0):
    numberString.append(decMillions[2])
  if (thousand % 10 == 1):
    numberString.append(decThousands[0])
  elif (thousand % 10 == 2):
    numberString.append(decThousands[1])
  elif (thousand % 10 == 3) or (thousand % 10 == 4):
    numberString.extend(getNumberString(thousand))
    numberString.append(decThousands[2])
  elif (thousand % 10 >= 5) or (thousand % 10 == 0 and thousand != 0):
    numberString.extend(getNumberString(thousand))
    numberString.append(decThousands[3])
  numberString.extend(getNumberString(hundred))
  return numberString

def mergeString(array, separator):
  string = ''
  for i in array:
    string += str(i) + separator
  return string

def main():
  while True:
    number = int(input('Введите число от 1 до 999999999999 (или 0 для выхода): '))
    if number < 0 or number > 999999999999:
      continue
    elif number == 0:
      print('До связи...')
      break
    result = convertNumberToString(number)
    print(mergeString(result, ' '))

main()