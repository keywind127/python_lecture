## example 1

def filter_names(names):
    for name in names:
        if name != "":
            yield name

male_names = ["kevin", "david", "", "daniel"]
female_names = ["lydia", "gloria", "", ""]

for name in filter_names(male_names):
    print(name)

for name in filter_names(female_names):
    print(name)

## example 2

male_names = ["kevin", "david", "", "daniel"]
female_names = ["lydia", "gloria", "", ""]

for name in (name for name in male_names if name != ""):
    print(name)

for name in (name for name in female_names if name != ""):
    print(name)

## example 3

male_names = ["", "kevin", "david", "", "daniel"]

print(next((name for name in male_names if name != "")))

## example 4

# implement your code 
# so that the names are filtered
# and "reversed"

def filter_names(names):
    # your code here
    # :)
    # ;)
    for i in reversed(range(len(names))):
        if names[i] != "":
            yield names[i]

male_names = ["kevin", "david", "", "daniel"]
female_names = ["lydia", "gloria", "", ""]

for name in filter_names(male_names):
    print(name)

for name in filter_names(female_names):
    print(name)
