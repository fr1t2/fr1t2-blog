---
title: "Smart HVAC Control with Room Assistant and Raspberry Pi"
last_modified_at: 2023-02-09T17:38:06-05:00
date: 2023-02-09T17:38:06-05:00
excerpt_separator: "<!--more-->"
excerpt: "Experience reliable HVAC control through Home Assistant with the Room Assistant & Raspberry Pi furnace controller, ensuring energy savings and consistent temperature throughout your home."
categories:
  - homeAutomation
  - roomAssistant
excerpt_separator: "<!--more-->"
#layout: single
header:
  overlay_image: "/assets/images/roomassistant/raspi-header.png"
  overlay_filter: 0.5
  #caption: "Room Assistant on raspberry Pi Model B v1"
  teaser: "/assets/images/roomassistant/FurnaceRaspi-th.png"
  og_image: "/assets/images/roomassistant/FurnaceRaspi-th.png"
image:
  feature: "/assets/images/roomassistant/FurnaceRaspi-th.png"
  thumb: "/assets/images/roomassistant/FurnaceRaspi-th.png" #keep it square 200x200 px is good

#classes: wide
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
  - "furnace control"


gallery:
  - url: /assets/images/roomassistant/FurnaceRaspi-solid.png
    image_path: /assets/images/roomassistant/FurnaceRaspi-th.png
    alt: "furnace raspi wiring diagram"
    title: "Furnace Wiring Diagram"

---


## Furnace Raspi Overview

Smart HVAC control is now possible through Home Assistant with the help of [Room Assistant](https://www.room-assistant.io/) and a Raspberry Pi furnace controller, providing reliable energy savings and consistent temperature throughout your home.


<!--more-->

The furnace controller is one of my favorite and most used integrations so far.

This one is located in my furnace connected to the interface to control the fan, heat and AC for the furnace through some 5v relays and a Raspi model B.

On the Raspbian OS running on the pi I have installed [Room Assistant](https://www.room-assistant.io/) following [this guide](/blog/homeautomation/roomassistant/RoomAssistant/) to handle the low level communication stuff back to my [Home Assistant](https://www.room-assistant.io/) server.


### Wiring 

Wiring diagram for the furnace control devices and connections.

{% include gallery %}{: .align-center }

Not too difficult or complex, though when combined with multiple temperature sensors around the house the functionality is unmatched. 

Using some old hardware and a few relays, I have an smart furnace and energy savings!

### Furnace Info and Use

One of the issues in the rental home I live in is the inconsistency of HVAC coverage throughout the house. This drove me crazy! 

Upstairs is too hot while the downstairs rooms needed mittens and a hat. The main issue being with the main temp reading coming from the stair mid house.

We have a split level 3 bed with a small blower furnace in the crawl space of the house and duct work run all throughout (*except the downstairs bathroom for some reason*). 

The location of the thermostat, while central is not the best representation of the perceived temp felt in the rooms we actually spend time in.

I had enough, time to automate it!

## Hardware

Using on old Raspberry Pi that was a dumpster find, I built the controller with (3) 5v relay boards and a DHT11 temp sensor.

These relays are mounted to the top of the controller with DuPont cables connected to GPIO pins on the pi and the temp sensor up on a few stand-offs outside of the case.


### Network and Power

Previously I had run a bunch of network cables around the house through the crawl space and luckily I was able to re-purpose one of these for the cause. This hardwired connection provides reliable connectivity. 

Power is fed from a 5v android wall charger in the same outlet that feeds the furnace. There was an open socket and it is switched with the furnace by US building code, so it will shutdown if something needs service later.

### Furnace Controls

The furnace Pi is connected directly to the 12v furnace interface in parallel with the existing house thermostat controller.

This is due to the lack of confidence in the initial controllers performance and longevity, and due to the function being \*fairly important (*heat/ac + kids = must_have*).

Since the house is a rental, and the landlord likely wont approve, the main t-stat is still connected for immediate control if needed at the wall. Stealth home control!

#### Mounting

The unit is mounted in the furnace, resting in the return air path due to clearance, cable pathway requirements, and not wanting to modify anything not mine. 

This provided an additional benefit of having a dht11 temp/humid sensor in the return air path. More sensor data!!

## Software

Everything is controlled and mapped to the home assistant dashboard over MQTT via the room-assistant system. 

### Room Assistant Config

This config file is the meat and potatoes of the program. Find it in  `/home/$USER/room-assistant/config/local.yml` on the Raspberry Pi.

```yaml
{% include_relative /include/room-assistant/furnace.local.yaml %}
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
{% include_relative /include/room-assistant/script/furnace/cpuUp.sh %}
```

#### cpuTemp.sh

return the CPU reported temp

```bash
{% include_relative /include/room-assistant/script/furnace/cpuTemp.sh%}
```

#### freeMem.sh

returns the remaining RAM on the pi

```bash
{% include_relative /include/room-assistant/script/furnace/freeMem.sh%}
```

#### myDHT.py

adapted DHT11 temp sensor reading temp and humid

```py
{% include_relative /include/room-assistant/script/furnace/myDHT.py%}
```

#### temperature_sensor_code.py

read DS18B20 sensor, report value in F

```py
{% include_relative /include/room-assistant/script/furnace/temperature_sensor_code.py%}
```

#### cpuVolt.sh

return boolean if no issues with voltage (power supply failure)

```bash
{% include_relative /include/room-assistant/script/furnace/cpuVolt.sh%}
```


### Future Improvements

- Additional temp sensors affixed to the water pipe lines (hot water usage?) 
- Additional sensor in the crawl space generally (freeze protection).
- Leak detection around water pipe service connection and sprinkler branch


In conclusion, the Room Assistant and Raspberry Pi furnace controller provides a reliable and efficient solution to HVAC control, allowing for energy savings and consistent temperature throughout the home. 

The combination of low-cost hardware and smart automation software makes this project a great example of how to integrate IoT into your home. Whether you're looking to automate your furnace or just make your home more comfortable, this setup is a great starting point that can be adapted to suit your individual needs.