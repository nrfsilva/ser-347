# Exercício 03.

# definir os valores de NIR, Red e Green
nir = float(input("Insira o valor referente à banda do infravermelho próximo (escala 0 - 1): "))
red = float(input("Insira o valor referente à banda do vermelho (escala 0 - 1): "))
green = float(input("Insira o valor referente à banda do verde (escala 0 - 1): "))

# calcular o NDWI e o NDVI
ndwi = round((green - nir) / (green + nir), 3)
ndvi = round((nir - red) / (nir + red), 3)

# print os resultados
print("O valor do NDWI é", ndwi, "e o NDVI é", ndvi)



