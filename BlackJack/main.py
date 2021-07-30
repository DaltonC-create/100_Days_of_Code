import random, art, replit

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
dealer_cards = []

def deal_card():
  return random.sample(cards, 2)

def draw_card():
  return random.choice(cards)

def Blackjack():
  print(art.logo)
  user_cards = deal_card()
  dealer_cards = deal_card()
  user_score = sum(user_cards)
  dealer_score = sum(dealer_cards)
  print(f"Your cards: {user_cards}, current score: {user_score}")
  print(f"Dealer's first card: {dealer_cards[0]}")

  while user_score <= 21:
    draw_or_not = input("Type 'y' to get another card, type 'n' to pass: ")
    if draw_or_not == 'y':
      new_card = draw_card()
      user_cards.append(new_card)
      user_score = sum(user_cards)
    elif draw_or_not == 'n':
      break
    if user_score > 21:
      break
    if user_score > 21 and 11 in user_cards:
      for i in range(len(user_cards) - 1):
        if user_cards[i] == 11:
          user_cards[i] = 1
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Dealer's first card: {dealer_cards[0]}")
  
  while dealer_score < 17:
    dealer_cards.append(draw_card())
    dealer_score = sum(dealer_cards)
    if dealer_score > 21 and 11 in dealer_cards:
      for i in range(len(dealer_cards) - 1):
        if dealer_cards[i] == 11:
          dealer_cards[i] = 1
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")

  if dealer_score == 21:
    print("BlackJack dealer wins.")
  elif user_score == 21:
    print("Blackjack you win.")
  elif user_score > 21:
    print("You went over. You lose.")
  elif dealer_score > 21:
    print("Dealer went over. You win.")
  elif user_score > dealer_score:
    print("You win.")
  elif dealer_score > user_score:
    print("You lose.")
  elif user_score == dealer_score:
    print("It's a tie, You lose.")
  
  

keep_playing = True
yes_no = input("Would you like to play BlackJack? Type 'y' or 'n': ")
while keep_playing:
  if yes_no == 'y':
    replit.clear()
    Blackjack()
  else:
    keep_playing = False
    break
  yes_no = input("Would you like to play BlackJack? Type 'y' or 'n': ")
