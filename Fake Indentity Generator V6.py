import os
import random
import time
import string

os.system('cls')
os.system('color a')
start=input('Press Enter to Engage')
os.system('cls')
os.system('color a')
os.system('title Fake Identity Generator V6')
def adminst():
    os.system('cls')
    print('Hi,',user,'! Welcome to:')
    print("""
            Fake
                Identity
                        Generator
                        
           \            /  ____________
            \          /  |
             \        /   |
              \      /    |___________
               \    /     |           |
                \  /      |           |
                 \/       |___________|
     """)
    print('1 - Lowest, least info, 6 - Lv. 1 BEAST MODE')
    print('2 - barely any info, 7 - Lv. 2 BEAST MODE')
    print('3 - middle, some info, 8 - Lv. 3 BEAST MODE')
    print('4 - no sensitive info, 9 - Lv. 4 BEAST MODE')
    print('5 - Highest, all info, 10 - Lv. 5 BEAST MODE ---DANGER!')
    print('99 - Admin Console')
    temp=int(input('What Information level (Amount of info) to generate at? Choice:'))
user=input('Hi,What is your name? My name is:')
if(user=='admin'):
    passwd=input('Password:')
    if(passwd=='burgir'):
        adminst()
os.system('cls')
print('Hi,',user,'! Welcome to:')
print("""
            Fake
                Identity
                        Generator
                        
           \            /  ____________
            \          /  |
             \        /   |
              \      /    |___________
               \    /     |           |
                \  /      |           |
                 \/       |___________|
     """)
print('1 - Lowest, least info, 6 - Lv. 1 BEAST MODE')
print('2 - barely any info, 7 - Lv. 2 BEAST MODE')
print('3 - middle, some info, 8 - Lv. 3 BEAST MODE')
print('4 - no sensitive info, 9 - Lv. 4 BEAST MODE')
print('5 - Highest, all info, 10 - Lv. 5 BEAST MODE ---DANGER!')
temp=int(input('What Information level (Amount of info) to generate at? Choice:'))
def temp1():
    name=['Nancy Simpson','Elliott Wolfe','Hallie Neal','Kane Briggs','Alia Cisneros','Alden Russo','Tinsley Strong','Axl Perry','Clara Yates','Braylon Pugh','Landry Benton','Jamal Vang','Madisyn Wang','Cohen Hammond','Holly Leblanc','Braden Stein','Leilany Lara','Caiden Anthony','Macy Lynch','Zane Schneider','Delaney McCarthy','Devin Macdonald','Rosalia Edwards','Adrian Allen','Riley Blair','Troy Hensley','Malaya Nash','Chandler Lugo','Kaylie Gordon','Karter Woods','Reese Dawson','Iker Khan','Mabel Sims','Brian Gibbs','Carter Espinosa','Khalid Holt','Adelynn Watts','Dakota Dunlap','Iliana Esquivel','Bridger Chen','Valeria Higgins','Sterling Carter','Lucy Mosley','Rayden Tate','Skye Davidson','Dante Friedman','Aspyn Brewer','Cruz Wyatt','Liberty Faulkner','Jabari Paul','Daphne Graham','Giovanni Lugo','Kaylie Swanson','Hugo Arellano','Faye Patterson','Amir Weeks','Karen Quintero','Thatcher Cameron','Julie Schroeder','Izaiah Matthews','Lila Randolph','Eugene Rosales','Kinley McCoy','Jett Costa','Robin Matthews','Preston Patrick','Lyra Arias','Alec Finley','Jovie Jordan','Sawyer Figueroa','Lilith Cochran','Danny Cannon','Noa Blair','Troy Ward','Ariana Reilly','Alvaro Boyd','Georgia Boone','Mauricio Rasmussen','Esperanza Garza','Judah Caldwell','Evelynn Morrow','Kyree Dillon','Laurel Avalos','Coen Herman','Paulina Short','Hezekiah Sloan','Selene Wagner','Enzo Flowers','Ariya Corona','Darian Li','Paige Chan','Frank Bernard','Barbara Huerta','Douglas Douglas','Aniyah Adkins','Kylo Nava','Scout Tapia','Samir Carpenter','Lilly Tyler','Emmitt Vu','Kimora Barr','Harley Russo','Tinsley Kramer','Kylan Hudson','Kamila Cisneros',]
    print('Name: ',random.choice(name))
def temp2():
    name=['Nancy Simpson','Elliott Wolfe','Hallie Neal','Kane Briggs','Alia Cisneros','Alden Russo','Tinsley Strong','Axl Perry','Clara Yates','Braylon Pugh','Landry Benton','Jamal Vang','Madisyn Wang','Cohen Hammond','Holly Leblanc','Braden Stein','Leilany Lara','Caiden Anthony','Macy Lynch','Zane Schneider','Delaney McCarthy','Devin Macdonald','Rosalia Edwards','Adrian Allen','Riley Blair','Troy Hensley','Malaya Nash','Chandler Lugo','Kaylie Gordon','Karter Woods','Reese Dawson','Iker Khan','Mabel Sims','Brian Gibbs','Carter Espinosa','Khalid Holt','Adelynn Watts','Dakota Dunlap','Iliana Esquivel','Bridger Chen','Valeria Higgins','Sterling Carter','Lucy Mosley','Rayden Tate','Skye Davidson','Dante Friedman','Aspyn Brewer','Cruz Wyatt','Liberty Faulkner','Jabari Paul','Daphne Graham','Giovanni Lugo','Kaylie Swanson','Hugo Arellano','Faye Patterson','Amir Weeks','Karen Quintero','Thatcher Cameron','Julie Schroeder','Izaiah Matthews','Lila Randolph','Eugene Rosales','Kinley McCoy','Jett Costa','Robin Matthews','Preston Patrick','Lyra Arias','Alec Finley','Jovie Jordan','Sawyer Figueroa','Lilith Cochran','Danny Cannon','Noa Blair','Troy Ward','Ariana Reilly','Alvaro Boyd','Georgia Boone','Mauricio Rasmussen','Esperanza Garza','Judah Caldwell','Evelynn Morrow','Kyree Dillon','Laurel Avalos','Coen Herman','Paulina Short','Hezekiah Sloan','Selene Wagner','Enzo Flowers','Ariya Corona','Darian Li','Paige Chan','Frank Bernard','Barbara Huerta','Douglas Douglas','Aniyah Adkins','Kylo Nava','Scout Tapia','Samir Carpenter','Lilly Tyler','Emmitt Vu','Kimora Barr','Harley Russo','Tinsley Kramer','Kylan Hudson','Kamila Cisneros',]
    print('Name: ',random.choice(name))
    print('Age: ',random.randint(18,85))
def temp3():
    name=['Nancy Simpson','Elliott Wolfe','Hallie Neal','Kane Briggs','Alia Cisneros','Alden Russo','Tinsley Strong','Axl Perry','Clara Yates','Braylon Pugh','Landry Benton','Jamal Vang','Madisyn Wang','Cohen Hammond','Holly Leblanc','Braden Stein','Leilany Lara','Caiden Anthony','Macy Lynch','Zane Schneider','Delaney McCarthy','Devin Macdonald','Rosalia Edwards','Adrian Allen','Riley Blair','Troy Hensley','Malaya Nash','Chandler Lugo','Kaylie Gordon','Karter Woods','Reese Dawson','Iker Khan','Mabel Sims','Brian Gibbs','Carter Espinosa','Khalid Holt','Adelynn Watts','Dakota Dunlap','Iliana Esquivel','Bridger Chen','Valeria Higgins','Sterling Carter','Lucy Mosley','Rayden Tate','Skye Davidson','Dante Friedman','Aspyn Brewer','Cruz Wyatt','Liberty Faulkner','Jabari Paul','Daphne Graham','Giovanni Lugo','Kaylie Swanson','Hugo Arellano','Faye Patterson','Amir Weeks','Karen Quintero','Thatcher Cameron','Julie Schroeder','Izaiah Matthews','Lila Randolph','Eugene Rosales','Kinley McCoy','Jett Costa','Robin Matthews','Preston Patrick','Lyra Arias','Alec Finley','Jovie Jordan','Sawyer Figueroa','Lilith Cochran','Danny Cannon','Noa Blair','Troy Ward','Ariana Reilly','Alvaro Boyd','Georgia Boone','Mauricio Rasmussen','Esperanza Garza','Judah Caldwell','Evelynn Morrow','Kyree Dillon','Laurel Avalos','Coen Herman','Paulina Short','Hezekiah Sloan','Selene Wagner','Enzo Flowers','Ariya Corona','Darian Li','Paige Chan','Frank Bernard','Barbara Huerta','Douglas Douglas','Aniyah Adkins','Kylo Nava','Scout Tapia','Samir Carpenter','Lilly Tyler','Emmitt Vu','Kimora Barr','Harley Russo','Tinsley Kramer','Kylan Hudson','Kamila Cisneros',]
    address=['015 Dina Manors, Suite 728, 95976-2239, North Wardmouth, Rhode Island, United States','8392 Bauch Drives, Apt. 102, 44086, North Charleneland, Indiana, United States','57254 Hermann Plains, Suite 567, 25362-2942, Hagenesmouth, Washington, United States','144 Weimann Dam, Apt. 125, 59856-6617, Littlechester, Pennsylvania, United States','35565 Citlalli Station, Suite 021, 94597-4288, New Damian, Massachusetts, United States','916 Abdul Groves, Suite 573, 16041-8300, North Maximilian, Arizona, United States','87417 Kunde Bypass, Suite 901, 90383-8093, New Courtney, Michigan, United States','936 Jettie Isle, Apt. 144, 73703, East Raytown, Hawaii, United States','15262 Schimmel Plains, Apt. 814, 42560, Leoland, New York, United States','753 McDermott Club, Suite 314, 98774-2084, Mozelleshire, Wyoming, United States','683 Adelia Place, Apt. 614, 51810, O','Connellside, Minnesota, United States','1573 Travis Shore, Suite 993, 69018', 'OKonland, Indiana, United States','8049 Harvey Plaza, Apt. 917, 32223-5683, Lacybury, Michigan, United States','5268 Garrett Bridge, Apt. 568, 91252-4521, East Evangeline, Nebraska, United States','52032 Antonette Square, Apt. 517, 62156, South Rossiemouth, Minnesota, United States','837 Henderson Forges, Apt. 921, 60251-8344, East Orlandhaven, New Mexico, United States','676 Keebler Estate, Suite 671, 15930-2183, Lake Elsa, Idaho, United States','78917 Pfeffer Rapids, Suite 542, 47933-5406, New Zoratown, Montana, United States','1043 Beahan Trace, Suite 178, 94409, Uptonborough, New York, United States','5844 Kreiger Forges, Suite 532, 79588, Friesenstad, South Dakota, United States','116 Nitzsche Junction, Suite 938, 41056-7159, New Jamilmouth, Wyoming, United States','8936 Kuphal Light, Suite 948, 50751-5608, North Price, South Carolina, United States','76206 Koch Parks, Suite 909, 73120, Rickview, Montana, United States','5092 Feeney Courts, Apt. 705, 86107, Blancheside, Utah, United States','175 Homenick Crossing, Apt. 353, 23020, North Alivia, Oregon, United States','1161 Berge Club, Suite 830, 61683-4188, Port Lewshire, Tennessee, United States','0240 Alycia Park, Apt. 032, 37507-3820, Kreigerville, Massachusetts, United States','51257 Leonardo Plaza, Suite 983, 83229-3023, East Kaileyside, Michigan, United States','27222 Zulauf Crossing, Apt. 628, 33429, Port Horaciomouth, Pennsylvania, United States','473 Randi Overpass, Suite 966, 51534-7527, Barrowstown, Louisiana, United States','845 Neal Island, Apt. 640, 19353, East Kristofer, Arizona, United States','99869 Demario Springs, Apt. 120, 55958-6164, East Alysha, Delaware, United States','8756 Madisyn Village, Suite 883, 78684-9181, Harveystad, South Dakota, United States','07256 Hartmann Gardens, Apt. 260, 75569-9851, Dietrichside, Montana, United States','605 Kirlin Roads, Suite 062, 56606-3700, New Casimir, Vermont, United States','3711 Lehner Avenue, Apt. 546, 93673, West Jay, Maryland, United States','51818 Heidenreich Run, Apt. 219, 38572-1507, West Colebury, Mississippi, United States','7186 Herzog View, Suite 797, 19843-0853, West Anthony, Arkansas, United States','1011 Jennie Plaza, Suite 519, 17197, Nolastad, Alabama, United States','51873 Bridie Highway, Apt. 377, 04154-8725, North Justen, West Virginia, United States','4760 Gibson Overpass, Apt. 138, 85173-3599, Lake Paulmouth, North Carolina, United States','17618 Roberts Bypass, Suite 150, 99690-7771, North Yazmin, Florida, United States','156 Hayes Landing, Suite 479, 69914-7114, Lake Tracey, New Mexico, United States','05938 Maggio Glens, Suite 226, 41698-4882, Stantonstad, Texas, United States','757 Nitzsche Parks, Suite 998, 00516-1815, North Edgardo, Washington, United States','388 Blick Street, Apt. 948, 04981-3441, Johannamouth, Illinois, United States','720 Chadd Plaza, Apt. 041, 33867-5959, New Dina, Wisconsin, United States','37541 Koepp Estates, Apt. 220, 93041-9952, New Price, Pennsylvania, United States','02752 Grant Turnpike, Apt. 270, 02480, Bethelland, New York, United States','022 Oren Creek, Apt. 955, 86889, Kuvalisland, New Mexico, United States',]
    print('Name: ',random.choice(name))
    print('Age: ',random.randint(18,85))
    print('Address: ',random.choice(address))
def temp4():
    emailprovider=['@gmail.com','@hotmail.com','@outlook.com']
    letters=string.ascii_letters
    email1=random.choice(letters)+random.choice(letters)+random.choice(letters)+random.choice(letters)+random.choice(letters)
    email2=random.choice(letters)+random.choice(letters)+random.choice(letters)+random.choice(letters)+random.choice(letters)
    name=['Nancy Simpson','Elliott Wolfe','Hallie Neal','Kane Briggs','Alia Cisneros','Alden Russo','Tinsley Strong','Axl Perry','Clara Yates','Braylon Pugh','Landry Benton','Jamal Vang','Madisyn Wang','Cohen Hammond','Holly Leblanc','Braden Stein','Leilany Lara','Caiden Anthony','Macy Lynch','Zane Schneider','Delaney McCarthy','Devin Macdonald','Rosalia Edwards','Adrian Allen','Riley Blair','Troy Hensley','Malaya Nash','Chandler Lugo','Kaylie Gordon','Karter Woods','Reese Dawson','Iker Khan','Mabel Sims','Brian Gibbs','Carter Espinosa','Khalid Holt','Adelynn Watts','Dakota Dunlap','Iliana Esquivel','Bridger Chen','Valeria Higgins','Sterling Carter','Lucy Mosley','Rayden Tate','Skye Davidson','Dante Friedman','Aspyn Brewer','Cruz Wyatt','Liberty Faulkner','Jabari Paul','Daphne Graham','Giovanni Lugo','Kaylie Swanson','Hugo Arellano','Faye Patterson','Amir Weeks','Karen Quintero','Thatcher Cameron','Julie Schroeder','Izaiah Matthews','Lila Randolph','Eugene Rosales','Kinley McCoy','Jett Costa','Robin Matthews','Preston Patrick','Lyra Arias','Alec Finley','Jovie Jordan','Sawyer Figueroa','Lilith Cochran','Danny Cannon','Noa Blair','Troy Ward','Ariana Reilly','Alvaro Boyd','Georgia Boone','Mauricio Rasmussen','Esperanza Garza','Judah Caldwell','Evelynn Morrow','Kyree Dillon','Laurel Avalos','Coen Herman','Paulina Short','Hezekiah Sloan','Selene Wagner','Enzo Flowers','Ariya Corona','Darian Li','Paige Chan','Frank Bernard','Barbara Huerta','Douglas Douglas','Aniyah Adkins','Kylo Nava','Scout Tapia','Samir Carpenter','Lilly Tyler','Emmitt Vu','Kimora Barr','Harley Russo','Tinsley Kramer','Kylan Hudson','Kamila Cisneros',]
    phnm=random.randint(1000000000,9999999999)
    address=['015 Dina Manors, Suite 728, 95976-2239, North Wardmouth, Rhode Island, United States','8392 Bauch Drives, Apt. 102, 44086, North Charleneland, Indiana, United States','57254 Hermann Plains, Suite 567, 25362-2942, Hagenesmouth, Washington, United States','144 Weimann Dam, Apt. 125, 59856-6617, Littlechester, Pennsylvania, United States','35565 Citlalli Station, Suite 021, 94597-4288, New Damian, Massachusetts, United States','916 Abdul Groves, Suite 573, 16041-8300, North Maximilian, Arizona, United States','87417 Kunde Bypass, Suite 901, 90383-8093, New Courtney, Michigan, United States','936 Jettie Isle, Apt. 144, 73703, East Raytown, Hawaii, United States','15262 Schimmel Plains, Apt. 814, 42560, Leoland, New York, United States','753 McDermott Club, Suite 314, 98774-2084, Mozelleshire, Wyoming, United States','683 Adelia Place, Apt. 614, 51810, O','Connellside, Minnesota, United States','1573 Travis Shore, Suite 993, 69018', 'OKonland, Indiana, United States','8049 Harvey Plaza, Apt. 917, 32223-5683, Lacybury, Michigan, United States','5268 Garrett Bridge, Apt. 568, 91252-4521, East Evangeline, Nebraska, United States','52032 Antonette Square, Apt. 517, 62156, South Rossiemouth, Minnesota, United States','837 Henderson Forges, Apt. 921, 60251-8344, East Orlandhaven, New Mexico, United States','676 Keebler Estate, Suite 671, 15930-2183, Lake Elsa, Idaho, United States','78917 Pfeffer Rapids, Suite 542, 47933-5406, New Zoratown, Montana, United States','1043 Beahan Trace, Suite 178, 94409, Uptonborough, New York, United States','5844 Kreiger Forges, Suite 532, 79588, Friesenstad, South Dakota, United States','116 Nitzsche Junction, Suite 938, 41056-7159, New Jamilmouth, Wyoming, United States','8936 Kuphal Light, Suite 948, 50751-5608, North Price, South Carolina, United States','76206 Koch Parks, Suite 909, 73120, Rickview, Montana, United States','5092 Feeney Courts, Apt. 705, 86107, Blancheside, Utah, United States','175 Homenick Crossing, Apt. 353, 23020, North Alivia, Oregon, United States','1161 Berge Club, Suite 830, 61683-4188, Port Lewshire, Tennessee, United States','0240 Alycia Park, Apt. 032, 37507-3820, Kreigerville, Massachusetts, United States','51257 Leonardo Plaza, Suite 983, 83229-3023, East Kaileyside, Michigan, United States','27222 Zulauf Crossing, Apt. 628, 33429, Port Horaciomouth, Pennsylvania, United States','473 Randi Overpass, Suite 966, 51534-7527, Barrowstown, Louisiana, United States','845 Neal Island, Apt. 640, 19353, East Kristofer, Arizona, United States','99869 Demario Springs, Apt. 120, 55958-6164, East Alysha, Delaware, United States','8756 Madisyn Village, Suite 883, 78684-9181, Harveystad, South Dakota, United States','07256 Hartmann Gardens, Apt. 260, 75569-9851, Dietrichside, Montana, United States','605 Kirlin Roads, Suite 062, 56606-3700, New Casimir, Vermont, United States','3711 Lehner Avenue, Apt. 546, 93673, West Jay, Maryland, United States','51818 Heidenreich Run, Apt. 219, 38572-1507, West Colebury, Mississippi, United States','7186 Herzog View, Suite 797, 19843-0853, West Anthony, Arkansas, United States','1011 Jennie Plaza, Suite 519, 17197, Nolastad, Alabama, United States','51873 Bridie Highway, Apt. 377, 04154-8725, North Justen, West Virginia, United States','4760 Gibson Overpass, Apt. 138, 85173-3599, Lake Paulmouth, North Carolina, United States','17618 Roberts Bypass, Suite 150, 99690-7771, North Yazmin, Florida, United States','156 Hayes Landing, Suite 479, 69914-7114, Lake Tracey, New Mexico, United States','05938 Maggio Glens, Suite 226, 41698-4882, Stantonstad, Texas, United States','757 Nitzsche Parks, Suite 998, 00516-1815, North Edgardo, Washington, United States','388 Blick Street, Apt. 948, 04981-3441, Johannamouth, Illinois, United States','720 Chadd Plaza, Apt. 041, 33867-5959, New Dina, Wisconsin, United States','37541 Koepp Estates, Apt. 220, 93041-9952, New Price, Pennsylvania, United States','02752 Grant Turnpike, Apt. 270, 02480, Bethelland, New York, United States','022 Oren Creek, Apt. 955, 86889, Kuvalisland, New Mexico, United States',]
    print('Name: ',random.choice(name))
    print('Age: ',random.randint(18,85))
    print('Address: ',random.choice(address))
    print('                  ')
    print('Email:',email1,'.',email2,random.choice(emailprovider))
    print('Phone Number:',phnm)
def temp5():
    emailprovider=['@gmail.com','@hotmail.com','@outlook.com']
    letters=string.ascii_letters
    email1=random.choice(letters)+random.choice(letters)+random.choice(letters)+random.choice(letters)+random.choice(letters)
    email2=random.choice(letters)+random.choice(letters)+random.choice(letters)+random.choice(letters)+random.choice(letters)
    name=['Nancy Simpson','Elliott Wolfe','Hallie Neal','Kane Briggs','Alia Cisneros','Alden Russo','Tinsley Strong','Axl Perry','Clara Yates','Braylon Pugh','Landry Benton','Jamal Vang','Madisyn Wang','Cohen Hammond','Holly Leblanc','Braden Stein','Leilany Lara','Caiden Anthony','Macy Lynch','Zane Schneider','Delaney McCarthy','Devin Macdonald','Rosalia Edwards','Adrian Allen','Riley Blair','Troy Hensley','Malaya Nash','Chandler Lugo','Kaylie Gordon','Karter Woods','Reese Dawson','Iker Khan','Mabel Sims','Brian Gibbs','Carter Espinosa','Khalid Holt','Adelynn Watts','Dakota Dunlap','Iliana Esquivel','Bridger Chen','Valeria Higgins','Sterling Carter','Lucy Mosley','Rayden Tate','Skye Davidson','Dante Friedman','Aspyn Brewer','Cruz Wyatt','Liberty Faulkner','Jabari Paul','Daphne Graham','Giovanni Lugo','Kaylie Swanson','Hugo Arellano','Faye Patterson','Amir Weeks','Karen Quintero','Thatcher Cameron','Julie Schroeder','Izaiah Matthews','Lila Randolph','Eugene Rosales','Kinley McCoy','Jett Costa','Robin Matthews','Preston Patrick','Lyra Arias','Alec Finley','Jovie Jordan','Sawyer Figueroa','Lilith Cochran','Danny Cannon','Noa Blair','Troy Ward','Ariana Reilly','Alvaro Boyd','Georgia Boone','Mauricio Rasmussen','Esperanza Garza','Judah Caldwell','Evelynn Morrow','Kyree Dillon','Laurel Avalos','Coen Herman','Paulina Short','Hezekiah Sloan','Selene Wagner','Enzo Flowers','Ariya Corona','Darian Li','Paige Chan','Frank Bernard','Barbara Huerta','Douglas Douglas','Aniyah Adkins','Kylo Nava','Scout Tapia','Samir Carpenter','Lilly Tyler','Emmitt Vu','Kimora Barr','Harley Russo','Tinsley Kramer','Kylan Hudson','Kamila Cisneros',]
    phnm=random.randint(1000000000,9999999999)
    address=['015 Dina Manors, Suite 728, 95976-2239, North Wardmouth, Rhode Island, United States','8392 Bauch Drives, Apt. 102, 44086, North Charleneland, Indiana, United States','57254 Hermann Plains, Suite 567, 25362-2942, Hagenesmouth, Washington, United States','144 Weimann Dam, Apt. 125, 59856-6617, Littlechester, Pennsylvania, United States','35565 Citlalli Station, Suite 021, 94597-4288, New Damian, Massachusetts, United States','916 Abdul Groves, Suite 573, 16041-8300, North Maximilian, Arizona, United States','87417 Kunde Bypass, Suite 901, 90383-8093, New Courtney, Michigan, United States','936 Jettie Isle, Apt. 144, 73703, East Raytown, Hawaii, United States','15262 Schimmel Plains, Apt. 814, 42560, Leoland, New York, United States','753 McDermott Club, Suite 314, 98774-2084, Mozelleshire, Wyoming, United States','683 Adelia Place, Apt. 614, 51810, O','Connellside, Minnesota, United States','1573 Travis Shore, Suite 993, 69018', 'OKonland, Indiana, United States','8049 Harvey Plaza, Apt. 917, 32223-5683, Lacybury, Michigan, United States','5268 Garrett Bridge, Apt. 568, 91252-4521, East Evangeline, Nebraska, United States','52032 Antonette Square, Apt. 517, 62156, South Rossiemouth, Minnesota, United States','837 Henderson Forges, Apt. 921, 60251-8344, East Orlandhaven, New Mexico, United States','676 Keebler Estate, Suite 671, 15930-2183, Lake Elsa, Idaho, United States','78917 Pfeffer Rapids, Suite 542, 47933-5406, New Zoratown, Montana, United States','1043 Beahan Trace, Suite 178, 94409, Uptonborough, New York, United States','5844 Kreiger Forges, Suite 532, 79588, Friesenstad, South Dakota, United States','116 Nitzsche Junction, Suite 938, 41056-7159, New Jamilmouth, Wyoming, United States','8936 Kuphal Light, Suite 948, 50751-5608, North Price, South Carolina, United States','76206 Koch Parks, Suite 909, 73120, Rickview, Montana, United States','5092 Feeney Courts, Apt. 705, 86107, Blancheside, Utah, United States','175 Homenick Crossing, Apt. 353, 23020, North Alivia, Oregon, United States','1161 Berge Club, Suite 830, 61683-4188, Port Lewshire, Tennessee, United States','0240 Alycia Park, Apt. 032, 37507-3820, Kreigerville, Massachusetts, United States','51257 Leonardo Plaza, Suite 983, 83229-3023, East Kaileyside, Michigan, United States','27222 Zulauf Crossing, Apt. 628, 33429, Port Horaciomouth, Pennsylvania, United States','473 Randi Overpass, Suite 966, 51534-7527, Barrowstown, Louisiana, United States','845 Neal Island, Apt. 640, 19353, East Kristofer, Arizona, United States','99869 Demario Springs, Apt. 120, 55958-6164, East Alysha, Delaware, United States','8756 Madisyn Village, Suite 883, 78684-9181, Harveystad, South Dakota, United States','07256 Hartmann Gardens, Apt. 260, 75569-9851, Dietrichside, Montana, United States','605 Kirlin Roads, Suite 062, 56606-3700, New Casimir, Vermont, United States','3711 Lehner Avenue, Apt. 546, 93673, West Jay, Maryland, United States','51818 Heidenreich Run, Apt. 219, 38572-1507, West Colebury, Mississippi, United States','7186 Herzog View, Suite 797, 19843-0853, West Anthony, Arkansas, United States','1011 Jennie Plaza, Suite 519, 17197, Nolastad, Alabama, United States','51873 Bridie Highway, Apt. 377, 04154-8725, North Justen, West Virginia, United States','4760 Gibson Overpass, Apt. 138, 85173-3599, Lake Paulmouth, North Carolina, United States','17618 Roberts Bypass, Suite 150, 99690-7771, North Yazmin, Florida, United States','156 Hayes Landing, Suite 479, 69914-7114, Lake Tracey, New Mexico, United States','05938 Maggio Glens, Suite 226, 41698-4882, Stantonstad, Texas, United States','757 Nitzsche Parks, Suite 998, 00516-1815, North Edgardo, Washington, United States','388 Blick Street, Apt. 948, 04981-3441, Johannamouth, Illinois, United States','720 Chadd Plaza, Apt. 041, 33867-5959, New Dina, Wisconsin, United States','37541 Koepp Estates, Apt. 220, 93041-9952, New Price, Pennsylvania, United States','02752 Grant Turnpike, Apt. 270, 02480, Bethelland, New York, United States','022 Oren Creek, Apt. 955, 86889, Kuvalisland, New Mexico, United States',]
    print('Name: ',random.choice(name))
    print('Age: ',random.randint(18,85))
    print('Address: ',random.choice(address))
    print('                  ')
    print('Credit Card Number: ',random.randint(1000000000000000,9999999999999999))
    print('Expiration Date: ',random.randint(1,12),'/',random.randint(24,28))
    print('CVC: ',random.randint(100,999))
    print('PIN: ',random.randint(1000,9999))
    print('Balance: ',random.randint(300000,20000000),'$')
    print('             ')
    print('SSN: ',random.randint(100000000,999999999))
    print('TIN: ',random.randint(10,99),'-',random.randint(1000000,9999999))
    print('Email:',email1,'.',email2,random.choice(emailprovider))
    print('Phone Number:',phnm)
run=1
regened=0
if(temp==5):
    while(run==1):
        os.system('cls')
        temp5()
        regen=input('Press Enter to regenerate.')
if(temp==4):
    while(run==1):
        os.system('cls')
        temp4()
        regen=input('Press Enter to regenerate.')
if(temp==3):
    while(run==1):
        os.system('cls')
        temp3()
        regen=input('Press Enter to regenerate.')
if(temp==2):
    while(run==1):
        os.system('cls')
        temp2()
        regen=input('Press Enter to regenerate.')
if(temp==1):
    while(run==1):
        os.system('cls')
        temp1()
        regen=input('Press Enter to regenerate.')
if(temp==10):
    print("""      Welcome,""",user,""" to:      
                  
                   BEAST MODE
                   
                   
                 *intense music*""")
    stbstmd=input('Press enter to start BEAST MODE')
    while(run==1):
        os.system('cls')
        temp5()
if(temp==9):
    print("""      Welcome,""",user,""" to:      
                  
                   BEAST MODE
                   
                   
                 *intense music*""")
    stbstmd=input('Press enter to start BEAST MODE')
    while(run==1):
        os.system('cls')
        temp4()
if(temp==8):
    print("""      Welcome,""",user,""" to:      
                  
                   BEAST MODE
                   
                   
                 *intense music*""")
    stbstmd=input('Press enter to start BEAST MODE')
    while(run==1):
        os.system('cls')
        temp3()
if(temp==7):
    print("""      Welcome,""",user,""" to:      
                  
                   BEAST MODE
                   
                   
                 *intense music*""")
    stbstmd=input('Press enter to start BEAST MODE')
    while(run==1):
        os.system('cls')
        temp2()
if(temp==6):
    print("""      Welcome,""",user,""" to:      
                  
                   BEAST MODE
                   
                   
                 *intense music*""")
    stbstmd=input('Press enter to start BEAST MODE')
    while(run==1):
        os.system('cls')
        temp1()
if(temp==99 and passwd=='burgir'):
    while(run==1):
        print('Hi, Admin')
        cmd=input('C:/>')
        if(cmd=='help'):
            print('reboot - Reboots the machine')
            print('return - return to start menu')
            print('cmd - open the Windows command line')
        if(cmd=='reboot'):
            os.system('shutdown /r /t 0')
        if(cmd=='return'):
            adminst()
        if(cmd=='cmd'):
            while(run==1):
                print('Hi, Admin')
                cmd1=input('C:/>')
                os.system(cmd1)