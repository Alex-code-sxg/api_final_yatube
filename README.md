<h1 align="center">API для web проекта YaTube</h1>
<h2 align="center">
  
<img src="https://img.shields.io/npm/dy/silentlad">

<img src="https://img.shields.io/badge/vue-2.2.4-green.svg">

<img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103" >

<img src="https://img.shields.io/github/stars/silent-lad/VueSolitaire.svg?style=flat">

<img src="https://img.shields.io/github/languages/top/silent-lad/VueSolitaire.svg">

<img src="https://img.shields.io/github/issues/silent-lad/VueSolitaire.svg">

<img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat">
</p>

<img src="./readme_assets/h2.png" width="100%">  
  


## Описание.
- Проект позволяет осуществлять чтение и редактирование информации на ресурсе www.YaTubeprimer.ru

- Структура проекта выглядит следующим образом:

<img src="./readme_assets/3.png" width="100%"> 

## Корневые маршруты проекта

```
{
    "posts": "http://127.0.0.1:8000/api/v1/posts/",
    "groups": "http://127.0.0.1:8000/api/v1/groups/",
    "follow": "http://127.0.0.1:8000/api/v1/follow/"
}
```

## Общее описание

- Доступ к чтению информации предоставляется всем пользователям.

- Если вы хотите произвести редактирование ранее размещенной информации пожалуста авторизуйтесь.

## Посты проекта YaTube 

### Пост

```
http://127.0.0.1:8000/api/v1/posts/
```



### Комментарии к посту

```
http://127.0.0.1:8000/api/v1/posts/1/comments/
```

## Сообщества проекта YaTube 
!!! На текущий момент создание и редактирование групп через API не осуществляется !!!

- Для получения информации о текущих сообществах проекта YaTube необходимо отправить запрос на:
```
http://127.0.0.1:8000/api/v1/groups/
```
## Подписка на авторов проекта YaTube
!!! Необходима авторизация !!!
```
http://127.0.0.1:8000/api/v1/follow/
```
## Документация проекта API YaTube
```
http://127.0.0.1:8000/api/v1/redoc/
```
<img src="./readme_assets/5.png" width="100%">

## Техническое описание проекта API YaTube

Проек разработан с использованием следующих технологий, модулей, библиотек:

- Django Rest Framework v. 3.12.4
- Djoser (2.1.0)  Simple JWT (4.7.2)
- CORS
- дописать


- Пагинация 
- Фильтрация
- Поиск
- дописать