def buildGeoheatmap(frame,chosen_kpi):
    import folium
    import time
    from PIL import Image
    import plotly.plotly as py
    import country_converter as coco

    column_names = (list(frame.columns.values))

    if 'Country' in str(column_names):

        list_isos = []
        for single_country in frame["Country"]:
            iso3 = coco.convert(names=single_country, to='ISO3')
            list_isos.append(iso3)

        frame["Code"] = list_isos

        data = [dict(
            type='choropleth',
            colorscale='Greens',
            locations=frame['Code'],
            z=frame['Cost'],
            text=frame['country'],
            colorbar=dict(len=0.5, bordercolor='white', thickness=2, title='Spend', titlefont=dict(size=10),
                          tickfont=dict(size=10)), showlegend=False)]

        layout = dict(
            titlefont=dict(size=10),
            geo=dict(
                showcountries=True,
                showframe=True,
                showcoastlines=True,
                projection=dict(type='equirectangular')
            )
        )

        fig = dict(data=data, layout=layout)

        py.image.save_as({'data': fig}, 'buildGeoHeatmap.png')
        image = Image.open('buildGeoHeatmap.png')
        transposed = image.transpose(Image.ROTATE_90)
        transposed.save('buildGeoHeatmap.png')

    else:

        states = 'uk_cities.json'

        m = folium.Map(location=[55.386670, -3.804810], tiles="Mapbox Bright", zoom_start=7)  # veritcal horizontal tiles = "Stamen Toner" Mapbox Bright
        m.choropleth(geo_data=states, name='choropleth', data=frame, columns=['Region', 'Cost'],
                     key_on='properties.ctyua17nm', fill_color='Greens', fill_opacity=0.7, line_opacity=0.2,
                     legend_name='Spend')
        folium.LayerControl().add_to(m)

        m.save('buildGeoHeatmap.html')

        import selenium.webdriver
        driver = selenium.webdriver.PhantomJS()
        time.sleep(1)
        driver.set_window_size(1300, 1750)  # choose a resolution
        driver.get('buildGeoHeatmap.html')
        # You may need to add time.sleep(seconds) here
        driver.save_screenshot('buildGeoHeatmap.png')