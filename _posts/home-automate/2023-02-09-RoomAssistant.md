---
title: "Room Assistant on Raspberry Pi armv6"
last_modified_at: 2023-02-09T17:38:06-05:00
date: 2023-02-09T17:38:06-05:00
categories:
  - homeAutomation
  - roomAssistant
#layout: single

excerpt: "Room Assistant & Raspi armv6 installation and configuration"
#excerpt_separator: "<!--more-->"
header:
  overlay_image: "/assets/images/room-assistant-header.png"
  #caption: "Room Assistant on raspberry Pi Model B v1"
  teaser: "https://www.room-assistant.io/room-assistant.png"
image:
  feature: "/assets/images/room-assistant-header.png"
  thumb: "/assets/images/room-assistant250.png" #keep it square 200x200 px is good
tags:
  - Homeassistant
  - hass
  - room-assistant
  - "raspberry pi"
  - automation
  - controls
  - IoT
classes: wide
toc: true
sidebar:
  title: "Home Automation"
  nav: home-automation

feature_row:
  - image_path: "../assets/images/roomassistant/SprinklerRaspi.png"
    alt: "sprinkler raspi wiring"
    title: "Sprinkler Control"
    excerpt: "Sprinkler zond controls and automation for an 8 zone system."
    url: "/blog/homeautomation/roomassistant/RoomAssistant_Sprinkler/"
    btn_label: "Read More"
    btn_class: "btn--inverse"
  - image_path: "../assets/images/roomassistant/FurnaceRaspi.png"
    alt: "furnace wiring"
    title: "Furnace Control"
    excerpt: "HVAC Controls for Heat and AC through Home Assistant"
    url: "/blog/homeautomation/roomassistant/RoomAssistant_Furnace/"
    btn_label: "Read More"
    btn_class: "btn--inverse"
  - image_path: "../assets/images/roomassistant/GarageRaspi.png"
    alt: "garage raspi wiring"
    title: "Garage Control"
    excerpt: "Garage Controls, including overhead door."
    url: "/blog/homeautomation/roomassistant/RoomAssistant_Garage/"
    btn_label: "Read More"
    btn_class: "btn--inverse"


#  - image_path: /assets/images/roomassistant/kitchen/KitchenRaspi.png
#    alt: "kitchen raspi wiring"
#    title: "Kitchen Control"
#    excerpt: "Kitchen controls and monitoring."
#    url: "/homeautomation/roomassistant/RoomAssistant_Furnace/"
#    btn_label: "Read More"
#    btn_class: "btn--inverse"

#  - image_path: /assets/images/roomassistant/office/OfficeRaspi.png
#    alt: "office raspi wiring"
#    title: "Office Control"
#    excerpt: "Control and monitoring for the Office"
#    url: "/homeautomation/roomassistant/RoomAssistant_Furnace/"
#    btn_label: "Read More"
#    btn_class: "btn--inverse"
---


![](/assets/images/room-assistant250.png ){: .align-left} 



I've spent years searching for a home automation system that meets my needs, which is not an easy task. 
My criteria is a little strict on what I will allow into my private life and home. 

What started as a want to control the sprinkler from my phone lead down a dark and lonely path, 
full of shady vendors wanting into my private network to scrape my data. Looking at commercial 
solutions left me discouraged, around every corner someone trying to take your data for their own use (looking at you amazon...) 

During the search for the perfect solution a few key pieces fell into place:

- I discovered [Home Assistant](https://www.home-assistant.io/) and began using it to collect all of my devices into a single dashboard. My data stays home (mostly)
- I was given 30+ old Raspberry Pi's that were installed in a commercial application that was sunset and removed. Instead of the dumpster I gave them a new home.

Now I just needed a way to use all of these old Raspberry Pi's to interface with my world and home assistant. 

**Enter Room-Assistant!**

> Using recycled hardware, Open Source projects, some time and ingenuity, I've managed to automate my house!

I settled on building custom devices on the [Room assistant platform](https://www.room-assistant.io/), communicating with Home Assistant through MQTT, 
using [Raspberry Pi single board computers](https://www.raspberrypi.com/).

These Raspi's came with nice little milled aluminum cases that keep the pi cool that allows a variety of devices to be mounted to the case, 
such as relay boards and occupancy sensors. Off to building some IoT devices to make controlling our environment easier and more efficient.


Once I had the software installed and all of the required packages configured deploying a device could not be easier. 
Setup the GPIO pins for the devices you are using and start the system. MQTT connections and sensor additions happened automagically 
in Home Assistant and began talking immediately.

{% include feature_row %}

### Deployed devices


The table below contains all of the devices I have deployed using the home assistant software and these old raspi's. I've included the config files and scripts used to set 
these devices up in their respective blog pages.


| Room | Device Use  | Config |
| --- |--- | --- |
| [Furnace](/blog/homeautomation/roomassistant/RoomAssistant_Furnace/) | Relays connected through the furnace heat, cool and fan functions, temp/humid sensor in the return air path. Wired in parallel with wall thermostat for backup control of the furnace. Wall unit is switched off. | [Furnace Config File](/assets/file/room-assistant/furnace.local.yaml) |
| [Kitchen](/blog/homeautomation/roomassistant/RoomAssistant_Kitchen) | Temperature/humidity, motion, light control. Connected through Ubiquity Pico station as a client for remote network location | [Kitchen Config File](/assets/file/room-assistant/kitchen.local.yaml) |
| [Sprinkler](/blog/homeautomation/roomassistant/RoomAssistant_Sprinkler) | Sprinkler controls for 6 zones plus the common leg to sprinkler solenoids This is connected in parallel with the usual sprinkler controller allowing either to activate zones as needed. Also connected through a physical switch to activate individual zones. | [Sprinkler Config File](/assets/file/room-assistant/sprinkler.local.yaml) |
| [Garage](/blog/homeautomation/roomassistant/RoomAssistant_Garage) | Garage door control, temp sensor, overhead fan, door monitoring, motion sensor. | [Garage Config File](/assets/file/room-assistant/garage.local.yaml) |
| [Office](/blog/homeautomation/roomassistant/RoomAssistant_Office) | Test bed for room assistant installs. Motion sensor and relay for lights poorly implemented   | [Office Config File](/assets/file/room-assistant/office.local.yaml) |




## Typical installation

> Raspberry Pi Model B v1 (arm6) setup

Installing and configuring the raspi to work with home assistant as a stand alone room instance. This allows 
a variety of automation and sensor measurements to be easily deployed.


### Install OS

Using the latest raspiOS found at [The Raspberry Pi site](#) install to an SD card

#### raspi-config

- resize fs
- change localization/keyboard
- change password
- set hostname
- enable ssh
- enable camera
- set over-clock to medium
- set GPU to 144

#### Update && upgrade 

`sudo apt-get update && sudo apt-get upgrade -y && sudo reboot`

#### Install Room-Assistant

I use the node version of the room-assistant package. Though there are other ways to run that may suit your needs, 
this fit mine just fine and works, the most important point!

##### Install Node Arm6l


Following the guide at [https://www.room-assistant.io](https://www.room-assistant.io/guide/installation.html#running-with-nodejs) it points us to install version 14 or 12 of NodeJS. to accomplish this on the arm6 chip follow these steps.


```bash
wget https://unofficial-builds.nodejs.org/download/release/v12.18.3/node-v12.18.3-linux-armv6l.tar.gz
tar -xzf node-v12.18.3-linux-armv6l.tar.gz
cd node-v12.18.3-linux-armv6l
sudo cp -R * /usr/local
```

check the node version with `node --version`

##### Dependencies

With that out of the way install dependencies for the control software.

```bash
sudo apt-get install libavahi-compat-libdnssd-dev
```

##### Installation

```bash
sudo npm i --global --unsafe-perm room-assistant
```

##### Create a Service

Add this to systemd to enable automatic restarts after power loss.

edit/create the file `nano /etc/systemd/system/room-assistant.service`
 
```sh
[Unit]
Description=room-assistant service

[Service]
ExecStart=/usr/local/bin/room-assistant
WorkingDirectory=/home/pi/room-assistant
Restart=always
RestartSec=10
User=pi

[Install]
WantedBy=multi-user.target
```
Enable the service on restart

```bash
sudo systemctl enable room-assistant.service
```

#### Install scripts

Install and configure scripts to suit installation.

For temp/humidity dht11 sensors, use the following command to install
```bash
sudo apt-get install -y python3-pip && sudo python3 -m pip install --upgrade pip setuptools wheel && sudo pip3 install Adafruit_DHT
```

Set permissions 

`chmod +x /home/pi/room-assistant/script/*`

#### Configure Room-Assistant

Now that we have the packages loaded and the pi all up to date, create a room-assistant directory with sub-directories config, script. We will need to create a config file named `local.yaml` in the config file. 

make the directory for the config to live

`mkdir -p /home/pi/room-assistant/config /home/pi/room-assistant/script`

See this example below for the basic structure and layout from my Furnace control device. This must be in valid YAML format to run the software.

```yaml
{% include_relative /include/room-assistant/furnace.local.yaml %}
```

Edit the configuration to suit the device at hand and start the system manually to verify function and catch any errors.

```bash
cd ~/room-assistant
room-assistant
```

Watch the console load the software and once complete check your home assistant dashboard for the new devices.

Once the system is running error free in the cli restart it using the system service setup earlier

```bash
sudo systemctl start room-assistant.service
```

## Upgrading

Following the [great room-assistant documentation ](https://www.room-assistant.io/guide/upgrading.html#upgrading) updating is simple enough. 


Stop the service for the time being:

```bash
sudo service room-assistant stop
```
Since we are using the node version, run the following to upgrade:

```bash
sudo npm i --global --unsafe-perm room-assistant
```
> This is very process heavy and may take a long time on the pi. Recommend running in a `screen` session to detach.

Config files and scripts live in the same locations and configuration directives \*should not change across versions.


Have fun!