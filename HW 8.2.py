email = " USER@DOMAIN.COM "
cleaned_email = email.strip() #убираем пробелы
normalized_email = cleaned_email.lower() #меняем регистр
print(normalized_email)

divided_email = normalized_email.split("@") #разделяем, убирая знак @
print(divided_email)

Username = "User"
domain = "domain.com"
info = f"Username: {Username}, domain: {domain}"
print(info)