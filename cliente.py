class Cliente:
	def __init__(self, nombre, presupuesto):
		self.nombre = nombre
		self.presupuesto = presupuesto

	def resumen(self):
		return f"{self.nombre} tiene un presupuesto de {self.presupuesto}"

cliente1 = Cliente("Juan", 500000)
print(cliente1.resumen())