from requests import get
import board
import busio
from circuitpython_i2c_lcd import I2cLcd
from time import sleep

i2c = busio.I2C(board.SCL, board.SDA)
while i2c.try_lock():
    pass
DEFAULT_I2C_ADDR = 0x27
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

url = 'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en'

while True:
    data = get(url).json()
    temp_data = data['temperature']['data']
    for entry in temp_data:
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr(entry['place'][:15])
        lcd.move_to(0, 1)
        lcd.putstr(str(entry['value']))
        sleep(2)
