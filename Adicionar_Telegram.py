import csv
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChat
from openpyxl import Workbook
import tkinter as tk
from tkinter import messagebox

phone_number = "5512981054720"
api_id = "25190918"
api_hash = "63709e45408c464132b04380e7ebddb5"

def extract_group_members(group_name):
    with TelegramClient(phone_number, api_id, api_hash) as client:
        # Encontre o grupo pelo nome
        chats = client.get_dialogs()
        for chat in chats:
            if chat.title == group_name and isinstance(chat.entity, InputPeerChat):
                members = client.get_participants(chat)
                return members

        return []

def save_members_to_excel(members):
    # Crie um novo arquivo Excel e adicione os membros a uma planilha
    wb = Workbook()
    ws = wb.active

    # Escreva os cabeçalhos na primeira linha
    headers = ['ID', 'Nome', 'Username']
    ws.append(headers)

    # Escreva os membros nas linhas subsequentes
    for member in members:
        row = [member.id, member.first_name, member.username]
        ws.append(row)

    # Salve o arquivo Excel
    wb.save('members.xlsx')

def extract_members_and_save():
    # Obtenha os valores inseridos nos campos de entrada
    api_id = api_id_entry.get()
    api_hash = api_hash_entry.get()
    phone_number = phone_number_entry.get()
    group_name = group_name_entry.get()

    if api_id == '' or api_hash == '' or phone_number == '' or group_name == '':
        messagebox.showerror('Erro', 'Preencha todos os campos')
        return

    members = extract_group_members(group_name)

    if members:
        save_members_to_excel(members)
        messagebox.showinfo('Sucesso', 'Membros extraídos e salvos com sucesso no arquivo "members.xlsx"')
    else:
        messagebox.showerror('Erro', 'Grupo não encontrado ou você não tem permissão para acessá-lo')

# Crie a janela principal
window = tk.Tk()
window.title('Extração de Membros do Telegram')
window.geometry('400x200')

# Crie os rótulos e campos de entrada
api_id_label = tk.Label(window, text='API ID:')
api_id_label.pack()
api_id_entry = tk.Entry(window)
api_id_entry.pack()

api_hash_label = tk.Label(window, text='API Hash:')
api_hash_label.pack()
api_hash_entry = tk.Entry(window)
api_hash_entry.pack()

phone_number_label = tk.Label(window, text='Número de Telefone:')
phone_number_label.pack()
phone_number_entry = tk.Entry(window)
phone_number_entry.pack()

group_name_label = tk.Label(window, text='Nome do Grupo:')
group_name_label.pack()
group_name_entry = tk.Entry(window)
group_name_entry.pack()

# Crie o botão de extração e salvamento
extract_button = tk.Button(window, text='Extrair e Salvar', command=extract_members_and_save)
extract_button.pack()

# Inicie o loop de eventos da janela
window.mainloop()
