cards = (
    # Heart (♥)
    {
        'symbol': 'heart',
        'value': 1
    },
    {
        'symbol': 'heart',
        'value': 2
    },
    {
        'symbol': 'heart',
        'value': 3
    },
    {
        'symbol': 'heart',
        'value': 4
    },
    {
        'symbol': 'heart',
        'value': 5
    },
    {
        'symbol': 'heart',
        'value': 6
    },
    {
        'symbol': 'heart',
        'value': 7
    },
    {
        'symbol': 'heart',
        'value': 8
    },
    {
        'symbol': 'heart',
        'value': 9
    },
    {
        'symbol': 'heart',
        'value': 10
    },
    {
        'symbol': 'heart',
        'value': 'J'
    },
    {
        'symbol': 'heart',
        'value': 'Q'
    },
    {
        'symbol': 'heart',
        'value': 'K'
    },

    # Diamond (♦)
    {
        'symbol': 'diamond',
        'value': 1
    },
    {
        'symbol': 'diamond',
        'value': 2
    },
    {
        'symbol': 'diamond',
        'value': 3
    },
    {
        'symbol': 'diamond',
        'value': 4
    },
    {
        'symbol': 'diamond',
        'value': 5
    },
    {
        'symbol': 'diamond',
        'value': 6
    },
    {
        'symbol': 'diamond',
        'value': 7
    },
    {
        'symbol': 'diamond',
        'value': 8
    },
    {
        'symbol': 'diamond',
        'value': 9
    },
    {
        'symbol': 'diamond',
        'value': 10
    },
    {
        'symbol': 'diamond',
        'value': 'J'
    },
    {
        'symbol': 'diamond',
        'value': 'Q'
    },
    {
        'symbol': 'diamond',
        'value': 'K'
    },

    # Spade (♠)
    {
        'symbol': 'spade',
        'value': 1
    },
    {
        'symbol': 'spade',
        'value': 2
    },
    {
        'symbol': 'spade',
        'value': 3
    },
    {
        'symbol': 'spade',
        'value': 4
    },
    {
        'symbol': 'spade',
        'value': 5
    },
    {
        'symbol': 'spade',
        'value': 6
    },
    {
        'symbol': 'spade',
        'value': 7
    },
    {
        'symbol': 'spade',
        'value': 8
    },
    {
        'symbol': 'spade',
        'value': 9
    },
    {
        'symbol': 'spade',
        'value': 10
    },
    {
        'symbol': 'spade',
        'value': 'J'
    },
    {
        'symbol': 'spade',
        'value': 'Q'
    },
    {
        'symbol': 'spade',
        'value': 'K'
    },

    # Club (♣)
    {
        'symbol': 'club',
        'value': 1
    },
    {
        'symbol': 'club',
        'value': 2
    },
    {
        'symbol': 'club',
        'value': 3
    },
    {
        'symbol': 'club',
        'value': 4
    },
    {
        'symbol': 'club',
        'value': 5
    },
    {
        'symbol': 'club',
        'value': 6
    },
    {
        'symbol': 'club',
        'value': 7
    },
    {
        'symbol': 'club',
        'value': 8
    },
    {
        'symbol': 'club',
        'value': 9
    },
    {
        'symbol': 'club',
        'value': 10
    },
    {
        'symbol': 'club',
        'value': "J"
    },
    {
        'symbol': 'club',
        'value': 'Q'
    },
    {
        'symbol': 'club',
        'value': 'K'
    },

)

card_symbols = ('♥', '♦', '♠', '♣')

game_cards = []
dealer_cards = []


def name_to_symbol(name):
    return {
        'heart': card_symbols[0],
        'diamond': card_symbols[1],
        'spade': card_symbols[2],
        'club': card_symbols[3]
    }.get(name, 'Invalid symbol!')
