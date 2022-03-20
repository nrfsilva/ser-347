# Exercício 04.

import math

# printar o objetivo do programa
print("#### Cálculo da distância entre dois pontos baseando-se na fórmula de Haversine ####")

# inserir as coordenadas (lat, long), em graus decimais, para o ponto 1
p1_lat = float(input("Insira a latitude do ponto 1 (graus decimais): "))
p1_long = float(input("Insira a longitude do ponto 1 (graus decimais): "))

print("Ponto 1 - Latitude:", p1_lat, "Longitude:", p1_long)

# inserir as coordenadas (lat, long), em graus decimais, para o ponto 2
p2_lat = float(input("Insira a latitude do ponto 2 (graus decimais): "))
p2_long = float(input("Insira a longitude do ponto 2 (graus decimais): "))

print("Ponto 2 - Latitude:", p2_lat, "Longitude:", p2_long)

# calcular a distância entre os pontos utilizando a fórmula de Haversine
# referência: https://en.wikipedia.org/wiki/Haversine_formula

raio = 6371 # quilômetros
p1_lat_rad = math.radians(p1_lat) # converter de graus para radianos
p1_long_rad = math.radians(p1_long) # converter de graus para radianos
p2_lat_rad = math.radians(p2_lat) # converter de graus para radianos
p2_long_rad = math.radians(p2_long) # converter de graus para radianos

dlat = p2_lat_rad - p1_lat_rad
dlong = p2_long_rad - p1_long_rad

a = math.sin(dlat/2)**2
b = math.cos(p1_lat_rad)
c = math.cos(p2_lat_rad)
d = math.sin(dlong/2)**2

dist = 2 * raio * math.asin(math.sqrt(a + (b * c * d))) # fórmula de Haversine
print("A distância entre os dois pontos é:", round(dist,2), "km")