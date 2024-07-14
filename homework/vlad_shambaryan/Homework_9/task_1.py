from datetime import datetime


date_str = "Jan 15, 2023 - 12:05:33"

date_obj = datetime.strptime(date_str, "%b %d, %Y - %H:%M:%S")

full_name = date_obj.strftime("%B")
print(f"Полное название месяца: {full_name}")

formatted = date_obj.strftime("%d.%m.%Y, %H:%M")
print(f"Форматированная дата: {formatted}")
