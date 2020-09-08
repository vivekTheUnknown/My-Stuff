#RELEASE: 0.0.1

supplies = {}
exit_status = False
done = False

while exit_status == False:
    print('1) Display available supplies')
    print('2) Add supplies')
    print('3) exit')
    choice = int(input('please enter your choice: '))
    if choice == 1:
        print(f"{supplies} \n")
        continue
    elif choice == 2:
        supply_name_and_unit = input('enter supply name and unit: ')
        supply_qty = int(input('enter supply qty: '))
        supplies[supply_name_and_unit] = supply_qty
        #done = input('are you satisfied? y/n')
        #if done == 'y':
        #    done == True
        #    continue
        #else:
        #    done == False
    elif choice == 3:
        print('thanks for useing the supply manager!')
        exit()


