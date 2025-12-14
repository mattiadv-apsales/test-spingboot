import json

def return_stats():
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

    tables_separate = build_tables_separate(all_full_datas)

    for i, table in enumerate(tables_separate, 1):
        print(f"\n=== TABLE {i} ===")
        for player in table:
            print(player)