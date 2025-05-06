# BaseStationParser 

## ✨ Функционал:

- Парсинг UML-модели из XML и генерация meta.json с описанием классов и связей

- Сравнение config.json и patched_config.json с формированием delta.json

- Применение delta.json к config.json для получения res_patched_config.json

- Генерация config.xml на основе структуры UML

## 🤖 Стек:

- Python 3.10+

- Стандартные библиотеки: xml.etree.ElementTree, json, typing, copy

## ⚡ Инструкция по запуску:

1. Клонируем репозиторий 
git clone https://github.com/Kurillccc/BaseStationParser
cd base-station-parser

2. В папку input нужно поместить желаемы входные файлы, прежварительно удалив старые

3. Запустить скрипт 
python main.py
