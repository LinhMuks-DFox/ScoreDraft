#!/usr/bin/python3

import ScoreDraft
from ScoreDraft.Notes import *

doc=ScoreDraft.Document()

seq=[do(),do(),so(),so(),la(),la(),so(5,96)]

doc.playNoteSeq(seq, ScoreDraft.NaivePiano())
doc.mixDown('Hello.wav')
