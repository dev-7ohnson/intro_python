# def greet_user():
#     first_name = input("Enter your first name: ")
#     last_name = input("Enter your last name: ")
#     print(f"Welcome {first_name} {last_name}!")

# use call
# greet_user()
#
# def greeting(user):
#     print(f"Hello {user}!")
#
# greeting("Peter")

def area_circle(radius, precision):
    a = 22/7 * radius * radius
    result = round(a, precision)
    print(result)

area_circle(2.9, 2)
area_circle(6.11, 0)

def volume_cylinder(r , h):
    v = 22/7 * r * r * h
    print(v)

volume_cylinder(2.9, 2)

