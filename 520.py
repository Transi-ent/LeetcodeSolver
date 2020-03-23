def detectCapitalUse(word: str) -> bool:
    all_lower = True
    all_upper = True
    long = False
    restLower = True

    if len(word)>1:
        long = True

    for i, ch in enumerate(word):
        all_lower = all_lower and ch.islower()
        all_upper = all_upper and ch.isupper()

        if i>=1:
            restLower = restLower and ch.islower()

    return all_upper or all_lower or restLower

def detectCapitalUse2(word: str) -> bool:
    return word.islower() or word.isupper() or word.istitle()
