def get_temperature(country):
    temperature_data = {
         "brasil": {"inverno": 25, "primavera": 30, "verão": 35, "outono": 28},
        "eua": {"inverno": 10, "primavera": 20, "verão": 30, "outono": 15},
        "alemanha": {"inverno": 5, "primavera": 15, "verão": 25, "outono": 10},
        "canada": {"inverno": -10, "primavera": 5, "verão": 20, "outono": 10},
        "australia": {"inverno": 15, "primavera": 25, "verão": 35, "outono": 20},
        "japao": {"inverno": 5, "primavera": 15, "verão": 30, "outono": 20},
        "china": {"inverno": 0, "primavera": 20, "verão": 30, "outono": 15},
        "india": {"inverno": 20, "primavera": 30, "verão": 40, "outono": 25},
        "russia": {"inverno": -20, "primavera": 5, "verão": 25, "outono": 10},
        "franca": {"inverno": 0, "primavera": 15, "verão": 25, "outono": 10},
        "argentina": {"inverno": 10, "primavera": 20, "verão": 30, "outono": 15},
    }

    country = country.lower()
    if country in temperature_data:
        return temperature_data[country]
    else:
        return None

def get_season(month):
    if month in [12, 1, 2]:
        return "inverno"
    elif month in [3, 4, 5]:
        return "primavera"
    elif month in [6, 7, 8]:
        return "verão"
    else:
        return "outono"

def main():
    print("Bem-vindo ao verificador de temperatura mundial!")
    while True:
        country = input("Digite o nome do país que você deseja visitar: ")
        temperature_data = get_temperature(country)
        if temperature_data:
            month = int(input("Digite o número do mês da visita (1 a 12): "))
            season = get_season(month)

            if season in temperature_data:
                temperature = temperature_data[season]
                print(f"A temperatura média em {country.capitalize()} durante {season} é de {temperature}°C.")
                if temperature < 10:
                    print("Recomenda-se trazer roupas quentes.")
                elif temperature > 25:
                    print("Recomenda-se trazer roupas leves.")
                else:
                    print("O clima parece agradável!")
            else:
                print("Desculpe, não foi possível encontrar dados de temperatura para essa época do ano.")
        else:
            print("Desculpe, não foi possível encontrar dados de temperatura para esse país.")
        
        choice = input("Você gostaria de verificar a temperatura de outro país? (s/n): ")
        if choice.lower() != 's':
            break

if __name__ == "__main__":
    main()
