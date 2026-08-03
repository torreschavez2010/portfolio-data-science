def calcular_costo_por_lead(gasto, leads):
    return gasto / leads

campanas = [
    {"nombre": "Campaña Enero", "gasto": 7401.06, "leads": 572},
    {"nombre": "Campaña Febrero", "gasto": 5245.31 + 406.43, "leads": 684},
    {"nombre": "Campaña Marzo", "gasto": 5632.10, "leads": 412}
]

mejor_campana = None
menor_costo = None

for campana in campanas:
    costo_por_lead = calcular_costo_por_lead(campana["gasto"], campana["leads"])
    print(f"{campana['nombre']}: costo por lead = {costo_por_lead:.4f}")

    if menor_costo is None or costo_por_lead < menor_costo:
        menor_costo = costo_por_lead
        mejor_campana = campana["nombre"]

print(f"\nLa campaña más eficiente es: {mejor_campana} con costo por lead de {menor_costo:.4f}")