import folium
import json

def sergipe():
    sergipe_map = folium.Map(
        location=[-10.5472, -37.0731],
        zoom_start=8,
        control_scale=True,
    )

    folium.TileLayer(
        tiles='https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_nolabels/{z}/{x}/{y}.png',
        attr='© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        name='Mapa Base',
    ).add_to(sergipe_map)

    with open('C:/Users/luan-/Desktop/Faculdade/Materias/GRAFOS E ALGORITMOS COMPUTACIONAIS/Projeto/sergipe.json', 'r') as geojson_file:
        geojson_data = json.load(geojson_file)

    folium.GeoJson(geojson_data, name='sergipe_boundary', style_function=lambda x: {'color': 'black'}).add_to(sergipe_map)

    for feature in geojson_data['features']:
        name = feature['properties']['name']
        geometry = feature['geometry']
        if geometry['type'] == 'Polygon':
            coordinates = geometry['coordinates'][0]
        else:
            coordinates = geometry['coordinates'][0][0]
        centroid_x = sum(coord[0] for coord in coordinates) / len(coordinates)
        centroid_y = sum(coord[1] for coord in coordinates) / len(coordinates)
        
        folium.CircleMarker(location=[centroid_y, centroid_x], radius=5, tooltip=name, fill=True, color='white').add_to(sergipe_map)
        folium.map.Marker([centroid_y, centroid_x], icon=folium.DivIcon(html=f"<div>{name}</div>")).add_to(sergipe_map)

    sergipe_map.save('mapa.html')

def acre():
    sergipe_map = folium.Map(
        location=[-8.914650, -70.441382],
        zoom_start=8,
        control_scale=True,
    )

    folium.TileLayer(
        tiles='https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_nolabels/{z}/{x}/{y}.png',
        attr='© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        name='Mapa Base',
    ).add_to(sergipe_map)

    with open('C:/Users/luan-/Desktop/Faculdade/Materias/GRAFOS E ALGORITMOS COMPUTACIONAIS/Projeto/acre.json', 'r') as geojson_file:
        geojson_data = json.load(geojson_file)

    folium.GeoJson(geojson_data, name='sergipe_boundary', style_function=lambda x: {'color': 'black'}).add_to(sergipe_map)

    for feature in geojson_data['features']:
        name = feature['properties']['name']
        geometry = feature['geometry']
        if geometry['type'] == 'Polygon':
            coordinates = geometry['coordinates'][0]
        else:
            coordinates = geometry['coordinates'][0][0]
        centroid_x = sum(coord[0] for coord in coordinates) / len(coordinates)
        centroid_y = sum(coord[1] for coord in coordinates) / len(coordinates)
        
        folium.CircleMarker(location=[centroid_y, centroid_x], radius=5, tooltip=name, fill=True, color='white').add_to(sergipe_map)
        folium.map.Marker([centroid_y, centroid_x], icon=folium.DivIcon(html=f"<div>{name}</div>")).add_to(sergipe_map)

    sergipe_map.save('mapa.html')

sergipe()

# acre()