#!/usr/bin/env python3
from airmap import AirMapAPI

token = input("Enter your API Token for airmap: ")
airmap_api = AirMapAPI(token)
# geo map coordinates for ASU Tempe Campus
geo_json = {
	"type": "FeatureCollection",
	"features": [
		{
		"type": "Feature",
		"properties": {},
		"geometry": {
			"type": "Polygon",
			"coordinates": [
			[
				[
				-111.94244384765625,
				33.41209918127008
				],
				[
				-111.91300392150879,
				33.41209918127008
				],
				[
				-111.91300392150879,
				33.431083186694096
				],
				[
				-111.94244384765625,
				33.431083186694096
				],
				[
				-111.94244384765625,
				33.41209918127008
				]
			]
			]
		}
		}
	]
}
print(airmap_api.search_airspace(geo_json))