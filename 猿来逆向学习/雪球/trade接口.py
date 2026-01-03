import requests

cookies = {
    'cookiesu': '401763716955185',
    'device_id': '66bff363b7f725f8260cad650a9d8d97',
    'u': '401763716955185',
    'Hm_lvt_1db88642e346389874251b5a1eded6e3': '1763716956,1765163705',
    'HMACCOUNT': '7F77C2B6C739E12F',
    'xq_a_token': '7ed879d430984f6ea5a546808b7b9fcd64f39eb9',
    'xqat': '7ed879d430984f6ea5a546808b7b9fcd64f39eb9',
    'xq_r_token': 'ef2ca2a5140cc8bab4810c2509fdec718b6f63a5',
    'xq_id_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTc2ODA5NDE1NSwiY3RtIjoxNzY1Nzc3NTQ0ODQzLCJjaWQiOiJkOWQwbjRBWnVwIn0.luTZTtIKZeBfG5YlKsXubXDw0CjRimr-nYO8SA2nB4rxrjsfnQ1ATruBKssaH-DE2GWeg--xG1fR-iHHfNiKjlr32N4mcA0yRrJfsNFvhELq03u-XrnwBCfgpZ5mKKPtS6UzFAQ6iFmZ7we2msp2BD14UV3T_KczyGJKCdvVD6up2vVuijGu0so0qd9PrpzcsZ0-cYTSc7xZEVWUos9kzGRAMrS4r7RZSkmzRMnC_-lgTFFXdMW1Qb9PAbIfJtUEhd9nEiSuV9oBxAgQeil5r6f7IXJlJL3rxnvybim59ED-0ceKNjVC5W_okk4VnJRqf9MXVv0C-BLvB7yWnxMLWQ',
    'is_overseas': '0',
    'Hm_lpvt_1db88642e346389874251b5a1eded6e3': '1765851491',
    'ssxmod_itna': '1-QuDtGKiKBKYIeWTqeFqmuC4x_aDI61DDqGHDyxW9K0CDmxjKidoDUQiyDcb9jD7qm4bt7rnDs=YpYOqDlpweDZDGFQDqx0ob2tWAWqsdeorRTKF73orTdPFNRbTyqzKjEAS=t091/cUyqXde248GiobDAEoD7QDb4DyDGtWDG=b3GeD44dDt4DIDAYDDxDWneDBi6bWDGprgeWbTePovARrxi3WGjPWDitGxi57apcrTCGHxA3YHxaW7eGnli8W8OWDj4BamKGyGeGW8fTXZKGuttbKE2nWHPp0oODlAvmbbYTYz8GK30_rCmqi4PnwKlGsQ0KQDdDxYmGwYxzCXoF4DDPolrPoY7YrgivSGeM0mbAux1_TF01Yheeh7COq32hSxiebtbiqaDd6GPl2xFiebDP2EDD',
    'ssxmod_itna2': '1-QuDtGKiKBKYIeWTqeFqmuC4x_aDI61DDqGHDyxW9K0CDmxjKidoDUQiyDcb9jD7qm4bt7rnDs=YpYoDAYgu4E4o3D7pKgf4PDs2KWZ0aUQfIYhXep5lAdeddfKMDera5Y44w6q4k1ZFjfd4M324dbSUfI4_ReoxdfR0mYEm3ox4z/oYoRu4YWGRiTfbxD',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'origin': 'https://xueqiu.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://xueqiu.com/S/SZ000833',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    # 'cookie': 'cookiesu=401763716955185; device_id=66bff363b7f725f8260cad650a9d8d97; u=401763716955185; Hm_lvt_1db88642e346389874251b5a1eded6e3=1763716956,1765163705; HMACCOUNT=7F77C2B6C739E12F; xq_a_token=7ed879d430984f6ea5a546808b7b9fcd64f39eb9; xqat=7ed879d430984f6ea5a546808b7b9fcd64f39eb9; xq_r_token=ef2ca2a5140cc8bab4810c2509fdec718b6f63a5; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTc2ODA5NDE1NSwiY3RtIjoxNzY1Nzc3NTQ0ODQzLCJjaWQiOiJkOWQwbjRBWnVwIn0.luTZTtIKZeBfG5YlKsXubXDw0CjRimr-nYO8SA2nB4rxrjsfnQ1ATruBKssaH-DE2GWeg--xG1fR-iHHfNiKjlr32N4mcA0yRrJfsNFvhELq03u-XrnwBCfgpZ5mKKPtS6UzFAQ6iFmZ7we2msp2BD14UV3T_KczyGJKCdvVD6up2vVuijGu0so0qd9PrpzcsZ0-cYTSc7xZEVWUos9kzGRAMrS4r7RZSkmzRMnC_-lgTFFXdMW1Qb9PAbIfJtUEhd9nEiSuV9oBxAgQeil5r6f7IXJlJL3rxnvybim59ED-0ceKNjVC5W_okk4VnJRqf9MXVv0C-BLvB7yWnxMLWQ; is_overseas=0; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1765851491; ssxmod_itna=1-QuDtGKiKBKYIeWTqeFqmuC4x_aDI61DDqGHDyxW9K0CDmxjKidoDUQiyDcb9jD7qm4bt7rnDs=YpYOqDlpweDZDGFQDqx0ob2tWAWqsdeorRTKF73orTdPFNRbTyqzKjEAS=t091/cUyqXde248GiobDAEoD7QDb4DyDGtWDG=b3GeD44dDt4DIDAYDDxDWneDBi6bWDGprgeWbTePovARrxi3WGjPWDitGxi57apcrTCGHxA3YHxaW7eGnli8W8OWDj4BamKGyGeGW8fTXZKGuttbKE2nWHPp0oODlAvmbbYTYz8GK30_rCmqi4PnwKlGsQ0KQDdDxYmGwYxzCXoF4DDPolrPoY7YrgivSGeM0mbAux1_TF01Yheeh7COq32hSxiebtbiqaDd6GPl2xFiebDP2EDD; ssxmod_itna2=1-QuDtGKiKBKYIeWTqeFqmuC4x_aDI61DDqGHDyxW9K0CDmxjKidoDUQiyDcb9jD7qm4bt7rnDs=YpYoDAYgu4E4o3D7pKgf4PDs2KWZ0aUQfIYhXep5lAdeddfKMDera5Y44w6q4k1ZFjfd4M324dbSUfI4_ReoxdfR0mYEm3ox4z/oYoRu4YWGRiTfbxD',
}

params = {
    # 'symbol': 'SZ000833',
    'symbol': 'SZ002938',
    'count': '10',
}

response = requests.get('https://stock.xueqiu.com/v5/stock/history/trade.json', params=params, cookies=cookies, headers=headers)
print(response.text)