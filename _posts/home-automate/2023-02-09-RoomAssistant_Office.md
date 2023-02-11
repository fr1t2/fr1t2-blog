---
title: "Room Assistant - Office Raspi"
last_modified_at: 2023-02-10T17:35:06-05:00
date: 2023-02-10T17:38:06-05:00
excerpt_separator: "<!--more-->"
excerpt: "Office controller built using a Raspberry Pi, Home-Assistant, and Room-Assistant for full motion and occupancy sensing and light control."
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
  - "Smart Office"
  - "Office Control"


gallery:
  - url: /assets/images/roomassistant/OfficeRaspi-solid.png
    image_path: /assets/images/roomassistant/OfficeRaspi-th.png
    alt: "Kitchen raspi wiring diagram"
    title: "Kitchen Wiring Diagram"

---


## Office Overview


Custom built Raspberry Pi model B used as a room controller and extension of my home assistant installation. Monitoring and controlling devices in the Office utilizing the Room Assistant software.

This device is located in the equipment rack mounted to my office desk. Providing motion sensing and temp readings, not very complex at this point. 

Down the road this will interface with LED lighting and any other physical devices that can be automated.

### Office Info and Use

The main functions are occupancy and temp sensing. The occupancy sensor is tied to LIFX lights on my desk and a lamp in the room through a home assistant automation to trigger the lights on motion detection.

### Hardware

Raspberry pi model 1b is the brain here, providing MQTT communication to the controller and reading sensor inputs via GPIO pins.

- [x] Motion Sensor (PIR)
- [x] Temp Sensor (DS18B20)
- [x] Input Switches (Not Connected)
- [x] Relay Control (Not Connected)


### Network and Power

This lives directly next to network equipment and power on my desk, simple installation.

### Controls

Future control of a relay to be added with an LED light strip for accent lighting to the desk.

### Temp Sensor

Using a DHT11 sensor and a script to report the temp every min (cron job through [room-assistant script](#mydhtpy). 

I'm using the old [depreciated Adafruit_Python_DHT library](https://github.com/adafruit/Adafruit_Python_DHT)  due to issues with the new circuit python version and already having this working.

**Room-Assistant config excerpt:**

```yaml
shell:
  sensors:
    # DS18B20 Shelll Sensor
    - name: Office Temperature
      command: 'python3.7 /home/pi/room-assistant/script/temperature_sensor_code.py'
      cron: '* * * * *'
      icon: mdi:temperature-fahrenheit
      unitOfMeasurement: '°F'
      deviceClass: temperature
```

### Mounting


The Raspberry Pi came with a robust aluminum case, which I have modified to mount to a 2 RU blank rack panel, screwed into the 2 post 19" rack rails living on my desk. Simple, industrial and functional.

## Software

Everything is controlled and mapped to the home assistant dashboard over MQTT via the room-assistant system. 

### Room Assistant Config

This config file is the meat and potatoes of the program. Find it in  `/home/$USER/room-assistant/config/local.yml` on the Raspberry Pi.

```yaml
{% include_relative /include/room-assistant/office.local.yaml %}
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
{% include_relative /include/room-assistant/script/office/cpuUp.sh %}
```

#### cpuTemp.sh

return the CPU reported temp

```bash
{% include_relative /include/room-assistant/script/office/cpuTemp.sh%}
```

#### freeMem.sh

returns the remaining RAM on the pi

```bash
{% include_relative /include/room-assistant/script/office/freeMem.sh%}
```

#### myDHT.py

adapted DHT11 temp sensor reading temp and humid

```py
{% include_relative /include/room-assistant/script/office/myDHT.py%}
```

#### temperature_sensor_code.py

read DS18B20 sensor, report value in F

```py
{% include_relative /include/room-assistant/script/office/temperature_sensor_code.py%}
```

#### cpuVolt.sh

return boolean if no issues with voltage (power supply failure)

```bash
{% include_relative /include/room-assistant/script/office/cpuVolt.sh%}
```
