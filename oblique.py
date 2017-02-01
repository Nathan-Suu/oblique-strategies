import random

# TODO - handle/wrap cards longer than the card width
# TODO - specify card width from console

def blank_line(card_width, repeats=1):
    for repeat in range(repeats):
        print('|{}|'.format(' ' * card_width))

def card_edge(card_width):
    print('\n+{}+'.format('-' * card_width))

def display(card, card_width=40):
    card_edge(card_width)
    blank_line(card_width, repeats=3)

    # print the message
    for line in card:
        print('|{}|'.format(str.center(line, card_width)))
    if len(card) == 1:
        blank_line(card_width)

    blank_line(card_width, repeats=3)
    card_edge(card_width)

def draw_card(text_width=30):
    with open('strategies.txt', 'r') as f:
        rows = f.readlines()
    cards = [row.strip() for row in rows]

    card = []
    line = ''

    words = random.choice(cards).split(' ')
    while words:
        word = words.pop(0)
        newline = line + ' ' + word
        if len(newline) > text_width:
            card.append(line.strip())
            line = word
        else:
            line = newline.strip()
    card.append(line)

    return card


def main():
    card = draw_card()
    display(card)

if __name__ == '__main__':
    main()