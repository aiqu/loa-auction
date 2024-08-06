import requests
import json
import math
import time
from item import Item

API_KEY=''
URL='https://developer-lostark.game.onstove.com/auctions/items'
HEADERS = {
    'accept': 'application/json',
    'authorization': f'bearer {API_KEY}',
    'content-type': 'application/json'
}

# "Subs": [
#         {
#           "Code": 200010,
#           "CodeName": "목걸이"
#         },
#         {
#           "Code": 200020,
#           "CodeName": "귀걸이"
#         },
#         {
#           "Code": 200030,
#           "CodeName": "반지"
#         },
#         {
#           "Code": 200040,
#           "CodeName": "팔찌"
#         }
#       ],
#       "Code": 200000,
#       "CodeName": "장신구"
#     {
#       "Value": 7,
#       "Text": "연마 효과",
#       "Tiers": [
#         4
#       ],
#       "EtcSubs": [
#         {
#           "Value": 45,
#           "Text": "공격력 %",
#           "Class": "",
#           "Categorys": [
#             200020
#           ],
#           "Tiers": null
#         },
#         {
#           "Value": 53,
#           "Text": "공격력 +",
#           "Class": "",
#           "Categorys": null,
#           "Tiers": null
#         },
#         {
#           "Value": 44,
#           "Text": "낙인력",
#           "Class": "",
#           "Categorys": [
#             200010
#           ],
#           "Tiers": null
#         },
#         {
#           "Value": 46,
#           "Text": "무기 공격력 %",
#           "Class": "",
#           "Categorys": [
#             200020
#           ],
#           "Tiers": null
#         },
#         {
#           "Value": 54,
#           "Text": "무기 공격력 +",
#           "Class": "",
#           "Categorys": null,
#           "Tiers": null
#         },
#         {
#           "Value": 57,
#           "Text": "상태이상 공격 지속시간",
#           "Class": "",
#           "Categorys": null,
#           "Tiers": null
#         },
#         {
#           "Value": 43,
#           "Text": "세레나데, 신성, 조화 게이지 획득량 증가",
#           "Class": "",
#           "Categorys": [
#             200010
#           ],
#           "Tiers": null
#         },
#         {
#           "Value": 51,
#           "Text": "아군 공격력 강화 효과",
#           "Class": "",
#           "Categorys": [
#             200030
#           ],
#           "Tiers": null
#         },
#         {
#           "Value": 52,
#           "Text": "아군 피해량 강화 효과",
#           "Class": "",
#           "Categorys": [
#             200030
#           ],
#           "Tiers": null
#         },
#         {
#           "Value": 42,
#           "Text": "적에게 주는 피해 증가",
#           "Class": "",
#           "Categorys": [
#             200010
#           ],
#           "Tiers": null
#         },
#         {
#           "Value": 58,
#           "Text": "전투 중 생명력 회복량",
#           "Class": "",
#           "Categorys": null,
#           "Tiers": null
#         },
#         {
#           "Value": 56,
#           "Text": "최대 마나",
#           "Class": "",
#           "Categorys": null,
#           "Tiers": null
#         },
#         {
#           "Value": 55,
#           "Text": "최대 생명력",
#           "Class": "",
#           "Categorys": null,
#           "Tiers": null
#         },
#         {
#           "Value": 41,
#           "Text": "추가 피해",
#           "Class": "",
#           "Categorys": [
#             200010
#           ],
#           "Tiers": null
#         },
#         {
#           "Value": 49,
#           "Text": "치명타 적중률",
#           "Class": "",
#           "Categorys": [
#             200030
#           ],
#           "Tiers": null
#         },
#         {
#           "Value": 50,
#           "Text": "치명타 피해",
#           "Class": "",
#           "Categorys": [
#             200030
#           ],
#           "Tiers": null
#         },
#         {
#           "Value": 48,
#           "Text": "파티원 보호막 효과",
#           "Class": "",
#           "Categorys": [
#             200020
#           ],
#           "Tiers": null
#         },
#         {
#           "Value": 47,
#           "Text": "파티원 회복 효과",
#           "Class": "",
#           "Categorys": [
#             200020
#           ],
#           "Tiers": null
#         }
#       ]
#     },
#     {
#       "Value": 8,
#       "Text": "아크 패시브",
#       "Tiers": [
#         4
#       ],
#       "EtcSubs": [
#         {
#           "Value": 1,
#           "Text": "깨달음",
#           "Class": "",
#           "Categorys": [
#             200010,
#             200020,
#             200030
#           ],
#           "Tiers": [
#             4
#           ]
#         },
#         {
#           "Value": 2,
#           "Text": "도약",
#           "Class": "",
#           "Categorys": [
#             200040
#           ],
#           "Tiers": [
#             4
#           ]
#         }
#       ]
#     }
#   ],

data = {
  "ItemLevelMin": 0,
  "ItemLevelMax": 1800,
  "EtcOptions": [
    {
      "FirstOption": 8,
      "SecondOption": 1,
      "MinValue": 9,
    #   "MaxValue": null
    },
    {
      "FirstOption": 7,
      "SecondOption": 46,
    #   "MinValue": ,
    #   "MaxValue": 
    },
  ],
  "Sort": "BUY_PRICE",
  "CategoryCode": 200000,
  "ItemGrade": "유물",
  "SortCondition": "ASC"
}

def parse_response(json_response):
    pageno = json_response['PageNo']
    pagesize = json_response['PageSize']
    totalcount = json_response['TotalCount']
    totalpagecount = math.ceil(totalcount/pagesize)
    print(f'{pagesize} items on page {pageno}/{totalpagecount}. Total {totalcount} items.')
    items = list()
    for item_response in json_response['Items']:
        new_item = Item(item_response)
        if new_item.price:
            items.append(new_item)
    return pageno, pagesize, totalcount, totalpagecount, items

def throttle_request():
    global count, start_time
    if count >= 100:
        elapsed_time = time.time() - start_time
        sleep_time = 65-elapsed_time
        if sleep_time > 0:
            time.sleep(sleep_time)
        start_time = time.time()
        count = 1

def post_request():
    global count
    throttle_request()
    response = requests.post(URL, headers=HEADERS, json=data)
    count += 1
    return response

def get_remaining_items(pageno):
    data['PageNo'] = pageno
    return post_request()

start_time = time.time()
count = 1
while True:
    try:
        response = post_request()
        response.raise_for_status()
        json_response = response.json()
        pageno, pagesize, totalcount, totalpagecount, items = parse_response(json_response)
        for pageno in range(2, totalpagecount+1):
            response = get_remaining_items(pageno)
            response.raise_for_status()
            json_response = response.json()
            _, _, _, _, next_items = parse_response(json_response)
            items.extend(next_items)
    except requests.exceptions.RequestException as e:
        print(f"요청 실패: {e}")
        print(f"응답 코드: {response.status_code}")
        print(f"응답 내용: {response.text}")
        print(response.request.url)  # 요청 URL 출력
        print(response.request.method)  # HTTP 메서드 출력
        print(response.request.headers)  # 요청 헤더 출력
        print(response.request.body)  # 요청 본문 출력 (바이트 형태)
    else:
        with open('ear.txt', 'w', encoding='utf-8') as f:
            f.write(json.dumps([item.to_dict() for item in items], ensure_ascii=False))
        break