import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re

# 配置區
TARGET_MODELS = ["RX350h", "RX 350h"]
TARGET_YEARS = [2023, 2024, 2025, 2026]
BASE_URL = "https://www.tpkonsale.moj.gov.tw"

def is_target_vehicle(title, description=""):
    """檢查標題或描述是否包含目標車款與年份"""
    content = (title + " " + description).upper()
    
    # 檢查車型
    model_match = any(m.upper() in content for m in TARGET_MODELS)
    
    # 檢查年份 (簡單篩選，實際可能需要更複雜的正則表達式)
    year_match = any(str(y) in content for y in TARGET_YEARS)
    
    return model_match and year_match

def fetch_future_auctions():
    """抓取未來一個月的拍賣公告"""
    print("正在搜尋未來一個月的拍賣公告...")
    # TODO: 這裡需要填入實際的「拍賣公告」網址與查詢參數
    # 假設網址結構
    url = f"{BASE_URL}/Chattel" 
    
    # 模擬搜尋未來一個月
    start_date = datetime.now()
    end_date = start_date + timedelta(days=30)
    
    try:
        # TODO: 發送請求 (可能需要帶入 cookie 或 form data)
        # response = requests.get(url, ...)
        # soup = BeautifulSoup(response.text, 'html.parser')
        
        results = []
        # 模擬資料結構 (請替換為實際爬蟲邏輯)
        # for item in soup.select(".auction-row"):
        #     title = item.select_one(".title").text
        #     date_str = item.select_one(".date").text
        #     auction_date = datetime.strptime(date_str, "%Y-%m-%d")
        #     
        #     if start_date <= auction_date <= end_date:
        #         if is_target_vehicle(title):
        #             results.append({
        #                 "date": date_str,
        #                 "title": title,
        #                 "link": BASE_URL + item.select_one("a")['href'],
        #                 "round": "待確認" # 需要解析內文得知是第幾拍
        #             })
        return results
    except Exception as e:
        print(f"Error fetching future auctions: {e}")
        return []

def fetch_past_results():
    """抓取過去三個月的成交紀錄"""
    print("正在搜尋過去三個月的成交紀錄...")
    # TODO: 這裡需要填入實際的「拍定價格」或「歷史查詢」網址
    url = f"{BASE_URL}/History" 
    
    start_date = datetime.now() - timedelta(days=90)
    
    try:
        results = []
        # 模擬邏輯
        # for item in soup.select(".history-row"):
        #     title = item.select_one(".title").text
        #     date_str = item.select_one(".date").text
        #     price = item.select_one(".price").text # 成交價
        #     round_num = item.select_one(".round").text # 拍次
        #     
        #     if is_target_vehicle(title):
        #          results.append({
        #              "date": date_str,
        #              "title": title,
        #              "price": price,
        #              "round": round_num,
        #              "status": "拍定" # 或流標
        #          })
        return results
    except Exception as e:
        print(f"Error fetching past results: {e}")
        return []

if __name__ == "__main__":
    print(f"開始搜尋目標：Lexus RX350h ({TARGET_YEARS})")
    
    # 1. 搜尋未來
    future_cars = fetch_future_auctions()
    if future_cars:
        print(f"\n[未來拍賣] 找到 {len(future_cars)} 輛：")
        for car in future_cars:
            print(f"- {car['date']} | {car['title']} | {car['link']}")
    else:
        print("\n[未來拍賣] 無符合車輛 (或尚未實作選擇器)。")

    # 2. 搜尋歷史
    past_cars = fetch_past_results()
    if past_cars:
        print(f"\n[歷史成交] 找到 {len(past_cars)} 輛：")
        for car in past_cars:
            print(f"- {car['date']} | {car['title']} | 成交價: {car['price']} | {car['round']}")
    else:
        print("\n[歷史成交] 無符合車輛 (或尚未實作選擇器)。")
