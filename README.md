# PTC_QAP_tests

Итоговый проект по автоматизации тестирования

→ Объект тестирования: https://b2c.passport.rt.ru

Заказчик передал вам следующее задание:

Протестировать требования.

Разработать тест-кейсы (не менее 15). Необходимо применить несколько техник тест-дизайна.

Провести автоматизированное тестирование продукта (не менее 15 автотестов). Заказчик ожидает по одному автотесту на каждый написанный тест-кейс. Оформите свой набор автотестов в GitHub.

Оформить описание обнаруженных дефектов. Во время обучения вы работали с разными сервисами и шаблонами, используйте их для оформления тест-кейсов и обнаруженных дефектов. (если дефекты не будут обнаружены, то составить описание трех дефектов)



___________

conftest.py - файл с фикстурой инициализации драйвера и глобальными переменными

base_page.py - описание методов работы с базовой страницей

auth_page.py - описание страницы авторизации (локаторы и функции)

register_page.py - описание страницы регистрации (локаторы и функции)

forgot_pass_page.py - описание страницы восстановления пароля (локаторы и функции)

user_page.py - описание страницы личного кабинета юзера (локаторы и функции)

tests/ - папка с тестами