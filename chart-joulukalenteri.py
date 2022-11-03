#!/usr/bin/env python3
from alignmentchart import alignmentchart

output_file = 'joulukalenterichart.png'
chart_title = 'joulukalenteri\nalignment\nchart'
explainer = '\non joulukalenteri'

main_descs_goodness = [
    ('kalenteripuristi',
        'tuote on yleisesti hyväksytty\najan seuraamiseen\nerityisesti jouluna'),
    ('kalenterineutraali',
        'tuotteella voi seurata ajan kulua,\nsopii sattumalta jouluaikaan'),
    ('kalenteriradikaali',
        'tuote on teknisesti jaettavissa\n24 osaan, ajan kulumisen\nseuranta kyseenalaista'),
]

main_descs_lawfulness = [
    ('joulupuristi',
        'tuote on objektiivisesti tunnustettu\nosa joulun kulttuuria\nvauvasta vaariin'),
    ('jouluneutraali',
        'tuotteen teema\nsopii kulttuurissa hyvin\njoulun odottamiseen'),
    ('jouluradikaali',
        'tuotteen teema tai laatu\non väkisin tai huonosti\nväännetty joulun yhteyteen'),
]

alignments = [
    'lawful good', 'neutral good', 'chaotic good',
    'lawful neutral', 'true neutral', 'chaotic neutral',
    'lawful evil', 'neutral evil', 'chaotic evil',
]

filenames = ['joulukalenteri/%s' % x for x in [
    'adventtikalenteri', 'suklaa', 'huono',
    'tv', 'kalenteri', 'chanel',
    'marmeladi', 'kalja', 'pillerit',
]]

explanations = [
        'partiolaisten hieno\nadventtikalenteri', 'suklaajoulukalenteri', 'halpa paperikalenteri,\njonka luukkujen sisällöt\neivät täsmää kuvaan',
        '24-jaksoinen joulukuussa\nesitettävä tv-sarja', 'joulukuun seinäkalenteri', 'wannabe lokerikko\nkosmetiikkatuotteita',
        'purkillinen vihreää marmeladia', '24 oluen pakkaus', 'neljän viikon ehkäisypillerit',
]

if __name__ == "__main__":
    alignmentchart(output_file, chart_title, explainer, filenames, main_descs_lawfulness, main_descs_goodness, alignments, explanations)
