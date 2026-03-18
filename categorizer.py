def categorize(title, content):

    text = f"{title} {content}".lower()

    categories = {
        "Race Results": [
            "win", "winner", "podium", "grand prix", "race result", "victory"
        ],
        "Driver News": [
            "contract", "transfer", "driver", "signed", "extends", "retire"
        ],
        "Team Updates": [
            "team principal", "team", "management", "strategy"
        ],
        "Technical_Regulation": [
            "upgrade", "aero", "aerodynamic", "floor", "regulation", "fia"
        ]
    }

    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in text:
                return category
    return "Other"