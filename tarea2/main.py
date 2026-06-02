# main.py
# Simulador Mundialista con POO y Pandas – Selección España
# EIE 434 – Programación 2

import pandas as pd
import os
from jugadores import Portero, Defensa, Mediocampista, Delantero

# ──────────────────────────────────────────────
# PARTE 1 – Selección elegida
# ──────────────────────────────────────────────

pais_elegido = "España"

# 11 titulares con formación 4-4-2
jugadores_titulares = [
    # Portero (1)
    Portero("David Raya",        30, 1.83,  1, atajadas_historicas=312, partidos_sin_gol=58),

    # Defensas (4)
    Defensa("Pedro Porro",       26, 1.73,  12, balones_recuperados=143, duelos_ganados=210),
    Defensa("Pau Cubarsí",       19, 1.83,  15, balones_recuperados=98,  duelos_ganados=175),
    Defensa("Aymeric Laporte",   30, 1.89,  14, balones_recuperados=167, duelos_ganados=298),
    Defensa("Alejandro Grimaldo",30, 1.71,  3, balones_recuperados=119, duelos_ganados=189),

    # Mediocampistas (4)
    Mediocampista("Rodri Hernandez", 29, 1.90,  16, asistencias=31, pases_completados=2540),
    Mediocampista("Pedri",           23, 1.74,  20, asistencias=50, pases_completados=3120),
    Mediocampista("Fabián Ruiz",     30, 1.89,   8, asistencias=35, pases_completados=2890),
    Mediocampista("Fermín López",    22, 1.76,  19, asistencias=18, pases_completados=1640),

    # Delanteros (2)
    Delantero("Lamine Yamal",  18, 1.77, 10, goles_anotados=36, regates_exitosos=187),
    Delantero("Nico Williams", 23, 1.81, 17, goles_anotados=33, regates_exitosos=201),
]

# ──────────────────────────────────────────────
# PARTE 4 – Demostración de métodos
# ──────────────────────────────────────────────

print("=" * 55)
print("     SIMULADOR DE CAMPEÓN DEL MUNDO 2026 🏆")
print(f"          Selección: {pais_elegido.upper()}")
print("=" * 55)

print("\n--- ACCIONES EN LA CANCHA ---")

# Métodos heredados y propios del portero
portero = jugadores_titulares[0]
print(portero.correr())
print(portero.atajar())
print(portero.despejar())

# Métodos de un defensa
defensa = jugadores_titulares[2]
print(defensa.correr())
print(defensa.marcar())
print(defensa.cortar_pase())

# Métodos de un mediocampista
medio = jugadores_titulares[6]
print(medio.correr())
print(medio.dar_pase())
print(medio.recuperar_balon())

# Métodos de un delantero
delantero = jugadores_titulares[9]
print(delantero.correr())
print(delantero.patear_al_arco())
print(delantero.regatear())

# Polimorfismo: mostrar_rol() para todos los jugadores
print("\n--- ROLES DEL EQUIPO (Polimorfismo) ---")
for jugador in jugadores_titulares:
    print(jugador.mostrar_rol())

# Presentación individual de cada jugador
print("\n--- PRESENTACIÓN DEL PLANTEL ---")
for jugador in jugadores_titulares:
    print(jugador.saludar())

# ──────────────────────────────────────────────
# PARTE 5 – Pandas: DataFrame, análisis y CSV
# ──────────────────────────────────────────────

# Construir lista de diccionarios para el DataFrame
datos = []
for j in jugadores_titulares:
    fila = {
        "Pais":     pais_elegido,
        "Dorsal":   j.dorsal,
        "Nombre":   j.nombre,
        "Edad":     j.edad,
        "Altura_m": j.altura,
        "Posicion": j.mostrar_rol().split(" - ")[1],  # extrae sólo el rol
    }

    # Columnas opcionales según el tipo de jugador
    fila["Goles"]               = j.goles_anotados       if isinstance(j, Delantero)      else 0
    fila["Asistencias"]         = j.asistencias           if isinstance(j, Mediocampista)  else 0
    fila["Atajadas"]            = j.atajadas_historicas   if isinstance(j, Portero)        else 0
    fila["Balones_recuperados"] = j.balones_recuperados   if isinstance(j, Defensa)        else 0

    datos.append(fila)

df = pd.DataFrame(datos)

# ── Mostrar tabla completa ──
print("\n--- TABLA COMPLETA DEL EQUIPO ---")
print(df.to_string(index=False))

# ── Estadísticas básicas ──
print("\n--- ESTADÍSTICAS DEL PLANTEL ---")
print(f"Edad promedio del equipo  : {df['Edad'].mean():.2f} años")
print(f"Altura máxima del equipo  : {df['Altura_m'].max():.2f} m  ({df.loc[df['Altura_m'].idxmax(), 'Nombre']})")
print(f"Altura mínima del equipo  : {df['Altura_m'].min():.2f} m  ({df.loc[df['Altura_m'].idxmin(), 'Nombre']})")
print(f"Total de goles anotados   : {df['Goles'].sum()}")
print(f"Total de asistencias      : {df['Asistencias'].sum()}")

print("\n--- JUGADORES POR POSICIÓN ---")
print(df["Posicion"].value_counts().to_string())

print("\n--- PROMEDIO DE EDAD POR POSICIÓN ---")
print(df.groupby("Posicion")["Edad"].mean().round(2).to_string())

# ── Exportar a CSV ──
os.makedirs("output", exist_ok=True)
nombre_csv = f"output/titulares_{pais_elegido.lower()}.csv"
df.to_csv(nombre_csv, index=False, encoding="utf-8-sig")
print(f"\n✅ Archivo exportado exitosamente: {nombre_csv}")
print("=" * 55)