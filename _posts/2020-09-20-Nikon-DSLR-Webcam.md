---
title: "Nikon DSLR Webcam"
last_modified_at: 2020-09-20T00:00:06-05:00
#layout: single
excerpt_separator: "<!--more-->"
header:
  overlay_image: "/assets/images/nikon/nikonDslr2.png"
  caption: "Photo credit: [**5it3**](https://5it3.com)"
  teaser: /assets/images/nikon/nikonDslrTeaser.png
  categories:
  - Hardware
  - Camera
  - Video
tags:
  - "Nikon DSLR"
  - Cameras
  - Webcam
  - gphoto2
  - ffmpeg
  - D3300
  - "Nikon D3300"
  - "Nikon Webcam"
  - "DSLR Webcam"
  - Linux
  - Ubuntu
  - "Zoom Webcam"
  - telecommuting 


---

Hacking together a nice webcam over USB with a [Nikon D3300](https://www.amazon.com/gp/product/B07GWKDLGT/ref=as_li_tl?ie=UTF8&tag=fr1t2-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B07GWKDLGT&linkId=b6d32dfec06e3650839e246d35088c3d) DSLR and Ubuntu Focal 20.04 to work from home.

With covid forcing me to work remotely, I needed to find a webcam and with the crisis hitting the entire world the stock available for a quality camera was limited. When the WFH orders were given, I immediately began setting up my new office and command center.
<!--more-->

*[WFH]: Work From Home


My daily life pre-covid typically had me attending meetings most of the day, and now that they are remote getting "Face-To-Face" can be difficult. My search for a webcam online was not panning out. Nothing with more than a one star rating and a lot of pissed off customers in the comments was turning up at the major re-sellers.

![Nikon D3300](/assets/images/nikon/nikonCam.png){: .align-right}

I simply refuse to buy crap, and I already have a *very* nice camera we bought a few years ago for vacations and family photo ops. I thought to my self, "I Wonder if I can use the Nikon DSLR for this?"

Off to Google I go, searching for any juicy keywords I can think of... `Nikon D3300 Ubuntu Webcam` To my surprise I actually hit some results on a few people trying various setup s and having some luck with other Nikon models, perhaps there is hope!

I owe my success to this Blog post [how-to-use-your-dslr-as-a-webcam-in-linux/](https://www.crackedthecode.co/how-to-use-your-dslr-as-a-webcam-in-linux/) which goes into great detail how and why this all works. All credit to [Ben Chapman](https://www.crackedthecode.co/), thanks for posting that great write up. Seriously go there and read that!

## Hardware Used


For this to work well I picked up some hardware that helped me along. 


[![Nikon D3300 Power supply](/assets/images/nikon/51tlzfCtMuL._AC_SL1000_.png)](https://amzn.to/35ORhKG){: .align-left}


First I found the battery would last about an hour or less if I was constantly using the camera. To solve this I picked up a tricky power supply that replaces the battery, and plugs into mains voltage powering the camera.

[Pick one up from Amazon Here for the D3300](https://amzn.to/35ORhKG)
<br>
<br>
[![Nikon D3300 USB Adapter](/assets/images/nikon/61aQeqHOUKL._AC_SL1500_white.png)](https://amzn.to/3hO8C8H){: .align-right}
<br>
I also had to get a [Nikon USB interface adapter](https://amzn.to/3hO8C8H) to plug into my PC since I had lost the original cable that came with the camera.

[Grab a USB cable from Amazon Here](https://amzn.to/3hO8C8H)

The added benefit of the new cable is that it is longer, removing the need for one of these great [USB extension cables](https://amzn.to/35Xg538). I use these everywhere I need to add a few feet of USB to a connection.

[![ESDDI LED Video Light](/assets/images/nikon/esddi.png)](https://amzn.to/2ZXbb2c){: .align-left}

While I was there I also picked up a new "cold shoe" mountable light to add to the quality of the video. You can grab the [ESDDI 176 LED Video Light here](https://amzn.to/2ZXbb2c)


This thing is great, plenty bright and it comes with swappable lenses in different colors to allow color balancing. I ended up using the amber lens as it seems to work the best in my space. 

I did need to find an old power supply to keep the light on without the battery. Luckily I keep old transformers around for just this occasion. Again, it just does not last for constant video. `Applicable DC adapter: 6.5-17V(DC Plug Dimension : 5.5mm x 2.1mm)`


## Ubuntu Install Steps

Following the directions from the blog I found, I installed the required dependencies and began looking for my camera in the supported list for Gphoto2. This was actually much easier than I expected it to be!

### Dependencies

I'm running Ubuntu Studio on my desktop PC, so I followed the Ubuntu/Debian setup steps. Refer to the original blog By Ben for the additional installation methods.

```bash
sudo apt-get install gphoto2 v4l2loopback-utils v4l2loopback-dkms ffmpeg
```

### Loading the Kernel Module

This command will load the need kernel modules for this login session. Once you reboot you will need to run this again. Instead add to `modprobe` and load the kernel persistently.


#### One Time Load

```bash
sudo modprobe v4l2loopback exclusive_caps=1 max_buffers=2
```

#### Persistent Kernel

Add to modprobe and modules.

```bash
echo "dslr-webcam" |sudo tee -a /etc/modules && echo -e "alias dslr-webcam v4l2loopback \noptions v4l2loopback exclusive_caps=1 max_buffers=2" | sudo tee -a /etc/modprobe.d/dslr-webcam.conf
```


### Discovering the Camera

To find your camera type `gphoto2 --auto-detect` which should show your camera if plugged in and turned on.


### Streaming From Camera

This assumes the camera was found with the step above. See the original blog for more details and trouble shooting.


```bash
gphoto2 --stdout --capture-movie | ffmpeg -i - -vcodec rawvideo -pix_fmt yuv420p -threads 0 -f v4l2 /dev/video0
```

### Adding to `bash_aliases`

For ease the next time you want to launch the camera and stream some sweet video of you to your local `/dev/video0` interface we need to add a line to our `~/.bash_aliases` file.

```bash
echo -e "# Nikon DSLR Webcam Stream, Camera should be connected, switched off 'auto' mode and not mounted as a drive \nalias DSLR-WebCam='gphoto2 --stdout --capture-movie | ffmpeg -i - -vcodec rawvideo -pix_fmt yuv420p -threads 0 -f v4l2 /dev/video0' |tee -a ~/.bash_aliases" && source ~/.bash_aliases
```

Now you can issue the `DSLR-WebCam` command to launch the camera stream and begin using your nice camera fro a webcam.


## Video Chat with DSLR

Now that you have a video stream at your `/dev/video0` address you should be able to utilize this camera in all of the popular video chat applications. Obviously you will need a microphone and speaker still for the chat but your video feed will be the sharpest in the group.

#### VLC Testing

You can open VLC and monitor the `/dev/video0` interface to see your camera feed and tune anything needed like zoom and focus. 

### Quality Video

There are a ton of factors that lead to a quality video feed. Too many to list here but I will hit the top few.

#### Mounting

Don't risk your fancy camera to some shoddy placement. You can only really drop these one time. Get a nice tripod to mount the camera to and ensure it is not going to be knocked over

Here are my picks for a quality tripod:

* [Manfrotto MKELEB5RD-BH Tripod](https://amzn.to/3hPhdIz)
* [GEEKOTO AT24EVO Aluminum Tripod](https://amzn.to/33NT002)


#### Lighting

Lighting is a must! Those nasty Fluorescent lights need thrown out, and new led lights put in their place. Pay attention to the color of the light and shoot for options to adjust to your complexion and room lighting conditions

* [10" LED Ring Light with Stand](https://amzn.to/3cis1xv)
* [Dimmable 5600K USB LED Video Light ](https://amzn.to/33KOOyj)

## Summary

Using my already existing camera ended up saving me money and got em up and running in no time. I'm not sure if the added stress and heavy use will end up costing more than it's worth, only time will tell. 

I can say that as soon as stock levels are back to normal I will be looking for a replacement purpose built camera for this. I find the Nikon camera body gets warm after a few hours of use and I don't want to explain how I broke the nice camera running web meetings.

