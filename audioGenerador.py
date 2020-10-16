import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate


frecuenciaSegmento = SinSignal(freq=900, amp=1, offset=0)
frecuenciaTexto = SinSignal(freq=300, amp=1, offset=0)
frecuenciaP = SinSignal(freq=400, amp=1, offset=0)
frecuenciaR = SinSignal(freq=1120, amp=1, offset=0)
frecuenciaO = SinSignal(freq=1080, amp=1, offset=0)
frecuenciaV = SinSignal(freq=480, amp=1, offset=0)
frecuenciaA = SinSignal(freq=200, amp=1, offset=0)


#para la cantidad de letras
wave_Texto = frecuenciaTexto.make_wave(duration=0.5, start=0, framerate=44100)

#para el Segmento
wave_Segmento = frecuenciaSegmento.make_wave(duration=0.3, start=0.5, framerate=44100)

#P
wave_P = frecuenciaP.make_wave(duration=0.5, start=0.8, framerate=44100)

#R
wave_R = frecuenciaR.make_wave(duration=0.5, start=1.3, framerate=44100)

#O
wave_O = frecuenciaO.make_wave(duration=0.5, start=1.8, framerate=44100)

#V
wave_V = frecuenciaV.make_wave(duration=0.5, start=2.3, framerate=44100)

#A
wave_A = frecuenciaA.make_wave(duration=0.5, start=2.8, framerate=44100)

#R2
wave_R2 = frecuenciaR.make_wave(duration=0.5, start=3.3, framerate=44100)



wave_audio = wave_Segmento + wave_Texto + wave_P + wave_R + wave_O + wave_V + wave_A + wave_R2

wave_audio.write("audio.wav")