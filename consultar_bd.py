import sqlite3

conexion = sqlite3.connect("campanas.db")
cursor = conexion.cursor()

# Consulta 1: traer todo
print("=== Todas las campañas ===")
cursor.execute("SELECT * FROM campanas")
for fila in cursor.fetchall():
    print(fila)

# Consulta 2: la más eficiente (recuerdas esta lógica de sesiones pasadas)
print("\n=== Campaña mas eficiente ===")
cursor.execute("""
    SELECT nombre, gasto, leads, (gasto / leads) AS costo_por_lead
    FROM campanas
    ORDER BY costo_por_lead ASC
    LIMIT 1
""")
resultado = cursor.fetchone()
print(f"{resultado[0]}: costo por lead = {resultado[3]:.4f}")

conexion.close()