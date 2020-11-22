from time import sleep

print('-' * 9)
print('TIMER'.center(9))
print('-' * 9)

value = int(input('How many time you want to set? [numbers only] '))
print('-' * 9)
print('1 - Sec')
print('2 - Min')
print('-' * 9)
unity = int(input(f'{value} seconds or minutes? '))
while True:
    if unity != 1 and unity != 2:
        unity = int(input(f'{value} sec or min? '))
    else:
        print('-' * 9)
        start = input('Press ENTER to start!')
        print('Starting...')
        sleep(1)
        if unity == 1:
            for sec in range(value, -1, -1):
                print(sec)
                sleep(1)
            break
        else:
            for sec in range(value * 60, -1, -1):
                print(sec)
                sleep(1)
            break
print('END!')
