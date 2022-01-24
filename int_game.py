# Integer Game 
import random

def generate_hand():
    hand = []
    for i in range(0, 4):
        num = random.randint(-10, 10)
        hand.append(num)
    return(hand)


def calculate_hand(hand):
    hand_sum = sum(hand)
    return(hand_sum)


def check_correct(hand, result):
    if calculate_hand(hand) == result:
        return('Correct!')
    else:    
        return('Try again!')


def get_discard(hand):
    discard_num = input('Enter integer to discard: ')
    discard_num = int(discard_num) 
    contains_discard = discard_num in hand
    if contains_discard is True:
       hand.remove(discard_num)
    else:
        return('Please select an integer in your hand to discard: ')


def check_win(hand, result):
    if check_correct(hand, result) == 'Correct':
        if result == 0:
            return('You Win!')
        else:
            get_discard(hand)
    

new_hand = generate_hand()
print(new_hand)
user_result = input('Enter the sum of your hand: ')
user_result = int(user_result)
print(check_correct(new_hand, user_result))