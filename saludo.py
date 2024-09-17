import pandas as pd

# Read the Excel file 
df = pd.read_excel('Saludo.xlsx', sheet_name=0)
# Read the Excel file 1
df1 = pd.read_excel('Saludo.xlsx', sheet_name=1)
# Read the Excel file 2
df2 = pd.read_excel('Saludo.xlsx', sheet_name=2)

n = 1
import time
import pywhatkit

# Asegúrate de que el número de teléfono esté en el formato correcto
numero_telefono = "+573146747578"

for _ in range(n):
    random_malsonante = df2['Malsonante'].sample().iloc[0]
    random_saludo = df1['Saludo'].sample().iloc[0]
    saludo_mar = random_saludo,random_malsonante
    saludo_mar = " ".join(saludo_mar)
    pywhatkit.sendwhatmsg_instantly(numero_telefono, saludo_mar)
    time.sleep(60)  # Esperar 60 segundos entre envíos para evitar ser bloqueado por spam
