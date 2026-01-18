import re

with open("tabla_0.csv", encoding="utf-8") as f:
    texto = f.read()


patron = re.compile(
    r'^\s*(\d+)\s*,\s*(\d+)\s*,\s*([^,"]*)\s*,\s*([^,"]+)\s*,\s*([^,"]*)\s*,\s*(\d+)\s*$',
    re.MULTILINE
)

filas = patron.findall(texto)

datos = []
for f in filas:
    datos.append({
        "No": int(f[0]),
        "SE": int(f[1]),
        "Area": f[2].strip(),
        "ETA": f[3].strip(),
        "Fuente": f[4].strip(),
        "Casos": int(f[5])
    })

datos.sort(key=lambda x: x["No"])

with open("cuadro3_limpio.txt", "w", encoding="utf-8") as f:
    f.write("Cuadro 3. ETA´s: Total de brotes reportados en año 2018\n\n")
    f.write("No | SE | Área de Salud | ETA | Fuente | Casos\n")
    for d in datos:
        f.write(
            f"{d['No']} | {d['SE']} | {d['Area']} | "
            f"{d['ETA']} | {d['Fuente']} | {d['Casos']}\n"
        )
