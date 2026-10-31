from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests


def update_target_label(event):
    code = target_combobox.get()
    target_label.config(text=currencies.get(code, ''))


def update_base1_label(event):
    code = base1_combobox.get()
    base1_label.config(text=currencies.get(code, ''))


def update_base2_label(event):
    code = base2_combobox.get()
    base2_label.config(text=currencies.get(code, ''))


def get_rate(base_code, target_code):
    """Возвращает курс target_code за 1 base_code или None при ошибке."""
    response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}', timeout=10)
    response.raise_for_status()
    data = response.json()
    return data['rates'].get(target_code)


def exchange():
    base1_code = base1_combobox.get().strip()
    base2_code = base2_combobox.get().strip()
    target_code = target_combobox.get().strip()

    if not (base1_code and base2_code and target_code):
        mb.showwarning('Внимание', 'Выберите обе базовые и целевую валюты')
        return

    try:
        rate1 = get_rate(base1_code, target_code)
        rate2 = get_rate(base2_code, target_code)

        if rate1 is None or rate2 is None:
            mb.showerror('Ошибка', 'Валюта не найдена в ответе API')
            return

        base1 = currencies[base1_code]
        base2 = currencies[base2_code]
        target = currencies[target_code]

        mb.showinfo(
            'Курс обмена',
            f'1 {base1} ({base1_code}) = {rate1:.4f} {target} ({target_code})\n'
            f'1 {base2} ({base2_code}) = {rate2:.4f} {target} ({target_code})'
        )
    except Exception as er:
        mb.showerror('Ошибка', str(er))


currencies = {
    'EUR': 'Евро',
    'USD': 'Доллар США',
    'JPY': 'Японская йена',
    'GBP': 'Фунт стерлингов',
    'AUD': 'Австралийский доллар',
    'CAD': 'Канадский доллар',
    'CHF': 'Швейцарский франк',
    'CNY': 'Китайский юань',
    'RUB': 'Российский рубль',
    'KZT': 'Казахстанский тенге',
    'UZS': 'Узбекский сум',
}

root = Tk()
root.title('Курс обмена валют')
root.geometry('380x340')


Label(root, text='Первая базовая валюта').pack(pady=(8, 0))
base1_combobox = ttk.Combobox(root, values=list(currencies.keys()), state='readonly')
base1_combobox.pack(pady=3, padx=10)
base1_combobox.bind('<<ComboboxSelected>>', update_base1_label)
base1_label = ttk.Label()
base1_label.pack()


Label(root, text='Вторая базовая валюта').pack(pady=(8, 0))
base2_combobox = ttk.Combobox(root, values=list(currencies.keys()), state='readonly')
base2_combobox.pack(pady=3, padx=10)
base2_combobox.bind('<<ComboboxSelected>>', update_base2_label)
base2_label = ttk.Label()
base2_label.pack()


Label(root, text='Целевая валюта').pack(pady=(8, 0))
target_combobox = ttk.Combobox(root, values=list(currencies.keys()), state='readonly')
target_combobox.pack(pady=3, padx=10)
target_combobox.bind('<<ComboboxSelected>>', update_target_label)
target_label = ttk.Label()
target_label.pack()

Button(text='Получить курсы обмена', command=exchange).pack(pady=14, padx=10)

root.mainloop()