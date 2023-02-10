---
title: "Blog.Fr1t2.com"
last_modified_at: 2020-09-20T22:38:06-05:00
#layout: single
excerpt_separator: "<!--more-->"
categories:
  - blog
  - intro
header:
  overlay_image: "/assets/images/firstBlog/making.blog.fr1t2CropFaded.png"
  caption: "Blog development"
  teaser: /assets/images/firstBlog/making.blog.fr1t2Teaser.png
  categories:
  - Blog
tags:
  - Jekyll
  - html
  - bloging
  - markup
  - css

---

A place to house my random thoughts!
<!--more-->

Welcome to my blog! Strange that it's now 2020 and I just got around to setting this up. Needles to say I have a ton of information to post that I hope will be interesting, even to only a small group of nerds like me.

I've created this place to house my random thoughts, walkthroughs and helpful tips that I stumble across in life. All opinions are my own and don't reflect anyone else's.

> No one said you have to have it all figured out, just give it a try and don't give up!



{% include figure image_path="/assets/images/firstBlog/making.blog.fr1t2Crop.png" alt="this is a placeholder image" caption="Building the new Blog!" %}


## Blog Topics

I write about what I'm interested in. I hope you share some of the same interests. If you like what you read, or would like to get in contact, please reach out. Bio in the links.

Random ramblings on various topics from technology to ideology:

- Renewable energy
- Automation
- Integration
- Family life
- Politics
- Construction
- Problem solving
- General *bad-assery*


## Building this Blog

This blog is built with most credit going out to the [Jekyll]() and the [Minimal Mistakes Theme]() developers. Without them I would not be here today, serving you these words.

These services remove most of the burden that usually comes with web development. While some of you may say it is not truly web development without banging your head against CSS bugs and learning about security the hard way. Well I'm here to tell you there is another way! *haha who am I kidding, I will still be learning these lessons the hard way.*

* Domain purchased through [domains.google.com](https://domains.google.com/)
* DNS hosted on [cloudflare CDN](https://www.cloudflare.com/)
* Cloud server hosted on a $5 [Digital Ocean](https://m.do.co/c/139fae3d80b5) VPS
    * Ubuntu Server 20.04
    * Apache2 Webserver
    * Fail2Ban
* Code hosted at github for local development and remote deployment, plus version management


*[VPS]: Virtual Private Server - Someone else's computer aka "The Cloud"



## Blog Hosting Tips

Some important commands I use to launch the blog.

### Jekyll Clean

```bash
bundle exec jekyll clean 
```

### Bundle install Gem's

```bash
bundle install
```

### Jekyll Build

```bash
bundle exec jekyll build
```

### Algolia Search Index

Push the site index to the search index. See the [minimal-mistakes docs](https://mmistakes.github.io/minimal-mistakes/docs/configuration/#algolia) for instructions on getting this setup in the `_config.yaml` file.

Also see [Algolia](https://www.algolia.com/) for API keys and information on who is searching where...

```bash
ALGOLIA_API_KEY='WOULDNT-YOU-LIKE-TO-KNOW' jekyll  algolia 
```

### Serve the Site Locally

Will serve the site locally on `port: 4000`

```bash
bundle exec jekyll serve
```

### Deploy Live

Copy the entire \_site directory to your webhost and change the owner to the apache2 web host owner `www-data`

From inside of the freshly built root directory fire off:

```bash
sudo cp -r ./_site/* /var/www/html && sudo chown -R www-data:www-data /var/www/html
```

