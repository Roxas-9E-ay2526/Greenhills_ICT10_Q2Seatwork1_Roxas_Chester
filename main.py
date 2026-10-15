# Seatwork 2 - The Goon Squad Checker
from pyscript import document

# list of Goon Squad members
def candidate_checker(e):
    Squad_memebrs = ['chester roxas','joel gonzales','ezekiel backay','joseph co','franco maglaqui','rene butterbonia','rene buterbonia', 'jarence manacap',]

    # verify full candidate name and verify them
    first_name = document.getElementById('first_name').value.strip()
    last_name = document.getElementById('last_name').value.strip()

    candidate = f'{first_name} {last_name}'.strip()
    member_checker = candidate.lower() in Squad_memebrs
    
    messages = (
        f'Access Denied: {candidate} is not part of The Goon Squad.',
        f'Welcome, {candidate}! You are officially confirmed as a member of The Goon Squad.',
    )
    # Diplay the final message
    document.getElementById('result').innerHTML = messages[member_checker]