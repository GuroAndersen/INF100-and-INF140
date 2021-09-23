def hvem_eldst(name_1, age_1, name_2, age_2):
    if age_1<age_2:
        text_1 = (f"{name_2} er {age_2} år og eldst.")
        return text_1
    else:
        text_2 = (f"{name_1} er {age_1} år og eldst.")
        return text_2