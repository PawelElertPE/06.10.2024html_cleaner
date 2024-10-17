#tuples are immutable
empty_tupe = ()
print(f"Empty tuple: {empty_tupe}")

empty_tuple = tuple()
print(f"Empty tuple: {empty_tupe}")
type(empty_tupe)

tech_companies = ("Apple", "Google", "Microsoft", "Tesla", "Meta")
print(tech_companies)

print(tech_companies[1])

print(tech_companies[-2])

tech_companies[2] = "SSSSLLL"
print(tech_companies)

tech_companies = ("Google", "Apple", "Amazon")
# Convert the tuple to a list
tech_companies_list = list(tech_companies)

# Make the change
tech_companies_list[2] = "MSFT"

#Convert the list back to a tuple
tech_companies = tuple(tech_companies_list)

print(tech_companies)