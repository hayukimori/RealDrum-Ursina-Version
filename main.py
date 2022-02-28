import os, sys
from ursina import *
import drumconfig as dc
from importlib import reload as rlib

app = Ursina()


################ [[RECEBER DRUMKIT]] ######################
drumkit = dc.kit + "/"
###########################################################


## ==> Define texturas
bg_texture = drumkit + "fundo"
kickl_texture = drumkit + "kickl"
kickr_texture = drumkit + "kickr"
snare_texture = drumkit + "snare"
tom1_texture = drumkit + "tom1"
tom2_texture = drumkit + "tom2"
tom3_texture = drumkit + "tom3"
crashm_texture = drumkit + "crashm" 
crashl_texture = drumkit + "crashl"
crashr_texture = drumkit + "crashr"
ride_texture = drumkit + "ride"
closehhl_texture = drumkit + "closehhl"
openhhl_texture = drumkit + "openhhl"
floortom_texture = drumkit + "floorr"

		
## ==> Define sons
kickl_sound = drumkit + "kick.mp3"
kickr_sound = drumkit + "kick.mp3"
snare_sound = drumkit + "snare.mp3"
tom1_sound = drumkit + "tom1.mp3"
tom2_sound = drumkit + "tom2.mp3"
tom3_sound = drumkit + "tom3.mp3"
crashm_sound = drumkit + "crashm.mp3"
crashl_sound = drumkit + "crashl.mp3"
crashr_sound = drumkit + "crashr.mp3"
ride_sound = drumkit + "ride.mp3"
closehhl_sound = drumkit + "closehh.mp3"
openhhl_sound = drumkit + "openhh.mp3"
floortom_sound = drumkit + "floor.mp3"
##


background	= Entity(model='quad', texture=bg_texture, scale=(16*camera.aspect_ratio,9*camera.aspect_ratio), z=.3, y=-.5)

class GraphicalDrum(Entity):
	def __init__(self):
		super().__init__()

		self.kickl = Entity(
			model='quad',
			texture=kickl_texture, 
			scale=3.2, 
			y=-3, 
			x=-1.7, 
			z=-.1
			)

		self.kickr = Entity(
			model='quad', 
			texture=kickr_texture, 
			scale=3.2, 
			y=-3, 
			x=1.6, 
			z=-.1
			)

		self.snare = Entity(
			model='quad', 
			texture=snare_texture, 
			scale=3.2, 
			y=-1.2, 
			x=0, 
			z=-.3
			)

		self.tom1 = Entity(
			model='quad', 
			texture=tom1_texture, 
			scale=2.5, 
			y=-.2, 
			x=-2.2, 
			z=-.5
			)

		self.tom2 = Entity(
			model='quad', 
			texture=tom2_texture, 
			scale=2.5, 
			y=.9, 
			x=0, 
			z=-.5
			)

		self.tom3 = Entity(
			model='quad', 
			texture=tom3_texture, 
			scale=2.5, 
			y=-.2, 
			x=2.2, 
			z=-.5
			)

		self.crashm = Entity(
			model='quad', 
			texture=crashm_texture, 
			scale=2.2, 
			y=1.8, 
			x=-1.8, 
			z=-.7
			)

		self.crashl = Entity(
			model='quad', 
			texture=crashl_texture, 
			scale=3.5, 
			y=1, 
			x=-4.5, 
			z=-.7)

		self.crashr = Entity(
			model='quad', 
			texture=crashr_texture, 
			scale=2.8, 
			y=1.9, 
			x=1.6, 
			z=-.7
			)

		self.ride = Entity(
			model='quad', 
			texture=ride_texture, 
			scale=3.5, 
			y=.9, 
			x=4.6, 
			z=-.9
			)

		self.close_hh = Entity(
			model='quad', 
			texture=closehhl_texture, 
			scale=2.8, 
			y=-1.2, 
			x=-5.2, 
			z=-.2
			)

		self.open_hh = Entity(
			model='quad', 
			texture=openhhl_texture, 
			scale=2.8, 
			y=-2.8, 
			x=-5.3, 
			z=-.1
			)

		self.floortom = Entity(
			model='quad', 
			texture=floortom_texture, 
			scale=3.6, 
			y=-2.7, 
			x=5, 
			z=-.1
			)


		self.kickl.update = self.KickLUpdate
		self.kickr.update = self.KickRUpdate
		self.snare.update = self.SnareUpdate
		self.tom1.update = self.Tom1Update
		self.tom2.update = self.Tom2Update
		self.tom3.update = self.Tom3Update
		self.crashm.update = self.CrashMUpdate
		self.crashl.update = self.CrashLUpdate
		self.crashr.update = self.CrashRUpdate
		self.ride.update = self.RideUpdate
		self.close_hh.update = self.CloseHHUpdate
		self.open_hh.update = self.OpenHHUpdate
		self.floortom.update = self.FloorTomUpdate



		# => Update sections


	def KickLUpdate(self):
		if held_keys[dc.kickl_key]:
			self.kickl.scale = 3.1
		else:
			self.kickl.scale = 3.2


	def KickRUpdate(self):
		if held_keys[dc.kickr_key]:
			self.kickr.scale = 3.1
		else:
			self.kickr.scale = 3.2


	def SnareUpdate(self):
		if held_keys[dc.snare_key[0]] or held_keys[dc.snare_key[1]]:
			self.snare.scale = 3.1
		else:
			self.snare.scale = 3.2


	def Tom1Update(self):
		if held_keys[dc.tom1_key]:
			self.tom1.scale = 2.4
		else:
			self.tom1.scale = 2.5


	def Tom2Update(self):
		if held_keys[dc.tom2_key]:
			self.tom2.scale = 2.4
		else:
			self.tom2.scale = 2.4


	def Tom3Update(self):
		if held_keys[dc.tom3_key]:
			self.tom3.scale = 2.4
		else:
			self.tom3.scale = 2.5


	def CrashMUpdate(self):
		if held_keys[dc.crashm_key[0]] or held_keys[dc.crashm_key[1]]:
			self.crashm.scale = 2.1
		else:
			self.crashm.scale = 2.2


	def CrashLUpdate(self):
		if held_keys[dc.crashl_key[0]] or held_keys[dc.crashl_key[1]]:
			self.crashl.scale = 3.4
		else:
			self.crashl.scale = 3.5


	def CrashRUpdate(self):
		if held_keys[dc.crashr_key[0]] or held_keys[dc.crashr_key[1]]:
			self.crashr.scale = 2.7
		else:
			self.crashr.scale = 2.8


	def RideUpdate(self):
		if held_keys[dc.ride_key[0]] or held_keys[dc.ride_key[1]]:
			self.ride.scale = 3.4
		else:
			self.ride.scale = 3.5


	def CloseHHUpdate(self):
		if held_keys[dc.close_hh_key[0]] or held_keys[dc.close_hh_key[1]]:
			self.close_hh.scale = 2.7
		else:
			self.close_hh.scale = 2.8

	def OpenHHUpdate(self):
		if held_keys[dc.open_hh_key[0]] or held_keys[dc.open_hh_key[1]]:
			self.open_hh.scale = 2.7
		else:
			self.open_hh.scale = 2.8

	def FloorTomUpdate(self):
		if held_keys[dc.floortom_key[0]] or held_keys[dc.floortom_key[1]]:
			self.floortom.scale = 3.5
		else:
			self.floortom.scale = 3.6



		# Assign 


#############################################
#	GET USER INPUT FUNCTION (FROM URSINA)   #
#############################################

def input(key):
	# Kick L + R Sound
	if key == dc.kickl_key or key == dc.kickr_key:
		Audio(kickl_sound, volume=dc.kickl_vol)

	# Snare Sound
	if key == dc.snare_key[0] or key == dc.snare_key[1]:
		Audio(snare_sound, volume=dc.snare_vol)

	# Tom 1 Sound
	if key == dc.tom1_key:
		Audio(tom1_sound, volume=dc.tom1_vol)

	# Tom 2 Sound
	if key == dc.tom2_key:
		Audio(tom2_sound, volume=dc.tom2_vol)

	# Tom 3 Sound
	if key == dc.tom3_key:
		Audio(tom3_sound, volume=dc.tom3_vol)

	# CrashM Sound
	if key == dc.crashm_key[0] or key == dc.crashm_key[1]:
		Audio(crashm_sound, volume=dc.splash_vol)

	# Crash R Sound
	if key == dc.crashr_key[0] or key == dc.crashr_key[1]:
		Audio(crashr_sound, volume=dc.crashr_vol)

	# Crash L Sound
	if key == dc.crashl_key[0] or key == dc.crashl_key[1]:
		Audio(crashl_sound, volume=dc.crashl_vol)

	# Ride Sound
	if key == dc.ride_key[0] or key == dc.ride_key[1]:
		Audio(ride_sound, volume=dc.ride_vol)

	# Close HH Sound
	if key == dc.close_hh_key[0] or key == dc.close_hh_key[1]:
		Audio(closehhl_sound, volume=dc.close_hh_vol)

	# Open HH Sound
	if key == dc.open_hh_key[0] or key == dc.open_hh_key[1]:
		Audio(openhhl_sound, volume=dc.open_hh_vol)

	# FloorTom Sound
	if key == dc.floortom_key[0] or key == dc.floortom_key[1]:
		Audio(floortom_sound, volume=dc.floortom_vol)



def main():
	windowConfiguration()
	drum = GraphicalDrum()


def windowConfiguration():
	window.title = "RealDrum Linux"
	window.borderless = False
	window.fullscreen = False
	window.exit_button.visible = False
	window.fps_counter.enabled = False
	camera.y = -.5


if __name__ == "__main__":
	main()

app.run()


#window.forced_aspect_ratio = 1.769


# CÓDIGO NOVO
