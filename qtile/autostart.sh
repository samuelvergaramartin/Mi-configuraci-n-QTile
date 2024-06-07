#!/bin/bash

#configuración del teclado en español

setxkbmap es &

#iconos del sistema

udiskie -t &

nm-applet &

volumeicon &

cbatticon -u 5 &

nitrogen --restore &

#configuración transparencia para las terminales

picom &

xset s off
xset -dpms
lxpolkit & 
