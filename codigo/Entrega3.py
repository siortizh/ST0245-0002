import pandas as pd
import networkx as nx
import pydeck
#import folium
#from folium import plugins
df = pd.read_csv("https://raw.githubusercontent.com/siortizh/ST0245-002/master/codigo/calles_de_medellin_con_acoso.csv", sep=";")

#Coordenadas = []
#For lat,lng in zip(df.origin, df.destination):
#   Coordenadas.append([lat,lng])

#Inputs de origen y de destino del usuario
origen=input("Ingrese coordenadas de origen (latitud, logintud)")
destino=input("Ingrese coordenadas de destino (latitud, logintud)")

Dis_corta=nx.from_pandas_edgelist(df, source="origin", target="destination", edge_attr="length")
acoso_corta=nx.from_pandas_edgelist(df, source="origin", target="destination", edge_attr="harassmentRisk")

#Menor distancia y acoso en las rutas 
distancia=nx.dijkstra_path(Dis_corta, str(origen), str(destino), weight=True)
acoso=nx.dijkstra_path(acoso_corta, str(origen), str(destino), weight=True)

dt=pd.DataFrame(distancia, columns=["holii"])
hr=pd.DataFrame(acoso, columns=["holii"])

print(dt)
print(hr)