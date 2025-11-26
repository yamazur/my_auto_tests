# Изучаем selenium и pytest 
Пишем тексты на python, selenium, pytest
# How to start the project
1. Установка виртуального окружения
```python -m venv venv_test```
или
```py -3.9 -m venv venv_test```
или
```python3.13 -m venv venv_test```
2. Версия python
```python --version```
или
```py -0```
.
Нужная версия python -
```py -3.13 -m venv venv_test```
3. Инициализация Git:
```.git ignore```
,
```git init```
4. Создание коммита:
```git status```,
Добавление файлов - ```git add (имя файла)```
Коммит - ```git commit -m "Пример названия"```
5. Установка зависимостей : 
```pip install Имя пакета```,
```pip list```
Фиксируем зависимости: 
```pip freeze > requirments.txt```
#-------------------------------------------------------------------------------#

# My first git reposy
## Commands for git 
1. Initial git's repo 
``` 
git init
``` 
2. Check repo
```
git status
```
3. Add files to commit
```
git add . 
```
4. Make a commit
```
git commit -m 
```
5. Show history of commits
```
git show
```
```
detail info about last commit and display list of commits
```

```
git log (one line, all, n, -2)
```
6. Create a brench
```
 git switch -c develop
```
#-------------------------------------------------------------------------------#

# Connect by SHH
1. Создаем файл ```config``` и вставляем туда данный образец со своими данными 
    ```Host фамилия.ru
	HostName github.com
	User ваше имя с гит хаба
	IdentityFile ~/.ssh/id_25519_фамилия
	IdentitiesOnly=yes```

2. Вставляем команду в папку ssh, в которою вошли через git bush here(последующие команды вводим тут же!!!) --```ssh-keygen -t ed25519 -C "Ваш @gmail адрес"```
Затем вводим имя файла(во всех примерах я указал фамилию), затем создаете и подтверждаете ваш пароль
3. Вставляем команду```id_25519_ваша_фамилия```
4. Вставляем команду```clip < id_25519_фамилия.pub``` 
5. Вставляем команду```Вставляем ключ из команды №3 в гит хаб во вкладку 'ключи_ssh', вставляем ключ и задаем любое имя```
6. Вставляем команду```ssh -T git@фамилия.ru```
7. Должно появиться приветствие с вашим именем
проект по selenium python
первый большой проект
