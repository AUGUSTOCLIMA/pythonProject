usuarios = {}
usuarios = {
    "Chaves" : ["Chaves Silva", "17/06/2017", "Recep_01"],
    "Quico" : ["Enrico Flores", "03/06/1976", "Raiox_02"],
    "Quico" : ["Enrico Flores", "03/06/1976", "Raiox_03"],
}
usuarios["Florinda"] = ["Florinda flores", "26/11/2017", "Recep_01"]
usuarios["Florinda"] = ["Florinda flores", "26/11/2016", "Recep_01"]

print(usuarios)
print("###########=======##########")
print("Dados: ", usuarios.get("Florinda"))