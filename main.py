#SPACELIGHT

#procedurally generated space game where the player can fly to various planets and possibly different systems too.
#each planet will be unique in name, type and other features
#currency of 'credits' that the player can use to upgrade their ship and other things

#name , type , weather , life , rings , discovered , size , listening, age
#0    , 1    , 2       , 3    , 4     , 5          , 6    , 7        , 8

import os
import random as r
import time as t


def cs():
  os.system("clear")


rockTyp = open('rockTyp.txt', 'r')
rockTyp = rockTyp.readlines()
trT = r.choice(rockTyp).strip()
print(trT)

red = '\u001b[31m'
green = '\u001b[32m'
yellow = '\u001b[33m'
blue = '\u001b[34m'
magenta = '\u001b[35m'
cyan = '\u001b[36m'
white = '\u001b[37m'
res = '\u001b[0m'
grey = '\033[1;30;40m'

bold = '\033[1m'
faint = "\033[2m"

newStar = []

instatravel = 0

print(bold + "Loading..." + res)

inventory = []

c = 0
h = 0
he = 0
o = 0
si = 0

cred = 0

log = []
resources = [['Rock', 0], ['Water', 0], ['Soil', 0]]

talk1 = ['We', 'I', 'You', 'They']
talk2 = ['speak', 'turn', 'forget', 'suffer', 'live', 'writhe', 'cry', 'rejoice', 'explore', 'scream', 'sing']
talk3 = ['in harmony', 'together', 'conjoined', 'seperately', 'alone', 'by ourselves']

sizes = [['Small', '∙'], ['Medium', '•'], ['Large', '●'], ['Giant', '⬤']]

ele = ['C', 'H', 'He', 'O', 'Si']

rockColItems = [
    'C',
    'Si',
]

terraColItems = ['C', 'Si', 'H', 'O', 'He']

gasColItems = ['He', 'H']

mineWords = [
    'drill', 'bzz', 'collect', 'brr', 'pick up', 'slash', 'explore', 'find',
    'locate', 'dig', 'extract'
]

colors = [['Red', '\u001b[31m'], ['Green', '\u001b[32m'],
          ['Yellow', '\u001b[33m'], ['Blue', '\u001b[34m'],
          ['White', '\u001b[37m'], ['Cyan', '\u001b[36m']]

planetColors = [
    ['Red', '\u001b[31m'],
    ['Green', '\u001b[32m'],
    ['Yellow', '\u001b[33m'],
    ['Blue', '\u001b[34m'],
    ['Magenta', '\u001b[35m'],
    ['Cyan', '\u001b[36m'],
    ['Red', '\u001b[31m'],
    ['Green', '\u001b[32m'],
]

#corresponding planet colours, i.e. rock is white, ice is cyan - etc
corPC = ['\u001b[37m', '\u001b[36m', '\u001b[31m', '\u001b[32m']

#prefix of planet names
pname_1 = [
    'Gas', 'Temp', 'Eas', 'Log', 'Pass', 'Jak', 'Yrt', 'Zerk', 'Zirk', 'Wok',
    'Wes', 'Blan', 'Kol', 'Barr', 'Krok', 'Huss', 'Hus', 'Zor', 'Plos', 'Erq',
    'Quer', 'Eart', 'N', 'J', 'M', 'Amp', 'Aman', 'Aloir', 'Benad', 'Ben',
    'Opal', 'Barr', 'Vesc', 'Vasc', 'Vap', 'Vapor', 'Cor', 'Cas', 'Covin',
    'Lol', 'Golio', 'Reykjavik'
]
#suffix of planet names
pname_2 = [
    'iant', 'ion', 'ition', 'ikon', 'ikor', 'itiation', 'assio', 'o', '', 'e',
    'ite', 'oron', 'ie', 'opal', 'ocoral', 'otocol', 'asi', 'iez', 'oz',
    'ojis', 'epilo', 'uzi', 'u', 'i', 'oui', 'earth', 'ars', 'upiter',
    'eptune', 'uto', 'emorft', 'anch', 'onch', 'erch'
]

#different types of planets to be discovered
ptype = ['Rock', 'Ice', 'Gas Giant', 'Terrestrial']

#planet ages
ageunits = ['B', 'M', 'K', '']

#list where all planets in the system will be stored
systemPlanets = []

rockiceWeather = ["Exposed", "Barren", "Dusty"]
terraWeather = [
    "Calm", "Windy", "Airy", "Breezy", "Cool", "Warm", "Dusty", "Heavy winds",
    "Paradise"
]
hotWeather = ["Scorching", 'Hot Winds', "Lava Rain", 'Sandstorms']

lifeTypes = ["Plant", "Primordial", "Bacterium", "Primal", "Animalistic"]

#star defining
starColors = ['White', 'Yellow', 'Green', 'Red', 'Blue']
starCol = starColors[r.randint(0, len(starColors) - 1)]

prefix = open("prefix.txt", "r")
prefix = prefix.readlines()
rPrefix = r.choice(prefix)
rPrefix = rPrefix.strip()
print(rPrefix)

suffix = open("suffix.txt", "r")
suffix = suffix.readlines()
rSuffix = r.choice(suffix)
rSuffix = rSuffix.strip()

starName = rPrefix + rSuffix

## next star generation ##

rPrefix = r.choice(prefix)
rPrefix = rPrefix.strip()
print(rPrefix)

rSuffix = r.choice(suffix)
rSuffix = rSuffix.strip()

nextStarName = rPrefix + rSuffix

nextStarCol = starColors[r.randint(0, len(starColors) - 1)]
for i in range(0, len(colors)):
  if colors[i][0] == nextStarCol:
    nextStarTextCol = colors[i][1]


#new planet creation
def planetcreate():
  #list where all new planet data will be stored
  newplanet = []
  #new planet name creation
  rPrefix = r.choice(prefix)
  rPrefix = rPrefix.strip()

  rSuffix = r.choice(suffix)
  rSuffix = rSuffix.strip()

  c_pname = rPrefix + rSuffix

  if r.randint(0, 4) == 0:
    rPrefix = r.choice(prefix)
    rPrefix = rPrefix.strip()

    rSuffix = r.choice(suffix)
    rSuffix = rSuffix.strip()

    c_pname = c_pname + '-' + rPrefix + rSuffix
    if r.randint(0, 4) == 0:
      rPrefix = r.choice(prefix)
      rPrefix = rPrefix.strip()

      rSuffix = r.choice(suffix)
      rSuffix = rSuffix.strip()

      c_pname = c_pname + '-' + rPrefix + rSuffix

  if r.randint(0, 4) == 0:
    rnum = r.randint(65, 90)
    rnum = chr(rnum)
    rnum = rnum + str(r.randint(0, 9))

    c_pname = c_pname + ' ' + rnum

  if r.randint(0, 3) == 1:
    nn = r.randint(1, 9)
    nn = str(nn)
    c_pname = c_pname + '-' + nn
  #elif r.randint(0,3) == 1:
  #let = r.randint(65,90)
  #c_pname = c_pname + ' ' + chr(let)
  newplanet.append(c_pname)

  #print(newplanet)

  #new planet type creation
  rockTyp = open('rockTyp.txt', 'r')
  rockTyp = rockTyp.readlines()

  global iceTyp
  iceTyp = open('iceTyp.txt', 'r')
  iceTyp = iceTyp.readlines()

  global hotTyp
  hotTyp = open('hotTyp.txt', 'r')
  hotTyp = hotTyp.readlines()

  global terraTyp
  terraTyp = open('terraTyp.txt', 'r')
  terraTyp = terraTyp.readlines()
  print(terraTyp)

  global anomTyp
  anomTyp = open('anomTyp.txt', 'r')
  anomTyp = anomTyp.readlines()
  
  if r.randint(0, 1) == 0:
    trT = r.choice(rockTyp)
    c_Ptype = trT
    print(rockTyp)
  elif r.randint(0, 1) == 0:
    trT = r.choice(iceTyp)
    c_Ptype = trT
  elif r.randint(0, 2) == 0:
    print('')
    print('==========')
    print('')
    trT = r.choice(terraTyp)
    print(trT)
    c_Ptype = trT
  elif r.randint(0, 1) == 0:
    trT = r.choice(hotTyp)
    c_Ptype = trT
  elif r.randint(0, 2) == 0:
    trT = r.choice(anomTyp)
    c_Ptype = trT

  else:
    c_Ptype = 'Gas Giant'
  newplanet.append(c_Ptype)

  #print(newplanet)

  #new planet weather decider
  c_plife = 0
  c_plifeType = "None"
  print('---')
  print(c_Ptype)
  print('---')
  print(terraTyp)

  lifeChance = 10
  if c_Ptype == 'Gas Giant':
    c_pweather = "Heavy Winds"
  elif c_Ptype in rockTyp or c_Ptype in iceTyp:
    c_pweather = rockiceWeather[r.randint(0, len(rockiceWeather) - 1)]
    lifeChance -= 1
  elif c_Ptype in terraTyp:
    c_pweather = terraWeather[r.randint(0, len(terraWeather) - 1)]
    lifeChance = 0
    #life decider + type
  elif c_Ptype in hotTyp:
    lifeChance -= 1
    c_pweather = hotWeather[r.randint(0, len(hotWeather) - 1)]
  else:
    c_pweather = "UNKNOWN"
  if r.randint(0, lifeChance) == 0 and c_Ptype != 'Gas Giant':
    c_plife = 1
    c_plifeType = lifeTypes[r.randint(0, len(lifeTypes) - 1)]

  if lifeChance < 1:
    lifeChance = 1

  #print(c_plifeType)
  newplanet.append(c_pweather)
  newplanet.append(c_plifeType)
  #print(newplanet)

  c_pRings = r.randint(0, 3)
  if c_pRings == 1:
    newplanet.append("Yes")
  else:
    newplanet.append("No")
  print(newplanet)

  #the final element will be used to see if the planet has been traveled to
  newplanet.append('0')

  #size
  newplanet.append(r.randint(0, 3))

  #speech
  print(newplanet[3])
  sentence = '/'
  if newplanet[3] == 'Primal' or newplanet[3] == 'Animalistic':
    sentence = ''
    sentence = sentence + talk1[r.randint(0,len(talk1)-1)] + '... '
    sentence = sentence + talk2[r.randint(0,len(talk2)-1)] + '... '
    sentence = sentence + talk3[r.randint(0,len(talk3)-1)] + '... '
    newplanet.append(sentence)
    print('------------------------')
    print(sentence)
  else:
    newplanet.append('/')

  #age
  newage = (r.randint(1,99))
  if r.randint(0,1) == 1:
    newage = newage / r.randint(2,4)
    newage = round(newage,1)
  newplanet.append(str(newage) + ageunits[r.randint(0,len(ageunits)-1)] + ' years')
    

  #record planet in system data
  systemPlanets.append(newplanet)
  print(systemPlanets)



rockTyp = open('rockTyp.txt', 'r')
rockTyp = rockTyp.readlines()

iceTyp = open('iceTyp.txt', 'r')
iceTyp = iceTyp.readlines()

hotTyp = open('hotTyp.txt', 'r')
hotTyp = hotTyp.readlines()

terraTyp = open('terraTyp.txt', 'r')
terraTyp = terraTyp.readlines()

anomTyp = open('anomTyp.txt', 'r')
anomTyp = anomTyp.readlines()

soltem = r.randint(0, 10)

if soltem != 0:
  for i in range(0, r.randint(2, 16)):
    planetcreate()
else:
  starCol = 'Yellow'
  starName = 'Sol'
  
  #
  
  systemPlanets.append(['Neptune', 'Gas Giant', 'Heavy Winds', 'None', 'No', '0', 2, '*heavy winds*', '4.6B years'])
  systemPlanets.append(['Saturn', 'Gas Giant', 'Heavy Winds', 'None', 'Yes', '0', 2, '*turning rings*', '4.6B years'])
  systemPlanets.append(['Mars', 'Rock\n', 'Barren', 'None', 'No', '0', 0, '*crumbling rocks*', '4.6B years'])
  systemPlanets.append(['Venus', 'Scorched\n', 'Radioactive', 'None', 'No', '0', 1, '*bubbling', '4.6B years'])
  systemPlanets.append(['Mercury', 'Rock\n', 'Dusted', 'None', 'No', '0', 0, '*slow scorching*', '4.6B years'])
  systemPlanets.append(['Earth', 'Terrestrial\n', 'Paradise', 'Primal', 'No', '0', 1, '*roars and growls*', '4.6B years'])
  systemPlanets.append(['Jupiter', 'Gas Giant', 'Heavy Winds', 'None', 'No', '0', 3, '*hurling storm*', '4.6B years'])
  systemPlanets.append(['Uranus', 'Gas Giant', 'Heavy Winds', 'None', 'No', '0', 2, '*slow turning*', '4.6B years'])

print(systemPlanets)

planetNames = []
lower_planetNames = []

for i in range(0, len(systemPlanets)):
  planetNames.append(systemPlanets[i][0])

for i in range(0, len(systemPlanets)):
  lower_planetNames.append(systemPlanets[i][0].lower())

global sName
sName = pname_1[r.randint(0,
                          len(pname_1) - 1)] + pname_2[r.randint(
                              0,
                              len(pname_2) - 1)]
temp = r.randint(1, 9999)
temp = str(temp)
sName = sName + "-" + temp

print(sName)

print("\n---\n===\n---")

print("")
#print("System " + starName + ", " + starCol.lower() + ' star')

#for i in range (0,len(systemPlanets)):
#print("")
#print("Planet " + systemPlanets[i][0])
#print("Type: " + systemPlanets[i][1])
#print("Weather: " + systemPlanets[i][2])
#print("Life: " + systemPlanets[i][3])
#print("Rings: " + systemPlanets[i][4])

cs()

colChance = 2

for i in range(0, len(colors)):
  if colors[i][0] == starCol:
    starTextCol = colors[i][1]

#
#
#
#ship creation


def systemView():
  global solarSystem

  for i in range(0, len(colors)):
    if colors[i][0] == starCol:
      starTextCol = colors[i][1]

  solarSystem = ''

  side = r.randint(0, 1)
  for i in range(0, len(systemPlanets) // 2):
    if side == 0:
      side = 1
    elif side == 1:
      side = 0

    if systemPlanets[i][1] in iceTyp:
      pct2 = blue
    elif systemPlanets[i][1] in terraTyp:
      pct2 = green
    elif systemPlanets[i][1] in rockTyp:
      pct2 = white
    elif systemPlanets[i][1] in hotTyp:
      pct2 = red
    elif systemPlanets[i][1] in anomTyp:
      pct2 = magenta
    else:
      pct2 = yellow

    img = sizes[systemPlanets[i][6]][1]
    sp = ''
    ln = 0
    if side == 1:
      for i in range(0, len(systemPlanets) // 2):
        sp += '  '
        ln += 1

    while r.randint(0, 2) != 0 and ln != len(systemPlanets):
      sp += '  '
      ln += 1

    if systemPlanets[i][4] == 'No':
      ring = ''
    else:
      ring = '-'
    print(sp + pct2 + img)
    solarSystem += ('\n' + sp + pct2 + ring + img + ring)

  sp = ''
  for i in range(0, len(systemPlanets) // 2):
    sp += '  '
  print(starTextCol + sp + '⬤')
  solarSystem += ('\n\n' + starTextCol + sp + '〄' + '\n')

  for i in range(len(systemPlanets) // 2, len(systemPlanets)):
    if side == 0:
      side = 1
    elif side == 1:
      side = 0
    if systemPlanets[i][1] in iceTyp:
      pct2 = blue
    elif systemPlanets[i][1] in terraTyp:
      pct2 = green
    elif systemPlanets[i][1] in rockTyp:
      pct2 = white
    elif systemPlanets[i][1] in hotTyp:
      pct2 = red
    else:
      pct2 = yellow

    img = sizes[systemPlanets[i][6]][1]
    sp = ''
    ln = 0

    if side == 1:
      for i in range(0, len(systemPlanets) // 2):
        sp += '  '
        ln += 1
    while r.randint(0, 2) != 0 and ln != len(systemPlanets):
      sp += '  '
      ln += 1
    if systemPlanets[i][4] == 'No':
      ring = ''
    else:
      ring = '-'
    print(sp + pct2 + img)
    solarSystem += ('\n' + sp + pct2 + ring + img + ring)

  print('\n---\n')
  print(solarSystem)


def newSys():
  global stName
  systemPlanets.clear()
  for i in range(0, r.randint(2, 16)):
    planetcreate()
  rPrefix = r.choice(prefix)
  rPrefix = rPrefix.strip()
  print(rPrefix)

  rSuffix = r.choice(suffix)
  rSuffix = rSuffix.strip()

  global nextStarName
  global starName
  starName = nextStarName
  
  newStar.clear()
  newStar.append(nextStarName)

  global nextStarCol
  global starCol
  starCol = nextStarCol

  ## next star generation ##
  
  rPrefix = r.choice(prefix)
  rPrefix = rPrefix.strip()
  print(rPrefix)

  rSuffix = r.choice(suffix)
  rSuffix = rSuffix.strip()

  nextStarName = rPrefix + rSuffix


  nextStarCol = starColors[r.randint(0, len(starColors) - 1)]

  global nextStarTextCol
  for i in range(0, len(colors)):
    if colors[i][0] == nextStarCol:
      nextStarTextCol = colors[i][1]

  print(nextStarTextCol)
  
  lower_planetNames.clear()

  for i in range (len(systemPlanets)):
    lower_planetNames.append(
      systemPlanets[i][0].lower())
  
  cs()


def landMoreOp(planet, pno, pct2):
  cs()
  print("Stationed on " + bold + planet + res + ' // MORE OPTIONS')
  print(blue + 'R' + str(resources[0][1]) +
     ' / W' + str(resources[1][1]) +
     ' / S' + str(resources[2][1])) 
  print("")

  print(bold + red + "[enter]" + res + " to go back")
  print(bold + cyan + "[1]" + res + " Listen")
  print(bold + magenta + "[2]" + res + " Take sample")
  print(bold + green + "[3]" + res + " Harvest")

  print(res + "")
  sel = input("> ")

  if sel == '':
    cs()
    landed(planet)
  elif sel == '1':
    cs()
    print('Listening...')
    t.sleep(r.randint(1,3))
    if systemPlanets[pno][7] == '/':
      print(red + 'Silence...' + res)
      t.sleep(1.5)
      cs()
      landMoreOp(planet,pno, pct2)
    else:
      print('"' + green + systemPlanets[pno][7] + res + '"')
      t.sleep(3)
      cs()
      landMoreOp(planet,pno,pct2)
    
  elif sel == "2":
    cs()
    print(bold + 'Taking sample...' + res)
    if systemPlanets[pno][1] in rockTyp:
      newsamp = (bold + systemPlanets[pno][0] + res + ' Rock Sample')
      resources[0][1] += r.randint(1,2)
    elif systemPlanets[pno][1] in iceTyp:
      newsamp = (bold + blue + systemPlanets[pno][0] + res + ' Ice Sample')
      resources[0][1] += r.randint(0,1)
      resources[1][1] += r.randint(1,2)
    elif systemPlanets[pno][1] in terraTyp:
      resources[0][1] += r.randint(1,2)
      resources[1][1] += r.randint(1,2)
      resources[2][1] += r.randint(1,2)
      if systemPlanets[pno][3] == 'Plant':
        newsamp = (bold + green + systemPlanets[pno][0] + res + ' Plant Sample')
        resources[2][1] += r.randint(1)
      elif systemPlanets[pno][3] == 'Animalistic' or systemPlanets[pno][3] == 'Primal':
        newsamp = (bold + green + systemPlanets[pno][0] + res + ' Living Tissue Sample')
      elif systemPlanets[pno][3] == 'Primordial':
        newsamp = (bold + green + systemPlanets[pno][0] + res + ' Bacterium Sample')
      else:
         newsamp = (bold + green + systemPlanets[pno][0] + res + ' Unknown Terra Sample')
    elif systemPlanets[pno][1] in hotTyp:
      newsamp = (bold + red + systemPlanets[pno][0] + res + ' Molten Sample')
      resources[0][1] += r.randint(2,4)
    elif systemPlanets[pno][1] == 'Gas Giant':
      newsamp = (bold + red + systemPlanets[pno][0] + res + ' Gaseous Sample')
      resources[1][1] += r.randint(0,2)
    else:
      newsamp = (bold + magenta + systemPlanets[pno][0] + res + ' Unknown Sample')
      resources[0][1] += r.randint(0,3)
      resources[1][1] += r.randint(0,3)
      resources[2][1] += r.randint(0,3)
    inventory.append(newsamp)
    t.sleep(r.randint(2,3))
    print(newsamp + res + ' collected.')
    log.insert(0, "Took a " + magenta + "sample" + res + " from " + bold + pct2 + planet + res)
    t.sleep(2)
    landMoreOp(planet,pno,pct2)

  elif sel == '3':
    a = 0
    b = 0
    c = 0
    cs()
    print(bold + 'Harvesting...' + res)
    if systemPlanets[pno][1] in rockTyp:
      a = r.randint(1,2)
      resources[0][1] += a
    elif systemPlanets[pno][1] in iceTyp:
      a = r.randint(0,1)
      b = r.randint(1,2)
      resources[0][1] += a
      resources[1][1] += b
    elif systemPlanets[pno][1] in terraTyp:
      a = r.randint(1,2)
      b = r.randint(1,2)
      c = r.randint(1,2)
      resources[0][1] += a
      resources[1][1] += b
      resources[2][1] += c
      if systemPlanets[pno][3] == 'Plant':
        resources[2][1] += 1
    elif systemPlanets[pno][1] in hotTyp:
      a = r.randint(2,4)
      resources[0][1] += a
    elif systemPlanets[pno][1] == 'Gas Giant':
      b = r.randint(0,2)
      resources[1][1] += b
    else:
      a = r.randint(0,3)
      b = r.randint(0,3)
      c = r.randint(0,3)
      resources[0][1] += a
      resources[1][1] += b
      resources[2][1] += c
    t.sleep(r.randint(1,3))
    print(green + '+ R' + str(a) +
         ' / W' + str(b) +
         ' / S' + str(c) + res)
    print('')
    print(blue + '> R' + str(resources[0][1]) +
     ' / W' + str(resources[1][1]) +
     ' / S' + str(resources[2][1]) + res)
    t.sleep(2)
    landMoreOp(planet,pno,pct2)
    
  
  elif sel == '234532':
    prevCol = 0
    typ = ''
    if systemPlanets[pno][1] == "Rock" or systemPlanets[pno][1] == "Ice":
      resTyp = 1
    elif systemPlanets[pno][1] == "Terrestrial":
      resTyp = 2
    else:
      resTyp = 3
      prevCol = 0

    while typ != '0':
      cs()
      if prevCol == 1:
        print("Collected " + bold + magenta + inventory[len(inventory) - 1] +
              res)
      else:
        print("Collected " + bold + red + "nothing" + res)
      print("Collecting resources on " + cyan + systemPlanets[pno][1] + res +
            " planet " + bold + planet + res)

      print("")
      word = mineWords[r.randint(0, len(mineWords) - 1)]
      print("Type " + magenta + word + res)
      typ = input("> " + magenta)
      if typ == word:
        if r.randint(0, colChance) == 0:
          prevCol = 1
          if resTyp == 1:
            nCol = rockColItems[r.randint(0, len(rockColItems) - 1)]
          elif resTyp == 2:
            nCol = terraColItems[r.randint(0, len(terraColItems) - 1)]
          elif resTyp == 3:
            nCol = gasColItems[r.randint(0, len(gasColItems) - 1)]
          inventory.append(nCol)
        else:
          prevCol = 0

      print(res)
    cs()
    landMoreOp(planet, pno, pct2)

  else:
    cs()
    landMoreOp(planet, pno, pct2)


#when the ship is stationed on a planet
def landed(planet):
  global cred
  #165-167 defines what position the planet is in the list.
  for i in range(0, len(systemPlanets)):
    if systemPlanets[i][0] == planet:
      pno = i
      break

  if systemPlanets[pno][1] in iceTyp:
    pct2 = blue
  elif systemPlanets[pno][1] in terraTyp:
    pct2 = green
  elif systemPlanets[pno][1] in rockTyp:
    pct2 = white
  elif systemPlanets[pno][1] in hotTyp:
    pct2 = red
  elif systemPlanets[pno][1] == 'Gas Giant':
    pct2 = yellow
  else:
    pct2 = magenta

  psize = sizes[systemPlanets[pno][6]][0]

  if systemPlanets[pno][4] == 'No':
    print("Stationed on " + bold + planet + res + ' // ' + pct2 +
          sizes[systemPlanets[pno][6]][1] + res)
  else:
    print("Stationed on " + bold + planet + res + ' // ' + '-' + pct2 +
          sizes[systemPlanets[pno][6]][1] + res + '-')
  print("")

  print(bold + red + "[enter]" + res + " Leave")

  if systemPlanets[pno][5] == 1:
    print(grey + "[1] Scan" + res)
  else:
    print(bold + cyan + "[1]" + res + " Scan")

  if systemPlanets[pno][5] == 1:
    print(bold + cyan + "[2]" + res + " Planet data")
    print(bold + cyan + "[3]" + res + " More options")
  else:
    print(grey + "[2] Planet data")
    print(grey + "[3] More options")

  print(res + "")
  sel = input("> ")

  #scan planet
  if sel == '1':
    cs()
    if systemPlanets[pno][5] == 1:
      landed(planet)
    else:
      #define current planet as 'explored'
      print("Scanning " + bold + planet + res + "...")
      t.sleep(r.randint(2, 4))
      for i in range(0, len(systemPlanets)):
        if systemPlanets[i][0] == planet:
          systemPlanets[i][5] = 1
      print(bold + cyan + "Scan complete!" + res)
      log.insert(0, cyan + "Scanned " + res + bold + pct2 + planet + res)
      ncred = r.randint(1, 10)
      t_ncred = str(ncred)
      print("+ " + yellow + bold + t_ncred + "c" + res)
      cred += ncred
      t.sleep(2)
      cs()
      landed(planet)

  #view planet data
  elif sel == '2':
    if systemPlanets[pno][5] == 1:
      cs()
      #print(systemPlanets[pno][5])
      print("[enter] to go back")
      print("")
      print("Name: " + bold + systemPlanets[pno][0] + res)
      print("Type: " + bold + cyan + systemPlanets[pno][1].strip() + res)
      print("Weather: " + bold + magenta + systemPlanets[pno][2] + res)
      print("Life: " + bold + green + systemPlanets[pno][3] + res)
      print("Rings: " + bold + red + systemPlanets[pno][4] + res)
      print("Size: " + bold + yellow + psize + res)
      print("Age: " + bold + cyan + systemPlanets[pno][8] + res)

      input("> ")
      cs()
      landed(planet)
    else:
      print("You must scan this planet first.")
      t.sleep(2)
      cs()
      landed(planet)

  #leave planet
  elif sel == '':
    cs()
    if instatravel == 0:
      print("Traveling to " + bold + cyan + 'Space' + res + "...")
      t.sleep(r.randint(1, 3))
      cs()
    if advSynths[1][4] == True:
      fuels[0][4] += r.randint(0,1)
    travel()

  #more options for the planet
  elif sel == '3':
    if systemPlanets[pno][5] == 1:
      cs()
      landMoreOp(planet, pno, pct2)

    else:
      print("You must scan this planet first.")
      t.sleep(2)
      cs()
      landed(planet)

  else:
    cs()
    landed(planet)


def go(planet):
  for i in range(0, len(systemPlanets)):
    if lower_planetNames[i] == planet:
      planet = systemPlanets[i][0]
  
  for i in range(0, len(systemPlanets)):
    if systemPlanets[i][0] == planet:
      pno = i
      break

  if systemPlanets[pno][1] in iceTyp:
    pct2 = blue
  elif systemPlanets[pno][1] in terraTyp:
    pct2 = green
  elif systemPlanets[pno][1] in rockTyp:
    pct2 = white
  elif systemPlanets[pno][1] in hotTyp:
    pct2 = red
  else:
    pct2 = yellow
  
  print("Traveling to " + bold + planet + res + "...")
  if instatravel == 0:
    t.sleep(r.randint(1, 3))
  if advSynths[1][4] == True:
      fuels[0][4] += r.randint(0,1)

  cs()
  log.insert(0, "Landed on " + bold + pct2 + planet + res)
  landed(planet)


#travel selection
def travel():
  print(cyan + '[enter]' + res + ' to go back')
  print("")
  for i in range(0, len(systemPlanets)):
    pct = white
    bold2 = faint

    if systemPlanets[i][5] == 1:
      pct = white
      bold2 = bold

    if systemPlanets[i][1] in iceTyp:
      pct2 = blue
    elif systemPlanets[i][1] in terraTyp:
      pct2 = green
    elif systemPlanets[i][1] in rockTyp:
      pct2 = white
    elif systemPlanets[i][1] in hotTyp:
      pct2 = red
    elif systemPlanets[i][1] in anomTyp:
      pct2 = magenta
    else:
      pct2 = yellow

    print(pct + bold2 + pct2 + systemPlanets[i][0] + res)

  print(res + "")
  sel = input("> ")

  if sel == '':
    cs()
    menu(solarSystem)
  elif sel.lower() in lower_planetNames:
    cs()
    go(sel)
  else:
    cs()
    travel()

# synthesisation #

# # name, rock, water, soil, built?
advSynths = [['Hyperdrive', 3, 0, 0], ['Motion Fueller', 3, 5, 0]]
for i in range(0,len(advSynths)):
  advSynths[i].append(False)

def synthAdv():
  print(magenta + '-- Advanced Synthesisation --')
  print('')
  for i in range (0,len(resources)):
    print(blue + resources[i][0] + ':' , resources[i][1])

  print('')
  for i in range(0,len(advSynths)):
    if advSynths[i][4] == False:
      print(res + magenta + advSynths[i][0] + ' >')
      print('  > ' + 'R' + str(advSynths[i][1]) + ' / '
            + 'W' + str(advSynths[i][2]) + ' / '
           + 'S' + str(advSynths[i][3]))
      print('')
    else:
      print(res + grey + green + advSynths[i][0] + ' >')
      print('(built)')
      print('')

  sel = input(res + '> ')

  check = 0

  #EXPLANATION FOR THIS HORRIBLE CODE
  #first line goes through all the synths
  ##if sel is equal to the name of the synth, it is now selected
  ###third line checks if the synth is built
  ####fourth line goes through all the player's resources
  #####fifth line checks if the player's count of that resource is more than or equal to the amount required by the synth, the 'check' variable goes up by one
  #######the seventh line checks if all checks are in order. if not, the player cannot craft it.
  #########if the check is equal to three, the ninth line takes off the resources
  ##########the tenth line creates the synth (sets built to true)
  if sel == '':
    cs()
    synth()
  for i in range(0,len(advSynths)):
    if sel.lower() == advSynths[i][0].lower():
      if advSynths[i][4] == False:
        for a in range (0,len(resources)):
          if resources[a][1] >= advSynths[i][a+1]:
            check += 1
        if check == 3:
          for a in range (0,len(resources)):
            resources[a][1] -= advSynths[i][a+1]
          advSynths[i][4] = True
        else:
          cs()
          synthAdv()
      else:
        cs()
        synthAdv()
  cs()
  synthAdv()
    
fuels = [['Hyperfuel', 0, 2, 0,]]
for i in range(0,len(fuels)):
  fuels[i].append(0)

def synthBase():
  print(cyan + '-- Basic Synthesisation --')
  print('')
  for i in range (0,len(resources)):
    print(blue + resources[i][0] + ':' , resources[i][1])

  print('')
  for i in range(0,len(fuels)):
    print(res + cyan + fuels[i][0] + ' (' + str(fuels[i][4]) + ') >')
    print('  > ' + 'R' + str(fuels[i][1]) + ' / '
            + 'W' + str(fuels[i][2]) + ' / '
           + 'S' + str(fuels[i][3]))
    print('')

  sel = input(res + '> ')

  check = 0

  #FOR EXPLANATION, LOOK AT synthAdv()
  if sel == '':
    cs()
    synth()
  for i in range(0,len(fuels)):
    if sel.lower() == fuels[i][0].lower():
      for a in range (0,len(resources)):
        if resources[a][1] >= fuels[i][a+1]:
          check += 1
      if check == 3:
        for a in range (0,len(resources)):
          resources[a][1] -= fuels[i][a+1]
        fuels[i][4] += 1
      else:
        cs()
        synthBase()
  cs()
  synthBase()
  

def synth():
  cs()
  print(yellow + '-- Synthesise --')
  print('')
  for i in range (0,len(resources)):
    print(blue + resources[i][0] + ':' , resources[i][1])

  print('')
  print(res + bold + '[1]' + res + ' Base Resources')
  print(bold + magenta + '[2]' + res + magenta + ' Advanced Synthesisation')


  sel = input(res + '\n> ')

  if sel == '':
    cs()
    menu(solarSystem)
  elif sel == '1':
    cs()
    synthBase()
  elif sel == '2':
    cs()
    synthAdv()
  else:
    cs()
    synth()
  
##

#ship settings
def ship(sName):
  global cred
  global instatravel
  print("Ship " + bold + cyan + sName + res)
  t_cred = str(cred)
  print(yellow + bold + t_cred + "c" + res)
  print("")
  print(bold + red + "[enter]" + res + ' to go back')
  print(bold + cyan + "[1]" + res + " Inventory")
  print(bold + cyan + "[2]" + res + " Upgrades")
  #print(bold + cyan + "[R]" + res + " Rename")

  sel = input("> ")

  if sel == '':
    cs()
    menu(solarSystem)
  elif sel.lower() == 'r':
    cs()
    print("Renaming Ship " + bold + cyan + sName + res)
    print("")
    sName = input("Rename to: " + bold + red)
    print(res)
    cs()
    ship(sName)
  elif sel == '1':
    cs()
    print(cyan + bold + '[enter]' + res + ' to go back')
    print('')
    if len(inventory) == 0:
      print(red + 'Your inventory is empty.')
    else:
      for i in range (len(inventory)):
        print(inventory[i])
    print('')
    input('> ')
    cs()
    ship(sName)

  elif sel == '2':
    cs()
    print(red + bold + '--= UPGRADES =--' + res)
    print(yellow + bold + str(cred) + "c" + res)
    print(red + bold + '[enter]' + res + ' to go back')
    print('')
    if instatravel == 0:
      tempcol = blue
    else:
      tempcol = grey
    print(tempcol + bold + "[INSTATRAVEL] 10c" + res +
          " - Instantly travel to any planet. Overpowered warp drive.")
    print(cyan + bold + "[INSTASCAN] 10c" + res +
          " - Instantly scan any planet. Super holograms.")

    print("")
    sel = input("> ")

    if sel == "":
      cs()
      ship(sName)
    elif sel.lower() == "instatravel":
      if cred >= 10:
        cred -= 10
        instatravel = 1
      cs()
      ship(sName)

def logShow():
  print(magenta + '-- Log --' + res)
  print('')
  if len(log) == 0:
    print(red + "You haven't done anything yet." + res)
  else:
    for i in range(0, len(log)):
      print(log[i])
  print('')
  input('> ')
  cs()
  menu(solarSystem)

z = ''

def randText():
  global z
  ab = ''
  for i in range (12):
    for i in range (1,r.randint(1,10)):
      z = r.randint(33,126)
      z = chr(z)
      col = planetColors[r.randint(0,len(planetColors)-1)][1]
      z = col + z
      print(ab + z)
      t.sleep(0.01)
      cs()
    ab += z
    print(ab)
  cs()
  ab = ''
  for i in range (12):
    cs()
    z = r.randint(33,126)
    z = chr(z)
    col = planetColors[r.randint(0,len(planetColors)-1)][1]
    z = col + z
    ab += z
    print(ab)
    t.sleep(0.01)
  cs()
  print(ab)

def sysMoreOp():
  cs()
  print(solarSystem)
  print('')
  print(res + "-- System " + bold + starTextCol + starName + res + ' --')
  print(red + '[enter]' + res + ' to go back')
  print('')
  print(blue + "[1]" + res + " System Data")
  #print(cyan + "[2]" + res + " Space-harvest")

  sel = input('\n> ')

  if sel == '':
    cs()
    menu(solarSystem)
  if sel == '1':
    cs()
    print(bold + starTextCol + starName + res + ' Data')
    print('')
    print(green + str(len(systemPlanets)) + res + ' Planets')
    input('\n> ')
    cs()
    sysMoreOp()
  else:
    cs()
    sysMoreOp()

def newSysLoad():
  menu(solarSystem)

def menu(solarSystem):
  print(solarSystem)
  print('')
  for i in range(0, len(colors)):
    if colors[i][0] == starCol:
      starTextCol = colors[i][1]
  print(res + "-- System " + bold + starTextCol + starName + res + ' --')
  print("")
  print(blue + "[1]" + res + " Travel")
  print(cyan + "[2]" + res + " Ship")
  print(blue + "[3]" + res + " Synthesise")
  print(cyan + "[4]" + res + " More options")
  if advSynths[0][4] == False:
    print(grey + "[T] Warp to another system")
    print(grey + '(synthesise a' + magenta + ' hyperdrive' + res + grey + ')' + res)
  else:
    print(green + "[T]" + res + " Warp to another system" + res)
  print(magenta + "[L]" + res + " Log")
  print('')
  #print(magenta + bold + '[T]' + res + ' Travel to a new system')

  print("")
  sel = input("> ")

  if sel == '1':
    cs()
    travel()
  elif sel == '2':
    cs()
    ship(sName)
  elif sel.lower() == 't':
    if advSynths[0][4] == False:
      cs()
      menu(solarSystem)
    cs()

    
    print(res + 'Preparing to travel to ' + bold + nextStarTextCol + nextStarName + res + '.')
    t.sleep(0.5)
    print(red + 'You will be ' + grey + 'unable' + res + red + ' to return.' + res)
    t.sleep(0.5)
    if fuels[0][4] == 0:
      print(grey + 'You need hyperdrive fuel.' + res)
    else:
      print('Please type out the name of the next star to warp.')

    
    sel = input('\n> ')
    if sel.lower() == nextStarName.lower() and fuels[0][4] >= 1:
      fuels[0][4] -= 1
      cs()
      newSys()
      stName = newStar[0]
      systemView()
      cs()
      t.sleep(0.25)
      randText()
      print(magenta + '↑ ACCELERATE ↑' + res)
      t.sleep(0.5)
      randText()
      print(cyan + '→ MAINTAINING →' + res)
      t.sleep(0.5)
      randText()
      print(red + '↓ DECELLERATE ↓' + res)
      t.sleep(0.5)
      randText()
      cs()
      log.insert(0, res + '-')
      log.insert(0, 'Traveled to '+ bold + starTextCol + starName + res)
      systemView()
      cs()
      newSysLoad()
    else:
      cs()
      menu(solarSystem)
  elif sel.lower() == '3':
    cs()
    synth()
  elif sel.lower() == '4':
    sysMoreOp()
  elif sel.lower() == 'l':
    cs()
    logShow()
  elif sel == 'w':
    print(systemPlanets)
  else:
    cs()
    menu(solarSystem)


systemView()
print(systemPlanets)
cs()
log.insert(0, 'Traveled to '+ bold + starTextCol + starName + res)
menu(solarSystem)