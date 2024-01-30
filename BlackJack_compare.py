def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    hand1_value = 0
    hand2_value = 0
    rango = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
    #CALCULAMOS EL VALOR DE HAND_1
    for card in hand_1:
        if card in ['J', 'Q', 'K']:
            hand1_value += 10
        elif card in rango:
            hand1_value += int(card)

    As = hand_1.count('A')
    if As > 1:
        hand1_value += (As-1)
        if hand1_value <= 10:
            hand1_value += 11
        else:
            hand1_value += 1
    elif As == 1:
        if hand1_value <= 10:
            hand1_value += 11
        else:
            hand1_value += 1
    print(hand1_value)
    #CALCULAMOS EL VALOR DE HAND_2
    for card in hand_2:
        if card in ['J', 'Q', 'K']:
            hand2_value += 10
        elif card in rango:
            hand2_value += int(card)

    As = hand_2.count('A')
    if As > 1:
        hand2_value += (As-1)
        if hand2_value <= 10:
            hand2_value += 11
        else:
            hand2_value += 1
    elif As == 1:
        if hand2_value <= 10:
            hand2_value += 11
        else:
            hand2_value += 1
    print(hand2_value)
    
    if hand1_value > 21:
        hand1_value = 0
    if hand2_value > 21:
        hand2_value = 0
        
    return hand1_value > hand2_value

# Check your answer

blackjack_hand_greater_than(['9'], ['9', 'Q', '8', 'A'])