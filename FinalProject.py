#Mohamed hamed
#1644926
# I imported csv for the reader
import csv
# the operator is how use itemgetter and sort whichever element needs to sorted
import operator
# This the way that pulled the current date and time
from datetime import datetime

# This whole loop is how I combined each of the input files
with open('C:/Users/MJ/Desktop/ManufacturerList.csv','r') as csvfile1:
    maker_reader = csv.reader(csvfile1, delimiter=',')
    sort = sorted(maker_reader, key=operator.itemgetter(0))
    for gag in sort:
        for word in gag:
            if word == '':
                gag.remove(word)
        with open('C:/Users/MJ/Desktop/PriceList.csv','r') as csvfile2:
            price_maker = csv.reader(csvfile2, delimiter=',')
            sort2 = sorted(price_maker, key=operator.itemgetter(0))
            for a in sort2:
                if gag.count('damaged') == 1:
                    if gag[0] == a[0]:
                        gag.insert(-1,a[1])
                elif gag.count('damaged') == 0:
                    if gag[0] == a[0]:
                        gag.append(a[1])
        with open('C:/Users/MJ/Desktop/ServiceDatesList.csv', 'r') as csvfile3:
            date_maker = csv.reader(csvfile3, delimiter=',')
            sort3 = sorted(date_maker, key=operator.itemgetter(0))
            for dates in sort3:
                if gag.count('damaged') == 1:
                    if gag[0] == dates[0]:
                        gag.insert(-1, dates[1])
                elif gag.count('damaged') == 0:
                    if gag[0] == dates[0]:
                        gag.append(dates[1])
#each with open is just me making the output files requested with itemgetter
final_sort = sorted(sort, key=operator.itemgetter(1))
with open ('C://Users//MJ//Desktop//FullInventory.csv', 'w') as file1:
    write = csv.writer(file1)
    write.writerows(final_sort)
with open('C://Users//MJ//Desktop//PhoneInventory.csv', 'w') as file2:
    write2 = csv.writer(file2)
    for row in sort[:]:
        if row.count('phone') != 1:
            continue
        write2.writerow(row)
with open('C://Users//MJ//Desktop//LaptopInventory.csv', 'w') as file3:
    write3 = csv.writer(file3)
    for row in sort[:]:
        if row.count('laptop') != 1:
            continue
        write3.writerow(row)
with open('C://Users//MJ//Desktop//TowerInventory.csv', 'w') as file4:
    write4 = csv.writer(file4)
    for row in sort[:]:
        if row.count('tower') != 1:
            continue
        write4.writerow(row)
#This was one was a little bit difficult but datetime allowed me to pull today's date
date_sort = sorted(sort, key=lambda row: datetime.strptime(row[4], "%m/%d/%Y"))
the_date = datetime.now()
with open('C://Users//MJ//Desktop//PastServiceDateInventory.csv', 'w') as file5:
    write5 = csv.writer(file5)
    for x in date_sort:
        inv_date = x[4]
        need_date = datetime.strptime(inv_date, "%m/%d/%Y")
        if need_date >= the_date:
            continue
        write5.writerow(x)
#Damaged_sort is sorted by price which is why i used it in the next part of my code
damaged_sort = sorted(sort, key=operator.itemgetter(3), reverse=True)
with open('C://Users//MJ//Desktop//DamagedInventory.csv', 'w') as file6:
    write6 = csv.writer(file6)
    for b in damaged_sort:
        if b.count('damaged') != 1:
            continue
        write6.writerow(b)
#last list is already sorted by price so the for loop is how i took out the things that damaged and past the Service date
last_list = []
for a in damaged_sort:
    imp_date = a[4]
    get_date = datetime.strptime(imp_date, "%m/%d/%Y")
    if get_date <= the_date:
        continue
    if a.count('damaged') == 1:
        continue
    last_list.append(a)
#the manufacturer is outside of the loop so after one loop you can exit out
the_rest = []
the_manufacturer = str(input('Please enter Manufacturer: '))
#I put the the rest list in the while loop so it clears if the user doesnt press q
while the_manufacturer != 'q':
    the_rest = []
    if the_manufacturer == 'q':
        break
    else:
        the_type = str(input('Please enter your item type: '))
        manu_input = the_manufacturer.split(' ')
        type_input = the_type.split(' ')
        #split both inputs into lists to compare with last list
        for a in last_list:
            for item in manu_input:
                if item in a[0:2]:
                    for pyt in type_input:
                        if pyt in a[2:]:
                            for z in a:
                                the_rest.append(z)
        #that for loop prepared the_rest for this list of options
        if len(the_rest) == 0:
            print('No such item in inventory')
        if len(the_rest) == 5:
            #This whole if statement is in my code twice because it also works for if the Lenth exceeds 5 as well
            price1 = int(the_rest[3])
            cons_list = []
            #this for loop is how I took out the item that was already chosen from the inventory
            for done in last_list:
                comp_price = int(done[3])
                if price1 == comp_price:
                    continue
                else:
                    cons_list.append(done)
            #this for loop is how  I made the extra element in my list to sort by which one is closer in price
            for changes in cons_list:
                dif = abs(int(changes[3]) - price1)
                changes.append(dif)
            cons_sort = sorted(cons_list, key=operator.itemgetter(5), reverse=False)
            yesem = cons_sort[0]
            alm_done = yesem[0:5]
            listtostr = ' '.join([str(nba) for nba in the_rest])
            conlisttostr = ' '.join([str(cert) for cert in alm_done])
            print('Your item is:', listtostr)
            print('You may, also, consider:', conlisttostr)
        #This option is if the input had any other items
        if len(the_rest) > 5:
            #this the same as the previous if statement but i used inyt so the statements mirror each other
            inyt = the_rest[0:5]
            price2 = int(inyt[3])
            cons_list2 = []
            for done in last_list:
                comp_price2 = int(done[3])
                if price2 == comp_price2:
                    continue
                else:
                    cons_list2.append(done)
            for changes in cons_list2:
                differ = abs(int(changes[3]) - price2)
                changes.append(differ)
            cons_sort2 = sorted(cons_list2, key=operator.itemgetter(5), reverse=False)
            yesem2 = cons_sort2[0]
            alm_done2 = yesem2[0:5]
            listto_st3 = ' '.join([str(duh) for duh in inyt])
            conlisttostr2 = ' '.join([str(cert2) for cert2 in alm_done2])
            print('Your item is:', listto_st3)
            print('You may, also, consider:', conlisttostr2)
    #this is how the program asks the same question but with quit option
    the_manufacturer = str(input('Please enter Manufacturer or enter q to quit: '))

