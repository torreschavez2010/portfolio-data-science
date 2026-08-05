costos_por_lead = [12.9389, 8.2628, 13.6701]

# Media
media = sum(costos_por_lead) / len(costos_por_lead)

# Mediana (ordenamos primero)
ordenados = sorted(costos_por_lead)
n = len(ordenados)
if n % 2 == 0:
    mediana = (ordenados[n//2 - 1] + ordenados[n//2]) / 2
else:
    mediana = ordenados[n//2]

# Desviación estándar (paso a paso, para que veas la lógica)
diferencias_cuadradas = [(x - media) ** 2 for x in costos_por_lead]
varianza = sum(diferencias_cuadradas) / len(costos_por_lead)
desviacion_estandar = varianza ** 0.5

print(f"Media: {media:.4f}")
print(f"Mediana: {mediana:.4f}")
print(f"Desviacion estandar: {desviacion_estandar:.4f}")
print(f"Minimo: {min(costos_por_lead):.4f}")
print(f"Maximo: {max(costos_por_lead):.4f}")