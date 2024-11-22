import pandas as pd

def abrir_archivo(nombre):
    return pd.read_csv(nombre)

def eliminar_columna(df_, nombre):
    df_.drop(columns = [nombre], inplace = True)

def guardar_archivo(df_, nombre):
    df_.to_csv(nombre, index = False)

def corregir_columna(df_, columna, valor_viejo, valor_nuevo):
    df_[columna] = df_[columna].replace(valor_viejo, valor_nuevo)

if __name__ == '__main__':
    df = abrir_archivo("Participación en clase.csv")

    # Eliminamos la columna de la hora
    eliminar_columna(df, "Marca temporal")

    # Correcciones
    corregir_columna(df, "¿Crees que la participación en clase te ayuda a mejorar tu rendimiento escolar?", "SI", "Sí")
    corregir_columna(df, "¿Crees que la participación en clase te ayuda a mejorar tu rendimiento escolar?", "Si", "Sí")
    corregir_columna(df, "¿Considerás que tu asistencia a clases influye en tu rendimiento escolar?", "Si", "Sí")

    guardar_archivo(df, "Participación en clase (limpio).csv")