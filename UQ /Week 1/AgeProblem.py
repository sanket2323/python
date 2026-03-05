first_person_name, first_person_age = input ("First person name and age ?").split()
second_person_name, second_person_age = input("Second Person  name and age ?").split()

if(second_person_age > first_person_age ):
    print(f"{second_person_name} is older than {first_person_name}")
elif(second_person_age == first_person_age):
    print(f"{second_person_name} and {first_person_name} are of same age")
else:
    print(f"{first_person_name} is older than {second_person_name}")

