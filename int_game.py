# Integer Game 
import random


# generate new game hand
def generate_hand():
    hand = []
    for i in range(0, 3):
        num = random.randint(-10, 10)
        hand.append(num)
    return(hand)


# get user hand sum
def get_user_answer():
    user_result = input('Enter the sum of your hand: ')
    user_result = int(user_result)
    return(user_result)


# calculate the sum of the hand to be compared to user calculation
def calculate_hand(hand):
    hand_sum = sum(hand)
    return(hand_sum)


# draw pile
def draw_new():
    num = random.randint(-10, 10)
    return(num)


# get number user wants to discard
def get_discard_num():
    discard_num = input('Enter integer to discard: ')
    discard_num = int(discard_num) 
    return(discard_num)


# edit the user's hand for the discard exchange
def get_discard(hand):
    num = get_discard_num()
    contains_discard = num in hand
    while contains_discard is True:
       hand.remove(num)
       print(hand)
       print('Generating new integer...')
       new_num = draw_new()
       hand.append(new_num)
       print(hand)
       continue_game(hand)
       break
    while contains_discard is False:
        print('Please select an integer in your hand to discard: ')
        num = get_discard_num()
        break


# determine if user has won the game
def check_win(hand, result):
    if result == 0:
        print('You Win!')
        exit
    else:
        print('Keep Trying!')
        get_discard(hand)

 
# determine if user result is correct
def check_correct(hand, result):
    correct_result = calculate_hand(hand)
    if correct_result == result:
        print('Correct!')
        check_win(hand, result)
    else:    
        print('Try again!')
        result = get_user_answer()
        check_correct(hand, result)


# continue game function
# using hand already made, check results and if the user won the game
# if loser did not win, user must choose number to discard
# user then draws a new number to add to their hand
# process reruns until the user has won


def continue_game(hand):
    user_result = get_user_answer()
    check_correct(hand, user_result)




def main():
   hand = generate_hand()
   print(hand)
   continue_game(hand)


if __name__ == '__main__':
    main()