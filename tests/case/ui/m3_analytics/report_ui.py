import time

import allure
from playwright.sync_api import expect, Page

from pages.UI._3_Analytics.reports_page import ReportsPage


@allure.step("Открыть страницу 'Отчеты'")
def open_page_by_steps(browser: Page):
    page = ReportsPage(browser)

    with allure.step("Перейти в 'Настройки уведомлений'"):
        page.goto_page("/notification-center")
        browser.wait_for_url(page.host + "/notification-center")

    with allure.step("Клик в боковом меню 'Аналитика'"):
        page.SB_ANALYTICS.click()

    with allure.step("Клик в меню 'Отчеты'"):
        page.SB_ANALYTICS_REPORTS.click()

    with allure.step("Открылась страница 'Отчеты'"):
        browser.wait_for_url(page.host + ReportsPage.page_path)

    # todo: legacy
    """
    =============
    @allure.title('Отчеты - проверка отображения отчета со статусом "Не опубликован+Закрыт"')
    > Открыть Отчеты /report
    < Проверить, что нужная страница открыта
    > Создать новый отчет
    >> создание отчета по шагам
    > logout
    > зайти под другим пользователем
    ...
    < Проверить, что созданный отчет не отображается для другого пользователя
    
    =============
    @allure.title('Отчеты - проверка отображения отчета со статусом "Опубликован+Закрыт"')
    > Открыть Отчеты /report
    < Проверить, что нужная страница открыта
    > Создать новый отчет
    >> создание отчета по шагам
    > сделать отчет публичным
    > logout
    > зайти под другим пользователем
    ...
    > Кнопка редактирования отчета disabled
    ...
    < Проверить, что отчет публичен, но его нельзя редактировать
    
    =============
    @allure.title('Отчеты - проверка отображения отчета со статусом "Опубликован+Открыт"')
    > Открыть Отчеты /report
    < Проверить, что нужная страница открыта
    > Создать новый отчет
    > сделать отчет публичным
    > сделать отчет open
    > logout
    > зайти под другим пользователем
    ...
    > ? Кнопка редактирования disabled
    > ? Изменения доступа к отчету недоступны
    >> PUBLESHED_TOGLER; REPORT_CLOSED_TOGLER ..is_disabled
    >> Добавление доступа к отчету для роли .is_disabled
    
    =============
    @allure.title('Отчеты - установка доступа к отчету для роли на "Чтение"')
    > Открыть Отчеты /report
    < Проверить, что нужная страница открыта
    > Создать новый отчет
    > Установить доступ роли "Чтение"
    > logout
    > зайти под другим пользователем
    ...
    > Кнопка редактирования недоступна
    > Изменения доступа к отчету недоступны
    < Проверить, что отчет в доступе "Чтение", но редактировать его нельзя
    > Чекбокс "Чтение" выбран
   
    =============
    @allure.title('Отчеты - установка доступа к отчету для роли на "Запись"')
    > Открыть Отчеты /report
    < Проверить, что нужная страница открыта
    > Создать новый отчет
    > Установить доступ роли "Запись"
    > logout
    > зайти под другим пользователем
    ...
    > Кнопка редактирования доступна
    > Изменения доступа к отчету недоступны
    > Чекбокс "Запись" выбран
    
    =============
    @allure.title('Отчеты - установка доступа к отчету для роли на "Выполнение"')
    > Открыть Отчеты /report
    < Проверить, что нужная страница открыта
    > Создать новый отчет
    > Установить доступ роли "Выполнение"
    > logout
    > зайти под другим пользователем
    ...
    > Кнопка редактирования отчета недоступна
    > Изменения доступа к отчету недоступны
    > Чекбокс "Выполнение" выбран
    
    =============
    @allure.title('Отчеты - установка доступа к отчету для роли на "Настройка доступа"')
    > Открыть Отчеты /report
    < Проверить, что нужная страница открыта
    > Создать новый отчет
    > Установить доступ роли "Настройка доступа"
    > logout
    > зайти под другим пользователем
    ...
    > Кнопка редактирования отчета доступна
    >> PUBLESHED_TOGLER; REPORT_CLOSED_TOGLER ..is_disabled
    > Чекбокс "Настройка доступа" выбран

    =============
    Установка доступа, но уже для пользователя ^4^ кейса
    
    =============
    @allure.title('Отчеты - удаление доступа к отчету для пользователя, роль которого имеет доступ на "Выполнение"')
    > Открыть Отчеты /report
    < Проверить, что нужная страница открыта
    > Создать новый отчет
    > Установить доступ пользователю "Выполнение"
    > logout
    > зайти под другим пользователем
    ...
    > Кнопка редактирования недоступна
    > Настройки доступа недоступны
    > Добавить пользователя в "Настройках доступа" нельзя
    > Чекбокс "Настройка доступа" выбран
    > logout
    > Авторизация первым пользователем
    ...
    > В "Настройках доступа" убрать чекбоксы "выполнение.запись.чтение" 
    > logout
    > зайти под другим пользователем
    ...
    > Отчет перестал отображаться для другого пользователя
    
    =============
    @allure.title('Отчеты - проверка доступа к детализации, фильтрам и настройкам визуализации в отчете (для роли на ''Чтение)')
    > Открыть Отчеты /report
    > Открыть тестовый отчет
    > Проверка наличия компонентов страницы
    
    =============
    @allure.title('Отчеты - Удаление последнего отчета')
    
    """
