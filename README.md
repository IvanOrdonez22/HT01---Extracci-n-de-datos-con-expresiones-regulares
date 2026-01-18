# Extracción del Cuadro 3 – ETAs 2018

## Descripción
Se realizó la extracción de la tabla "Cuadro 3. ETA´s: Total de brotes reportados en año 2018"
desde el archivo "Analisis Anual 2018 ETAS.pdf".

## Herramientas utilizadas
- Python 3
- Visual Studio Code
- camelot-py
- PyPDF2 (<3.0)
- regex101.com

## Procedimiento
1. Se utilizó Camelot-py para extraer las tablas de la página 5 del PDF.
2. El resultado fue exportado a archivos CSV.
3. Se aplicaron expresiones regulares con los flags global y multiline para filtrar
   únicamente las filas válidas del Cuadro 3.
4. El resultado final se guardó en el archivo cuadro3_limpio.txt.
<img width="378" height="280" alt="Captura de pantalla 2026-01-18 002700" src="https://github.com/user-attachments/assets/d63ec45f-855f-4bab-84c2-51b8596ef9f7" />
