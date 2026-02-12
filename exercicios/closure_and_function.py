def create_greeting(greeting):
    def greet(name):
        return f'{greeting}, {name}'
    return greet

speak_good_morning = create_greeting('Bom dia!')
speak_good_night = create_greeting('Boa Noite!')

# print(speak_good_morning('Edgar'))
# print(speak_good_night('Fulano'))

for name in ['edgar', 'Fulano', 'Maria']:
    print(speak_good_morning(name))
    print(speak_good_night(name))
