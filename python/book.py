import json
from datetime import date, timedelta
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
import time
from playwright.sync_api import sync_playwright

BASE_SCORES = "https://www.mlb.com/scores/"
BASE_MLB = "https://www.mlb.com"

today = str(date.today())
dates = [today]
print(dates)

def fetch_box_url(day):
    url = BASE_SCORES + day

    try:
        response = requests.get(url, timeout=5)
    except:
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    span = soup.find("span", string="Box")

    if not span:
        return None

    a_tag = span.find_parent("a")
    if not a_tag:
        return None

    href = a_tag.get("href")
    if not href:
        return None

    return BASE_MLB + href


print("🔎 Recupero link Boxscore...")

box_urls = []
with ThreadPoolExecutor(max_workers=20) as ex:
    for link in ex.map(fetch_box_url, dates):
        if link:
            box_urls.append(link)

print(f"📌 Trovati {len(box_urls)} link Boxscore")

def extract_tables_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    tables = soup.find_all("table")

    extracted = []

    for table in tables:
        parsed = []
        thead = table.find("thead")
        tbody = table.find("tbody")

        if thead:
            headers = [th.get_text(strip=True) for th in thead.find_all("th")]
            parsed.append(headers)

        if tbody:
            for tr in tbody.find_all("tr"):
                row = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
                parsed.append(row)

        if parsed:
            extracted.append(parsed)

    return extracted

print("📦 Estrazione dati da tutte le partite (headless Playwright)...")

final_data = []

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)
    context = browser.new_context()

    for url in box_urls:

        page = context.new_page()

        try:
            page.goto(url, wait_until="domcontentloaded", timeout=30000)
        except Exception as e:
            print("❌ Errore caricamento:", url, e)
            continue

        # Aspetta che compaia il container principale (non networkidle!)
        try:
            page.wait_for_selector("div[data-testid='boxscore']", timeout=8000)
        except:
            print("⚠️ Boxscore non trovato (carico comunque):", url)

        # Click su tab importanti se presenti
        tab_names = ["Batting", "Pitching", "Fielding", "Game Summary"]

        for t in tab_names:
            try:
                page.get_by_role("button", name=t).click(timeout=1500)
                time.sleep(0.3)
            except:
                pass

        # ⬇️ Estrai l'HTML già renderizzato da React
        html = page.content()
        tables = extract_tables_from_html(html)

        final_data.append({
            "url": url,
            "tables": tables
        })

        print("✔️ Estratto:", url)

    browser.close()

output_file = "mlb_boxscores.json"

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(final_data, f, indent=4)

print(f"💾 Salvato in: {output_file}")
