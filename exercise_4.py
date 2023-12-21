import sqlite3

# Nombre y ubicación de la base de datos
database_path = 'empleados.db'

# Conexión a la base de datos
conn = sqlite3.connect(database_path)

# Objeto cursor
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS SALARIES (
        Professor_Name TEXT,
        Department TEXT,
        Salary INT
    );
''')

# Insertar datos de ejemplo (puedes omitir esta parte si ya tienes datos en la tabla)
cursor.execute("INSERT INTO SALARIES VALUES ('Prof1', 'Dep1', 70000)")
cursor.execute("INSERT INTO SALARIES VALUES ('Prof2', 'Dep1', 60000)")
cursor.execute("INSERT INTO SALARIES VALUES ('Prof3', 'Dep2', 55000)")
cursor.execute("INSERT INTO SALARIES VALUES ('Prof4', 'Dep2', 25000)")

# Guardar los cambios
conn.commit()

# Ejecutar la consulta SQL corregida
cursor.execute('''
    SELECT Department, AVG(Salary) as AverageSalary
    FROM SALARIES
    GROUP BY Department
    ORDER BY AverageSalary DESC
''')

# Mostrar los resultados
results = cursor.fetchall()
for row in results:
    print(row)

# Cerrar la conexión
conn.close()

# Cerrar la conexión
conn.close()