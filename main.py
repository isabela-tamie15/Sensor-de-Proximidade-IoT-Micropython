from machine import Pin, time_pulse_us
import time

# 1. Declara as variáveis de todos os componentes
# LEDs
led_verde = Pin(2, Pin.OUT)
led_amarelo = Pin(4, Pin.OUT)
led_vermelho = Pin(5, Pin.OUT)

# Relé
rele = Pin(18, Pin.OUT)

# Sensor
trigger = Pin(12, Pin.OUT)
echo = Pin(14, Pin.IN)

# 2. Define a função de distância
def medir_distancia():
    trigger.off()
    time.sleep_us(2)
    trigger.on()
    time.sleep_us(10)
    trigger.off()

    # 30000 significa 30ms para receber a ligação ou desliga
    duracao = time_pulse_us(echo, 1, 30000) 

    if duracao <= 0:
        return 100

    distancia = (duracao * 0.0343) / 2
    return distancia

while True:
    distancia = medir_distancia()
    print("Distância:", distancia)

    # 3. Desliga todos os componentes para só ligar mediante a condição
    led_verde.off()
    led_amarelo.off()
    led_vermelho.off()
    rele.off()

    # 4. Cada condição atendida, acende uma cor de led
    if distancia < 70:
        led_verde.on()

    if distancia < 40:
        led_amarelo.on()

    if distancia < 20:
        led_vermelho.on()
        rele.on() # rele só aciona na menor distância 20cm

    time.sleep(0.5)


