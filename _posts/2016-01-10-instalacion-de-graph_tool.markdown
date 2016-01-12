---
layout: post
title:  "Instalacion de graph-tool"
date:   2016-01-10 09:13:55
categories: tutorial
---

En este tutorial seguiremos instrucciones para la instalacion de el
framework para analisis de grafos [graph-tool](https://graph-tool.skewed.de/). Las instrucciones
oficiales de instalacion estan
[aqui](https://graph-tool.skewed.de/download).
El software esta basado en [Python](http://python.org) por lo que es necesario tener
*python-2.x* instalado
(recomiendo esta en vez de la version 3).

## MacOSX

Antes de empezar a instalar cualquier cosa en _MacOSX_ necesitamos tener
_Xcode_ instalado. Este lo podemos descargar de la AppStore. Luego de
tenerlo instalado, abrimos una _Terminal_ (esta en la carpeta de `/Applications`)
y escribimos: `xcode-select --install`. Luego de instalar esto
necesitamos aceptar los terminos y condiciones de _Apple_ para poder usar _Xcode_,
asi que en la misma terminal escribimos: `sudo xcodebuild -license`,
leemos y seguimos los pasos que nos idiquen.Esto deberia instalar todo el
software necesario para comenzar.

Puesto que *graph-tool* requiere varias dependencias lo mejor es usar un
gestor de paquetes como [MacPorts](https://www.macports.org/) u [Homebrew](http://brew.sh/).
Las instalaciones de ambos frameworks son elementales.

# MacPorts

Para instalar _MacPorts_ solo tenemos que ir al link de
[descarga](https://www.macports.org/install.php), descargar y ejecutar el `.dmg`
que corresponda con la version de nuestro sistema operativo.

# Homebrew (preferida)

_HomeBrew_ puede ser instalado escribiendo en la terminal el siguiente
comando:

```shell
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

**NOTA:** Si tienen otra version de _Python_, tal vez al terminar de instalar _Homebrew_ les
pida correr algunos commandos para hacer compatibles las librerias que se
instalan desde `brew` con la de su instalacion de _Python_ actual. En
los logs de instalacion estan las instrucciones (que cambian segun el
sistema asi que no tiene sentido que las ponga aqui).

Una vez que tenemos instalados _MacPorts_ u _Homebrew_ podemos instalar
_graph-tool_ con los siguientes commandos

> MacPorts: `port install py-graph-tool`

> Homebrew:
> `brew tap homebrew/science && brew install graph-tool`

**NOTA:** Es probable que _MacPorts_ necesite sudo, i.e: `sudo port install
py-graph-tool`

## Ubuntu

En _Ubuntu_ necesitamos primero agregar a nuestros sources de nuestro
gestor de paquetes _aptitude_ los de el repositorio de _graph-tool_.
Para esto abrimos una terminal y corremos los siguientes commandos

**Nota:** Las instrucciones siguientes presuponen que tenemos _trusty_
que es la ultima distribucion (a la fecha) de _Ubuntu_

```shell
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo deb http://downloads.skewed.de/apt/trusty trusty universe
sudo deb-src http://downloads.skewed.de/apt/trusty trusty universe
```

Despues actualizamos nuestro sistema con: `sudo apt-get update`. Y
finalmente instalamos _graph-tool_ con sus dependencias

```shell
sudo apt-get install python-graph-tool
```

## Despues de instalar..

Para verificar que la instalacion esta completa y correcta, abrimos una
consola de _Python_ (abrimos la terminal y escribimos `python`) y una vez adentro
escribimos: `from grap_tool import *`. Si no da
ningun mensaje de error entonces terminamos.

**NOTA:** Sin embargo puede que hayan algunos warnings. Es normal :).


