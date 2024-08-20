import requests
import tkinter as tk
from tkinter import ttk, messagebox
import geocoder
import datetime

def obter_previsao(cidade):
    api_key = "01f71d97317f9c2c85c481065c73452b"
    link = f"https://api.openweathermap.org/data/2.5/forecast?q={cidade}&appid={api_key}&units=metric&lang=pt_br"
    requisicao = requests.get(link)
    return requisicao.json()

def atualizar_interface(cidade):
    previsao = obter_previsao(cidade)
    lista_temperaturas = []
    lista_condicoes = []
    lista_horas = []

    for item in previsao['list']:
        hora = item['dt_txt'][11:16]  # Extrai a hora da previsão
        temp = round(item['main']['temp'], 1)
        condicao = item['weather'][0]['main']
        lista_temperaturas.append(temp)
        lista_condicoes.append(condicao)
        lista_horas.append(hora)

    temperatura_atual.set(f"{lista_temperaturas[0]:.1f}°C")
    hora_atual.set(datetime.datetime.now().strftime('%H:%M'))

    for i in range(8):
        temp_labels[i].config(text=f"{lista_temperaturas[i]:.1f}°C")
        hour_labels[i].config(text=f"{lista_horas[i]}")
        icon_labels[i].config(text=icone_condicoes[lista_condicoes[i]])

def obter_localizacao_atual():
    g = geocoder.ip('me')
    cidade = g.city if g.city else "São Paulo"
    return cidade

def perguntar_localizacao():
    resposta = messagebox.askyesno("Permissão de Localização", "Você deseja usar a sua localização atual?")
    if resposta:
        cidade = obter_localizacao_atual()
        cidade_entry.insert(0, cidade)
        atualizar_interface(cidade)
    else:
        cidade_entry.insert(0, "Digite sua cidade")

def carregar_icones():
    icones = {
        "Clear": "☀️",
        "Clouds": "☁️",
        "Rain": "🌧️",
        "Snow": "❄️",
        "Thunderstorm": "⛈️",
        "Drizzle": "🌦️",
        "Mist": "🌫️",
    }
    return icones

root = tk.Tk()
root.title("Previsão do Tempo")

root.configure(bg='white')
frame = ttk.Frame(root, padding="10", style='MainFrame.TFrame')
frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Cidade:", background='white', font=('Arial', 12)).grid(row=0, column=0, sticky=tk.W)
cidade_entry = ttk.Entry(frame, width=20, font=('Arial', 12))
cidade_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

botao_buscar = tk.Button(frame, text="Buscar", command=lambda: atualizar_interface(cidade_entry.get()), bg='dodgerblue', fg='white', font=('Arial', 12))
botao_buscar.grid(row=0, column=2, sticky=tk.W)

temperatura_atual = tk.StringVar()
hora_atual = tk.StringVar()
ttk.Label(frame, text="Temperatura atual:", background='white', font=('Arial', 12)).grid(row=1, column=0, sticky=tk.W)
ttk.Label(frame, textvariable=temperatura_atual, background='white', font=('Arial', 12, 'bold')).grid(row=1, column=1, sticky=tk.W)
ttk.Label(frame, textvariable=hora_atual, background='white', font=('Arial', 12)).grid(row=1, column=2, sticky=tk.W)

icons_frame = ttk.Frame(frame, style='MainFrame.TFrame')
icons_frame.grid(row=2, column=0, columnspan=3, pady=10)

temp_labels = []
hour_labels = []
icon_labels = []
icone_condicoes = carregar_icones()

for i in range(8):
    icon_label = ttk.Label(icons_frame, background='white', font=('Arial', 20))
    icon_label.grid(row=0, column=i, padx=5)
    icon_labels.append(icon_label)

    temp_label = ttk.Label(icons_frame, background='white', font=('Arial', 10))
    temp_label.grid(row=2, column=i, padx=5)
    temp_labels.append(temp_label)

    hour_label = ttk.Label(icons_frame, background='white', font=('Arial', 10))
    hour_label.grid(row=3, column=i, padx=5)
    hour_labels.append(hour_label)

style = ttk.Style()
style.configure('MainFrame.TFrame', background='white')

root.after(100, perguntar_localizacao)

root.mainloop()
