import camelot

tables = camelot.read_pdf(
    "Analisis Anual 2018 ETAS.pdf",
    pages="5",
    flavor="stream"   # MUY IMPORTANTE
)

print("Tablas encontradas:", tables.n)

for i, table in enumerate(tables):
    table.df.to_csv(f"tabla_{i}.csv", index=False)
