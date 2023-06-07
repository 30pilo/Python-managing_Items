def SelectPage():
  print("\nChoose one topic\n")
  print("1. Get items")
  print("2. Send Items")
  print("3. See Items")
  print("4. Check Items fewer than 25")
  print("5. Search item distribution")
  print("6. Exit program")
  print("----------")
  select = input("Your choice this : ")
  return select

#Initial Inventory Creation

def inventory():
  with open("ppe.txt","w") as fileread :
    print(fileread())
  inventory = [["HC","Head Cover","s1",100],
               ["FS","Face Shield","s1",100],
               ["MS","Mask","s2",100],
               ["GL","Gloves","s2",100],
               ["GW","Gown","s3",100],
               ["SC","Shoe Covers","s3",100]]

#Item Inventory Update

def supplierinfo():
  with open("suppliers.txt","w") as fh :
    print(fh())
  supplierinfo = [["s1","amazon","USA","Head Cover and Face Shield"],
                  ["s2","rakuten","Japan","Mask and Glove"],
                  ["s3","Lazada","Malaysia","Gown and Shoe Cover"]]

def hospitalinfo():
  with open("hospital.txt","w") as f :
    print(f())
  hospitalinfo = [["h1","Seoul Hospital","Korea"],
                  ["h2","Tokyo Hospital","Japan"],
                  ["h3","KL Hospital","Malaysia"]]

def distributioninfo():
  with open("distribution.txt","w") as ff:
    print(ff())
  distributioninfo = {'HC':{1:'0',2:'0',3:'0'},
                      'FS':{1:'0',2:'0',3:'0'},
                      'MS':{1:'0',2:'0',3:'0'},
                      'GL':{1:'0',2:'0',3:'0'},
                      'GW':{1:'0',2:'0',3:'0'},
                      'SC':{1:'0',2:'0',3:'0'}}

#when I get items

def if_get(inventory):
  select = input("Which item do you get?: HC,FS,MS,GL,GW,SC: ")
  amount = input("How many boxes do you get?: ")
  if select == "HC" or "FS" or "MS" or "GL" or "GW" or  "SC":
    if select == "HC":
      inventory[0][3] = inventory[0][3] + amount
    elif select == "FS":
       inventory[1][3] = inventory[1][3] + amount
    elif select == "MS":
       inventory[2][3] = inventory[2][3] + amount
    elif select == "GL":
       inventory[3][3] = inventory[3][3] + amount
    elif select == "GW":
       inventory[4][3] = inventory[4][3] + amount
    elif select == "SC":
        inventory[5][3] = inventory[5][3] + amount
  else:
      print("That value is not acceptable")

#when I send items
def if_send(inventory):
  select = input("Which item do you send?: HC,FS,MS,GL,GW,SC: ")
  amount = input("How many boxes do you get?: ")
  hospital = input("Which hospital?: H1,H2,H3: ")
  if select == "HC" and hospital == "H1" or "H2" or "H3":
    if inventory[0][3] <  amount:
      print("You can't distribute")
    else:
      inventory[0][3] = inventory[0][3] - amount
      if hospital == "H1":
        distributioninfo[0][1] = distributioninfo[0][1] + amount
      elif hospital == "H2":
         distributioninfo[0][2] = distributioninfo[0][2] + amount
      elif hospital == "H3":
         distributioninfo[0][3] = distributioninfo[0][3] + amount
  elif select == "FS" and hospital == "H1" or "H2" or "H3":   
    if inventory[2][3] <  amount:
      print("You can't distribute")
    else:
      inventory[1][3] = inventory[1][3] - amount
      if hospital == "H1":
        distributioninfo[1][1] = distributioninfo[1][1] + amount
      elif hospital == "H2":
         distributioninfo[1][2] = distributioninfo[1][2] + amount
      elif hospital == "H3":
         distributioninfo[1][3] = distributioninfo[1][3] + amount
  elif select == "MS" and hospital == "H1" or "H2" or "H3":   
    if inventory[2][3] <  amount:
      print("You can't distribute")
    else:
      inventory[2][3] = inventory[2][3] - amount
      if hospital == "H1":
        distributioninfo[2][1] = distributioninfo[2][1] + amount
      elif hospital == "H2":
         distributioninfo[2][2] = distributioninfo[2][2] + amount
      elif hospital == "H3":
         distributioninfo[2][3] = distributioninfo[2][3] + amount
  elif select == "GL" and hospital == "H1" or "H2" or "H3":   
    if inventory[3][3] <  amount:
      print("You can't distribute")
    else:
      inventory[3][3] = inventory[3][3] - amount
      if hospital == "H1":
        distributioninfo[3][1] = distributioninfo[3][1] + amount
      elif hospital == "H2":
         distributioninfo[3][2] = distributioninfo[3][2] + amount
      elif hospital == "H3":
         distributioninfo[3][3] = distributioninfo[3][3] + amount
  elif select == "GW" and hospital == "H1" or "H2" or "H3":   
    if inventory[4][3] <  amount:
      print("You can't distribute")
    else:
      inventory[4][3] = inventory[4][3] - amount
      if hospital == "H1":
        distributioninfo[4][1] = distributioninfo[4][1] + amount
      elif hospital == "H2":
         distributioninfo[4][2] = distributioninfo[4][2] + amount
      elif hospital == "H3":
         distributioninfo[4][3] = distributioninfo[4][3] + amount
  elif select == "SC" and hospital == "H1" or "H2" or "H3":   
    if inventory[5][3] <  amount:
      print("You can't distribute")
    else:
      inventory[5][3] = inventory[5][3] - amount
      if hospital == "H1":
        distributioninfo[5][1] = distributioninfo[5][1] + amount
      elif hospital == "H2":
         distributioninfo[5][2] = distributioninfo[5][2] + amount
      elif hospital == "H3":
         distributioninfo[5][3] = distributioninfo[5][3] + amount
  else:
    print("That value is not acceptable")

#Item Inventory Tracking

def see():
  with open("ppe.txt") as fileread:
    lines = fileread.readlines()
    print(lines)
    lines.sort()
    counter = 0
    while counter <= 5:
      print(lines[counter])
      counter += 1

def check(inventory):
    count = 0
    if inventory[0][3] < 25:
       print(inventory)
       count += 1
    elif inventory[1][3] < 25:
       print(inventory)
       count += 1   
    elif inventory[2][3] < 25:
       print(inventory)
       count += 1   
    elif inventory[3][3] < 25:
       print(inventory)
       count += 1   
    elif inventory[4][3] < 25:
       print(inventory)
       count += 1   
    elif inventory[5][3] < 25:
       print(inventory)
       count += 1   
    else:
      pass
    if (count == 0):
          print("Items are more than 25 boxes.")

#Searching Functionalities
import glob

for file in glob.glob('**/distribution.txt'):

 def search(distributioninfo):
  count = 1
  ff = open("distribution.txt","r")
  lines = ff.readlines()
  select = input("Which item do you search?: HC,FS,MS,GL,GW,SC:")
  if select == "HC" or "FS" or "MS" or "GL" or "GW" or  "SC":
     if select == lines[0]:
      print(lines[0])
     else:
      count += 1 
  else:
   print("That value is not acceptable.")


#main function
def main():
  inventory = [["HC","Head Cover","s1",100],
               ["FS","Face Shield","s1",100],
               ["MS","Mask","s2",100],
               ["GL","Gloves","s2",100],
               ["GW","Gown","s3",100],
               ["SC","Shoe Covers","s3",100]]
  hospitalinfo = [["h1","Seoul Hospital","Korea"],
                  ["h2","Tokyo Hospital","Japan"],
                  ["h3","KL Hospital","Malaysia"]]
  distributioninfo = {'HC':{1:'0',2:'0',3:'0'},
                      'FS':{1:'0',2:'0',3:'0'},
                      'MS':{1:'0',2:'0',3:'0'},
                      'GL':{1:'0',2:'0',3:'0'},
                      'GW':{1:'0',2:'0',3:'0'},
                      'SC':{1:'0',2:'0',3:'0'}}
  while True:
    inventory
    select = SelectPage()
    if select == "1":
      if_get(inventory)
    elif select == "2":
      if_send(inventory)
    elif select == "3":
      see()
    elif select == "4":     
      check(inventory)
    elif select == "5":
      search(distributioninfo)
    elif select == "6":
      break 
    else:
      print("That number is not acceptable}")
main()

