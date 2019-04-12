def buildGeoheatmap(frame,chosen_kpi):
    import folium
    import time
    from PIL import Image
    import plotly.plotly as py
    import country_converter as coco

    column_names = (list(frame.columns.values))



    states = 'uk_cities.json'

    m = folium.Map(location=[55.386670, -3.804810], tiles="Mapbox Bright", zoom_start=7)  # veritcal horizontal tiles = "Stamen Toner" Mapbox Bright
    m.choropleth(geo_data=states, name='choropleth', data=frame, columns=['Region', 'Cost'],
                 key_on='properties.ctyua17nm', fill_color='Greens', fill_opacity=0.7, line_opacity=0.2,
                 legend_name='Spend')
    folium.LayerControl().add_to(m)

    m.save('buildGeoHeatmap.html')

    # import selenium.webdriver
    # driver = selenium.webdriver.PhantomJS()
    # time.sleep(1)
    # driver.set_window_size(1300, 1750)  # choose a resolution
    # driver.get('buildGeoHeatmap.html')
    # # You may need to add time.sleep(seconds) here
    # driver.save_screenshot('buildGeoHeatmap.png')