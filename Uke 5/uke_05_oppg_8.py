def stones_to_pounds(stones):
    pounds = stones * 14
    return pounds

def stones_to_kg(stones):
    kilo = round(stones / 0.15747, 2)
    return kilo

def pounds_to_kg(pounds):
    kilo = round(pounds / 2.20462, 2)
    return kilo

def imperial_to_metric(stones, pounds):
    kilo_stones = round(stones / 0.15747, 2)
    kilo_pounds = round(pounds / 2.20462, 2)
    return kilo_stones + kilo_pounds