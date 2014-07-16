#!/usr/bin/env python
# -*- coding:utf-8 -*-

import gtk
import pygtk
import subprocess
from os import system

class Iluminax():
	
	def DebugTrue(self):
		return False
	
	def DetectarDispositivos(self):
		disp_conectados = []
		salida_xrandr = subprocess.check_output('xrandr -q', shell=True)
		lineas = salida_xrandr.split('\n')
		for line in lineas:
			palabras = line.split(' ')
			for word in palabras:
				if word == 'connected':
					disp_conectados.append(palabras[0])
		return disp_conectados
	
	def __init__(self):
		b = gtk.Builder()
		b.add_from_file("interfaz.xml")
		self.DispositivosDetectados = self.DetectarDispositivos()
		self.NumDispositivosDetectados = len(self.DispositivosDetectados)
		if self.NumDispositivosDetectados == 1:
			if self.DebugTrue():
				print 'Detectado :)'
			self.PrimerDispositivo = self.DispositivosDetectados[0]
		else:
			self.PrimerDispositivo = 'No Encontrado :('
		self.comandos_dispositivo = []
		self.valor = 0.00
		for i in xrange(0, 101):
			comando_primer_dispositivo = "xrandr --output \%s --brightness %s" % (self.PrimerDispositivo, self.valor)
			self.comandos_dispositivo.append(comando_primer_dispositivo)
			self.valor += 0.01
		self.FrmPrincipal = b.get_object("FrmPrincipal")
		self.BtnCerrar = b.get_object("BtnCerrar")
		self.BtnInfo = b.get_object("BtnInfo")
		self.BtnBajo = b.get_object("BtnBajo")
		self.BtnMedio = b.get_object("BtnMedio")
		self.BtnAlto = b.get_object("BtnAlto")
		self.FrmInfo = b.get_object("FrmInfo")
		self.ImagenPantalla = b.get_object("PicturePantalla")
		b.connect_signals(self)
		self.FrmPrincipal.show()
	
	def on_BtnBajo_clicked(self, widget, data=None):
		system(self.comandos_dispositivo[70])
		self.ImagenPantalla.set_from_file("pantalla1.png")
	
	def on_BtnMedio_clicked(self, widget, data=None):
		system(self.comandos_dispositivo[85])
		self.ImagenPantalla.set_from_file("pantalla2.png")
	
	def on_BtnAlto_clicked(self, widget, data=None):
		system(self.comandos_dispositivo[100])
		self.ImagenPantalla.set_from_file("pantalla3.png")
	
	def on_BtnCerrar_clicked(self, widget, data=None):
		gtk.main_quit()
	
	def on_BtnInfo_clicked(self, widget, data=None):
		self.FrmInfo.run()
		self.FrmInfo.hide()
	
	def on_FrmPrincipal_destroy(self, widget, data=None):
		gtk.main_quit()
	
	def on_RbtnRojo_toggled(self, widget, data=None):
		system("xrandr --output \%s --gamma %s" % (self.PrimerDispositivo, "1.5:1.0:1.0"))
		
	def on_RbtnAzul_toggled(self, widget, data=None):
		system("xrandr --output \%s --gamma %s" % (self.PrimerDispositivo, "0.5:1.0:1.0"))
		
	def on_RbtnNormal_toggled(self, widget, data=None):
		system("xrandr --output \%s --gamma %s" % (self.PrimerDispositivo, "1.0:1.0:1.0"))
		
Iluminax()
gtk.main()
