# Часть с созданием кода взаимствована у пользователя SerdarAD
# Я лишь доработал это, чтобы постоянно не запускать по новой
# И сделал удобную запись в файл, при необходимости, можно все поменять, если, конечно, руки из нужного места.

# Код наипростейший, как по мне.
# Удачного пользования.

#Я доработал изменненый скрипт 
#Убрал все что не нужно, сделал возможность использования под линуксом
import random
import httpx
import os
import time
import requests
from hashlib import md5

keys = requests.get(
    "https://keysesforwarp.serdarad.repl.co/").content.decode().split(",")
if len(keys) == 0:
    print("Нет ключей для генерации!")
    exit()
gkeys = []
os.system('cls' if os.name == "nt" else 'clear')
# Самая важная строчка кода, без нее ничего работать не будет!
print("\n█░█░█ ▄▀█ █▀█ █▀█ ▄█▄\n▀▄▀▄▀ █▀█ █▀▄ █▀▀ ░▀░\n")
print(
    'Автор кода: неизвестен  Дописали код: @v1kesl (TG)'
)
# Заголовок окна
print()  #его нет(

# Получение значения для цикла
value_int = int(
    input(
        "Добро пожаловать в генератор ключей WARP+\nВведите желаемое количество ключей: "
    ))
a = 0
# Самый обычный цикл while
while a < value_int:
    a += 1
    print(
        "<======================================WARP+ Generate=============================================>"
    )
    print("Создается ключ:", a)

    try:
        # Заголовок с переменными
        headers = {
            "CF-Client-Version": "a-6.11-2223",
            "Host": "api.cloudflareclient.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.1",
        }

        with httpx.Client(base_url="https://api.cloudflareclient.com/v0a2223",
                          headers=headers,
                          timeout=30.0) as client:

            r = client.post("/reg")
            id = r.json()["id"]
            license = r.json()["account"]["license"]
            token = r.json()["token"]
            r = client.post("/reg")
            id2 = r.json()["id"]
            token2 = r.json()["token"]

            headers_get = {"Authorization": f"Bearer {token}"}
            headers_get2 = {"Authorization": f"Bearer {token2}"}
            headers_post = {
                "Content-Type": "application/json; charset=UTF-8",
                "Authorization": f"Bearer {token}",
            }

            json = {"referrer": f"{id2}"}
            client.patch(f"/reg/{id}", headers=headers_post, json=json)

            client.delete(f"/reg/{id2}", headers=headers_get2)

            key = random.choice(keys)

            json = {"license": f"{key}"}
            client.put(f"/reg/{id}/account", headers=headers_post, json=json)

            json = {"license": f"{license}"}
            client.put(f"/reg/{id}/account", headers=headers_post, json=json)

            r = client.get(f"/reg/{id}/account", headers=headers_get)
            account_type = r.json()["account_type"]
            referral_count = r.json()["referral_count"]
            license = r.json()["license"]

            client.delete(f"/reg/{id}", headers=headers_get)
            
            if referral_count < 500:
                
                requests.get(
                    f"https://keysesforwarp.serdarad.repl.co/?d={key}&s={md5((key + 'iop').encode()).hexdigest()}"
                )
                a -= 1
                print("1гб лицензия, ключ удален")
                del keys[keys.index(key)]
                continue
            gkeys.append(license)
            print(
                f"Лицензия:{license}\nДанных: {referral_count}gb\nТип:{account_type}"
            )
            if referral_count == 1:
                with open('gened1GB.txt','a') as f:
                    f.write(license + '\n')
            else:
                with open('gened12PB.txt','a') as f:
                    f.write(license + '\n')

    # Ошибка
    except:
        print("Ошибка.")
        time.sleep(15)
    if a % 2 == 0:
        time.sleep(60)

os.system('cls' if os.name == 'nt' else 'clear')
for x in gkeys:
    print(x)
print('Вывести список?через запятую,ответы[y\\n]')
a = input()
if a == "y":
    for z in range(10):
        print()
    for z in gkeys:
        print(f"\"{z}\",")

input('\nНажмите Enter для выхода\n')
