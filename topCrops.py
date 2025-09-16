import requests
def getPrices(state="Karnataka",crops=["water melon"]):
  nameMap = {"soyabeans":"Soyabean","cowpeas":"cowpea","groundnuts":"groundnut","watermelon":"water melon"}
  crops = [nameMap[x] if x in nameMap else x for x in crops]
  tops = []
  for crop in crops:
    resp = requests.get(
        f"https://api.data.gov.in//resource/9ef84268-d588-465a-a308-a864a43d0070",
        params={
            "api-key": API_KEY,
            "format": "json",
            "filters[state.keyword]" : state,
            "filters[commodity]" : crop,
            "limit": 1,
        }
    )
    data = resp.json()
    records = data.get("records", [])
    if records:
      x = records[0]
      tops.append([x['commodity'],x['min_price'],x['max_price'],x['modal_price']])
  tops.sort(key=lambda x: int(x[-2]), reverse=True)
  return tops[:3]
