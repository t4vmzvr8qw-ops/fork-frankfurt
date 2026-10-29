#!/usr/bin/env python3
"""Fetch public OSM restaurant listings as a static, GitHub Pages-friendly JSON file."""
import datetime as dt
import json
import pathlib
import urllib.parse
import urllib.request

ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/'data'/'restaurants.json'
QUERY='[out:json][timeout:90];(node["amenity"="restaurant"](50.055,8.48,50.235,8.81);way["amenity"="restaurant"](50.055,8.48,50.235,8.81););out center;'
HOSTS=['https://overpass.kumi.systems/api/interpreter','https://overpass.private.coffee/api/interpreter','https://overpass-api.de/api/interpreter']

def fetch():
    for host in HOSTS:
        try:
            payload=urllib.parse.urlencode({'data':QUERY}).encode()
            req=urllib.request.Request(host,data=payload,headers={'User-Agent':'ForkFrankfurt/3.0 (static GitHub Pages restaurant directory)','Accept':'application/json'})
            with urllib.request.urlopen(req,timeout=110) as resp:
                data=json.load(resp)
            seen=set(); places=[]
            for e in data.get('elements',[]):
                t=e.get('tags') or {}
                lat=e.get('lat',e.get('center',{}).get('lat'))
                lng=e.get('lon',e.get('center',{}).get('lon'))
                if not t.get('name') or not isinstance(lat,(int,float)) or not isinstance(lng,(int,float)):continue
                key=(t['name'].casefold(),round(lat,4),round(lng,4))
                if key in seen:continue
                seen.add(key)
                street=' '.join(filter(None,(t.get('addr:street'),t.get('addr:housenumber'))))
                addr=', '.join(filter(None,(street,t.get('addr:postcode'),t.get('addr:city'))))
                places.append({'id':f"osm-{e['type']}-{e['id']}",'name':t['name'],'cuisine':t.get('cuisine',''),'area':t.get('addr:suburb') or t.get('addr:city') or 'Frankfurt','address':addr,'lat':lat,'lng':lng,'source':'OpenStreetMap'})
            if len(places)<100:raise RuntimeError(f'Unexpectedly small dataset: {len(places)}')
            return places
        except Exception as exc:print(f'{host}: {exc}')
    raise SystemExit('No source responded with a valid full dataset: keeping last good data unchanged')

if __name__=='__main__':
    places=fetch()
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps({'updated':dt.datetime.now(dt.timezone.utc).isoformat(),'source':'OpenStreetMap contributors / Overpass API','places':places},ensure_ascii=False,separators=(',',':'))+'\n')
    print(f'Saved {len(places)} restaurants')
