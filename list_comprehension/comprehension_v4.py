def get_day_type(day):
    days = {
        (1, 7): "Fim de semana",
        tuple(range(2, 7)): "Dia de semana",
    }

    selected_day = (type for numbers, type in days.items() if day in numbers)

    return next(selected_day, "Dia inválido")


if __name__ == "__main__":
    for day in range(0, 9):
        print(f"{day}: {get_day_type(day)}")
