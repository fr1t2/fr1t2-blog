---
title: "Smart Garage Control using Raspberry Pi and Room-Assistant"
last_modified_at: 2023-02-10T14:58:06-05:00
date: 2023-02-09T17:38:06-05:00
excerpt_separator: "<!--more-->"
excerpt: "Garage door smart controller using a Raspberry Pi, Home-Assistant and Room-Assistant providing full control of the garage door, temperature and door status monitoring, and advanced automations."
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
  - "garage control"


gallery:
  - url: /assets/images/roomassistant/GarageRaspi-solid.png
    image_path: /assets/images/roomassistant/GarageRaspi-th.png
    alt: "garage raspi wiring diagram"
    title: "Garage Wiring Diagram"

---

## Garage Raspi Overview


Smart garages are the next big thing in home automation, and with the help of a Raspberry Pi, Home-Assistant and Room-Assistant, you can easily convert your garage into a smart garage that provides full control of your garage door, temperature and door status monitoring, and advanced automations. 

In this post, we'll be covering the complete guide to building a smart garage control system using a Raspberry Pi and Room-Assistant, including the wiring, hardware, and network and power requirements. 

We'll also be discussing the various garage functions that you can add, such as relay for garage door opener, reed switch for manual doors open/closed status, PIR motion for occupancy sensor, and DHT11 temperature and humidity sensor. 

<!-- more -->

This garage controller was one of the first devices I built and integrated into Home Assistant. Using the Raspberry pi I already had on hand and some amazon sensors and relays I've successfully converted my garage into a Smart Garage!

### Garage Functions

The main goal to the automation was to get full control of the garage door opener as the 2 that came with the rental home never worked. Could we have asked the homeowners to fix or replace the units, sure but where the innovation in that? 

On top of the door control, I also added some devices to allow some advanced automatons to happen through Home Assistant.

- [x] Relay for Garage door opener *(5v relay)*
- [x] Relay for 120v outlet control *(5v relay)*
- [x] Reed Switch for Man doors open/closed status
- [x] PIR Motion for Occupancy sensor
- [x] DHT11 Temp/Humid sensor


### Wiring

Everything wires to the GPIO pins of the Raspberry Pi as seen in the photo below. Nothing too complex going on here, just don't forget the resistor for the LED. 


{% include gallery %}{: .align-center }

**Undocumented Change!** I ended up needing to add a capacitor to the PIR motion sensor as the power was not consistent at the device. Small little 4.7UF capacitor did the trick! (*Change not shown in diagram below*)
{: .notice}


## Hardware

Using on old Raspberry Pi Model B v1 that was a dumpster find, I built the controller with (2) 5v relay boards, PIR motion senor, Reed Switches for the doors, and a DHT11 temp sensor mounted to the top of the controller.

- Raspberry Pi Model B v1 
- (2) 5v relay boards
- DHT11 Temperature and Humidity Sensor
- PIR Motion Sensor
- (3) Reed Switches
- Case LED (5v blue)


![](/assets/images/raspi-full-th.png)


### Network and Power

I have a network switch in the garage for devices like this that is within 20' of the controller. Easy cable run for hardwired connectivity. 

Power is fed from the outlet that also feeds the garage door opener. It's conveniently located directly next to the opener in the ceiling.

### Garage Door Controls

Using the N/O (normally open) relay contacts I've wired the wall switch in parallel. This gives both automated functionality through the home assistant app, it also allows the wall switch to function as intended.

This has an issue where the door controller is looking for a momentary switch, press the wall switch to initiate and release once door moves. As I have a latching relay with this setup, some *trickery* was needed.

In home assistant I've created an automation that watches for state change on the relay switch, and if seen turns it back off. Less than 1 sec of delay between initiation and deactivation. 

This works like a charm for this application, turning the relay into a momentary switch.


**Automation excerpt:**

```yaml
automation:
  # If the garage latching relay has been activated,
  # turn the garage relay off immediately, creating a momentary relay
  - alias: "Turn off garage door relay"
    trigger:
        platform: state
        entity_id: switch.garage_door
        to: 'on'
    action:
        service: switch.turn_off
        entity_id: switch.garage_door
``` 

**Room-Assistant config excerpt:**

```yaml
switches:
    # Relay 1 - Garage door open/close
    - name: Garage Door
      pin: 17
      icon: mdi:garage-variant

```
### Electrical Outlet Control

Using the other relay to control an outlet in the garage for things like fans and lights. Setup the relay in Room-Assistant and then automate things in Home Assistant to control the outlet.

**Room-Assistant config excerpt**

```bash
    # Relay 2 - FAN
    - name: Garage Fan
      pin: 18
      icon: mdi:fan
```
### Door Status

Door status is attained using some reed switches mounted to the door frames, magnets mounted adjacent on the doors with wires running back to the controller. 

**Room-Assistant config excerpt:**

> [From Garage room-assistant config](https://github.com/fr1t2/HomeAutomate/blob/ef1f1596dc550156049650bb312dbbf6e7ad8477/Software/RoomAssistant/garage/config/local.yml#L112)

```yaml
gpio:
  binarySensors:
    # Garage Back Door position reed switch
    - name: Garage Back Door
      pin: 15
      deviceClass: door
    
    # Garage House Door position reed switch
    - name: Garage House Door
      pin: 4
      deviceClass: door
```

### Temperature

Using the DHT11 sensor and a script to report the temp every min (cron job through [room-assistant script](https://github.com/fr1t2/HomeAutomate/blob/master/Software/RoomAssistant/garage/script/myDHT.py). 

I'm using the old [depreciated Adafruit_Python_DHT library](https://github.com/adafruit/Adafruit_Python_DHT) due to issues with the new circuit python version and already having this working.

The sensor is mounted to the controller which is up in the unfinished rafters of the garage. This gives a skewed reading as the air up there is way hotter than below at head height.

**Room-Assistant config excerpt:**

> [From Garage room-assistant config](https://github.com/fr1t2/HomeAutomate/blob/ef1f1596dc550156049650bb312dbbf6e7ad8477/Software/RoomAssistant/garage/config/local.yml#L142)

```yaml
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

     # DHT11 Sensor reporting the humid % result
    - name: Garage Humidity
      command: 'python3.7 /home/pi/room-assistant/script/myDHT.py'
      regex: '(-?[0-9.]+)%'
      cron: '*/5 * * * *'
      icon: mdi:water-percent
      unitOfMeasurement: '%'
      deviceClass: humidity
```

### Motion

PIR sensor connected to the controller and mounted using a few standoffs to give it \*better placement. The controller is mounted upside down putting the sensor on the ceiling next to the garage door opener. It is blocked by some obstructions but overall covers the doors.

No additional scripting was required as this is supported in room-assistant. Just give the pin number and name the sensor.

**Room-Assistant config excerpt:**

> [From Garage room-assistant config](https://github.com/fr1t2/HomeAutomate/blob/ef1f1596dc550156049650bb312dbbf6e7ad8477/Software/RoomAssistant/garage/config/local.yml#L112)

```yaml
gpio:
  binarySensors:
    # PIR motion sensor
    - name: Garage Motion 1
      pin: 14
      deviceClass: motion
```

Additional debounce configuration added for motion sensor using the [Room-assistant entities configuration](https://www.room-assistant.io/guide/entities.html#debounce). This clears up any bouncy input from the device, giving a stable reading to the front end.


```yaml
entities:
  behaviors:
    garage_motion_sensor:
      debounce:
        wait: 0.75
        maxWait: 2
```

## Software
Everything is controlled and mapped to the home assistant dashboard over MQTT via the room-assistant system. 

### Room Assistant Config

This config file is the meat and potatoes of the program. Find it in the `/home/$USER/room-assistant/config/local.yml`

```yaml
{% include_relative /include/room-assistant/garage.local.yaml %}
```

### Scripts

Some additional helper scripts were also developed to return some info on the device for integrations and status's over in home assistant. 

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
{% include_relative /include/room-assistant/script/garage/cpuUp.sh %}
```

#### cpuTemp.sh

return the CPU reported temp

```bash
{% include_relative /include/room-assistant/script/garage/cpuTemp.sh%}
```

#### freeMem.sh

returns the remaining RAM on the pi

```bash
{% include_relative /include/room-assistant/script/garage/freeMem.sh%}
```

#### myDHT.py

adapted DHT11 temp sensor reading temp and humid

```py
{% include_relative /include/room-assistant/script/garage/myDHT.py%}
```

#### temperature_sensor_code.py

read DS18B20 sensor, report value in F

```py
{% include_relative /include/room-assistant/script/garage/temperature_sensor_code.py%}
```

#### cpuVolt.sh

return boolean if no issues with voltage (power supply failure)

```bash
{% include_relative /include/room-assistant/script/garage/cpuVolt.sh%}
```