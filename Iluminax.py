# Iluminax! - Minisoftware para controlar el brillo y color de la pantalla #
# Autor: Genesis Vargas J #
# Website: http://www.genesisvargasj.com #
# Licencia: GPL V3 !Software Libre! #

from gi.repository import Gtk, GdkPixbuf, Gdk
from os import system
import subprocess

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
		b = Gtk.Builder()
		b.add_from_file("interfaz.glade")
		
		self.FrmPrincipal = b.get_object("FrmPrincipal")
		self.FrmInfo = b.get_object("FrmInfo")
		self.BoxHorizontal = b.get_object("eventbox1")
		self.ImagenPantalla = b.get_object("ImagenPantalla")
		self.BoxIzquiero = b.get_object("eventbox2")
		self.CambiarColorFondo(self.BoxIzquiero, "#FFF")
		self.CambiarColorFondo(self.BoxHorizontal, "#2F6EA9")
		self.CambiarColorFondo(self.FrmPrincipal, "#89A4F1")
		b.connect_signals(self)
		self.FrmPrincipal.show()
	
	def on_BtnBajo_clicked(self, button):
		CambiarBrilloPantalla(70, "pantalla1.png")
	
	def on_BtnMedio_clicked(self, button):
		CambiarBrilloPantalla(85, "pantalla2.png")
	
	def on_BtnAlto_clicked(self, button):
		CambiarBrilloPantalla(100, "pantalla3.png")
	
	def on_BtnSalir_clicked(self, button):
		Gtk.main_quit()
	
	def on_BtnInfo_clicked(self, button):
		self.FrmInfo.run()
		self.FrmInfo.hide()
	
	def on_FrmPrincipal_destroy(self, button):
		gtk.main_quit()
	
	def on_RbtnRojo_toggled(self, button):
		system("xrandr --output \%s --gamma %s" % (self.PrimerDispositivo, "1.5:1.0:1.0"))
		
	def on_RbtnAzul_toggled(self, button):
		system("xrandr --output \%s --gamma %s" % (self.PrimerDispositivo, "0.5:1.0:1.0"))
		
	def on_RbtnNormal_toggled(self, button):
		system("xrandr --output \%s --gamma %s" % (self.PrimerDispositivo, "1.0:1.0:1.0"))
		
	#procedimiento para cambiar brillo de pantalla
	def CambiarBrilloPantalla(self, numerobrillo, imagen):
		system(self.comandos_dispositivo[numerobrillo])
		self.ImagenPantalla.set_from_file("imagenes/" + imagen)
		
	#procedimiento para cambiar color de fondo a window o eventbox con el metodo modify_bg
	def CambiarColorFondo(self, widget, color):
		widget.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse(color))
		
Iluminax()
Gtk.main()
