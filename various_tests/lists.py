empty_list = []

print("Empty list: %s" % empty_list)

empty_list = list()

print("Empty list: %s" % empty_list)

countries_list = ["Unites States", "France", "India", "Japan"]

countries_list
type(countries_list)
countries_list[0]
countries_list[1]

countries_list[-1]

countries_list[2] = "INDIA"

countries_list

countries_list.append("USA")
countries_list.append("Canada")
countries_list.append("Singapore")

countries_list

new_countries = ["France", "Germany", "Spain"]

countries_list.extend(new_countries)

print(countries_list)

countries_list.remove("INDIA")
countries_list

removed_country = countries_list.pop(1)

removed_country

countries_list

del countries_list[0]
countries_list

countries_list.insert(1, "Germany")
countries_list
countries_list.insert(0, "Poland")
countries_list
countries_list.insert(-1, "Romania")
countries_list.insert(len(countries_list), "Czechy")
countries_list.insert(len(countries_list)-1, "Pepiki")
countries_list.insert(len(countries_list), "Germany")
countries_list

student_ages = [23, 17, 19, 25, 34, 18]
student_ages

student_gpas = [2.1, 3.3, 4.0, 3.7, 2.9]
student_gpas

doris_record = ["Doris", 23, 3.3, True, "Columbia University"]
doris_record