import requests
import json

info_cep_dict= {}
def main():
    while True:
        cep = input('Digite o CEP que deseja informacoes:')
        if len(cep) == 8:
            print(f'O Cep {cep} foi computado com sucesso')
            print()
            break
        else:
            print('Cep Invalido')
    
   
    url = 'https://viacep.com.br/ws/'+cep+'/json/'

    info_cep = requests.get(url)
    info_cep = info_cep.json()
    info_cep_dict['Bairro'] = info_cep['bairro']
    info_cep_dict['Localidade'] = info_cep['localidade']
    info_cep_dict['Logradouro'] = info_cep['logradouro']
    info_cep_dict['Estado'] = info_cep['uf']
    print(f'Info do cep {cep}')
    print()
    for chave,valor in info_cep_dict.items():
        print(f'{chave}: {valor}')

if __name__ =='__main__':
    main()    

    