
"""
[easy] challenge #2

Source / Reddit Post - https://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/
"""

#? Making a Physics Calculator
# Code can be further shortened if using lambdas or not using methods at all
# Although this is to show the basic idea for this
# anyhow this is just an "easy" challenge


def computeForce(mass, acc):
    return mass * acc

def computeMass(force, acc):
    return force / acc

def computeAcceleration(force, mass):
    return force / mass

if __name__ == "__main__":
    while True:
        user_in = ''

        print('Compute for: ')
        print(' 1  | Force')
        print(' 2  | Mass')
        print(' 3  | Acceleration')
        print('Any | Exit')
        user_in = input('> ')

        if user_in == '1':
            m = int(input('Known Mass (kg): '))
            a = int(input('Known Acceleration (m/s^2): '))
            print(f'The computed force is: {computeForce(m, a)} N')
        elif user_in == '2':
            f = int(input('Known Force (N): '))
            a = int(input('Known Acceleration (m/s^2): '))
            print(f'The computed mass is: {computeMass(f, a)} kg')
        elif user_in == '3':
            f = int(input('Known Force (N): '))
            m = int(input('Known Mass (kg): '))
            print(f'The computed acceleration is: {computeAcceleration(f, m)} m/s^2')
        else:
            break

        print('\n######################\n')

