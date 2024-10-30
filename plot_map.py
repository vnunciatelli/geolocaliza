import geocoder
import folium

# Obtém a localização a partir do IP
g = geocoder.ip('me')  # 'me' obtém o IP da máquina local

# Verifica se a localização foi encontrada
if g.latlng:
    latitude, longitude = g.latlng
    
    # Cria um mapa com folium
    mapa = folium.Map(location=[latitude, longitude], zoom_start=15)

    # Adiciona um marcador para a localização
    folium.Marker(
        location=[latitude, longitude],
        popup='Sua Localização',
        icon=folium.Icon(color='blue')
    ).add_to(mapa)

    # Salva o mapa em um arquivo HTML
    mapa.save("mapa_localizacao.html")

    print("Mapa criado com sucesso! Abra 'mapa_localizacao.html' para visualizar.")
else:
    print("Não foi possível obter a localização.")
