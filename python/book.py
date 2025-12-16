import json
from datetime import date, timedelta
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
import time
from playwright.sync_api import sync_playwright

separate_tab = []

def return_stats():
    global separate_tab
    all = []

    with open("mlb_boxscores.json") as file:
        all = json.load(file)

    top_left_table = all[0]["tables"][2]
    bottom_left_table = all[0]["tables"][3]
    top_right_table = all[0]["tables"][4]
    bottom_right_table = all[0]["tables"][5]

    tables_in_order = [top_left_table, bottom_left_table, top_right_table, bottom_right_table]

    R = []
    H = []
    RBI = []
    BB = []
    K = []
    IP_bl = []
    H_bl = []
    R_bl = []
    ER_bl = []
    BB_bl = []
    K_bl = []
    R_tr = []
    H_tr = []
    RBI_tr = []
    BB_tr = []
    K_tr = []
    IP_br = []
    H_br = []
    R_br = []
    ER_br = []
    BB_br = []
    K_br = []
    players = {}

    # In alto a destra 

    # Prendiamo R
    for row in top_left_table[1:]:
        new_data = {
            "player": row[0],
            "R": row[2]
        }
        R.append(new_data)

    # Prendiamo H
    for row in top_left_table[1:]:
        new_data = {
            "player": row[0],
            "H": row[3]
        }
        H.append(new_data)

    # Prendiamo RBI
    for row in top_left_table[1:]:
        new_data = {
            "player": row[0],
            "RBI": row[4]
        }
        RBI.append(new_data)

    # Prendiamo BB
    for row in top_left_table[1:]:
        new_data = {
            "player": row[0],
            "BB": row[5]
        }
        BB.append(new_data)

    # Prendiamo K
    for row in top_left_table[1:]:
        new_data = {
            "player": row[0],
            "K": row[6]
        }
        K.append(new_data)

    # Passiamo a basso sinistra

    # Prendiamo IP
    for row in bottom_left_table[1:]:
        new_data = {
            "player": row[0],
            "IP": row[1]
        }
        IP_bl.append(new_data)

    # Prendiamo H
    for row in bottom_left_table[1:]:
        new_data = {
            "player": row[0],
            "H": row[2]
        }
        H_bl.append(new_data)

    # Prendiamo R
    for row in bottom_left_table[1:]:
        new_data = {
            "player": row[0],
            "R": row[3]
        }
        R_bl.append(new_data)

    # Prendiamo ER
    for row in bottom_left_table[1:]:
        new_data = {
            "player": row[0],
            "ER": row[4]
        }
        ER_bl.append(new_data)

    # Prendiamo BB
    for row in bottom_left_table[1:]:
        new_data = {
            "player": row[0],
            "BB": row[5]
        }
        BB_bl.append(new_data)

    # Prendiamo K
    for row in bottom_left_table[1:]:
        new_data = {
            "player": row[0],
            "K": row[6]
        }
        K_bl.append(new_data)

    # In alto a destra 

    # Prendiamo R
    for row in top_right_table[1:]:
        new_data = {
            "player": row[0],
            "R": row[2]
        }
        R_tr.append(new_data)

    # Prendiamo H
    for row in top_right_table[1:]:
        new_data = {
            "player": row[0],
            "H": row[3]
        }
        H_tr.append(new_data)

    # Prendiamo RBI
    for row in top_right_table[1:]:
        new_data = {
            "player": row[0],
            "RBI": row[4]
        }
        RBI_tr.append(new_data)

    # Prendiamo BB
    for row in top_right_table[1:]:
        new_data = {
            "player": row[0],
            "BB": row[5]
        }
        BB_tr.append(new_data)

    # Prendiamo K
    for row in top_right_table[1:]:
        new_data = {
            "player": row[0],
            "K": row[6]
        }
        K_tr.append(new_data)

    # Passiamo a basso destra

    # Prendiamo IP
    for row in bottom_right_table[1:]:
        new_data = {
            "player": row[0],
            "IP": row[1]
        }
        IP_br.append(new_data)

    # Prendiamo H
    for row in bottom_right_table[1:]:
        new_data = {
            "player": row[0],
            "H": row[2]
        }
        H_br.append(new_data)

    # Prendiamo R
    for row in bottom_right_table[1:]:
        new_data = {
            "player": row[0],
            "R": row[3]
        }
        R_br.append(new_data)

    # Prendiamo ER
    for row in bottom_right_table[1:]:
        new_data = {
            "player": row[0],
            "ER": row[4]
        }
        ER_br.append(new_data)

    # Prendiamo BB
    for row in bottom_right_table[1:]:
        new_data = {
            "player": row[0],
            "BB": row[5]
        }
        BB_br.append(new_data)

    # Prendiamo K
    for row in bottom_right_table[1:]:
        new_data = {
            "player": row[0],
            "K": row[6]
        }
        K_br.append(new_data)

    # Dati di tutte le tabelle

    all_datas_top_left = [R, H, RBI, BB, K]
    all_datas_bottom_left = [IP_bl, H_bl, R_bl, ER_bl, BB_bl, K_bl]
    all_datas_top_right = [R_tr, H_tr, RBI_tr, BB_tr, K_tr]
    all_datas_bottom_right = [IP_br, H_br, R_br, ER_br, BB_br, K_br]

    all_full_datas = [all_datas_top_left, all_datas_bottom_left, all_datas_top_right, all_datas_bottom_right]

    def build_tables_separate(all_full_datas):
        tables = []

        for section in all_full_datas:          # es: top_left
            table_players = {}

            for stat_list in section:            # es: R, H, RBI...
                for item in stat_list:
                    player = item["player"]

                    if player not in table_players:
                        table_players[player] = {"player": player}

                    for key, value in item.items():
                        if key != "player":
                            table_players[player][key] = value

            # trasformiamo in lista (ordine di inserimento preservato)
            tables.append(list(table_players.values()))

        return tables

    separate_tab = build_tables_separate(all_full_datas)

    for i, table in enumerate(separate_tab, 1):
        print(f"\n=== TABLE {i} ===")
        for player in table:
            print(player)

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

def extract_full_text(html):
    soup = BeautifulSoup(html, "html.parser")
    containers = soup.select("div[data-mlb-test='gamedayVisibleContentWrapper']")
    all_texts = []

    for container in containers:
        text_parts = []

        sections = container.select("div.BoxscoreInfostyle__ContentWrapper-sc-1g9pw6v-4")
        for sec in sections:
            # Titolo sezione
            title_tag = sec.select_one("span.BoxscoreInfostyle__ContentTitleWrapper-sc-1g9pw6v-2")
            if title_tag:
                text_parts.append(title_tag.get_text(strip=True))

            # Tutti i div dei field
            fields = sec.select("div[data-mlb-test='gamedayFieldListWrapper']")
            for f in fields:
                spans = f.select("span.BoxscoreInfostyle__FieldListInnerWrapper-sc-1g9pw6v-6")
                if spans:
                    field_title = spans[0].get_text(strip=True)
                    # Prendi tutto il testo del div, rimuovi il titolo
                    field_value = f.get_text(" ", strip=True).replace(field_title, "")
                    # Concatena titolo + valore senza spazi inutili
                    text_parts.append(field_title + field_value)

        all_texts.append("\n".join(text_parts))

    return all_texts

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
            "tables": tables,
        })

        print("✔️ Estratto:", url)

    browser.close()

output_file = "mlb_boxscores.json"

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(final_data, f, indent=4)

print(f"💾 Salvato in: {output_file}")
all_add_infos = extract_full_text(html)
return_stats()

campi = ["2B", "HR", "GIDP", "Runners left in scoring position, 2 out", 
         "SF", "SAC", "SB", "CS", "DP", "E"]

def filtra_campi(tabelle):
    risultati = []
    for tab in tabelle:
        if not tab.strip():
            continue
        lines = tab.split("\n")
        estratti = []
        for line in lines:
            for campo in campi:
                if line.startswith(campo):
                    estratti.append(line)
        risultati.append("\n".join(estratti))
    return risultati

estratti = filtra_campi(all_add_infos)
righe = [r.strip() for tab in estratti for r in tab.split("\n") if r.strip()]

lista_dizionari = []

for tab in estratti:
    righe = [r.strip() for r in tab.split("\n") if r.strip()]
    diz = {}
    for r in righe:
        for campo in campi:
            if r.startswith(campo):
                diz[campo] = r[len(campo):].strip()
                break
    lista_dizionari.append(diz)

about_info_plus_for_first_table = lista_dizionari[0]
about_info_plus_for_second_table = lista_dizionari[1]

all_plus_info = [about_info_plus_for_first_table, about_info_plus_for_second_table]

print("\n")

tabella = 1

for all_info in all_plus_info:
    print(f"=== Tabella plus data per 'tabella {tabella}' ===")
    print(all_info)
    print("\n")
    tabella += 2

datas = []

for player in separate_tab:
    for p in player:
        datas.append(p)

for plus in all_plus_info:
    for k, v in plus.items():
        for data in datas:
            if k == 'Runners left in scoring position, 2 out':
                k = "RLSP"
            name = data['player'].split(",")[0].strip().lower()
            if name in v.lower(): 
                data[k] = v 
            else:
                data[k] = 0

for data in datas:
    print(data)