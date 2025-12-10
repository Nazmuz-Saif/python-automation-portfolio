import random
print('---Game Fun---')
print("Let's think a number!! OK, I'm done.")

num = random.randint(1, 100)
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    guess = int(input(f'Attempt {attempts+1}/{max_attempts} - Guess a number between 1 and 100: '))
    attempts += 1

    if guess == num:
        print(f'Congrats! You won in {attempts} attempts.')
        break
    elif guess > num:
        print('Too high!')
    else:
        print('Too low!')
    if attempts == max_attempts:
        print(f'You lost!. the number was {num}.')
        break