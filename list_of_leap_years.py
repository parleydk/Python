## List of leap years
start_year = int(input("Enter a four digit year to start leap year listing: "))
how_many = int(input("How many leap years would you like? "))
leap_years = []
i = start_year - start_year % 4

while i > 0:
    if i % 100 == 0 and i % 400 != 0:
        pass
    else:
        leap_years.append(i)
    if len(leap_years) < how_many:
        pass
    else:
        break        
    i += 4

for leap in leap_years:
    print(leap)
