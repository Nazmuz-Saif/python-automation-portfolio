#created by Nazmuz Saif

print('---CHECK STRENGTH---')

passward = input('Enter your password: ')

length = False
length = len(passward) >= 8

number = False
for char in passward:
    if char.isdigit():
        number = True
        break
special_char = "!@#$%^&*()_+-=[]{}|;:,.<>?"
special = False
for char in passward:
    if char in special_char:
        special = True
        break
print('---Analysis---')
print(f'At least 8 charecters: {'YES' if length else 'NO'}')
print(f'Contains numbers: {'YES' if number else 'NO'}')
print(f'Contains special characters: {'YES' if special else 'NO'}')

if length and number and special:
    print('Strong password')
else:
    print('Week Password')