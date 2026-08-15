empty_list = [] #declaring an empty list
lst = ['A', 'B', 'C', 'D', 'E']
print(len(lst))
select = [lst[0], lst[2], lst[4]]
print(select)

mixed_data_variable = ["Tenish", 19, 5.5, "unmarried", "Pokhara"]

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(mixed_data_variable)
print(len(it_companies))

#select
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
select = [it_companies[0], it_companies[3], it_companies[6]]
print(select)


#insert
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
it_companies.insert(2, "Samsung")
print(it_companies)

#uppercase
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies[2] = it_companies[2].upper()
print(it_companies)

#join data type
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
joint = '#'.join(it_companies)
print(joint)

#exist
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
does_exist = "Google" in it_companies
print(does_exist)

#sort
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.sort()
print(it_companies)

#reverse sort
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.sort(reverse = True)
print(it_companies)

#slice
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies1 = it_companies[-4:]
print(it_companies1)
it_companies2 = it_companies[1:4]
print(it_companies2)
it_companies3 = it_companies[1:-1]


