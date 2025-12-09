import asyncio
from playwright.async_api import async_playwright
import json
import re

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.spotrac.com/mlb/rankings/player/_/year/2026/sort/cap_total")
        await page.wait_for_selector("#table-wrapper ul")

        player_uls = await page.query_selector_all("#table-wrapper ul")
        players = []

        for ul in player_uls:
            lis = await ul.query_selector_all("li")
            for li in lis:
                text = await li.text_content()
                text = re.sub(r"\s+", " ", text).strip()
                
                # Match del pattern "Nome Cognome TEAM, RUOLO $SALARY"
                match = re.match(r"^(.*?) ([A-Z]{2,3}), ([A-Z/0-9]+) (\$\d[\d,]+)$", text)
                if match:
                    name = match.group(1).strip()
                    # Rimuove eventuali numeri iniziali nel nome
                    name = re.sub(r"^\d+\s+", "", name)
                    team = match.group(2).strip()
                    position = match.group(3).strip()
                    salary = match.group(4).strip()
                    players.append({
                        "name": name,
                        "team": team,
                        "position": position,
                        "salary": salary
                    })

        # Salva JSON pulito
        with open("mlb_players_2026.json", "w", encoding="utf-8") as f:
            json.dump(players, f, indent=4, ensure_ascii=False)

        print(f"Salvati {len(players)} giocatori in 'mlb_players_2026.json'.")

        await browser.close()

asyncio.run(main())
