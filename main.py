from m5stack import *
from m5ui import *
from uiflow import *
from easyIO import *
import urequests
import json
import wifiCfg
import time

WIFI_SSID = ''
WIFI_PASSWORD = ''


# Chama as funções e imprime as informações na tela
def printInfos():
  
  BlockLabel = M5TextBox(14, 40, "Block: Loading", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
  title0 = M5Title(title="Dados do Bitcoin", x=3, fgcolor=0xFFFFFF, bgcolor=0x0032FF)
  PriceLabel = M5TextBox(14, 62, "Price: Loading", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
  TransactionLabel = M5TextBox(14, 86, "Transactions: Loading", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
  
  BlockLabel.setText(str((str('Block: ') + str(getBlock()))))
  PriceLabel.setText(str((str('Price: R$ ') + str((getBitcoinData()['price'])))))
  TransactionLabel.setText('Transactions: '+ str(getTransactions()))
  
  
# Obtem o preco do bitcoin
def getBitcoinData():
  try:
    req = urequests.request(method='GET', url='https://api.coinsamba.com/v0/index?base=BTC&quote=BRL')
    return {'price':((json.loads((req.text)))['close']),'change':((json.loads((req.text)))['change'])}
  except:
    return 0

# Obtem o bloco atual
def getBlock():
  try:
    req = urequests.request(method='GET', url='https://mempool.space/api/blocks/tip/height')
    return req.text
  except:
    return 0

# Obtem as transacoes na mempool
def getTransactions():
  try:
    req = urequests.request(method='GET', url='https://mempool.space/api/mempool')
    return json.loads(req.text)['count']
  except:
    return 0

setScreenColor(0x000000)
lcd.setRotation(3)

# Declara os campos na tela
Battery = M5TextBox(190, 118, "", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
BlockLabel = M5TextBox(14, 40, "Block: Loading", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
title0 = M5Title(title="Dados do Bitcoin", x=3, fgcolor=0xFFFFFF, bgcolor=0x0032FF)
PriceLabel = M5TextBox(14, 62, "Price: Loading", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
TransactionLabel = M5TextBox(14, 86, "Transactions: Loading", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)


wifiCfg.doConnect(WIFI_SSID, WIFI_PASSWORD)


while True:
  Battery.setText(str(map_value((axp.getBatVoltage()), 3.7, 4.1, 0, 100)) + "%")
  printInfos()
  wait(10000)
