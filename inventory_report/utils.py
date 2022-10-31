from datetime import date

TODAY = date.today()


def nearest(items, pivot=TODAY):
    return min(items, key=lambda x: abs(date.fromisoformat(x) - pivot))
