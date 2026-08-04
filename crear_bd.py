import sqlite3

# 1. Conectar (crea el archivo campanas.db si no existe)
conexion = sqlite3.connect("campanas.db")
cursor = conexion.cursor()

# 2. Crear la tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS campanas (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        gasto REAL,
        leads INTEGER
    )
""")

# 3. Insertar tus datos reales
datos = [
    ("Campaña Enero", 7401.06, 572),
    ("Campaña Febrero", 5651.74, 684),
    ("Campaña Marzo", 5632.10, 412)
]

cursor.executemany(
    "INSERT INTO campanas (nombre, gasto, leads) VALUES (?, ?, ?)",
    datos
)

# 4. Guardar cambios
conexion.commit()

# 5. Cerrar
conexion.close()

print("Base de datos creada con exito.")