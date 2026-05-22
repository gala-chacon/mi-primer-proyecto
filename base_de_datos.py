import sqlite3

# Conectar a la base de datos (la crea si no existe)
conexion = sqlite3.connect("mi_base_datos.db")
cursor = conexion.cursor()

# Crear una tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS movimientos (
        id INTEGER PRIMARY KEY,
        fecha TEXT,
        tipo TEXT,
        cantidad REAL,
        saldo REAL
    )
""")

conexion.commit()
print("¡Base de datos creada correctamente!")
conexion.close()
conexion = sqlite3.connect("mi_base_datos.db")
cursor = conexion.cursor()
cursor.execute("""
    INSERT INTO movimientos (fecha, tipo, cantidad, saldo)
    VALUES (?, ?, ?, ?)
""", ("22/05/2026 17:00", "Ingreso", 500.0, 1500.0))

conexion.commit()
print("¡Movimiento guardado!")
cursor.execute("SELECT * FROM movimientos")
movimientos = cursor.fetchall()
print("\n📋 Movimientos guardados:")
for movimiento in movimientos:
    print(movimiento)

cursor.execute("""
    INSERT INTO movimientos (fecha, tipo, cantidad, saldo)
    VALUES (?, ?, ?, ?)
""", ("22/05/2026 17:10", "Retirada", 200.0, 1300.0))
conexion.commit()
print("Retirada")
cursor.execute("SELECT * FROM movimientos WHERE tipo = 'Retirada'")
movimientos_retirada = cursor.fetchall()
print("\n📋 Movimientos de Retirada:")
for movimiento in movimientos_retirada:
    print(movimiento)

conexion.close()