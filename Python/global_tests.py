# global tests

var = [7]

def mutate_sans_global(value):
    var[0] = value

def print_global():
    print(var[0])

def mutate_with_global(value):
    global var
    var[0] = value

print_global()
mutate_sans_global(42)
print_global()
mutate_with_global(42)
print_global()
