Задание даннеое на практику:

Цель работы: разработка платформы парсинга данных о соискателях и 
вакансиях с платформ hh.ru, avito.ru, habr Карьера. 
Задачи: 
1) изучить существующие платформы для парсинга (beautiful soap, 
selenium или API платформ); 
2) сформулировать функциональные требования к системе; 
3) спроектировать базу данных; 
4) написать инструкцию пользователя; 
5) провести тестирование системы. 
Требования к функционалу: 
1) Возможность формирования запроса для парсинга данных по таким 
полям, как фио, название должности, навыки, формат работы и т.д. 
2) Загрузка в базу данных информации по результатам парсинга и 
вывод аналитики по параметрам (например, сколько есть вакансий и 
сколько кандидатов на вакансию). 
Требования к frontend: 
Может быть реализован в качестве веб-интерфейса на любом стеке 
технологий (например, фреймворк Django). Также в качестве интерфейса 
взаимодействия с клиентом может быть реализован телеграм-бот. 
Требования к backend: 
Язык программирования: Python. 
База данных: MySQL, PostgreSQL, MongoDB. 
Каждый сервис должен быть упакован в отдельный Docker-контейнер. 
Вся система должна подниматься посредством docker-compose.
