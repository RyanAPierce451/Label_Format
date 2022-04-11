"""
PROGRAMMER: RYAN A PIERCE
DATE:   APRIL 05, 2022
ASSIGNMENT:  FUNCTIONS AND STRINGS ASSIGNMENT
ALGORITHM: USER-INPUT FORMATTED TO SPECIFIED GUIDELINES | MAILING LABEL FORMATTING
************
label Design:
first_name middle_name last_name
street_address  (** this information may take two lines to represent)
city, state, zip_code
--------------
GUIDELINES:
    MAX LINES: 5
    MAX CHARACTER PER LINE: 35
"""
from unicodedata import name
import List_Dic_Variables


# Label: Name Format Function
def capitalize_n_count(first_name, middle_name, last_name):
    f_name = first_name.capitalize()
    m_name = middle_name.capitalize()
    l_name = last_name.capitalize()
    name_label = []
    count = len(f_name) + len(m_name) + len(l_name) + 2 #blank spaces
    if count > 35 and len(f_name) > 0 and len(l_name) > 0:
        count -= len(m_name)
        if count > 35:
            name_label = [f_name]
            name_label = ' '.join(name_label).strip()
            return name_label
        name_label = [f_name, l_name]
        name_label = ' '.join(name_label).strip()
        return name_label
    elif count <= 35 and len(l_name) > 0:
        if len(m_name) > 0:
            name_label = [f_name,m_name,l_name]
            name_label = ' '.join(name_label).strip()
            return name_label
        name_label = [f_name,l_name]
        name_label = ' '.join(name_label).strip()
        return name_label



# Label: City, State, Zip Format Function
def city_state_zip_format(city,state,zip_convertion):
    global city_state_zip_count
    city_state_zip = city + state + zip_convertion
    city_state_zip_split = []
    count = len(city) + len(state) + len(zip_convertion) # ',' spaces and 2 blank spaces
    if count >= 35:
        for i in range(0, len(city_state_zip), 34):
            city_state_zip_split.append(city_state_zip[i : i + 34])
        city_state_zip_split[0] = city_state_zip_split[0] + '-' 
        city_state_zip_count.append(city_state_zip_split[0])
        if len(city_state_zip_split[1]) == 35: 
            city_state_zip_count.append(city_state_zip_split[1])
            city_state_zip_split = '\n'.join(city_state_zip_split)
            return city_state_zip_split
        else:
            city_state_zip_count.append(city_state_zip_split[1])
        city_state_zip_split = '\n'.join(city_state_zip_split)
        return city_state_zip_split
    city_state_zip_split = [city,state,zip_convertion]
    city_state_zip_split = ''.join(city_state_zip_split)
    city_state_zip_count.append(city_state_zip)
    return city_state_zip_split


# State Abbreviation Function
def find_state_abbreviation(state):
    while True:
        state = state.capitalize().title()
        states_abbreviate = List_Dic_Variables.states_abb
        find_state_abbreviation = List_Dic_Variables.find_state

        if state in find_state_abbreviation:
            return find_state_abbreviation[state]
        elif state.upper() in states_abbreviate:
            return state.upper()
        elif state.upper() not in states_abbreviate and state not in find_state_abbreviation:
            print('\n**ERROR: State Not Found**\n**Re-enter State**')
            state = str(input('State: ')).strip()
        


# Street Abbtrviation Funtion
def find_street_abbreviaiton(street_add):
    while True:
        street_suffix = street_add.title().split()
        street_suffix = street_suffix[-1]
        street_abbrev = List_Dic_Variables.street_abbrev
        street_name_abbreviate = List_Dic_Variables.street_name_abbrev
        if street_suffix in street_name_abbreviate:
            street_add = street_add.replace(street_suffix,street_name_abbreviate[street_suffix])
            return street_add
        elif street_suffix.upper() in street_abbrev:
            street_add = street_add.replace(street_suffix,street_suffix.upper())
            return street_add
        elif street_suffix not in street_name_abbreviate and street_suffix.upper() not in street_abbrev :
            print('\n**Street Suffix Not Found**\n**Re-enter Street Address**')
            street_add = str(input('Street Address: ')).strip().title()
        


# Label: Street Address Format Function
def street_convert(street_add):
    global street_count
    street_split = []
    if len(street_add) >= 35:
        for i in range(0, len(street_add), 34):
            street_split.append(street_add[i : i + 34])
        street_split[0] = street_split[0] + '-' 
        street_count.append(street_split[0])
        street_count.append(street_split[1])     
        if len(street_add) > 70:
            street_split[1] = street_split[1] + '-'
            street_count[1] = street_split[1]
            street_count.append(street_split[2])
        street_split = '\n'.join(street_split) 
        return street_split
    street_count.append(street_add)     
    return street_add

        
# Zip Converter [9 to 5] Function
def zip_convert(zip_code):
    while zip_code[:5].isdigit() != True or len(zip_code) < 5:
        if zip_code[:5].isdigit() != True:
            print('\n**Error: 5 Digit Zip Code Is Not Integers**\n**Re-enter Zip Code**')
            zip_code = str(input('Zip Code: '))
        elif len(zip_code) < 5:
            print('\n**Error: Zip Code Length Too Short**\n**Re-enter Zip Code**')
            zip_code = str(input('Zip Code: '))
    zip_convert = zip_code
    zip_convert = zip_code[:5]
    return zip_convert

# User Inputs, Print Label Format, Print Label Line Lengths
def main():
    global street_count
    global city_state_zip_count
    first_name = str(input('First Name: ')).strip().title()
    while len(first_name) > 35:
        print('\n**Error: First Name Exceeds Limit**\n**Re-enter First Name**\n')
        first_name = str(input('First Name: ')).strip().title()
    middle_name = str(input('Middle Name: ')).strip().title()
    last_name = str(input('Last Name: ')).strip().title()

    street_add = str(input('Street Address: ')).strip().title()
    street_add = find_street_abbreviaiton(street_add)
    while len(street_add) > 103:
        street_count = []
        print('\n**Error: Street Address Exceeds Label Limit**\n**Re-enter Street Address**')
        street_add = str(input('Street Address: ')).strip().title()
        street_add = find_street_abbreviaiton(street_add)
    
    city = str(input('City: ')).strip().title() + ', '
    state = str(input('State: ')).strip()
    state = find_state_abbreviation(state) + ', '
    zip_code = str(input('Zip Code: ')).strip()
    zip_convertion = zip_convert(zip_code)
    while len(city_state_zip_format(city, state, zip_convertion)) > 70:
        city_state_zip_count = []
        print('\n**Error: City, State, Zip Exceed Label Limit**\n**Re-enter City, State, Zip**')
        city = str(input('City: ')).strip().title() + ', '
        state = str(input('State: ')).strip()
        state = find_state_abbreviation(state) + ', '
        zip_code = str(input('Zip Code: ')).strip()
        zip_convertion = zip_convert(zip_code)
        print()
    
    if len(street_add) > 70 and len(city_state_zip_format(city + ',', state + ',', zip_convertion)) > 35:
            print('\n**ERROR: Label Exceeds Format**')
            print(capitalize_n_count(first_name, middle_name, last_name))
            print(street_convert(street_add+','))
            print(city_state_zip_format(city, state, zip_convertion))
            print('**ERROR: Label Exceeds Format**')
            return
    print('')
    print(capitalize_n_count(first_name, middle_name, last_name))
    print(street_convert(street_add+','))
    print(city_state_zip_format(city, state, zip_convertion))

    print('\nName Formated Length: ',len(capitalize_n_count(first_name, middle_name, last_name)))
    print('Street Line 1 Length: ',len(street_count[0]))
    if len(street_count[0]) == 35: 
        print('Street Line 2 Length: ',len(street_count[1]))
        if len(street_count[1]) == 35: print('Street Line 3 Length: ',len(street_count[2]))
    if len(city_state_zip_format(city, state, zip_convertion)) > 35: 
        print('City, State, Zip Line Length 1: ',len(city_state_zip_count[0]),'\nCity, State, Zip Line Length 2: ', len(city_state_zip_count[1]))
    else: print('City, State, Zip Line Length 1: ',len(city_state_zip_count[0]))




 


## Runs Main, Assigns Global Variables
if __name__=="__main__":
    while True:
        street_count = []
        city_state_zip_count = []
        main()
        print('')
        while True:
            user_input = str(input('CREATE ANOTHER LABEL (Y) OR EXIT (N): ')).upper()
            if user_input != 'Y' and user_input != 'N':
                 print("***ERROR: INVALID INPUT; TRY AGAIN***")
            else:
                break
        if user_input == 'N': break