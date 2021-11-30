
#Objetivo
#Cuando haya completado este laboratorio de aprendizaje, podrá:

#Aproveche la clave X-Meraki-API-Key para autorizar las llamadas a la API REST a la plataforma en la nube de Meraki.
#Presentar la jerarquía utilizada por Meraki para organizar redes y dispositivos.
#Exponga llamadas introductorias que permitan el acceso a elementos de red administrados por Meraki.

import requests
import json
#Evaluación final de Habilidades de DEVASCAssignment
print ('*'*100)
api_key = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
baseUrl = 'https://api.meraki.com/api/v1'
headers = {'X-Cisco-Meraki-API-Key':api_key}
#Punto 1:
print ("Paso 1: Obtener los id de las organizaciones.")
url_org = baseUrl + "/organizations"
response_org = requests.get(url_org,headers=headers) #se está construyendo un objeto tipo Request de la URL  https://api.meraki.com/api/v1/organizations.
response_org = response_org.json()
print (json.dumps(response_org,indent=4))
print ('*'*100)
#Punto 2:
print ("Paso 2: consiga las redes en la organización")
id_org = response_org [0]['id'] # Elegimos un elemento ID en este caso el 3ro de la lista y lo guardamos en una variable
print (f'El ID elegido es: {id_org}')
url_network = f'{url_org}/{id_org}/networks'
response_network = requests.get(url_network,headers=headers)
response_network = response_network.json()
print (json.dumps(response_network,indent=4))
print ('*'*100)
#Punto 3:
print ("Paso 3: coloca los dispositivos en una red")
network_id = response_network [0]['id']
print (f"El network device es {network_id}")     
url_device = f'{url_org}/{id_org}/networks/{network_id}/devices' # armamos nuestra url con el id del eje anterior id_org
response_device = requests.get(url_device,headers=headers)
response_device = response_device.json()
print (json.dumps(response_device,indent=4))
print ('*'*100)
#Punto 4:
print (f"4 Paso 4: obtenga información de la red con el Network_id {network_id}")
url_net_id = f'{baseUrl}/networks/{network_id}' # armamos nuestra url con el id del eje anterior network_id
response_device = requests.get(url_net_id,headers=headers)
response_device = response_device.json()
print (json.dumps(response_device,indent=4))
print ('*'*100)
#Punto 5: 
print (f"5 Paso 5: Obtén información del dispositivo con el serial id {network_id}")
url_dev_id = f'{baseUrl}/networks/{network_id}/devices/' # armamos nuestra url con el id del eje anterior network_id
response_device = requests.get(url_dev_id,headers=headers)
response_device = response_device.json()
serial_id = response_device [0]['serial']
print (f'El serial_id del dispositivo es {serial_id}')
url_dev_id = f'{baseUrl}/networks/{network_id}/devices/{serial_id}' # armamos nuestra url con el id del eje anterior network_id y serial_id
response_device = requests.get(url_dev_id,headers=headers)
response_device = response_device.json()
print (json.dumps(response_device,indent=4))
print ('*'*100)
#Punto 6: 
print (f"6 Paso 6: obtenga información SSID para el network ID  {network_id}")
url_dev_ssid = f'{baseUrl}/networks/{network_id}/wireless/ssids'
response_device = requests.get(url_dev_ssid,headers=headers)
response_device = response_device.json()
print (json.dumps(response_device,indent=4))
print ('*'*100)


