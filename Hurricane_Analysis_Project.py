# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def convert_damages_data(damages):

  conversion = {"M": 1000000, "B": 1000000000}
  updated_damages = []

  for damage in damages:
    if damage == "Damages not recorded":
      updated_damages.append(damage)
    if damage[-1] == 'M':
      updated_damages.append(float(damage.strip('M'))*conversion["M"])
    if damage[-1] == 'B':
      updated_damages.append(float(damage.strip('B'))*conversion["B"])

  return updated_damages

updated_damages = convert_damages_data(damages)
print(updated_damages)

# 2 
# Create a Table 

def create_hurricanes_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):

  num_hurricanes = len(names)
  hurricanes = {}
  
  for index in range(num_hurricanes):
    hurricanes[names[index]] = {"Name": names[index],
    "Month": months[index],
    "Year": years[index],
    "Max Sustained Wind": max_sustained_winds[index],
    "Areas Affected": areas_affected[index],
    "Damage": updated_damages[index],
    "Deaths": deaths[index]}
  
  return hurricanes

# Create and view the hurricanes dictionary

hurricanes = create_hurricanes_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

print(hurricanes)

# 3
# Organizing by Year

def convert_to_year(hurricanes):
  new_dict = {}
  for key, value in hurricanes.items():
    current_year = value["Year"]
    current_cane = value
    if current_year in new_dict:
      new_dict[current_year].append(value)
    else:
      new_dict[current_year] = []
      new_dict[current_year].append(value)
  return new_dict


# create a new dictionary of hurricanes with year and key

hurricanes_organized_by_year = convert_to_year(hurricanes)

#print(hurricanes_organized_by_year) 


# 4
# Counting Damaged Areas

def counting_damaged_areas(hurricanes):

  areas_dictionary = {}
      
  for value in hurricanes.values():
    for area in value["Areas Affected"]:
      if area not in areas_dictionary:
        areas_dictionary[area] = 1
      if area in areas_dictionary:
        areas_dictionary[area] += 1

  return(areas_dictionary)

# create dictionary of areas to store the number of hurricanes involved in

dictionary_of_areas = counting_damaged_areas(hurricanes)
print(dictionary_of_areas)

# 5 
# Calculating Maximum Hurricane Count
def maximum_hurricane_count(dictionary_of_areas):
  current_value = 0
  maximum_hurricane = {}
  for key, value in dictionary_of_areas.items():
    if value > current_value:
      current_value = value
      maximum_hurricane[key] = value

  return(maximum_hurricane)

# find most frequently affected area and the number of hurricanes involved in

most_frequently_affected_area = maximum_hurricane_count(dictionary_of_areas)
print(most_frequently_affected_area)

# 6
# Calculating the Deadliest Hurricane
def calculating_deadliest_hurricane(hurricanes):
  current_max_deaths = 0
  current_name = str()
  deathliest_hurricane = []
  for keys, values in hurricanes.items():
    for key, value in values.items():
      if key == "Deaths" and value > current_max_deaths:
        current_max_deaths = value 
        current_name = keys

  deathliest_hurricane = current_name + " " + str(current_max_deaths)

        
  
  return deathliest_hurricane

# find highest mortality hurricane and the number of deaths
highest_mortality_hurricane = calculating_deadliest_hurricane(hurricanes)
print(highest_mortality_hurricane)
# 7
# Rating Hurricanes by Mortality
def rating_by_mortality(hurricanes):

  mortality_ratings_dic = {0:[],1:[],2:[],3:[],4:[],5:[]}

  for names, value in hurricanes.items():
      if value["Deaths"] == 0:
        mortality_ratings_dic[0].append(value)
      if value["Deaths"] > 0 and value["Deaths"] <= 100:
        mortality_ratings_dic[1].append(value)
      if value["Deaths"] > 100 and value["Deaths"] <= 500:
        mortality_ratings_dic[2].append(value)
      if value["Deaths"] > 500 and value["Deaths"] <= 1000:
        mortality_ratings_dic[3].append(value)
      if value["Deaths"] > 1000 and value["Deaths"] <= 10000:
        mortality_ratings_dic[4].append(value)
    
  return mortality_ratings_dic 

# categorize hurricanes in new dictionary with mortality severity as key

mortality_ratings = rating_by_mortality(hurricanes)
print(mortality_ratings) 
  

# 8 Calculating Hurricane Maximum Damage

def maximum_damage_hurricane(hurricanes):
  current_max_damage = 0
  current_name = str()

  for name, values in hurricanes.items():
    for key, value in values.items():
      if value == "Damages not recorded":
        continue
      if key == "Damage" and value > current_max_damage:
        current_max_damage = value
        current_name = name
        
  max_hurricane_damage = current_name + " " + str     (current_max_damage)

  return max_hurricane_damage

# find highest damage inducing hurricane and its total cost

highest_damage = maximum_damage_hurricane(hurricanes)
print(highest_damage)

# 9
# Rating Hurricanes by Damage
# damage_scale = {0: 0,
              #  1: 100000000,
              #  2: 1000000000,
              #  3: 10000000000,
              #  4: 50000000000} 
  
def rating_by_damage_scale(hurricanes):

  damage_scale_dic = {"NaN":[],0:[],1:[],2:[],3:[],4:[],5:[]}
  

  for names, value in hurricanes.items():
      if value["Damage"] == "Damages not recorded":
        damage_scale_dic["NaN"].append(value)
        continue
      if value["Damage"] == 0:
        damage_scale_dic[0].append(value)
      if value["Damage"] > 0 and value["Damage"] <= 100000000:
        damage_scale_dic[1].append(value)
      if value["Damage"] > 100 and value["Damage"] <= 1000000000:
        damage_scale_dic[2].append(value)
      if value["Damage"] > 500 and value["Damage"] <= 10000000000:
        damage_scale_dic[3].append(value)
      if value["Damage"] > 1000 and value["Damage"] <= 50000000000:
        damage_scale_dic[4].append(value)

  return damage_scale_dic
  
# categorize hurricanes in new dictionary with damage severity as key

damage_scale = rating_by_damage_scale(hurricanes)
print(damage_scale)
