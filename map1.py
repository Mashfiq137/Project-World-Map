import folium
import pandas as pd
#reading data from a text file and selecting the columns and storing them in a list variable.
data = pd.read_csv("Volcano.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])

def set_color(elev):
	if elev < 1500:
		return "orange"
	elif elev>=1500 and elev<=2200:
		return "blue"
	else :
		return "red"

#creating the map inside an html file: 
map = folium.Map(location = [38.58,-99.09], zoom_start = 6,tiles ="cartodbpositron")
#add Marker to the Map:
fgv = folium.FeatureGroup(name = "Volcanoes")
#adding all the popups and store extended info's inside the popoup:

for lt,ln,el in zip(lat,lon,elev):
	fgv.add_child(folium.CircleMarker(location=[lt,ln],radius = 6, popup =str(el)+" m",fill_color=set_color(el),color='grey',fill = True, fill_opacity=0.7))

fgp = folium.FeatureGroup(name = "Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005']<10000000 else 'orange' if 10000000<=x['properties']['POP2005'] <20000000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
fg = folium.FeatureGroup(name="Aqila's Location")
fg.add_child(folium.CircleMarker(location=[23.748296,90.409065],radius = 6, popup ="Aqila Lives Here!!",fill_color="purple",color='grey',fill = True, fill_opacity=1))
map.add_child(fg)
map.add_child(folium.LayerControl())
#saving the map in html file
map.save("Map1.html") 

