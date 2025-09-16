import requests
def getPrices(state="Karnataka",crops=["Rice,Wheat"]):
  resp = requests.get(
      f"https://api.data.gov.in//resource/9ef84268-d588-465a-a308-a864a43d0070",
      params={
          "api-key": API_KEY,
          "format": "json",
          "filters[state.keyword]" : state,
          "filters[commodity]" : crops,
          "limit": 3,
      }
  )
  data = resp.json()
  return data.get("records", [])
