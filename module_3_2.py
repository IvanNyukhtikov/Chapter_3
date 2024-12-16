
def check_add(add):
    if "@" in add:
        if ".com" in add or ".ru" in add or ".net" in add:
            flag = True
        else:
            flag = False
    else:
        flag = False
    return flag

def send_email (message, recipient, *, sender = "university.help@gmail.com"):
    check_recipient = check_add(recipient)
    check_sender = check_add(sender)
    if check_recipient == False or check_sender == False:
        print("Невозможно отправить письмо с адреса ", sender, "на адрес ", recipient)
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(message, "Письмо успешно отправлено с адреса ",  sender, "на адрес", recipient)
    else:
        print(message, "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! ", "Письмо успешно отправлено с адреса ",  sender, "на адрес", recipient)

send_email("Salut!!!", "helpgmail.com")
send_email("Salut!!!", "help@gmail.com")
send_email("Salut!!!", "university.help@gmail.com")
send_email("Salut!!!", "help@gmail.com", sender="university.help@gmail.ru")