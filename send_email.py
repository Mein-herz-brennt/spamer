import smtplib
import time
from email.mime.text import MIMEText

""" Текст листа який ми відправляємо русні """

message = MIMEText("Всім привіт!\n"
                   "Ми з колегами з МВС запустили сайт і телеграм канал 'Ищи своих' з полоненими і вбитими росіянами.\n"
                   "Ціль сайту, щоб кожен росіянин міг подивитись чи не його це родич, близький, друг.\n "
                   "А то їм досі кажуть, що ми тікаємо і здаємось.\n"
                   "Надішліть це кожному кого знаєте в РФ.\n"
                   "Хай шукають своїх серед вбитих і полонених.\n"
                   "Оновлюємо постійно.\n"
                   "Є чим : \n"
                   "https://200rf.com \n"
                   "https://t.me/rf200_now/79")  # текст листа який ми відправляємо русні

""" Почта з якої ми відправляємо їм листи (обов'язково gmail) """

mail = "vashapochta@gmail.com"  # після того як програма завершила своє виконання замініть пошту на іншу обов'язково
                                # в лапках

""" Пароль до вказаної вище почти """

password = "******"  # після того як програма завершила своє виконання замініть пароль на пароль до нової
                     # пошти яку вставите вище обов'язково в лапках

""" Функція для відправки листів """


def send_mail(email, password, FROM, TO, msg):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()


""" Функція яка вже безпосередньо виконується і відправляє листи """
"""З однієї почти максимум 1095 листів, тобто по 3 листи на 1 почту це виходить за 1 раз програма обробляє 365 почт 
русні +- 2 години роботи програми на сервері"""


def main():
    with open("розсилка.txt") as file:
        text = file.readlines()

    text_all = []
    for i in range(365):
        text_all.append(text[i])
        text.pop(i)

    with open("розсилка.txt", "w") as file:
        file.writelines(text)
    for i in range(len(text_all)):
        text_all[i] = text_all[i].replace("\n", "")
    count = 0
    try:
        for to in text_all:
            for i in range(3):
                send_mail(mail, password, mail, to, message)
                time.sleep(10)
            count += 1
            print(count)
            time.sleep(2)
    except Exception as _e:
        print("Sending emails stopped Error ------>", _e)
    return "please insert a new email and password and run the code again"


if __name__ == "__main__":
    print(main())
