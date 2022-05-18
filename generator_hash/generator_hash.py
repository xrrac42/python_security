import hashlib
import string

while True:
    string_hash = input('Digite o texto para ser geradp uma Hash: ')

    menu = int(input('''
    |-------------------------|
    | Escolha um tipo de Hash |
    |-------------------------|                        
    |    1 - MD5              |
    |-------------------------|
    |    2 - SHA1             |
    |-------------------------|
    |    3 - SHA256           |
    |-------------------------|
    |    4 - SHA512           |
    |-------------------------|

    Digite o numero correspondetnte ao Hash: '''))

    if menu == 1:
        resultado = hashlib.md5(string_hash.encode('utf-8'))
        print(f'A hash MD5 de {string_hash}: {resultado.hexdigest()}')

    elif menu == 2:
        resultado = hashlib.sha1(string_hash.encode('utf-8'))
        print(f'A hash sha1 de {string_hash}: eh {resultado.hexdigest()}')
    elif menu == 3:
        resultado = hashlib.sha256(string_hash.encode('utf-8'))
        print(f'A hash sha256 de {string_hash}: {resultado.hexdigest()}')
    elif menu == 4:
        resultado = hashlib.sha512(string_hash.encode('utf-8'))
        print(f'A hash sha512 de {string_hash}: {resultado.hexdigest()}')
    else:
        print('Algo errado, n deu certo')
    decisao = input('Deseja continuar?[N][S] ')
    if decisao.upper() == 'N':
        break