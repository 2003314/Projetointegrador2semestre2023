import machine
import utime
import dht

from pico_i2c_lcd import I2cLcd
from machine import I2C
from machine import Pin

i2c = I2C(id=1,scl=Pin(27),sda=Pin(26),freq=100000)
lcd = I2cLcd(i2c, 0x3B, 2, 16) # LCD 16x2

 
sensor = dht.DHT11(machine.Pin(4))
vermelho = machine.Pin(13, machine.Pin.OUT)
azul = machine.Pin(15, machine.Pin.OUT)
verde = machine.Pin(14, machine.Pin.OUT)
 
while True:
    sensor.measure()
    h = sensor.humidity()
    t = sensor.temperature()
    if (t<35 or h>40):
        vermelho.value(0)
        verde.value(1)
        azul.value(0)
    elif (t==0 or h==20):
        vermelho.value(0)
        verde.value(0)
        azul.value(1)
    else:
        vermelho.value(1)
        verde.value(0)
        azul.value(0)
       
    lcd.putstr('Temperatura: ',t)
    lcd.move_to(1,1)
    lcd.putstr('Umidade:',h)
    lcd.move_to(2,1)
    utime.sleep(2)