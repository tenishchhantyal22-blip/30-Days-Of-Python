# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# exercise level-1
print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
more_companies = {'Twitter', 'Samsung', 'Tenish'}
it_companies.update(more_companies)
print(it_companies)
it_companies.remove('Facebook')
print(it_companies)
# the major difference between remove and discard is, remove raises a keyerror if the iteam is not found but discard does nothing

# Exercise: level-2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


print(A.union(B))
intersect = A.intersection(B)
print(intersect)
subst = A.issubset(B)
print(subst)
disjont = A.isdisjoint(B)
print(disjont)
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
del A
del B
del age

# Exercise: Level
age = [22, 19, 24, 25, 26, 24, 25, 24]
st1 = set(age)
print(st1)
print(len(age))
print(len(st1))
print(len(age)>len(st1))

# Difference between different data types
# string:- ordered, non-changable, can be duplicate
# list = ordered, changable, duplicate
# tuples = ordered, non-changable, duplicate
# set = unordered, changable, can't duplicate

sentence = "I am a teacher and I love to inspire and teach people."
cleaned_sentence = sentence.replace(".","")
word_list = cleaned_sentence.split()
unique_words = set(word_list)
print(word_list)
print(unique_words)









