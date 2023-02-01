# Update Values in Dictionaries and Lists

x = [[5, 2, 3], [10, 8, 9]]
x[1][0]=15
#print(x)

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
students[0]["last_name"] = "Bryant"
#print(students)

sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory["soccer"][0] = "Andres"
#print(sports_directory)

z = [{'x': 10, 'y': 20}]
z[0]["y"]=30
#print(z)
