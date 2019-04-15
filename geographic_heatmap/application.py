import pandas as pd

def buildGeoheatmap(frame):
    import folium
    import time
    import json
    from PIL import Image
    import plotly.plotly as py
    import country_converter as coco
    states = json.load(open('uk_cities.json'))

    m = folium.Map(location=[55.386670, -3.804810], tiles="Mapbox Bright", zoom_start=6)  # vertical horizontal tiles = "Stamen Toner" Mapbox Bright
    m.choropleth(geo_data=states, name='choropleth', data=frame, columns=['City', 'Spend'],
                 key_on='properties.ctyua17nm', fill_color='Greens', fill_opacity=0.7, line_opacity=0.2,
                 legend_name='Spend')
    folium.LayerControl().add_to(m)

    m.save('buildGeoHeatmap.html')


frame = pd.read_csv('sample_geographic_heatmap.csv')

buildGeoheatmap(frame)