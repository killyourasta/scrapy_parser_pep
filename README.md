## scrapy_parser_pep

## Описание проекта
Выполняется парсинг данных со страницы с общей информацией о PEP (https://peps.python.org/), переход по ссылкам и сбор данных о каждом PEP. Парсер подготавливает данные и сохраняет их в два файла формата csv в папку results.

## Запуск проекта
Выполните следующие команды в терминале:

Клонировать проект из репозитория:
```
git clone https://github.com/killyourasta/scrapy_parser_pep
```
Создать, активировать виртуальное окружение и в него установить зависимости:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
```
pip install -r requirements.txt
```
Запустить парсер из командной строки:
```
scrapy crawl pep
```
### Вывод результатов
Результатом работы парсера будет создание двух файлов:

1. *pep_ДатаВремя.csv*  - содержит список всех PEP (*number, name, status*);
2. *status_summary_ДатаВремя.csv* - содержит сводку по статусам PEP: сколько найдено документов в каждом статусе (*Status, Quantity*). В последней строке этого файла в колонке Total выводится общее количество всех документов.
