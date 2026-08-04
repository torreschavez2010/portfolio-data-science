import sqlite3

conexion = sqlite3.connect("campanas.db") 

cursor = conexion.cursor()


# ORDER BY: todas las campañas ordenadas de menor a mayor costo por lead
print("\n=== Todas ordenadas por eficiencia (mejor a peor) ===")
cursor.execute("""
    SELECT nombre, (gasto / leads) AS costo_por_lead
    FROM campanas
    ORDER BY costo_por_lead ASC
""")
for fila in cursor.fetchall():
    print(f"{fila[0]}: {fila[1]:.4f}")

# ORDER BY DESC: de mayor a menor gasto
print("\n=== Ordenadas por gasto (mayor a menor) ===")
cursor.execute("SELECT nombre, gasto FROM campanas ORDER BY gasto DESC")
for fila in cursor.fetchall():
    print(fila)