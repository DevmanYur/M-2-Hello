# Отправляем приветствие

## Зависимости
Установите зависимости командой:  
```sh
pip install -r requirements.txt
```

## Переменные окружения
### Как получить
Чтобы определить переменные окружения, создайте файл `.env` рядом с `main.py` и запишите туда данные в формате:  
`ПЕРЕМЕННАЯ=значение`.



#### Обязательные переменные:  

| Переменная    | Описание                                                                                        |
|:--------------|:------------------------------------------------------------------------------------------------|
| TELEGRAM_TOKEN     | токен от API [Telegram Bot](https://telegram.me/BotFather "получить токен от API Telegram Bot") |


***

## Запуск
Запустите программу командой
```sh
python bot.py
```