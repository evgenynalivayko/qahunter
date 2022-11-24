#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
в) Модифицируйте  авто-тест с помощью языка программирования python и библиотек selene, pytest

Для работы теста необходимо установить
python3.8

Библиотеки
pytest
selene==2.0.0b1
selenium==4.1.0
requests

Запуск теста

pytest test_integration_with_hh.py

В тесте сломан один из локаторов
Нужно починить

"""


from selene.support.shared import browser
from selene import have
import requests


def test_integration_with_hh():
    # Открываю страницу Вакансии
    browser.open("http://test.qahunter.ru")
    browser.element("/html/body/header/div/nav/ul/li[1]/a").click()

    # Достаю через api список вакансий с hh.ru, так как это делает бэкенд для qahunter
    response = requests.request('get', 'https://api.hh.ru/vacancies?text=qa&experience=noExperience&experience=moreThan6&specialization=1&only_with_salary=true')
    jobs_from_hh = response.json()["items"]
    jobs = jobs_from_hh[5:15]
    # Беру адрес второй вакансии
    vacancy_url = jobs[1]["alternate_url"]

    # Проверяю, что на сайте ссылка на вторую вакансию соотвествует ссылке взятой с hh.ru
    browser.element('(//div[@class="card__body"])[2]/a').should(have.attribute("href", vacancy_url))

