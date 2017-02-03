def Rabbits(months, babies):
    if months == 1 or months == 2: return 1
    else: return babies * Rabbits(months-2, babies) + Rabbits(months-1, babies)
