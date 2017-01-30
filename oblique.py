import random

# TODO - handle/wrap cards longer than the card width
# TODO - specify card width from console

def display(card, card_width=60):
    print('\n+{}+'.format('-' * card_width))
    print('|{}|'.format(' ' * card_width))
    print('|{}|'.format(' ' * card_width))
    print('|{}|'.format(' ' * card_width))
    print('|{}|'.format(str.center(card, card_width)))
    print('|{}|'.format(' ' * card_width))
    print('|{}|'.format(' ' * card_width))
    print('|{}|'.format(' ' * card_width))
    print('+{}+\n'.format('-' * card_width))

def draw(card_width=60):
    with open('strategies.txt', 'r') as f:
        rows = f.readlines()

    cards = [row.strip() for row in rows]
    card = None

    while not card:
        card = random.choice(cards) 
        if len(card) >= card_width:
            card = None
    return card


def main():
    card = draw()
    display(card)

if __name__ == '__main__':
    main()