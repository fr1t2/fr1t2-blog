---
title: "Room Assistant - Furnace Raspi"
last_modified_at: 2023-02-09T17:38:06-05:00
date: 2023-02-09T17:38:06-05:00
excerpt_separator: "<!--more-->"
excerpt: "Room Assistant & Raspi armv6 installation and configuration for the furnace controls"
categories:
  - homeAutomation
  - roomAssistant
excerpt_separator: "<!--more-->"
#layout: single
#header:
#  image: "/assets/images/roomassistant/room-assistant-header.png"
#  #caption: "Room Assistant on raspberry Pi Model B v1"
#  teaser: "https://www.room-assistant.io/room-assistant.png"
#image:
#  feature: "/assets/images/roomassistant/room-assistant-header.png"
#  thumb: "/assets/images/roomassistant/room-assistant250.png" #keep it square 200x200 px is good

classes: wide
toc: true

tags:
  - Homeassistant
  - hass
  - room-assistant
  - "raspberry pi"
  - automation
  - controls
  - IoT
  - "furnace control"

---

HVAC control through Home Assistant thanks to a Raspberry Pi and [Room Assistant](https://www.room-assistant.io/).

<!--more-->

Raspi model B used as a room controller and extension of the home assistant installation. This one is located in my furnace connected to the interface to control the fan, heat and AC for the furnace.


## Overview

The furnace controller is one of my favorite and most used integrations so far.

![furnace device wiring](/assets/images/roomassistant/furnace/FurnaceRaspi.png)

Not too difficult or complex, though when combined with multiple temperature sensors around the house the functionality is unmatched. Using some old hardware and a few relays, I have an smart furnace and energy savings!

## Info and Use

One of the issues in the rental home I live in is the inconsistency of HVAC coverage throughout the house. This drove me crazy, upstairs is too hot while the downstairs rooms needed mittens and a hat. The main issue being with the main temp reading coming from the stair mid house.

We have a split level 3 bed with a small blower furnace in the crawl space of the house and duct work run all throughout (*except the downstairs bathroom for some reason*). 

The location of the thermostat, while central is not the best representation of the perceived temp felt in the rooms we actually spend time in.

I had enough, time to automate it!

### Hardware

Using on old Raspberry Pi that was a dumpster find, I built the controller with (3) 5v relay boards and a DHT11 temp sensor.

These relays are mounted to the top of the controller with DuPont cables connected to GPIO pins on the pi and the temp sensor up on a few stand-offs outside of the case.


#### Network and Power

Previously I had run a bunch of network cables around the house through the crawl space and luckily I was able to re-purpose one of these for the cause. This hardwired connection provides reliable connectivity. 

Power is fed from a 5v android wall charger in the same outlet that feeds the furnace. There was an open socket and it is switched with the furnace by US building code, so it will shutdown if something needs service later.

#### Furnace Controls

The furnace Pi is connected directly to the 12v furnace interface in parallel with the existing house thermostat controller.

This is due to the lack of confidence in the initial controllers performance and longevity, and due to the function being \*fairly important (*heat/ac + kids = must_have*).

Since the house is a rental, and the landlord likely wont approve, the main t-stat is still connected for immediate control if needed at the wall. Stealth home control!

##### Mounting

The unit is mounted in the furnace, resting in the return air path due to clearance, cable pathway requirements, and not wanting to modify anything not mine. 

This provided an additional benefit of having a dht11 temp/humid sensor in the return air path. More sensor data!!

### Software

Everything is controlled and mapped to the home assistant dashboard over MQTT via the room-assistant system. 

#### Room Assistant Config

This config file is the meat and potatoes of the program. Find it in the `/home/$USER/room-assistant/config/local.yml`

```yaml
{% include_relative /include/room-assistant/furnace.local.yaml %}
```

#### Scripts

Some additional helper scripts were also developed to return some info on the device for integrations and status's over in home assistant. 

##### cpuUp.sh

return the uptime in seconds formatted as int

```bash
{% include_relative /include/room-assistant/script/furnace/cpuUp.sh %}
```

##### cpuTemp.sh

return the CPU reported temp

```bash
{% include_relative /include/room-assistant/script/furnace/cpuTemp.sh%}
```

##### freeMem.sh

returns the remaining RAM on the pi

```bash
{% include_relative /include/room-assistant/script/furnace/freeMem.sh%}
```

##### myDHT.py

adapted DHT11 temp sensor reading temp and humid

```py
{% include_relative /include/room-assistant/script/furnace/myDHT.py%}
```

##### temperature_sensor_code.py

read DS18B20 sensor, report value in F

```py
{% include_relative /include/room-assistant/script/furnace/temperature_sensor_code.py%}
```

##### cpuVolt.sh

return boolean if no issues with voltage (power supply failure)

```bash
{% include_relative /include/room-assistant/script/furnace/cpuVolt.sh%}
```


### Future Improvements

- Additional temp sensors affixed to the water pipe lines (hot water usage?) 
- Additional sensor in the crawl space generally (freeze protection).
- Leak detection around water pipe service connection and sprinkler branch
