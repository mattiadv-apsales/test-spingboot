all_variables = {}

lines_raw = open("test.mdv", "r").read().splitlines()

def esegui_comando(line):
    line = line.strip()
    if line.startswith("scrivi:"):
        output = line.replace("scrivi:", "").strip()
        for k, v in all_variables.items():
            output = output.replace("{" + k + "}", str(v))
        if output.startswith('"') and output.endswith('"'):
            output = output[1:-1]
        print(output)
    elif line.startswith("calcola:"):
        cmd = line.replace("calcola:", "").strip()
        for k, v in all_variables.items():
            cmd = cmd.replace(str(k), str(v))
        try:
            print(eval(cmd))
        except:
            raise ValueError(f"Calcolo non valido: {cmd}")
    elif line.startswith("variabile:"):
        if "=" not in line:
            raise ValueError("Errore: non puoi dichiarare una variabile senza '='")
        _, resto = line.split("variabile:", 1)
        nome, valore = resto.split("=", 1)
        nome = nome.strip()
        valore = valore.strip()
        if valore == "scriviamo":
            valore = input(f"Inserisci valore per {nome}: ")
            try:
                valore = eval(valore)
            except:
                pass
        else:
            valore = eval(valore, {}, all_variables)
        all_variables[nome] = valore
    elif line.startswith("scriviamo"):
        input()

def run_se_elif_else(i, lines_raw, condizione_iniziale):
    condizioni_blocchi = []
    blocchi = []

    condizioni_blocchi.append(condizione_iniziale)
    blocchi.append([])

    i += 1
    while i < len(lines_raw):
        line = lines_raw[i]
        if line.startswith("  "):
            blocchi[-1].append(line.strip())
            i += 1
        else:
            if line.startswith("altrimenti se"):
                condizione = line[len("altrimenti se"):].strip()
                if condizione.endswith(":"):
                    condizione = condizione[:-1]
                condizioni_blocchi.append(condizione)
                blocchi.append([])
                i += 1
            elif line.strip() == "altrimenti:":
                condizioni_blocchi.append(None)
                blocchi.append([])
                i += 1
            else:
                break

    eseguito = False
    for idx, cond in enumerate(condizioni_blocchi):
        if cond is None:
            esegui_blocco(blocchi[idx])
            eseguito = True
            break
        else:
            if "==" not in cond:
                continue
            var1, var2 = cond.split("==", 1)
            var1 = var1.strip()
            var2 = var2.strip()
            if var1 in all_variables:
                var1 = all_variables[var1]
            if var2 in all_variables:
                var2 = all_variables[var2]
            try: var1 = eval(str(var1))
            except: pass
            try: var2 = eval(str(var2))
            except: pass
            if var1 == var2:
                esegui_blocco(blocchi[idx])
                eseguito = True
                break
    return i

def esegui_blocco(blocco):
    for comando in blocco:
        esegui_comando(comando)

i = 0
while i < len(lines_raw):
    line = lines_raw[i].strip()
    if line.startswith("se") and line.endswith(":"):
        condizione = line[3:-1].strip()
        i = run_se_elif_else(i, lines_raw, condizione)
        continue
    else:
        esegui_comando(line)
    i += 1