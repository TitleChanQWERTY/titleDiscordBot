from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'привіт' in lowered:
        return 'вітання!'
    elif 'як справи' in lowered:
        return 'все добре!'
    elif 'гарного вечора' in lowered:
        return 'завтра побачимося!!'
    elif 'коли відео?' in lowered:
        return 'колись'
    elif '! кинути кубік' in lowered:
        return f'випало: {randint(1, 10)}'
    elif 'Слава україні' in lowered:
        return "героям слава!"
    elif '! посилання' in lowered:
        return "**ютуб** https://www.youtube.com/@titleyakumo"



