all_variables = {}

with open("test.mdv", "r") as f:
    for line in f:
        line = line.strip()

        if line.startswith("scrivi:"):
            exist = False
            for k, v in all_variables.items():
                if "{" + k + "}" in line:
                    exist = True
                    line = line.replace(str(k), str(v)).replace("{", "").replace("}", "").replace("\"", "")

            if "\"" in line and exist == False:
                print(line.replace("scrivi:", "").replace("\"", ""))
            elif exist == True:
                print(line.replace("scrivi:", ""))
            else:
                raise ValueError('You have to insert the string inside ""')
        elif line.startswith("calcola:"):
            for k, v in all_variables.items():
                if k in line:
                    line = line.replace(str(k), str(v))
            try:
                print(eval(line.replace("calcola:", "")))
            except:
                raise ValueError("You have to insert a valid calucaltion for 'calcola'")
        elif line.startswith("scriviamo"):
            input()
        elif line.startswith("variabile:"):
            if "=" in line:
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
            else:
                raise ValueError("Error: you can't declare a variable without '='")
        elif line.startswith("se"):
            if "==" in line:
                condizione = line[len("se"):].strip()
                var1, var2 = condizione.split("==", 1)
                var1 = var1.strip()
                var2 = var2.strip()
                if var1 in all_variables.keys():
                    var1 = all_variables[var1]
                if var2 in all_variables.keys():
                    var2 = all_variables[var2]

                try:
                    var1 = eval(str(var1))
                except:
                    pass

                try:
                    var2 = eval(str(var2))
                except:
                    pass

                if var1 == var2:
                    print("True")
                else:
                    print("False")