# шифоровать или дешифровать
# если шифровать, то для англ и рус
# тоже самое для дешифрования


def encrypt_en(text, num):
    symbols = '.,!&?+-" '
    for i in text:

        if 96 < ord(i) < 123: # нижний регистр
            if 96 < ord(i) + num < 123:  # прибавляем к символу
                print(chr(ord(i) + num), end='')
            elif num > 0:
                a = ord(i) + num - 26  # если выходит за пределы юникода
                print(chr(a), end='')
            elif num < 0:
                a = ord(i) - num + 26
        if 64 < ord(i) < 92: # заглавные
            if 64 < ord(i) + num < 92:  # прибавляем к символу
                print(chr(ord(i) + num), end='')
            elif num > 0:
                a = ord(i) + num - 26  # если выходит за пределы юникода
                print(chr(a), end='')
            elif num < 0:
                a = ord(i) - num + 26
        if i in symbols:
            print(i, end='')

def encrypt_ru(text,num):
    alfavit_RU = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    small_symbols = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    symbols = '.,!&?+- '
    for i in text:
        if i in alfavit_RU:  # можно сделать, чтобы проверялось на заглавную
            if alfavit_RU.index(i) + num < len(alfavit_RU):
                print(alfavit_RU[alfavit_RU.index(i) + num], end='')
            else:
                print(alfavit_RU[alfavit_RU.index(i) + num - 32], end='')
        if i in small_symbols:
            if small_symbols.index(i) + num < len(small_symbols):
                print(small_symbols[small_symbols.index(i) + num], end='')
            else:
                print(small_symbols[small_symbols.index(i) + num - 32], end='')
        if i in symbols:
            print(i, end='')

def decrypt_en(text):
    for j in range(1, 26):
        encrypt_en(text, j)
        print()

def decrypt_ru(text):
    for i in range(1, 32):
        encrypt_ru(text, i)
        print()

def main():
    print("------------------------------------------------")
    print('Шифрование и дешифрование с помощью шифра Цезаря')
    print("------------------------------------------------")

    ans_1 = int(input('шифрование или дешифрование(1-шифр, 2-дешифр): '))
    if ans_1 == 1:
        ins_lng = input('На каком языке?(en - англ, ru - рус): ')
        d = int(input('Сдвиг: '))
        text = input('Введите строку: ')
        if ins_lng == 'en':
            encrypt_en(text, d)
        else:
            encrypt_ru(text, d)
    if ans_1 == 2:
        ins_lng = input('На каком языке?(en - англ, ru - рус): ')
        text = input('Введите строку: ')
        if ins_lng == 'en':
            decrypt_en(text)
        else:
            decrypt_ru(text)
if __name__ == "__main__":
    main()