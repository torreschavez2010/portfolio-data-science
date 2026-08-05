class Campana:
    def __init__(self, nombre, gasto, leads):
        self.nombre = nombre
        self.gasto = gasto
        self.leads = leads

    def costo_por_lead(self):
        return self.gasto / self.leads

    def resumen(self):
        return f"{self.nombre}: costo por lead = {self.costo_por_lead():.4f}"


campanas = [
    Campana("Campaña Enero", 7401.06, 572),
    Campana("Campaña Febrero", 5651.74, 684),
    Campana("Campaña Marzo", 5632.10, 412)
]

mejor_campana = None
menor_costo = None

for campana in campanas:
    print(campana.resumen())

    if menor_costo is None or campana.costo_por_lead() < menor_costo:
        menor_costo = campana.costo_por_lead()
        mejor_campana = campana.nombre

print(f"\nLa campaña más eficiente es: {mejor_campana} con costo por lead de {menor_costo:.4f}")