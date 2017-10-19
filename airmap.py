import json

import requests

ROOT_API = 'https://api.airmap.com/{}/{}/{}'

SEARCH_API = ROOT_API.format("airspace", "v2", "search")

class AirMapAPI:
	def __init__(self, api_key):
		self.api_key = api_key
		self.headers = self._setup_header()

	def _setup_header(self):
		return {"X-API-Key": self.api_key}

	def search_airspace(self, geo_json):
		r = requests.get(
			SEARCH_API, 
			headers=self.headers,
			data={
				"geometry_format": "GeoJSON",
				"geometry": geo_json,
			}
		)

		return r.json()

		