# import simpleaudio.functionchecks as fc

# fc.LeftRightCheck.run()
# van Joris Gekregen 
import simpleaudio as sa
filename ='SNARE1.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)

print('How many Times would you like to Play the Sample')
playTimes = int(input())

for x in range(playTimes):
    play_obj = wave_obj.play()
    play_obj.wait_done()