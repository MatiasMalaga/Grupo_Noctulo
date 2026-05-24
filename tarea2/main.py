
import random
from jugadores import portero
from jugadores import defensa
from jugadores import mediocampista
from jugadores import delantero
import pandas as pd



pais_elegido = "España"

jugadores_titulares = [

    # 1 portero
    portero("unai simon", 29, 1.90, 1, 18, 94),

    # 4 defensas
    defensa("marcos llorente", 31, 1.84, 14, 82, 88),
    defensa("pau cubarsi", 19, 1.84, 4, 91, 85),
    defensa("aymeric laporte", 32, 1.91, 24, 95, 90),
    defensa("marc cucurella", 28, 1.73, 3, 87, 83),

    # 4 mediocampistas
    mediocampista("rodri", 29, 1.91, 16, 97, 89),
    mediocampista("pedri", 23, 1.74, 8, 95, 80),
    mediocampista("fermin lopez", 23, 1.74, 11, 88, 76),
    mediocampista("nico williams", 24, 1.81, 17, 84, 70),

    # 2 delanteros
    delantero("lamine yamal", 18, 1.80, 19, 93, 96),
    delantero("mikel oyarzabal", 29, 1.81, 21, 89, 84)
]




print("--- simulador de campeon del mundo ---")

print("\n--------------acciones en la cancha---------------\n")

numero_ale1=random.randint(0,10)
numero_ale2=random.randint(1,4)
numero_ale3=random.randint(5,8)
numero_ale4=random.randint(9,10)

jugadores_titulares[numero_ale1].correr()
jugadores_titulares[0].atajar()

numero_ale1=random.randint(0,10)

jugadores_titulares[numero_ale1].correr()
jugadores_titulares[numero_ale2].interceptar()

numero_ale1=random.randint(0,10)

jugadores_titulares[numero_ale1].correr()
jugadores_titulares[numero_ale3].organizar_juego()

numero_ale1=random.randint(0,10)

jugadores_titulares[numero_ale1].correr()
jugadores_titulares[numero_ale4].patear_al_arco()


print("\n----------roles del equipo:----------\n")

# polimorfismo
for jugador in jugadores_titulares:
    jugador.mostrar_rol()



lista_diccionarios = []
diccio={}
for jugador in jugadores_titulares:
    diccio={
        "pais": "España",
        "dorsal": jugador.dorsal,
        "nombre": jugador.nombre,
        "edad": jugador.edad,
        "altura_m": jugador.altura,
        "posicion": jugador.mostrar_rol()
    }
    lista_diccionarios.append(diccio)

df = pd.DataFrame(lista_diccionarios)


edad_media=df["edad"].mean()
#print(edad_media)

print("\n--------metricas--------")
print("la edad media del equipo es: ",round(edad_media, 2))
altura_max=df["altura_m"].max()
print("la altura maxima del equipo es de: ", (altura_max))

print("\n")
print("--------------------------------------tabla del equipo----------------------------------------")
print(df)
print("\n")




pos=df["posicion"]
edades=df["edad"]

porteros = []
defensas = []
mediocampistas = []
delanteros = []


edades_p=[]
edades_def=[]
edades_m=[]
edades_del=[]



for frase, edad in zip(pos, edades):
      
    if "portero" in frase:
        porteros.append(frase)
        edades_p.append(edad)  # Agregamos la edad a su lista correspondiente
        
    elif "defensa" in frase:
        defensas.append(frase)
        edades_def.append(edad)
        
    elif "mediocampista" in frase:
        mediocampistas.append(frase)
        edades_m.append(edad)
        
    elif "delantero" in frase:
        delanteros.append(frase)
        edades_del.append(edad)
        

print("\n----------jugadores por posicion:----------\n")

print("Cantidad de porteros: ", len(porteros))
print("Cantidad de defensas:", len(defensas))
print("Cantidad de mediocampistas:", len(mediocampistas))
print("Cantidad de delanteros:", len(delanteros))

print("\n----------edad media por posicion:----------\n")

media_p=sum(edades_p)/len(edades_p)
media_def=sum(edades_def)/len(edades_def)
media_m=sum(edades_m)/len(edades_m)
media_del=sum(edades_del)/len(edades_del)



print("edad media de porteros: %.2f" % (media_p))
print("edad media de defensas: %.2f" % (media_def))
print("edad media de mediacampistas: %.2f" % (media_m))
print("edad media de delanteros: %.2f" %  (media_del))




# Guardamos el resultado en un archivo nuevo (index=False evita la columna extra de números)
df.to_csv("titulares_españa.csv", index=False)
print("\nArchivo 'titulares_españa.csv' generado con éxito.")


