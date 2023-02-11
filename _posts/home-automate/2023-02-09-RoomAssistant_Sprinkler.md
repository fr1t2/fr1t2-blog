---
title: "Room Assistant - Sprinkler Raspi"
last_modified_at: 2023-02-10T17:35:06-05:00
date: 2023-02-09T17:38:06-05:00
excerpt_separator: "<!--more-->"
excerpt: "Smart sprinkler controller built using a Raspberry Pi, Home-Assistant, and Room-Assistant for full IoT control."
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
  - "Smart Sprinkler"
  - "Sprinkler Control"


gallery:
  - url: /assets/images/roomassistant/SprinklerRaspi-solid.png
    image_path: /assets/images/roomassistant/SprinklerRaspi-th.png
    alt: "garage raspi wiring diagram"
    title: "Garage Wiring Diagram"

---

## Sprinkler Raspi Overview


Raspberry Pi Model B v1 and a bunch or relays used as a smart sprinkler controller and extension of my [Home Assistant](https://www.room-assistant.io/) installation.

<!-- more -->


Using an old raspberry pi Model B and a few relay boards I have control of my "dumb" sprinkler controller through parallel 24v connections to the yard solenoids. This allows greater functionality in my rental house by allowing the old, landlord provided, controller to function. 

I additionally wired in a switch panel that allows for manual control of the zones in case the kids want to play, or I need to test functionality outside of software for things like blowing out the lines for winter.

- Sprinkler Zone Control
- \*Future Rain Sensor
- \*Future soil moisture sensor


### Sprinkler Info and Use

The sprinkler controls present to home assistant as switches from the Room-Assistant instance running in the garage connected to the relay boards through GPIO pins.

This allows simple interfacing and automation. For that I have laid out these primary goals to achieve a quality sprinkler system.

- [x] Full scheduling control of each zone
- [x] Multiple schedules to allow for complex watering routines
- [x] Easy manual control of all zones
- [x] Status of any running zone
- [x] Parallel control through the commercial controller, manual switches and automation software
- [ ] Rain sensing connected to reliable API's and/or a rain sensor
- [ ] Outdoor temp and humidity monitoring


### Wiring

Everything wires to the GPIO pins of the Raspberry Pi and to solenoids in the yard as seen in the photo below.

{% include gallery %}{: .align-center }


## Hardware

This controller is running [Room Assistant](https://github.com/mKeRix/room-assistant) living next to the existing off-the-shelf sprinkler controller provided with the house. 

In order to keep the original sprinkler controller functional, the relays are wired in parallel to the controller. Additionally I added a bank of switches to the mix for good measure and over complexity! 

The solenoid power is controlled through an 8 relay board, as well as an additional 2 relay board for a "rain cutout" that removes the common leg from the entire system *(more on that later)*. These relays are controlled through GPIO pins on the Raspberry Pi 

![](/assets/images/raspi-full-th.png)

These relays are enrolled in the home assistant system and are controllable through the dashboard and with automatons.

### Network and Power

Network and power are both at the device located in the garage equipment rack. Nothing of note here.

### Controls

Relays controlling sprinkler zones handle the majority of the heavy lifting for this device.

**Room-Assistant config excerpt:**

```yaml
gpio:
  switches:
    # Each zone wired into a relay to switch the 24V solenoid and release the water
    # Relay 1 - Side yard zone 1
    - name: sprinkler zone 1
      pin: 14
      icon: mdi:sprinkler-variant
```

## Software

Following the great example set by Github user [@rgconrad514](https://github.com/rgconrad514) and the [home-assistant sprinkler controller](https://github.com/rgconrad514/Home-Assistant-Sprinkler-Controller) I integrated the controls of the GPIO on the raspi into home assistant.

This allows enabling of multiple schedules for each zone with individual zone run times allowing the city water schedules to be met.


### Room Assistant Config

This config file is the meat and potatoes of the program. Find it in the `/home/$USER/room-assistant/config/local.yml`

```yaml
{% include_relative /include/room-assistant/sprinkler.local.yaml %}
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
{% include_relative /include/room-assistant/script/sprinkler/cpuUp.sh %}
```

#### cpuTemp.sh

return the CPU reported temp

```bash
{% include_relative /include/room-assistant/script/sprinkler/cpuTemp.sh%}
```

#### freeMem.sh

returns the remaining RAM on the pi

```bash
{% include_relative /include/room-assistant/script/sprinkler/freeMem.sh%}
```

#### myDHT.py

adapted DHT11 temp sensor reading temp and humid

```py
{% include_relative /include/room-assistant/script/sprinkler/myDHT.py%}
```

#### temperature_sensor_code.py

read DS18B20 sensor, report value in F

```py
{% include_relative /include/room-assistant/script/sprinkler/temperature_sensor_code.py%}
```

#### cpuVolt.sh

return boolean if no issues with voltage (power supply failure)

```bash
{% include_relative /include/room-assistant/script/sprinkler/cpuVolt.sh%}
```