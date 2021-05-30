
"""
[intermediate] challenge #1

Source / Reddit Post - https://www.reddit.com/r/dailyprogrammer/comments/pihtx/intermediate_challenge_1/
"""

#? Note that this solution will not be using a gui for the sake of convinience
#! Wrong Input Values are not accounted for in this program
# Also this is one of the first times I've used the "datetime module"
# Dates are not organized

import datetime, json

def mainLoop():
    running = True
    mode = ''
    while running:
        print('\n------------------------------\n')

        if  mode == '1':
            with open('1-intermediate/event.json', 'r+') as fp:
                temp = json.load(fp)
                for k, v in enumerate(temp):
                    print(f"{k} | {v['name']} | {datetime.datetime(*v['date'], *v['time']).strftime('%c')}")
                fp.close()
                input()

            mode = ''

        elif mode == '2':
            event = {}

            event['name'] = input('New Event Name: ')
            rDate = input('Date (dd/mm/yyyy): ')
            date = list(map(int, rDate.split('/', maxsplit=3)))
            rTime = input('Time (hh:mm:ss [24-hour time]): ')
            time = list(map(int, rTime.split(':', maxsplit=2)))

            event['date'] = date[::-1]
            event['time'] = time

            with open('1-intermediate/event.json', 'r+') as fp:
                temp = json.load(fp)
                temp.append(event)
                fp.seek(0)
                json.dump(temp, fp, indent = 4)
                fp.close()

            mode = ''

        elif mode == '3':
            with open('1-intermediate/event.json', 'r+') as fp:
                temp = json.load(fp)
                for k, v in enumerate(temp):
                    print(f"> {k} | {v['name']} | {datetime.datetime(*v['date'], *v['time']).strftime('%c')}")
                print('> e | Cancel')

                user_in = input()
                if isinstance(user_in, int):
                    temp.pop(user_in)

                fp.close()

            mode = ''

        elif mode == '4':
            with open('1-intermediate/event.json', 'r+') as fp:
                temp = json.load(fp)
                for k, v in enumerate(temp):
                    print(f"> {k} | {v['name']} | {datetime.datetime(*v['date'], *v['time']).strftime('%c')}")

                user_in = int(input())
                print()


                event = temp[user_in]
                date_time = datetime.datetime(*event['date'], *event['time'])
                print(f"> 0 | Name | {event['name']}")
                print(f"> 1 | Date | {date_time.strftime('%x')} ")
                print(f"> 2 | Time | {date_time.strftime('%X')} ")

                edit_k = int(input())

                if edit_k == 0:
                    event['name'] = input('New Event Name: ')
                elif edit_k == 1:
                    rDate = input('New Date (dd/mm/yyyy): ')
                    date = list(map(int, rDate.split('/', maxsplit=3)))
                    event['date'] = date[::-1]
                elif edit_k == 2:
                    rTime = input('New Time (hh:mm:ss [24-hour time]): ')
                    time = list(map(int, rTime.split(':', maxsplit=2)))
                    event['time'] = time


                fp.seek(0)
                json.dump(temp, fp, indent = 4)

                fp.close()

            mode = ''

        elif mode == '0':
            break

        else:
            print('> 1 - List Events \n> 2 - Add Event \n> 3 - Delete Event \n> 4 - Edit Event \n> 0 - Exit Program')
            print('##################')
            mode = input()
            print()

if __name__ == "__main__":
    mainLoop()