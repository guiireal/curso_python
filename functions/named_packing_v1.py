def result_f1(**podium):
    for position, driver in podium.items():
        print(f"{position}: {driver}")


if __name__ == "__main__":
    result_f1(first="Hamilton", second="Verstappen", third="Bottas")
