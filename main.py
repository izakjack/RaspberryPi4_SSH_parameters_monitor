import psutil
import paramiko
from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self, ip_address, username, password):
        self.ip_address = ip_address
        self.username = username
        self.password = password

     def find_cpu_temperature_path(self):
            possible_paths = [
                "/sys/class/thermal/thermal_zone0/temp",  # Przykładowa standardowa ścieżka na niektórych systemach Linux
                "/proc/acpi/thermal_zone/THM/temperature",  # Przykładowa standardowa ścieżka na innych systemach Linux
                # Dodaj więcej możliwych ścieżek, jeśli to konieczne
            ]
            for path in possible_paths:
                if os.path.exists(path):
                    return path
            # Jeśli nie znaleziono żadnej ścieżki, zwróć None lub podaj jakąś domyślną ścieżkę
            return None

     #Klasa abstrakcyjna devica i metody czytające
    # musi być zhermetyzowana
    # Klasa która odnajdzie ścieżkę do pliku i zwróci ścieżkę dalej
    #Ta ścieżka zwrócona musi być argumentem danej funkcji czytającej

    #kod zhermetyzowany
    #Metoda czytająca