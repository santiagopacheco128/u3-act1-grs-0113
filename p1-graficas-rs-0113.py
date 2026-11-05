
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Crearemos nuestra tabla y la guardaremos con Pandas

fb = ['Facebook', 8833, True, 2006]
twt = ['Twitter', 8575, False, 2008]
ig = ['Instagram', 7575, True, 2010]
wsp = ['Whatsapp', 8828, True, 2009]
tel = ['Telegram', 2992, False, 2010]
lkn = ['LinkedIn', 7277, False, 2012]

# Creamos una lista de listas
lista_redes_sociales = [fb, twt, ig, wsp, tel, lkn]

# Creamos el DataFrame
df_redes_sociales = pd.DataFrame(
    lista_redes_sociales,
    columns=["nombre", "cantidad", "ES_FB", "año"]
)

# Mostramos la tabla
print(df_redes_sociales)

# Creamos y guardamos el archivo CSV
df_redes_sociales.to_csv("redessociales.csv", index=False)

print("Archivo CSV guardado correctamente")
# crear grafica de lienas
# donde x es nombre en el eje horizontal
# donde y es cantidad en el eje vertical
plt.plot(df_redes_sociales["nombre"],df_redes_sociales["cantidad"])
plt.title("grafica redes sociales 0113")
plt.xlabel("nombre de las redes")
plt.ylabel("cantidad de usuarios")
plt.show()
# creamos una grafica de puntos
plt.scatter(df_redes_sociales["nombre"],df_redes_sociales["cantidad"])
plt.show()
# graficas de barra
plt.bar(df_redes_sociales["nombre"],df_redes_sociales["cantidad"])
plt.title("grafica redes sociales 0113")
plt.xlabel("nombre de las redes")
plt.ylabel("cantidad de usuarios")
plt.show()
# ordenar la grafica de barras de manera descente
# de la mas grande a la mas puqueña
df_rs_ordenar=df_redes_sociales.sort_values("cantidad",ascending=False)
plt.bar(df_rs_ordenar["nombre"],df_rs_ordenar["cantidad"])
plt.show()
# coloreando la grafica
df_rs_ordenar=df_redes_sociales.sort_values("cantidad",ascending=False)
plt.bar(df_rs_ordenar["nombre"],df_rs_ordenar["cantidad"],
        color=["b","g","c","m","y","r"])
plt.show()

# grafica de pastel
# plt.plot(df_redes_sociales["nombre"],df_redes_sociales["cantidad"])
plt.pie(df_redes_sociales["cantidad"],labels=df_redes_sociales["nombre"])
plt.show()