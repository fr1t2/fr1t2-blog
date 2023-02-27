---
title: "First Impressions Of GitHub Co-Pilot"
last_modified_at: 2023-02-17T11:42:00-05:00
date: 2023-02-17T07:26:06-05:00
excerpt_separator: "<!--more-->"
#excerpt: "My first impressions while using the new GitHub AI Copilot in Sublime text while developing a python program in linux."
categories:
  - development
  - ai
#layout: single
classes: wide
header:
  overlay_image: "/assets/images/github-copilot/Copilot.webp"
  overlay_filter: 0.5
  #caption: "Room Assistant on raspberry Pi Model B v1"
  teaser: "/assets/images/github-copilot/github_logo-copilot-tease.webp"
  og_image: "/assets/images/github-copilot/github_copilot_og.webp"

image:
  feature: "/assets/images/github-copilot/github_logo-copilot-tease.webp"
  thumb: "/assets/images/github-copilot/github_logo-teaser-sq.webp" #keep it square 200x200 px is good

tags:
  - Github
  - Copilot
  - Artifical Intelegence
  - Development
  - Code
  - Python
  - Sublime Text

---

GitHub Copilot is a groundbreaking new tool that has taken the world of software development by storm. It's a revolutionary technology that uses artificial intelligence (AI) to assist developers in writing code.


{: .notice--primary }
"GitHub Copilot uses the OpenAI Codex to suggest code and entire functions in real-time, right from your editor." - [Github](https://github.com/features/copilot)


<!--more-->

## Introduction

[![github-copilot logo](/assets/images/github-copilot/github_logo-copilot-tease-th.webp){: .align-left}](https://github.com/features/copilot)

GitHub Copilot, the AI-powered code generation tool, has been making waves in the software development community since its beta release in June 2021. 

With its ability to generate code based on natural language descriptions of tasks and context, Copilot promises to save developers time and effort in writing code. But does it live up to the hype? 

In this blog post, we'll share our first impressions of Copilot and explore its potential benefits and limitations for developers. Whether you're a seasoned developer or just getting started in the world of code, read on to learn more about this exciting new tool.

### What is Github Copilot

GitHub Copilot is an AI-powered code assistant that can generate code suggestions and complete lines of code within a developer's integrated development environment (IDE). It uses machine learning models to suggest code based on the context of the code being written and can even write entire functions or classes. 

Copilot is built on OpenAI's Codex technology and is trained on a massive dataset of publicly available source code. It is available as a plugin for multiple IDE's and can be used for a wide range of programming languages, including Python, JavaScript, TypeScript, Ruby, and Go.

[![github-copilot logo](/assets/images/github-copilot/OpenAI_Logo-sm.webp){: .align-center}](https://openai.com/)

Overall, GitHub Copilot aims to improve the speed and accuracy of code development by providing developers with intelligent code completion suggestions based on their context and previous coding patterns.

### How does Github Copilot work

GitHub Copilot works by using a machine learning model trained on a vast amount of code from open source repositories to generate suggestions for completing lines of code. It uses a type of artificial intelligence known as GPT (Generative Pre-trained Transformer) to predict what code you might want to write next based on the context of the code you've already written.

To use GitHub Copilot, you simply start typing in your code editor, and it will provide suggestions for how to complete the current line or block of code. These suggestions are based on the context of the code you've already written and can range from simple code snippets to entire functions. Could not be simpler!

GitHub Copilot also allows you to give it examples of what you want to achieve, and it will generate code for you based on those examples. You can also train it to recognize specific code patterns or styles that you frequently use, allowing it to provide more accurate suggestions in the future.

### The significance of Github Copilot in AI-assisted programming

GitHub Copilot is a significant advancement in programming as it has the potential to revolutionize the way developers write code. With Copilot and other systems like it, developers can save time and increase productivity by having an AI assistant that can generate code snippets and suggest code completions in real-time. This can help developers to focus on the high-level logic of their code and allow the AI to handle some of the more mundane aspects of coding.

Additionally, GitHub Copilot has the potential to democratize coding making it more accessible to a wider range of people. The tool can be used to generate functional code in multiple programming languages and can help beginners and experts alike to write better code, faster. This can help to level the playing field in the tech industry and make coding more inclusive.

## Installation and setup

Before any integration or usage of the Copilot system you have to log in and subscribe to the feature over on GitHub. 

As of the time of writing this they are offering a 60 day free trial of the system. After this free trial the monthly fee is **$10** or **$100** per yearly subscription *(\*savings of $20 for the yearly subscription)*

### Configuring Github Copilot

Log into your github account and head to the settings under your avatar in the top right corner.

Under the copilot tab, sign up for the free trial and add payment details for after the trial ends. You can cancel anytime however if you go past the date they give you there will be a charge to the payment method provided.

### Sublime Text Github Copilot Setup

I use [Sublime Text](https://www.sublimetext.com/) to develop on as I like the simple interface wilt little fuss. While there are likely functions of more robust IDE's out there I would enjoy, I've paid for a license for this and have gotten quite used to it to make a change. Luckily for me I found this plugin available to be added on to the editor.


[![sublime text logo](/assets/images/github-copilot/sublime-text-logo-med.webp){: .align-center}](https://www.sublimetext.com/)


The project [LSP-Copilot](https://github.com/TerminalFi/LSP-copilot) is a plugin for the copilot system for sublime text editor, allowing the Copilot AI access to the project you are working on. Installation is simple following the steps found in the github repo.

> Installation instructions below taken from the [LSP-copilot Readme](https://github.com/TerminalFi/LSP-copilot/blob/master/README.md)

1. Using the package manager install the `LSP` package
2. Using the package manager install the `LSP-Copilot` package
3. Open the `command palette` using the Tools menu or hitting `ctrl + shift + p` enter the `Copilot: Sign In` command
4. Follow the prompts to authenticate LSP-copilot

  * The User Code will be auto copied to your clipboard
  * Paste the User Code into the pop-up GitHub authentication page
  * Return to Sublime Text and press OK on the dialog
  * If you see a "sign in OK" dialog, LSP-copilot should start working

You can check the status of the system by using the `Copilot: Check Status` command which should pop up a window showing the user who is logged in.

> "*GitHub Copilot support for Sublime Text LSP plugin provided through Copilot.vim.*" - *[LSP-Copilot](https://github.com/TerminalFi/LSP-copilot)*


## Ethical concerns of using AI in code development

As AI technology continues to develop and become more prevalent in various industries, it's becoming increasingly important to address the concerns surrounding its use. Here we cover a few of the issues that are on the horizon.

### Intellectual Property and Copyright

Copilot can generate code based on existing code and programming concepts, which raises questions about who owns the intellectual property rights for the code generated. It's important to ensure that the use of AI tools like Copilot does not infringe on the intellectual property rights of others.

To avoid the use of any publicly available code snips being used in the responses, you can configure the `Suggestions matching public code *` setting in your github settings under the Copilot tab to `Block`.

With this defined the results available may be limited but the potential for infringing code is reduced significantly however, it may not prevent all potential intellectual property rights issues, especially if the public code snippets used as a basis for the generated code are not properly attributed or licensed. 

### Large Potential for Bias 

AI models are trained on existing data and can perpetuate biases that exist in that training data, such as racial or gender biases. If not carefully monitored, this can result in biased code that perpetuates or even amplifies these biases. One of the best ways to help combat this is to allow the model access to use your (hopefully) unbiased code to learn from. This will provide additional context for future help provided by the AI.

As you code and use the Copilot, it is important to audit the code provided for both accuracy and functionality, but also with this bias in mind.


### Over reliance on Github Copilot

As developers become more reliant on AI-generated code, they may lose the ability to write code manually, which can lead to a lack of understanding of how the code works and an over-reliance on pre-existing solutions. We can see this in practice with most adults born before 1980 when you had to remember important numbers. Now with the advent of cell phones and phone books contained within most people don't have these important number in memory, instead relying on the phone to keep them. 

This dependency can lead to a situation where developers are no longer able to innovate or adapt to new challenges, which can have a negative impact on the field of software development.

### Conclusion


Github Copilot is a powerful tool that can help developers write code more efficiently and effectively. However, it's important to recognize that over-reliance on AI-generated code can lead to a lack of understanding, creativity, and innovation in the field of software development. 

It's crucial that developers maintain a balance between using AI-generated code and writing code manually, and take steps to address the potential ethical, legal, and security issues that can arise. By doing so, developers can leverage the benefits of AI-powered tools while also ensuring that their code is fair, non-discriminatory, and secure. 

Ultimately, the responsible use of tools like Copilot can help to advance the field of software development and benefit society as a whole.



{: .notice }
This blog was developed with help from [OpenAI's](https://openai.com/) [ChatGPT](https://chat.openai.com/chat). Quite a few paragraphs are completely written by the AI including most of the ethical concerns section.