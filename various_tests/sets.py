empty_set = set()

print(empty_set)

type(empty_set)

numbers_list = [100, 200, 300, 400, 500, 200, 500]
numbers_list

numbers_set = {100, 200, 300, 400, 500, 200, 500}
numbers_set

numbers_set.add(1000)
numbers_set.add(100)
numbers_set.add(6.6)

numbers_set
numbers_set.add("python")
numbers_set

numbers_set.remove("Python")
numbers_set.remove("python")

numbers_set.discard(12)
numbers_set.remove(12)


multiples_of_5 = {5, 10, 15, 20, 25, 30, 35, 40,}

multiples_of_10 = {10, 20, 30, 40, 50, 60}

union = multiples_of_5 | multiples_of_10
union

union = multiples_of_5.union(multiples_of_10)
union

intersection = multiples_of_5 & multiples_of_10

intersection

multiples_of_5 = {5 ,10, 15, 20, 25, 30, 35, 40}
multiples_of_10 = {10, 20, 30, 40, 50, 60}

difference = multiples_of_5 - multiples_of_10
difference

print(type(difference))

symmetric_difference = multiples_of_5 ^ multiples_of_10
symmetric_difference