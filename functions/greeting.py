from datetime import datetime

def dynamic_greeting(name: str) -> None:
    current_hour = datetime.now().hour

    if 5 <= current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    print(f"{greeting}, {name}!")


dynamic_greeting("Patrick")

