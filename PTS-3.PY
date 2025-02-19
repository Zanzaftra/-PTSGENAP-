#rumus dan input nya
def suhu(celsius):
    return (celsius * 9/5) + 32
celsius = float(input("Masukkan suhu dalam Celcius: "))
fahrenheit = suhu(celsius)

# hasilnya
print(f"{celsius}°C sama dengan {fahrenheit}°F")
