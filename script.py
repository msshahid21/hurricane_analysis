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

# write your update damages function here:
def update_damages(damages):
    '''
    Returns a list equal to damages list with elements converted into float
    equivalents.
    '''
    updated_damages = []

    for item in damages:
        if item[-1] == 'B':
            updated_damages.append(float(item[:-1]) * 1000000000)
        elif item[-1] == 'M':
            updated_damages.append(float(item[:-1]) * 1000000)
        else:
            updated_damages.append(item)
    return updated_damages

# write your construct hurricane dictionary function here:
def construct_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    '''
    Returns a dictionary with the keys of the dictionary being the names of the hurricanes and the
    values of the dictionary being a dictionary containing information of the hurricane.
    '''
    hurricane_dict = {}
    for i, name in enumerate(names):
        hurricane_dict[name] = {'Name': name,
                                'Month': months[i],
                                'Year': years[i],
                                'Max Sustained Wind': max_sustained_winds[i],
                                'Areas Affected': areas_affected[i],
                                'Damage': damages[i],
                                'Deaths': deaths[i]}
    return hurricane_dict

# write your construct hurricane by year dictionary function here:
def construct_year_dict(hurricane_dict):
    '''
    Returns a dictionary object where hurricane information is organized by year as key.
    '''
    year_dict = {}
    for info in hurricane_dict.values():
        year = info['Year']
        if year not in year_dict:
            year_dict[year] = [info]
        else:
            year_dict[year].append(info)
    return year_dict

# write your count affected areas function here:
def count_affected_areas(hurricane_dict):
    '''
    Return a dictionary object containing the number of times an area in the Atlantic has been affected.
    '''
    areas_dict = {}
    for info in hurricane_dict.values():
        affected_areas = info['Areas Affected']
        for area in affected_areas:
            if area not in areas_dict:
                areas_dict[area] = 1
            else:
                areas_dict[area] += 1
    return areas_dict

# write your find most affected area function here:
def most_affected_area(affected_areas_dict):
    '''
    Return a list containing the name of the most affected area and the number of times it was hit.
    '''
    most_affected = ''
    count_most_affected = 0

    for area in affected_areas_dict.keys():
        if affected_areas_dict.get(area) > count_most_affected:
            count_most_affected = affected_areas_dict.get(area)
            most_affected = area

    return [most_affected, count_most_affected]

# write your greatest number of deaths function here:
def most_deaths(hurricane_dict):
    '''
    Return a list containing the name of the hurricane the caused the most number of deaths and its deathcount.
    '''
    m_death = ''                # variable containing the name of the most deadly hurricane
    m_deathcount = 0            # variable containing the value of the deathcount for the most deadly hurricane

    for name in hurricane_dict.keys():
        deathcount = hurricane_dict.get(name)['Deaths']
        if deathcount > m_deathcount:
            m_death = name
            m_deathcount = deathcount

    return [m_death, m_deathcount]

# write your catgeorize by mortality function here:
def construct_mortality_dict(hurricane_dict):
    '''
    Return a dictionary containing the hurricanes ordered by a mortality scale.
    '''
    # Creating initial mortality dictionary
    mortality_dict = {0: [],
                      1: [],
                      2: [],
                      3: [],
                      4: [],
                      5: []}

    # Categorization
    for info in hurricane_dict.values():
        deathcount = info['Deaths']
        if deathcount <= 0:
            mortality_dict[0].append(info)
        elif deathcount <= 100:
            mortality_dict[1].append(info)
        elif deathcount <= 500:
            mortality_dict[2].append(info)
        elif deathcount <= 1000:
            mortality_dict[3].append(info)
        elif deathcount <= 10000:
            mortality_dict[4].append(info)
        else:
            mortality_dict[5].append(info)

    return mortality_dict

# write your greatest damage function here:







# write your catgeorize by damage function here:







# Function Tests
#print(update_damages(damages))
#hurricane_dict = construct_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
#print(hurricane_dict)
#print('\n')
#print(construct_year_dict(hurricane_dict))
#affected_areas_dict = count_affected_areas(hurricane_dict)
#print(affected_areas_dict)
#print('\n')
#print(most_affected_area(affected_areas_dict))
#print(most_deaths(hurricane_dict))
#print(construct_mortality_dict(hurricane_dict))
