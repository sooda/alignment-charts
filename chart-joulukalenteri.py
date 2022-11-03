from alignmentchart import alignmentchart

output_file = 'joulukalenterichart.png'
chart_title = 'joulukalenteri\nalignment\nchart'
explainer = '\non joulukalenteri'

main_descs_goodness = [
    ('kalenteri purist',
        'tuote on yleisesti hyväksytty\najan seuraamiseen\nerityisesti jouluna'),
    ('kalenteri neutral',
        'tuotteella voi seurata ajan kulua,\nväkisin väännetty joulun teemaan'),
    ('kalenteri radical',
        'tuote on teknisesti jaettavissa\n24 osaan, ajan kulumisen\nseuranta kyseenalaista'),
]

main_descs_lawfulness = [
    ('joulu purist',
        'tuote on objektiivisesti tunnustettu\nosa joulun kulttuuria\nvauvasta vaariin'),
    ('joulu neutral',
        'tuotteen teema\nsopii kulttuurissa hyvin\njoulun odottamiseen'),
    ('joulu radical',
        'tuotteen teema tai laatu\non väkisin tai huonosti\nväännetty joulun yhteyteen'),
]

alignments = [
    'lawful good', 'neutral good', 'chaotic good',
    'lawful neutral', 'true neutral', 'chaotic neutral',
    'lawful evil', 'neutral evil', 'chaotic evil',
]

filenames = [
    'adventtikalenteri', 'suklaa', 'huono',
    'tv', 'kalenteri', 'chanel',
    'marmeladi', 'kalja', 'pillerit',
]

explanations = [
        'partiolaisten hieno\nadventtikalenteri', 'suklaajoulukalenteri', 'halpa paperikalenteri,\njonka luukkujen sisällöt\neivät täsmää kuvaan',
        '24-jaksoinen joulukuussa\nesitettävä tv-sarja', 'joulukuun seinäkalenteri', 'wannabe lokerikko\nkosmetiikkatuotteita',
        'purkillinen vihreää marmeladia', '24 oluen pakkaus', 'neljän viikon ehkäisypillerit',
]

if __name__ == "__main__":
    alignmentchart(output_file, chart_title, explainer, filenames, main_descs_lawfulness, main_descs_goodness, alignments, explanations)
