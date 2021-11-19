#!/usr/bin/python3

import os 
import ScoreDraft
from ScoreDraft.Notes import *

def soS(octave=5, duration=48):
	return note(octave,Freqs[8],duration)

def set_soS(freq):
	Freqs[8]=freq

doc=ScoreDraft.Document()
doc.setReferenceFrequency(264.0 *1.25)
doc.setTempo(120)

set_re(10.0/9.0)
set_mi(5.0/4.0)
set_fa(4.0/3.0)
set_so(3.0/2.0)
set_la(5.0/3.0)
set_ti(15.0/8.0)
set_soS(25.0/16.0)

seq1 = [do(6,72), ti(5,24), la(5,24), so(5,72)]
seq2 = [la(3,192), BK(144), mi(4,48), so(4,48), do(5,48)]

seq1 = seq1 + [fa(5,96), BL(24), so(5,24), la(5,24), do(6,24)]
seq2 = seq2 + [re(3,192), BK(144), la(3,48), do(4,48),fa(4,48)]

set_re(9.0/8.0)
set_fa(21.0/16.0)

seq1 = seq1 + [ti(5,72), la(5,24), so(5,24), fa(5,72)]
seq2 = seq2 + [so(3,192), BK(144), re(4,48), fa(4,48), ti(4,48)]

set_fa(4.0/3.0)

seq1 = seq1 + [mi(5,144), BL(48)]
seq2 = seq2 + [do(3,192), BK(144), so(3,48), do(4,48), mi(4,48)]

set_re(10.0/9.0)

seq1 = seq1 + [la(5,72), so(5,24), fa(5,24), mi(5,72)]
seq2 = seq2 + [fa(3,192), BK(144), do(4,48), mi(4,48), la(4,48)]

seq1 = seq1 + [re(5,72), mi(5,24), fa(5,24), la(5,72)]
seq2 = seq2 + [re(3,192), BK(144), la(3,48), do(4,48), fa(4,48)]

set_re(35.0/32.0)
seq1 = seq1 + [soS(5,72), fa(5,24), mi(5,24), re(5,72)]
seq2 = seq2 + [mi(3,192), BK(144), ti(3,48), re(4,48), soS(4,48)]

set_re(10.0/9.0)
seq1 = seq1 + [do(5,144), BL(48)]
seq2 = seq2 + [la(3,192), BK(144), mi(4,48), so(4,48), do(5,48)]

seq1 = seq1 + [re(5,24), la(5,72), la(5,96)]
seq2 = seq2 + [re(3,192), BK(144), la(3,48), do(4,48), fa(4,48)]	

set_re(9.0/8.0)
set_fa(21.0/16.0)

seq1 = seq1 + [BL(96), do(6,24), ti(5,72)]
seq2 = seq2 + [so(3,192), BK(144), re(4,48), fa(4,48), ti(4,48)]	

set_fa(4.0/3.0)
seq1 = seq1 + [so(5,144), BL(48)]
seq2 = seq2 + [mi(3,192), BK(144), ti(3,48), re(4,48), so(4,48)]

set_re(10.0/9.0)
seq1 = seq1 + [la(4,24), fa(5,72), fa(5,96)]
seq2 = seq2 + [re(3,192), BK(144), la(3,48), do(4,48), fa(4,48)]

set_re(9.0/8.0)
set_fa(21.0/16.0)
set_la(27.0/16.0)

seq1 = seq1 + [BL(96), la(5,72), so(5,24)]
seq2 = seq2 + [so(3,192), BK(144), re(4,48), fa(4,48), ti(4,48)]	

seq1 = seq1 + [fa(5,24), mi(5,120), BL(48)]
seq2 = seq2 + [do(3,192), BK(144), so(3,48), do(4,48), mi(4,48)]

set_re(10.0/9.0)
set_fa(4.0/3.0)
set_la(5.0/3.0)

seq1 = seq1 +  [do(6,72), ti(5,24), la(5,24), so(5,72)]
seq2 = seq2 +  [la(3,192), BK(144), mi(4,48), so(4,48), do(5,48)]

seq1 = seq1 + [fa(5,96), BL(24), so(5,24), la(5,24), do(6,24)]
seq2 = seq2 + [re(3,192), BK(144), la(3,48), do(4,48),fa(4,48)]

set_re(9.0/8.0)
set_fa(21.0/16.0)

seq1 = seq1 + [ti(5,72), la(5,24), so(5,24), fa(5,72)]
seq2 = seq2 + [so(3,192), BK(144), re(4,48), fa(4,48), ti(4,48)]

set_fa(4.0/3.0)

seq1 = seq1 + [mi(5,144), BL(48)]
seq2 = seq2 + [do(3,192), BK(144), so(3,48), do(4,48), mi(4,48)]

set_re(10.0/9.0)

seq1 = seq1 + [la(5,72), so(5,24), fa(5,24), mi(5,72)]
seq2 = seq2 + [fa(3,192), BK(144), do(4,48), mi(4,48), la(4,48)]

seq1 = seq1 + [re(5,72), mi(5,24), fa(5,24), la(5,72)]
seq2 = seq2 + [re(3,192), BK(144), la(3,48), do(4,48), fa(4,48)]

set_re(35.0/32.0)
seq1 = seq1 + [soS(5,72), la(5,24), ti(5,24), ti(5,72)]
seq2 = seq2 + [mi(3,192), BK(144), ti(3,48), re(4,48), soS(4,48)]

set_re(10.0/9.0)
seq1 = seq1 + [do(6,24), ti(5,24), la(5,96), BL(48)]
seq2 = seq2 + [la(3,192), BK(144), mi(4,48), so(4,48), do(5,48)]

seq1 = seq1 + [la(5,24), so(5,72), la(5,24), so(5,24), fa(5,48)]
seq2 = seq2 + [re(3,192), BK(144), la(3,48), do(4,48), fa(4,48)]

set_re(9.0/8.0)
set_fa(21.0/16.0)

seq1 = seq1 + [BL(96), do(6,24), ti(5,72)]
seq2 = seq2 + [so(3,192), BK(144), re(4,48), fa(4,48), ti(4,48)]	

set_re(10.0/9.0)
set_fa(4.0/3.0)
seq1 = seq1 + [mi(6,144), BL(48)]
seq2 = seq2 + [fa(3,192), BK(144), do(4,48), mi(4,48), la(4,48)]

seq1 = seq1 + [mi(6,24), do(6,72), do(6,96)]
seq2 = seq2 + [re(3,192), BK(144), la(3,48), do(4,48), fa(4,48)]

set_re(9.0/8.0)
set_fa(21.0/16.0)

seq1 = seq1 + [BL(96), ti(5,24), re(6,72)]
seq2 = seq2 + [so(3,192), BK(144), re(4,48), fa(4,48), ti(4,48)]	

seq1 = seq1 + [do(6,192)]
seq2 = seq2 + [do(3,192), BK(180), so(3,180), BK(168), do(4,168), BK(156), mi(4,156), BK(144), so(4,144), BK(132), do(5,132) ]	


# instrument=ScoreDraft.Piano()
instrument = ScoreDraft.SF2Instrument('florestan-subset.sf2', 0)


doc.playNoteSeq(seq1, instrument)
doc.playNoteSeq(seq2, instrument)
doc.mixDown('FlyMeToTheMoon_just.wav')

#targetBuf=ScoreDraft.TrackBuffer()
#doc.mix(targetBuf)
#ScoreDraft.PlayTrackBuffer(targetBuf)

#import time
#while (ScoreDraft.PlayGetRemainingTime()>0.0):
	#time.sleep(1.0)


