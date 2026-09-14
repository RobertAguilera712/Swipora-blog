Title: Verb To Be
Date: 2026-09-09
Category: Basic Grammar
Tags: Gramática Básica
status: Draft
Summary: En este artículo aprenderás a la estructura y usos más comunes del Verb To Be. 

El **Verb To Be** es la estructura gramatical más sencilla y utilizada del
idioma inglés, por lo tanto es indispensable dominar todos sus usos. En esté artículo, veremos cual es la forma y uso del **Verb To Be**.

De manera general, el **Verb To Be** significa ser o estar y su forma es la siguiente:

{%grammar%}
:us: I am a teacher <br>
:mexico: Yo soy un maestro <br class="mb-2">

:us: You are tired <br>
:mexico: Tú estás cansado <br class="mb-2">

:us: He is strong <br>
:mexico: Él es fuerte <br class="mb-2">

:us: She is at home <br>
:mexico: Ella está en casa <br class="mb-2">

:us: It is cloudy <br>
:mexico: Está nublado <br class="mb-2">

:us: We are students <br>
:mexico: Nosotros somos estudiantes <br class="mb-2">

:us: They are angry <br>
:mexico: Ellos están enojados
{%endgrammar%}

<sub>En los ejemplos anteriores cada uno de los **pronombres personales** se encuentra
marcado con color **<span class="grammar-green">Verde</span>** y cada una de las formas del **Verb To Be**
se encuentan marcadas en color **<span class="grammar-pink">Rosa</span>**.</sub>

Como podemos ver el **Verb To Be** tiene solo 3 formas **<span class='grammar-pink'>Am</span>**, **<span class='grammar-pink'>Are</span>** y **<span class='grammar-pink'>Is</span>**, lo que lo hace muy sencillo.

## Usos del Verb To Be

A continuación, veremos cada uno de los usos del **Verb To Be**

### Descriptions with adjectives

El primer uso que tiene es el de describir un **sustantivo** con el uso de un **adjetivo**. Veamos algunos ejemplos.

{%grammar%}
:us: I am <span class='grammar-blue'>smart</span><br>
:mexico: Yo soy <span class='grammar-blue'>inteligente</span><br class="mb-2">

:us: You are <span class='grammar-blue'>strong</span><br>
:mexico: Tú eres <span class='grammar-blue'>fuerte</span><br class="mb-2">

:us: <span class='grammar-green'>The car</span> is <span class='grammar-blue'>fast</span><br>
:mexico: <span class='grammar-green'>El carro</span> es <span class='grammar-blue'>rápido</span>
{%endgrammar%}


I have a code server set up with cloudflare tunnel and I am wondering if I can move all my dev enviroment to there and integrate it with code magic. I was uisng my mac m1 to develop my flutter app but it is a pain in the neck because it runs out of space every time I compile the app


Hi! A while ago we planned a custom remote Flutter development environment, and I am now ready to set it up. 

Please provide the step-by-step terminal commands and configuration files to build this exact architecture:

### My Setup:
1. Client Device: M1 Mac (and occasionally an iPad with a keyboard) running via web browser/Remote-SSH.
2. Home Server: ThinkPad X280 (8th Gen Intel i5, 8GB RAM) running Ubuntu Server + i3 WM.
3. Network/Proxy: Cloudflare Tunnels (already running).
4. Physical Testing Device: Old Moto G Play connected via USB to the ThinkPad.
5. Cloud Builder: Codemagic (for iOS/production builds triggered via Git).

### What I need to accomplish today:
1. Linux Server Preparation: How to install the Flutter and Android SDKs on Ubuntu Server cleanly, without installing the heavy Android Studio GUI (to save the 8GB of RAM).
2. USB & ADB Permissions: How to configure Linux 'udev rules' so the server reliably detects the Moto G Play over USB, and how to start ADB in TCP/IP mode.
3. Web-Based Device Mirroring: The exact Docker Compose or systemd configuration to run `ws-scrcpy` so I can view and touch-control the Moto G Play screen directly in a browser tab.
4. Cloudflare Tunnel Config: How to route the ws-scrcpy interface (localhost:8000) through my tunnel safely.
5. Mac Cleanup: The exact terminal commands to completely purge Xcode, Android Studio, simulators, and old build caches from my local M1 Mac to free up 100+ GB of storage.

Let's start with Step 1 and 2 (Installing Flutter on the server and configuring the physical phone connection). Please give me the exact terminal commands to run on my ThinkPad!
