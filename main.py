import sys
from pathlib import Path

# Misc libs
from configparser import ConfigParser
from typing import Any

# Ursina Libs
import ursina
from ursina import (Ursina,
                    Audio,
                    Entity,
                    Text,
                    Button,
                    camera,
                    Func,
                    color,
                    window)

from ursina.prefabs.file_browser import FileBrowser

# Exceptions
from configparser import NoSectionError

app: Ursina = Ursina(title="RealDrum - Ursina version", 
                     borderless=False, fullscreen=False)
parser: ConfigParser = ConfigParser()


class Cardinal:
    def __init__(self):
        print("Cardinal started")

    def defineVars(self) -> None:
        self.defineSounds()
        self.defineTextures()
        self.defineKeys()
        self.defineVolume()
        self.defineAudio()

    def defineSounds(self):
        self.kickl_sound = drumkit + "kick.mp3"
        self.kickr_sound = drumkit + "kick.mp3"
        self.snare_sound = drumkit + "snare.mp3"
        self.tom1_sound = drumkit + "tom1.mp3"
        self.tom2_sound = drumkit + "tom2.mp3"
        self.tom3_sound = drumkit + "tom3.mp3"
        self.crashm_sound = drumkit + "crashm.mp3"
        self.crashl_sound = drumkit + "crashl.mp3"
        self.crashr_sound = drumkit + "crashr.mp3"
        self.ride_sound = drumkit + "ride.mp3"
        self.close_hh_sound = drumkit + "closehh.mp3"
        self.open_hh_sound = drumkit + "openhh.mp3"
        self.floortom_sound = drumkit + "floor.mp3"

    def defineTextures(self) -> None:
        # ==> Define texturas
        self.bg_texture = drumkit + "fundo"
        self.kickl_texture = drumkit + "kickl"
        self.kickr_texture = drumkit + "kickr"
        self.snare_texture = drumkit + "snare"
        self.tom1_texture = drumkit + "tom1"
        self.tom2_texture = drumkit + "tom2"
        self.tom3_texture = drumkit + "tom3"
        self.crashm_texture = drumkit + "crashm"
        self.crashl_texture = drumkit + "crashl"
        self.crashr_texture = drumkit + "crashr"
        self.ride_texture = drumkit + "ride"
        self.closehhl_texture = drumkit + "closehhl"
        self.openhhl_texture = drumkit + "openhhl"
        self.floortom_texture = drumkit + "floorr"

    def defineKeys(self):
        snare_key = parser.get('keys', 'snare_key')
        close_hh_key = parser.get('keys', 'close_hh_key')
        open_hh_key = parser.get('keys', 'open_hh_key')
        crashl_key = parser.get('keys', 'crashl_key')
        crashm_key = parser.get('keys', 'crashm_key')
        crashr_key = parser.get('keys', 'crashr_key')
        ride_key = parser.get('keys', 'ride_key')
        floortom_key = parser.get('keys', 'floortom_key')

        self.snare_key: list[str] = [
            x.strip() for x in snare_key.split(",")
        ]
        self.close_hh_key: list[str] = [
            x.strip() for x in close_hh_key.split(",")
        ]
        self.open_hh_key: list[str] = [
            x.strip() for x in open_hh_key.split(",")
        ]
        self.crashl_key: list[str] = [
            x.strip() for x in crashl_key.split(",")
        ]
        self.crashm_key: list[str] = [
            x.strip() for x in crashm_key.split(",")
        ]
        self.crashr_key: list[str] = [
            x.strip() for x in crashr_key.split(",")
        ]
        self.ride_key: list[str] = [
            x.strip() for x in ride_key.split(",")
        ]
        self.floortom_key: list[str] = [
            x.strip() for x in floortom_key.split(",")
        ]

        self.tom1_key = parser.get('keys', 'tom1_key')
        self.tom2_key = parser.get('keys', 'tom2_key')
        self.tom3_key = parser.get('keys', 'tom3_key')
        self.kickl_key = parser.get('keys', 'kickl_key')
        self.kickr_key = parser.get('keys', 'kickr_key')

    def defineVolume(self):
        self.kickr_volume: int = int(parser.get('volume',
                                                'kickr_vol'))

        self.kickl_volume: int = int(parser.get('volume',
                                                'kickl_vol'))
        self.snare_volume: int = int(parser.get('volume',
                                                'snare_vol'))

        self.close_hh_volume: int = int(parser.get('volume',
                                                   'close_hh_vol'))

        self.open_hh_volume: int = int(parser.get('volume',
                                                  'open_hh_vol'))

        self.crashl_volume: int = int(parser.get('volume',
                                                 'crashl_vol'))

        self.crashm_volume: int = int(parser.get('volume',
                                                 'crashm_vol'))

        self.crashr_volume: int = int(parser.get('volume',
                                                 'crashr_vol'))

        self.ride_volume: int = int(parser.get('volume',
                                               'ride_vol'))

        self.floortom_volume: int = int(parser.get('volume',
                                                   'floortom_vol'))

        self.tom1_volume: int = int(parser.get('volume', 'tom1_vol'))
        self.tom2_volume: int = int(parser.get('volume', 'tom2_vol'))
        self.tom3_volume: int = int(parser.get('volume', 'tom3_vol'))

    def defineAudio(self):
        # == > Define audio files to work with engine

        self.kick_audio = Audio(self.kickl_sound,
                                volume=self.kickl_volume,
                                autoplay=False)

        self.snare_audio = Audio(self.snare_sound,
                                 volume=self.snare_volume,
                                 autoplay=False)

        self.close_hh_audio = Audio(self.close_hh_sound,
                                    volume=self.close_hh_volume,
                                    autoplay=False)

        self.open_hh_audio = Audio(self.open_hh_sound,
                                   volume=self.open_hh_volume,
                                   autoplay=False)

        self.crashl_audio = Audio(self.crashl_sound,
                                  volume=self.crashl_volume,
                                  autoplay=False)

        self.crashm_audio = Audio(self.crashm_sound,
                                  volume=self.crashm_volume,
                                  autoplay=False)

        self.crashr_audio = Audio(self.crashr_sound,
                                  volume=self.crashr_volume,
                                  autoplay=False)

        self.ride_audio = Audio(self.ride_sound,
                                volume=self.ride_volume,
                                autoplay=False)

        self.floortom_audio = Audio(self.floortom_sound,
                                    volume=self.floortom_volume,
                                    autoplay=False)

        self.tom1_audio = Audio(self.tom1_sound,
                                volume=self.tom1_volume,
                                autoplay=False)

        self.tom2_audio = Audio(self.tom2_sound,
                                volume=self.tom2_volume,
                                autoplay=False)

        self.tom3_audio = Audio(self.tom3_sound,
                                volume=self.tom3_volume,
                                autoplay=False)


try:
    parser.read("config.ini")
    drumkit = parser.get('general', 'drumkit') + "/"
    
    cardinal = Cardinal()
    cardinal.defineVars()

except NoSectionError:
    print("\n\n[ERROR]: Arquivo de configuração inválido\n\n")
    sys.exit(1)

except FileNotFoundError:
    print("\n\n[ERROR]: No file found")

except Exception as e:
    print(f"\n\n[ERROR]: Unknown Exception: {str(e)}")
    raise e



class TopBar(Entity):
    def __init__(self):
        super().__init__(self)
        
        self.parent = camera.ui
        self.bar_bg: Entity = Entity(model='quad', 
                                     scale_x=1,
                                     scale_y = .02)


class GraphicalDrum(Entity):
    def __init__(self):
        super().__init__()

        self.background = Entity(model='quad',
                                 texture=cardinal.bg_texture,
                                 scale=(8*camera.aspect_ratio,
                                        4.5*camera.aspect_ratio),
                                 z=.3,
                                 y=-.5)

        self.kickl = Entity(
            model='quad',
            texture=cardinal.kickl_texture,
            scale=3.2,
            y=-3,
            x=-1.7,
            z=-.1
        )

        self.kickr = Entity(
            model='quad',
            texture=cardinal.kickr_texture,
            scale=3.2,
            y=-3,
            x=1.6,
            z=-.1
        )

        self.snare = Entity(
            model='quad',
            texture=cardinal.snare_texture,
            scale=3.2,
            y=-1.2,
            x=0,
            z=-.3
        )

        self.tom1 = Entity(
            model='quad',
            texture=cardinal.tom1_texture,
            scale=2.5,
            y=-.2,
            x=-2.2,
            z=-.5
        )

        self.tom2 = Entity(
            model='quad',
            texture=cardinal.tom2_texture,
            scale=2.5,
            y=.9,
            x=0,
            z=-.5
        )

        self.tom3 = Entity(
            model='quad',
            texture=cardinal.tom3_texture,
            scale=2.5,
            y=-.2,
            x=2.2,
            z=-.5
        )

        self.crashm = Entity(
            model='quad',
            texture=cardinal.crashm_texture,
            scale=2.2,
            y=1.8,
            x=-1.8,
            z=-.7
        )

        self.crashl = Entity(
            model='quad',
            texture=cardinal.crashl_texture,
            scale=3.5,
            y=1,
            x=-4.5,
            z=-.7)

        self.crashr = Entity(
            model='quad',
            texture=cardinal.crashr_texture,
            scale=2.8,
            y=1.9,
            x=1.6,
            z=-.7
        )

        self.ride = Entity(
            model='quad',
            texture=cardinal.ride_texture,
            scale=3.5,
            y=.9,
            x=4.6,
            z=-.9
        )

        self.close_hh = Entity(
            model='quad',
            texture=cardinal.closehhl_texture,
            scale=2.8,
            y=-1.2,
            x=-5.2,
            z=-.2
        )

        self.open_hh = Entity(
            model='quad',
            texture=cardinal.openhhl_texture,
            scale=2.8,
            y=-2.8,
            x=-5.3,
            z=-.1
        )

        self.floortom = Entity(
            model='quad',
            texture=cardinal.floortom_texture,
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
        if ursina.held_keys[cardinal.kickl_key]:
            self.kickl.scale = 3.1
        else:
            self.kickl.scale = 3.3

    def KickRUpdate(self):
        if ursina.held_keys[cardinal.kickr_key]:
            self.kickr.scale = 3.1
        else:
            self.kickr.scale = 3.3

    def SnareUpdate(self):
        if ursina.held_keys[cardinal.snare_key[0]] \
                or ursina.held_keys[cardinal.snare_key[1]]:
            self.snare.scale = 3.1
        else:
            self.snare.scale = 3.2

    def Tom1Update(self):
        if ursina.held_keys[cardinal.tom1_key]:
            self.tom1.scale = 2.4
        else:
            self.tom1.scale = 2.5

    def Tom2Update(self):
        if ursina.held_keys[cardinal.tom2_key]:
            self.tom2.scale = 2.4
        else:
            self.tom2.scale = 2.5

    def Tom3Update(self):
        if ursina.held_keys[cardinal.tom3_key]:
            self.tom3.scale = 2.4
        else:
            self.tom3.scale = 2.5

    def CrashMUpdate(self):
        if ursina.held_keys[cardinal.crashm_key[0]] \
                or ursina.held_keys[cardinal.crashm_key[1]]:
            self.crashm.scale = 2.1
        else:
            self.crashm.scale = 2.2

    def CrashLUpdate(self):
        if ursina.held_keys[cardinal.crashl_key[0]] \
                or ursina.held_keys[cardinal.crashl_key[1]]:
            self.crashl.scale = 3.4
        else:
            self.crashl.scale = 3.5

    def CrashRUpdate(self):
        if ursina.held_keys[cardinal.crashr_key[0]] \
                or ursina.held_keys[cardinal.crashr_key[1]]:
            self.crashr.scale = 2.7
        else:
            self.crashr.scale = 2.8

    def RideUpdate(self):
        if ursina.held_keys[cardinal.ride_key[0]] \
                or ursina.held_keys[cardinal.ride_key[1]]:
            self.ride.scale = 3.4
        else:
            self.ride.scale = 3.5

    def CloseHHUpdate(self):
        if ursina.held_keys[cardinal.close_hh_key[0]] \
                or ursina.held_keys[cardinal.close_hh_key[1]]:
            self.close_hh.scale = 2.7
        else:
            self.close_hh.scale = 2.8

    def OpenHHUpdate(self):
        if ursina.held_keys[cardinal.open_hh_key[0]] \
                or ursina.held_keys[cardinal.open_hh_key[1]]:
            self.open_hh.scale = 2.7
        else:
            self.open_hh.scale = 2.8

    def FloorTomUpdate(self):
        if ursina.held_keys[cardinal.floortom_key[0]] \
                or ursina.held_keys[cardinal.floortom_key[1]]:
            self.floortom.scale = 3.5
        else:
            self.floortom.scale = 3.6


#############################################
#   GET USER INPUT FUNCTION (FROM URSINA)   #
#############################################


def input(key):
    # Kick L + R Sound
    if key == cardinal.kickl_key or key == cardinal.kickr_key:
        cardinal.kick_audio.play()

    # Snare Sound
    if key == cardinal.snare_key[0] or key == cardinal.snare_key[1]:
        cardinal.snare_audio.play()

    # Tom 1 Sound
    if key == cardinal.tom1_key:
        cardinal.tom1_audio.play()

    # Tom 2 Sound
    if key == cardinal.tom2_key:
        cardinal.tom2_audio.play()

    # Tom 3 Sound
    if key == cardinal.tom3_key:
        cardinal.tom3_audio.play()

    # CrashM Sound
    if key == cardinal.crashm_key[0] or key == cardinal.crashm_key[1]:
        cardinal.crashm_audio.play()

    # Crash R Sound
    if key == cardinal.crashr_key[0] or key == cardinal.crashr_key[1]:
        cardinal.crashr_audio.play()

    # Crash L Sound
    if key == cardinal.crashl_key[0] or key == cardinal.crashl_key[1]:
        cardinal.crashl_audio.play()

    # Ride Sound
    if key == cardinal.ride_key[0] or key == cardinal.ride_key[1]:
        cardinal.ride_audio.play()

    # Close HH Sound
    if key == cardinal.close_hh_key[0] or key == cardinal.close_hh_key[1]:
        # Stop open hihat if is playing
        if cardinal.open_hh_audio.playing == True:
            cardinal.open_hh_audio.stop()
        cardinal.close_hh_audio.play()

    # Open HH Sound
    if key == cardinal.open_hh_key[0] or key == cardinal.open_hh_key[1]:
        cardinal.open_hh_audio.play()

    # FloorTom Sound
    if key == cardinal.floortom_key[0] or key == cardinal.floortom_key[1]:
        cardinal.floortom_audio.play()


def loadElements():
    GraphicalDrum()
    # TopBar()


def main():
    windowConfiguration()
    loadElements()


def windowConfiguration():
    window.exit_button.visible = False
    window.fps_counter.enabled = False

    camera.y = -.5
    camera.fov = 38


if __name__ == "__main__":
    main()

app.run()
