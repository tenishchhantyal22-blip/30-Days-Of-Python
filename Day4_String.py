# adding differnt string to form single string
variable = ['Thirty', 'Days', 'Of', 'Python']
variable_joint = ' '.join(variable)
print(variable_joint)

# coding assigning coding for all
company = 'Coding For All'
company1 = 'Python for Everyone'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(slice('For All'))
sub_string = 'coding'
print(company.index(sub_string))
print(company.replace('Coding','Python'))
print(company.split( ))
company2 = ''.join(word[0].upper() for word in company.split())
company3 = ''.join(word[0].upper() for word in company1.split())
print(company2)
print(company3)
print(company.index('C'))
print(company.index("F"))

#spliting various strings
social_media = ("Facebook, Google, Oracle, Microsoft, IBM, Apple")
print(social_media.split(", "))

# use of index string
sentence = "You cannot end a sentence with because because because is a conjunction"
first_idx = sentence.find("because")
second_idx = sentence.find("because", first_idx + 1)
third_idx = sentence.find("because", second_idx + 1)
print(second_idx)
print(first_idx)
print(third_idx)
print(company.endswith('coding'))
print(company.startswith('coding'))

# joining string
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
join_pylib = "#".join(python_libraries)
print(join_pylib)

# Escape characters uses
a = "I am enjoying this challenge\nI just wonder what is next."
print(a)

b = "Name\tAge\tCountry\tCity\t\nAsabeneht\t250\tinland\tHelsinki"
print(b)

radius = 10
area = 3.14 * radius ** 2
area_c = 'The area of a circle with {} radius is {} meters square'.format(str(radius), str(area))
print(area_c)

# calculation
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a+b))
print('{} - {} = {}'.format(a, b, a-b))
print('{} / {} = {}'.format(a, b, a/b))
print('{} % {} = {}'.format(a, b, a%b))
print('{} // {} = {}'.format(a, b, a//b))
print('{} ** {} = {}'.format(a, b, a**b))

#That's all for Day4
