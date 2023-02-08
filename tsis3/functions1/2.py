def fahrenheit_to_celsius(F):
    return (F - 32) * 5 / 9


temps_F = float(input())
print(fahrenheit_to_celsius(temps_F))