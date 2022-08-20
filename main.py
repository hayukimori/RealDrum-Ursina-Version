import os, sys, shutil
from ursina import *
from importlib import reload as rlib
import configparser
import vlc

app = Ursina()
parser = configparser.ConfigParser()




class Cardinal:
	def __init__(self):
		print("Cardinal started")

	def defineVars():
		Cardinal.defineSounds()
		Cardinal.defineTextures()
		Cardinal.defineKeys()
		Cardinal.defineVolume()
		Cardinal.defineAudio()

	def defineSounds():

		global kickl_sound
		global kickr_sound
		global snare_sound
		global tom1_sound
		global tom2_sound
		global tom3_sound
		global crashm_sound
		global crashl_sound
		global crashr_sound
		global ride_sound
		global close_hh_sound
		global open_hh_sound
		global floortom_sound
		

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
		close_hh_sound = drumkit + "closehh.mp3"
		open_hh_sound = drumkit + "openhh.mp3"
		floortom_sound = drumkit + "floor.mp3"



	def defineTextures():
		## ==> Define texturas
		global bg_texture
		global kickl_texture
		global kickr_texture
		global snare_texture
		global tom1_texture
		global tom2_texture
		global tom3_texture
		global crashm_texture
		global crashl_texture
		global crashr_texture
		global ride_texture
		global closehhl_texture
		global openhhl_texture
		global floortom_texture

				


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

				
		
		
	def defineKeys():
		global kickl_key
		global kickr_key
		global snare_key
		global close_hh_key
		global open_hh_key
		global crashl_key
		global crashm_key
		global crashr_key
		global ride_key
		global tom1_key
		global tom2_key
		global tom3_key
		global floortom_key

		kickl_key = parser.get('keys', 'kickl_key')
		kickr_key = parser.get('keys', 'kickr_key')
		snare_key = parser.get('keys', 'snare_key')
		close_hh_key = parser.get('keys', 'close_hh_key')
		open_hh_key = parser.get('keys', 'open_hh_key')
		crashl_key = parser.get('keys', 'crashl_key')
		crashm_key = parser.get('keys', 'crashm_key')
		crashr_key = parser.get('keys', 'crashr_key')
		ride_key = parser.get('keys', 'ride_key')
		tom1_key = parser.get('keys', 'tom1_key')
		tom2_key = parser.get('keys', 'tom2_key')
		tom3_key = parser.get('keys', 'tom3_key')
		floortom_key = parser.get('keys', 'floortom_key')


		snare_key = eval(snare_key)
		close_hh_key = eval(close_hh_key)
		open_hh_key = eval(open_hh_key)
		crashl_key = eval(crashl_key)
		crashm_key = eval(crashm_key)
		crashr_key = eval(crashr_key)
		ride_key = eval(ride_key)
		floortom_key = eval(floortom_key)


	def defineVolume():
		global kickr_volume
		global kickl_volume
		global snare_volume
		global close_hh_volume
		global open_hh_volume
		global crashl_volume
		global crashm_volume
		global crashr_volume
		global ride_volume
		global floortom_volume

		global tom1_volume
		global tom2_volume
		global tom3_volume


		kickr_volume = eval(parser.get('volume', 'kickr_vol'))
		kickl_volume = eval(parser.get('volume', 'kickl_vol'))
		snare_volume = eval(parser.get('volume', 'snare_vol'))
		close_hh_volume = eval(parser.get('volume', 'close_hh_vol'))
		open_hh_volume = eval(parser.get('volume', 'open_hh_vol'))
		crashl_volume = eval(parser.get('volume', 'crashl_vol'))
		crashm_volume = eval(parser.get('volume', 'crashm_vol'))
		crashr_volume = eval(parser.get('volume', 'crashr_vol'))
		ride_volume = eval(parser.get('volume', 'ride_vol'))
		floortom_volume = eval(parser.get('volume', 'floortom_vol'))
		tom1_volume = eval(parser.get('volume', 'tom1_vol'))
		tom2_volume = eval(parser.get('volume', 'tom2_vol'))
		tom3_volume = eval(parser.get('volume', 'tom3_vol'))


	def defineAudio():
		# DualKey
		global kick_audio
		global snare_audio
		global close_hh_audio
		global open_hh_audio
		global crashl_audio
		global crashm_audio
		global crashr_audio
		global ride_audio
		global floortom_audio

		global tom1_audio
		global tom2_audio
		global tom3_audio


		kick_audio = Audio(kickl_sound, volume=kickl_volume, autoplay=False)
		snare_audio = Audio(snare_sound, volume=snare_volume, autoplay=False)
		close_hh_audio = Audio(close_hh_sound, volume=close_hh_volume, autoplay=False)
		open_hh_audio = Audio(open_hh_sound, volume=open_hh_volume, autoplay=False)
		crashl_audio = Audio(crashl_sound, volume=crashl_volume, autoplay=False)
		crashm_audio = Audio(crashm_sound, volume=crashm_volume, autoplay=False)
		crashr_audio = Audio(crashr_sound, volume=crashr_volume, autoplay=False)
		ride_audio = Audio(ride_sound, volume=ride_volume, autoplay=False)
		floortom_audio = Audio(floortom_sound, volume=floortom_volume, autoplay=False)

		tom1_audio = Audio(tom1_sound, volume=tom1_volume, autoplay=False)
		tom2_audio = Audio(tom2_sound, volume=tom2_volume, autoplay=False)
		tom3_audio = Audio(tom3_sound, volume=tom3_volume, autoplay=False)



try:
	parser.read("config.ini")
	drumkit = parser.get('general', 'drumkit') + "/"
	Cardinal.defineVars()



except configparser.NoSectionError:
	print("\n\n[ERROR]: Arquivo de configuração inválido\n\n")
	sys.exit(1)

except Exception as e:
	print("Ocorreu um erro desconhecido ou arquivo 'config.ini' inexistente")
	print(f"\n\nTexto do erro: {str(e)}")
	sys.exit(1)


background	= Entity(model='quad', texture=bg_texture, scale=(16*camera.aspect_ratio,9*camera.aspect_ratio), z=.3, y=-.5)
current_song = vlc.MediaPlayer()


class TopBar(Entity):
	def __init__(self):
		super().__init__(
			parent=camera.ui,
			model='cube',
			color=color.rgb(22,22,22),
			scale_x=1.4,
			scale_y=.1,
			y=.45,
			update = self.TopBarUpdate
			)

		self.realdrumLogo = Entity(
			parent=self,
			model='quad',
			color = color.rgba(0,0,0,0),
			scale_x=.015,
			x=self.x + .022
			)

		self.realdrumLogoText = Text(
			parent=self.realdrumLogo,
			text="Real Drum",
			font='Fonts/Ubuntu-B.ttf',
			size=100,
			scale_x=5,
			scale_y=15,
			x=-.1,
			y=.15,
			color=color.rgb(20,112,173)
			)

		self.playMp3File_btn = Button(
			parent=self,
			model='quad',
			color=color.rgb(255,255,255,200),
			texture='assets/gfx/ic_play.png',
			scale_x=.0035,
			scale_y=.6,
			x=self.x - .029,
			on_click=SoundManager.mp3Clicked,
			update=self.playMp3File_btnUpdate
		)

	def TopBarUpdate(self):
		self.scale_x= camera.ui.scale_x
		self.scale_y= camera.ui.scale_y / .1,
		self.y= camera.ui.y + .45




	############ BETA FUNCTION ############



	def playMp3File_btnUpdate(self):
		media_state = current_song.get_state()

		if media_state == vlc.State.Playing:			
			self.playMp3File_btn.texture = 'assets/gfx/ic_stop.png'
			self.playMp3File_btn.on_click = SoundManager.stop

		else:
			self.playMp3File_btn.texture = 'assets/gfx/ic_play.png'
			self.playMp3File_btn.on_click = SoundManager.mp3Clicked


class SoundManager():

	def mp3Clicked():
		fb = FileBrowser(file_types=('.mp3'), enabled=True)
		fb.y = fb.y - .1
		
		

		def mp3Submitted(newSong):
			songpath = fb.path / newSong[0]
			SoundManager.playsong(str(songpath))

		fb.on_submit = mp3Submitted

	def playsong(newSong):
		global current_song
		current_song = vlc.MediaPlayer(newSong)
		current_song.play()

	def stop():
		current_song.stop()


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
		if held_keys[kickl_key]:
			self.kickl.scale = 3.1
		else:
			self.kickl.scale = 3.2


	def KickRUpdate(self):
		if held_keys[kickr_key]:
			self.kickr.scale = 3.1
		else:
			self.kickr.scale = 3.2


	def SnareUpdate(self):
		if held_keys[snare_key[0]] or held_keys[snare_key[1]]:
			self.snare.scale = 3.1
		else:
			self.snare.scale = 3.2


	def Tom1Update(self):
		if held_keys[tom1_key]:
			self.tom1.scale = 2.4
		else:
			self.tom1.scale = 2.5


	def Tom2Update(self):
		if held_keys[tom2_key]:
			self.tom2.scale = 2.4
		else:
			self.tom2.scale = 2.5


	def Tom3Update(self):
		if held_keys[tom3_key]:
			self.tom3.scale = 2.4
		else:
			self.tom3.scale = 2.5


	def CrashMUpdate(self):
		if held_keys[crashm_key[0]] or held_keys[crashm_key[1]]:
			self.crashm.scale = 2.1
		else:
			self.crashm.scale = 2.2


	def CrashLUpdate(self):
		if held_keys[crashl_key[0]] or held_keys[crashl_key[1]]:
			self.crashl.scale = 3.4
		else:
			self.crashl.scale = 3.5


	def CrashRUpdate(self):
		if held_keys[crashr_key[0]] or held_keys[crashr_key[1]]:
			self.crashr.scale = 2.7
		else:
			self.crashr.scale = 2.8


	def RideUpdate(self):
		if held_keys[ride_key[0]] or held_keys[ride_key[1]]:
			self.ride.scale = 3.4
		else:
			self.ride.scale = 3.5


	def CloseHHUpdate(self):
		if held_keys[close_hh_key[0]] or held_keys[close_hh_key[1]]:
			self.close_hh.scale = 2.7
		else:
			self.close_hh.scale = 2.8

	def OpenHHUpdate(self):
		if held_keys[open_hh_key[0]] or held_keys[open_hh_key[1]]:
			self.open_hh.scale = 2.7
		else:
			self.open_hh.scale = 2.8

	def FloorTomUpdate(self):
		if held_keys[floortom_key[0]] or held_keys[floortom_key[1]]:
			self.floortom.scale = 3.5
		else:
			self.floortom.scale = 3.6




#############################################
#	GET USER INPUT FUNCTION (FROM URSINA)   #
#############################################



def input(key):
	# Kick L + R Sound
	if key == kickl_key or key == kickr_key:
		kick_audio.play()

	# Snare Sound
	if key == snare_key[0] or key == snare_key[1]:
		snare_audio.play()

	# Tom 1 Sound
	if key == tom1_key:
		tom1_audio.play()

	# Tom 2 Sound
	if key == tom2_key:
		tom2_audio.play()

	# Tom 3 Sound
	if key == tom3_key:
		tom3_audio.play()

	# CrashM Sound
	if key == crashm_key[0] or key == crashm_key[1]:
		crashm_audio.play()

	# Crash R Sound
	if key == crashr_key[0] or key == crashr_key[1]:
		crashr_audio.play()

	# Crash L Sound
	if key == crashl_key[0] or key == crashl_key[1]:
		crashl_audio.play()

	# Ride Sound
	if key == ride_key[0] or key == ride_key[1]:
		ride_audio.play()

	# Close HH Sound
	if key == close_hh_key[0] or key == close_hh_key[1]:
		# Stop open hihat if is playing 
		if open_hh_audio.playing == True:
			open_hh_audio.stop()
		close_hh_audio.play()

	# Open HH Sound
	if key == open_hh_key[0] or key == open_hh_key[1]:
		open_hh_audio.play()

	# FloorTom Sound
	if key == floortom_key[0] or key == floortom_key[1]:
		floortom_audio.play()
		


def loadElements():
	drum = GraphicalDrum()
	topbar = TopBar()


def main():
	windowConfiguration()
	loadElements()
	


def windowConfiguration():
	window.title = "RealDrum - Ursina Cover"
	window.borderless = False
	window.fullscreen = False
	window.exit_button.visible = False
	window.fps_counter.enabled = False

	camera.y = -.5
	camera.fov = 38


if __name__ == "__main__":
	main()

app.run()
