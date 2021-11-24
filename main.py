import os, sys
from ursina import *
import drumconfig as dc
from importlib import reload as rlib

app = Ursina()



camera.y = -.5

background	= Entity(parent=window, model='quad', texture='fundo.jpg', scale=(16,9), z=.3, y=-.5)


kickl   = Entity(model='quad', texture='kickl.png', scale=3.2, y=-3, x=-1.7, z=0)
kickr   = Entity(model='quad', texture='kickr.png', scale=3.2, y=-3, x=1.6, z=0)
snare   = Entity(model='quad', texture='snare.png', scale=3.2, y=-1.2, x=0, z=-.2)
tom1    = Entity(model='quad', texture='tom1.png', scale=2.5, y=-.2, x=-2.2, z=-.3)
tom2    = Entity(model='quad', texture='tom2.png', scale=2.5, y=.9, x=0, z=-.3)
tom3    = Entity(model='quad', texture='tom3.png', scale=2.5, y=-.2, x=2.2, z=-.3)
splash  = Entity(model='quad', texture='crashm_reflector.png', scale=2.2, y=1.8, x=-1.8, z=-.6)
crashl  = Entity(model='quad', texture='crashl.png', scale=3.5, y=1, x=-4.5, z=-.6)
crashr  = Entity(model='quad', texture='crashr.png', scale=2.8, y=1.9, x=1.6, z=-.7)
ride    = Entity(model='quad', texture='ride.png', scale=3.5, y=.9, x=4.6, z=-.7)
close_hh= Entity(model='quad', texture='closehhl.png', scale=2.8, y=-1.2, x=-5.2, z=-.1)
open_hh = Entity(model='quad', texture='openhhl.png', scale=2.8, y=-2.8, x=-5.3, z=0)
floortom= Entity(model='quad', texture='floorr.png', scale=3.6, y=-2.7, x=5, z=0)


def update():
#	rlib(dc)

	if held_keys[dc.kickl_key]:
		kickl.z = -.1
	else:
		kickl.z = 0

	if held_keys[dc.kickr_key]:
		kickr.z = -.1
	else:
		kickr.z = 0

	if held_keys[dc.snare_key[0]] or held_keys[dc.snare_key[1]]:
		snare.z = -.2
	else:
		snare.z = -.3

	if held_keys[dc.tom1_key]:
		tom1.z = -.4
	else:
		tom1.z = -.5

	if held_keys[dc.tom2_key]:
		tom2.z = -.4
	else:
		tom2.z = -.5

	if held_keys[dc.tom3_key]:
		tom3.z = -.4
	else:
		tom3.z = -.5

	if held_keys[dc.splash_key]:
		splash.z = -.6
	else:
		splash.z = -.7

	if held_keys[dc.crashl_key]:
		crashl.z = -.6
	else:
		crashl.z = -.7

	if held_keys[dc.crashr_key]:
		crashr.z = -.6
	else:
		crashr.z = -.7

	if held_keys[dc.ride_key]:
		ride.z = -.6
	else:
		ride.z = -.7

	if held_keys[dc.close_hh_key[0]] or held_keys[dc.close_hh_key[1]]:
		close_hh.z = -.1
	else:
		close_hh.z = -.2

	if held_keys[dc.open_hh_key]:
		open_hh.z = 0
	else:
		open_hh.z = -.1

	if held_keys[dc.floortom_key]:
		floortom.z = -.1
	else:
		floortom.z = 0


def input(key):
	if key == dc.kickl_key or key == dc.kickr_key:
		Audio('kick.mp3', volume=dc.kickl_vol)

	if key == dc.snare_key[0] or key == dc.snare_key[1]:
		Audio('snare.mp3', volume=dc.snare_vol)

	if key == dc.tom1_key:
		Audio('tom1.mp3', volume=dc.tom1_vol)

	if key == dc.tom2_key:
		Audio('tom2.mp3', volume=dc.tom2_vol)

	if key == dc.tom3_key:
		Audio('tom3.mp3', volume=dc.tom3_vol)

	if key == dc.splash_key:
		Audio('crashm.mp3', volume=dc.splash_vol)

	if key == dc.crashr_key:
		Audio('crashr.mp3', volume=dc.crashr_vol)

	if key == dc.crashl_key:
		Audio('crashl.mp3', volume=dc.crashl_vol)

	if key == dc.ride_key:
		Audio('ride.mp3', volume=dc.ride_vol)

	if key == dc.close_hh_key[0] or key == dc.close_hh_key[1]:
		Audio('closehh.mp3', volume=dc.close_hh_vol)

	if key == dc.open_hh_key:
		Audio('openhh.mp3', volume=dc.open_hh_vol)

	if key == dc.floortom_key:
		Audio('floor.mp3', volume=dc.floortom_vol)


def windowConfiguration():
	window.title = "Virtual Duramu_U"
	window.borderless = False
	window.fullscreen = False
	window.forced_aspect_ratio = 1.769
	window.exit_button.visible = False
	window.fps_counter.enabled = True


def main():
	windowConfiguration()


#EditorCamera()
main()
app.run()
