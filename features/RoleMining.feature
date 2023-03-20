Feature: Role Mining

  Scenario: Авторизация в Dataplan
    Given Открыли ссылку на тестовый стенд
    Then Ввели логин и пароль
    When Осуществлен переход на главную страницу

  Scenario: Проверка перехода в Rolemining - Настройки
    Given Открыли ссылку на тестовый стенд
    Then Ввели логин и пароль
    Then Переход в Roleminig - Настройки
    When Осуществлен переход в Rolemining - Настройки


  Scenario: Проверка перехода в Rolemining - Состояние AD
    Given Открыли ссылку на тестовый стенд
    Then Ввели логин и пароль
    Then Переход в Roleminig - Состояние AD
    When Осуществлен переход в Rolemining - Состояние AD

  Scenario: Проверка перехода в Rolemining - Группы и пользователи
    Given Открыли ссылку на тестовый стенд
    Then Ввели логин и пароль
    Then Переход в Roleminig - Группы и пользователи
    When Осуществлен переход в Rolemining - Группы и пользователи

  Scenario: Проверка перехода в Rolemining - Ролевая модель
    Given Открыли ссылку на тестовый стенд
    Then Ввели логин и пароль
    Then Переход в Roleminig - Ролевая модель
    When Осуществлен переход в Rolemining - Ролевая модель


