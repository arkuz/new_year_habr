### Описание
Данный репозиторий содержит скрипт на Python для приближения нового 2021 года на Хабре :-)

### Стек
 - Python
 - Selene (Selenium)

### Требования к ПО
- Установленный браузер [Google Chrome](https://www.google.ru/chrome/)
- Установленный [Python 3.7 или позднее](https://www.python.org/getit/)
- Установленный инструмент для работы с виртуальными окружениями virtualenv
```bash
pip install virtualenv
```

### Установка на Linux и MacOS
```bash
git clone https://github.com/arkuz/new_year_habr
cd new_year_habr
virtualenv env
source env/scripts/activate
pip3 install -r requirements.txt
```

### Установка на Windows
```bash
https://github.com/arkuz/new_year_habr
cd new_year_habr
virtualenv env
cd env/scripts
activate.bat
pip install -r requirements.txt
```

### Запуск скрипта
Активируем виртуальное окружение и запускаем
```bash
python ny.py
```
