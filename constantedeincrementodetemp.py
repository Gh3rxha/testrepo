# Agrego código de python en lugar del código ensamblador

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def newton_cooling(t, k, T_a, T_0):
    return T_a + (T_0 - T_a) * np.exp(-k * t)

def main():
    
    T_a = float(input("Ingrese la temperatura ambiente (°C): "))


    T_0 = float(input("Ingrese la temperatura inicial del líquido (°C): "))

    
    t = []
    T = []
    while True:
        tiempo = input("Ingrese el tiempo en segundos (o 'fin' para terminar): ")
        if tiempo.lower() == 'fin':
            break
        temperatura = input("Ingrese la temperatura en °C correspondiente: ")
        t.append(float(tiempo))
        T.append(float(temperatura))

    if len(t) < 2:
        print("Necesitas al menos dos puntos de datos para realizar el ajuste.")
        return

    t = np.array(t)
    T = np.array(T)

    
    try:
        initial_guess = [0.01]  
        popt, _ = curve_fit(lambda t, k: newton_cooling(t, k, T_a, T_0), t, T, p0=initial_guess)
        k = popt[0]

        
        T_fit = newton_cooling(t, k, T_a, T_0)

        
        plt.scatter(t, T, label='Datos experimentales')
        plt.plot(t, T_fit, label=f'Ajuste: k = {k:.5f}', color='red')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Temperatura (°C)')
        plt.title('Enfriamiento de un Líquido')
        plt.legend()
        plt.grid(True)
        plt.show()

        
        print(f'La constante de proporcionalidad k es: {k:.5f} s⁻¹')

    except Exception as e:
        print(f"Error al ajustar los datos: {e}")

if __name__ == "__main__":
    main()
