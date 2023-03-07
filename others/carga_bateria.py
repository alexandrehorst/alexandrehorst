# Programa que mostra o percentual de bateria
import psutil

# Captura sensor da bateria
bat = psutil.sensors_battery()

# Captura percentual da bateria
percent = str(bat.percent)

# Mostra resultado
print(f'No momento você tem {percent}% de baterial')