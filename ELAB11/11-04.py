import csv
def fu(city,country):   
    with open(city) as city_file:
        city_reader = csv.DictReader(city_file)
        cities = list(city_reader)
        dic = dict()
        with open(country) as country_file:
            country_reader = csv.DictReader(country_file)
            print("Average temperature of countries having coastline, but not in EU:")
            countries = list(country_reader)
            for i in cities : 
                for j in countries: 
                    if i['country'] == j['country'] and j['EU'] == 'no' and  j['coastline'] == 'yes':
                        #print(f"{i['country']} {j['country']} ")
                        if not i['country'] in dic :
                            dic[i['country']] = list()
                            dic[i['country']].append(float(i['temperature']))
                        else :
                            dic[i['country']].append(float(i['temperature']))
            for i in sorted (dic.keys()) :
                print(f"{i} {sum(dic[i]) / len(dic[i]):.2f}")
city = input("Enter city file: ")
country = input("Enter country file: ")
fu(city,country)