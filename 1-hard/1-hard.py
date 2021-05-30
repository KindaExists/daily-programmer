
def run():
    print("Think of a number from 1-100, but don't type it here.")
    print('Once you are done, press enter.')
    input()

    hi = 101
    lo = 1

    attempt = 1
    while True:
        print('\n################################\n')

        mid = (hi + lo) // 2

        # Y - Yes, H - Higher, L - Lower
        user_in = input(f'{attempt} | Is the number ( {mid} )?: ').lower()

        if user_in == 'y':
            print('Yay, I got it')
            break
        elif mid <= 1 or mid >= 100 or (hi == lo):
            print('That can\'t be right... Let\'s try again')
            hi = 101
            lo = 1
            mid = (hi-lo) // 2
            attempt = 0
        elif user_in == 'l':
            hi = mid
        elif user_in == 'h':
            lo = mid

        attempt += 1

if __name__ == "__main__":
    run()