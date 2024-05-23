import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "practica"
)

# Extraemos los datos de la tabla de Empleados
info_empleados = "SELECT * FROM em_empleados"

# Llevamos la información de Empleados al Dataframe
df = pd.read_sql(info_empleados, connection)

# Lo pasamos a un archivo csv
df.to_csv("empleados.csv", index=False)



#Extraemos los datos de la tabla Proyectos y seguimos el mismo proceso para el dataframe
info_proyectos = "SELECT * FROM pr_proyectos"

df = pd.read_sql(info_proyectos, connection)
df.to_csv('proyectos.csv', index=False)



#Extraemos los datos de la tabla Empleados_Proyectos
info_empleado_proyecto = "SELECT * FROM pr_empleado_proyecto"
df = pd.read_sql(info_empleado_proyecto, connection)
df.to_csv("empleado_proyecto.csv", index = False)

connection.close()