import math
import re


def time(time_str):
    try:
        hours, minutes = map(int, time_str.split(":"))
        german_numbers = [
        "null", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf", "zwölf",
        "dreizehn", "vierzehn", "fünfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn", "zwanzig",
        "einundzwanzig", "zweiundzwanzig", "dreiundzwanzig", "vierundzwanzig", "fünfundzwanzig", "sechsundzwanzig",
        "siebenundzwanzig", "achtundzwanzig", "neunundzwanzig", "dreißig"
        ]
    
        german_hours = ["zwölf", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf"]
        
        next_hour = (hours + 1) % 12
        next_hour_german = german_hours[next_hour]
        
        if minutes == 0:
            return f"{german_hours[hours % 12]} Uhr"
        elif minutes == 15:
            return f"viertel nach {german_hours[hours % 12]}"
        elif minutes == 30:
            return f"halb {next_hour_german}"
        elif minutes == 45:
            return f"viertel vor {next_hour_german}"
        elif minutes < 30:
            return f"{german_numbers[minutes]} nach {german_hours[hours % 12]}"
        else:
            return f"{german_numbers[60 - minutes]} vor {next_hour_german}"

    except:
        print("incorrect format")
    


time_input = input("time in format hh:mm")
print(time(time_input))
