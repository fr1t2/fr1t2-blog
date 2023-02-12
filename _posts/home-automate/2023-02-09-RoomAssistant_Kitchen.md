---
title: "Building a Kitchen Assistant with Raspberry Pi and Room Assistant"
last_modified_at: 2023-02-10T17:35:06-05:00
date: 2023-02-10T17:38:06-05:00
excerpt_separator: "<!--more-->"
excerpt: "Transform your kitchen into a smart space with a Raspberry Pi Model B v1, Room-Assistant, and Home-Assistant, including motion and temperature sensors, and relays for full IoT control."
categories:
  - homeAutomation
  - roomAssistant
excerpt_separator: "<!--more-->"
#layout: single
#classes: wide
header:
  overlay_image: "/assets/images/roomassistant/raspi-header.png"
  overlay_filter: 0.5
  #caption: "Room Assistant on raspberry Pi Model B v1"
  teaser: "/assets/images/roomassistant/raspi-header-thumb.png"
  og_image: "/assets/images/roomassistant/raspi-header-thumb.png"

image:
  feature: "/assets/images/roomassistant/raspi-header.png"
  thumb: "/assets/images/roomassistant/raspi-header-thumb.png" #keep it square 200x200 px is good

toc: true
toc_sticky: true

sidebar:
  title: "Home Automation"
  nav: home-automation

tags:
  - Homeassistant
  - hass
  - room-assistant
  - "raspberry pi"
  - automation
  - controls
  - IoT
  - "Smart Kitchen"
  - "Kitchen Control"


gallery:
  - url: /assets/images/roomassistant/KitchenRaspi-solid.png
    image_path: /assets/images/roomassistant/KitchenRaspi-th.png
    alt: "Kitchen raspi wiring diagram"
    title: "Kitchen Wiring Diagram"

---




## Kitchen Overview

Raspi model B used as a room controller and extension of the home assistant installation. Monitoring and controlling devices in the kitchen. Built from a Raspberry Pi Model B v1, some 5v relays and a few temperature sensors.

I've installed Raspbian OS on the pi and have loaded [Room Assistant](https://www.room-assistant.io/) following [this guide](/homeautomation/roomassistant/RoomAssistant/) to handle the low level communication stuff back to my [Home Assistant](https://www.room-assistant.io/) server.

### Kitchen Info and Use

This device lives on top of our pantry freestanding unit that lives in our kitchen. Network cables were connected through the adjacent wall to the garage where I have a network switch.

**Main Functions**

Responsible for occupancy and temperature readings for one of the most used rooms in the house. The occupancy sensor is tied to a LIFX light above the stove through a home assistant automation to trigger the lights on motion detection.

Room temp is sent back to Home Assistant to be averaged into the whole house temperature used by the [Furnace Controller](homeautomation/roomassistant/RoomAssistant_Furnace/).

### Wiring

Everything wires to the GPIO pins of the Raspberry Pi using DuPont cables through a hole drilled into the case. Nothing too complex with this setup.

{% include gallery %}{: .align-center }

## Hardware

Raspberry Pi Model B v1 is the brain here, providing MQTT communication to the controller and reading sensor inputs via GPIO pins.

- [x] Motion Sensor (PIR)
- [x] Temp Sensor (DS18B20)
- [x] Temp/Humid (DHT11)
- [x] Input Switches (x2)
- [x] Relay Control (x2)

### Network and Power

WiFi connection required here due to location and limited access to run wire. Simple to configure the WiFi USB dongle through the `raspi-config` command line utility. Once connected to the network, assign a static IP through the DHCP server for consistency and cluster settings. 

Power is provided from the wall outlet below.

### Controls

- **Relays** for controlling LED's or any other thing that comes later. Not currently used.
- **Input Switches** for door switches or light switch. Not currently implemented

### Temp Sensors

There are 2 sensors attached to this device. Since it is mounted up near the ceiling, the temp is swayed to a higher reading than the actual feel. Due to this I added an additional sensor that hangs down to head height.

Using the DHT11 sensor and a script to report the temp every min (cron job through [room-assistant script](#mydhtpy). 

I'm using the old [depreciated Adafruit_Python_DHT library](https://github.com/adafruit/Adafruit_Python_DHT) due to issues with the new circuit python version and already having this working. I didn't feel like changing something that is working.

Using the DS18B20 sensor and a [script to check the temp using python](#temperature_sensor_codepy) and a onewire connection.


**Room-Assistant config excerpt:**

```yaml
shell:
  sensors:
     # DS18B20 Shelll Sensor
    - name: Kitchen Temperature 1
      command: 'python3.7 /home/pi/room-assistant/script/temperature_sensor_code.py'
      cron: '* * * * *'
      icon: mdi:temperature-fahrenheit
      unitOfMeasurement: '°F'
      deviceClass: temperature

     # DHT11 Sensor reporting the temp °F result
    - name: Kitchen Temperature
      command: 'python3.7 /home/pi/room-assistant/script/myDHT.py'
      regex: '(-?[0-9.]+)F'
      cron: '*/2 * * * *'
      icon: mdi:temperature-fahrenheit
      unitOfMeasurement: '°F'
      deviceClass: temperature

     # DHT11 Sensor reporting the humid % result
    - name: Kitchen Humidity
      command: 'python3.7 /home/pi/room-assistant/script/myDHT.py'
      regex: '(-?[0-9.]+)%'
      cron: '*/5 * * * *'
      icon: mdi:water-percent
      unitOfMeasurement: '%'
      deviceClass: humidity
```



### Mounting

This device sits on top of the furniture, hidden from view tucked behind some decorative molding. Only thing that is visible is the small PIR motion sensor looking at the room.

## Software

Everything is controlled and mapped to the home assistant dashboard over MQTT via the room-assistant system. 

### Room Assistant Config

This config file is the meat and potatoes of the program. Find it in  `/home/$USER/room-assistant/config/local.yml` on the Raspberry Pi.

```yaml
{% include_relative /include/room-assistant/kitchen.local.yaml %}
```


### Scripts

Some additional helper scripts were also developed to return info on the device for integrations and status's over in home assistant. 

Add these to room assistant using the `shell.sensors` function like this:

```bash
shell:
  sensors:

     # DHT11 Sensor reporting the temp °F result
    - name: Garage Temperature
      command: 'python3.7 /home/pi/room-assistant/script/myDHT.py'
      regex: '(-?[0-9.]+)F'
      cron: '*/2 * * * *'
      icon: mdi:temperature-fahrenheit
      unitOfMeasurement: '°F'
      deviceClass: temperature
```

#### cpuUp.sh

return the uptime in seconds formatted as int

```bash
{% include_relative /include/room-assistant/script/kitchen/cpuUp.sh %}
```

#### cpuTemp.sh

return the CPU reported temp

```bash
{% include_relative /include/room-assistant/script/kitchen/cpuTemp.sh%}
```

#### freeMem.sh

returns the remaining RAM on the pi

```bash
{% include_relative /include/room-assistant/script/kitchen/freeMem.sh%}
```

#### myDHT.py

adapted DHT11 temp sensor reading temp and humid

```py
{% include_relative /include/room-assistant/script/kitchen/myDHT.py%}
```

#### temperature_sensor_code.py

read DS18B20 sensor, report value in F

```py
{% include_relative /include/room-assistant/script/kitchen/temperature_sensor_code.py%}
```

#### cpuVolt.sh

return boolean if no issues with voltage (power supply failure)

```bash
{% include_relative /include/room-assistant/script/kitchen/cpuVolt.sh%}
```


## Future Improvements

- Additional temp sensors affixed to the water pipe lines (hot water usage?) 
- Additional sensor in the crawl space generally (freeze protection).
- Leak detection around water pipe service connection and sprinkler branch
