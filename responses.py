from random import choice, randint
import os
import json


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    with open("response.json", 'r', encoding='utf-8') as res:
        json_data = json.load(res)

    for key, values, in json_data.items():
        if key in lowered:
            return values
