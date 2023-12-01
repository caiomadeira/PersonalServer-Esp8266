import win32com.client as client
import re

Filter = "Novo documento adicionado na pasta Recibos disponível no site bervel"

months_2023 = ["Janeiro/2023", "Fevereiro/2023", "Março/2023", "Abril/2023", "Maio/2023", "Junho/2023", "Julho/2023",
               "Agosto/2023", "Setembro/2023", "Outubro/2023", "Novembro/2023"]

months_2023_short = ["01/2023", "02/2023", "03/2023", "04/2023", "05/2023", "06/2023", "07/2023",
                     "08/2023", "09/2023", "10/2023", "11/2023", "12/2023"]

claro_trash_chars = ["<https://www.claro.com.br/static/email/202107/07151401/images/box_parte6.png> \t\t",
                     "<https://www.claro.com.br/static/email/202107/07151401/images/box_parte6.png>",
                     r"\t", "<", ">", "<>", r" \t ", " "]

claro_MANUAL_VALUES = ["77,99", "107.24", "27,64", "105,63", "105,63", "111,96", "112,13", "112,09", "109,75", "112,49", "114,93", "109,75",]

count = 0
outlook = client.Dispatch('Outlook.Application').GetNameSpace('MAPI')
account = outlook.Folders
root_folder = outlook.Folders.Item(1)
bills = []


def set_messages(criteria):
    messages = []
    for folder in root_folder.Folders:
        if folder.Name == 'Caixa de Entrada':
            if criteria == "LIGHT":
                months = months_2023
                for month in months:
                    messages.append(folder.Items.Restrict(
                        f"[Subject] = 'CAIO CÉSAR MADEIRA MATTOSO DE SOUZA, sua fatura digital Light chegou! {month}'"))
            elif criteria == 'CLARO':
                months = months_2023_short
                for month in months:
                    messages.append(folder.Items.Restrict(
                        f"[Subject] = 'Sua fatura Claro Net por e-mail - {month}'"))
    print(messages)
    return messages


def get_bills_from_emails(criteria, bills):
    global messages_objects, search_string, claro_value
    if criteria == "LIGHT":
        search_string = "Valor da Fatura: R$"
    elif criteria == "CLARO":
        search_string = "Total a pagar "
    messages_objects = set_messages(criteria)
    for messages in messages_objects:
        for message in messages:
            # print(message.body.split("\n"))
            for value in str(message.body).split("\n"):
                if search_string in value:
                    if criteria == "LIGHT":
                        new_value = value.strip().replace(search_string, "")
                        bills.append(float(new_value.replace(",", ".")))
                    elif criteria == "CLARO":
                        new_value = value.strip().replace(search_string, "")
                        bills.append(new_value)
    claro_bills = []
    if criteria == "CLARO":
        for char in claro_trash_chars:
            for bill in bills:
                new_claro_val = bill.replace(char, "").split("<", 1)[0]
                final_claro_value = new_claro_val.replace(char, "\t", 2).split(">", 1)[0]
                final_claro_value = re.sub('\s+', '', final_claro_value)
                if final_claro_value != '':
                    if not 'claro.com.br' in final_claro_value:
                        claro_bills.append(final_claro_value)
        claro_bills = list(set(claro_bills))
        bills = claro_bills
    print("claro bills: ", claro_bills)
    print("claro bills count: ", len(bills))
