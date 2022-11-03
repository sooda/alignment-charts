from alignmentchart import alignmentchart

output_file = 'jouluesinekalenterichart.png'
chart_title = 'jouluesinekalenteri\nalignment\nchart'
explainer = '\non joulukalenteri'

main_descs_lawfulness = [
    ('hyötypuristi',
        'tuotteen sisällöstä on\nobjektiivista iloa ja/tai hyötyä\nkoko perheelle'),
    ('hyötyneutraali',
        'tuotteen sisältö on\nsuunnitellussa muodossaan\narvokasta jollekin ihmisryhmälle'),
    ('hyötyradikaali',
        'tuotteen sisältö on\npaskaa hienossa paketissa\nja maksaja häviää pelin'),
]

main_descs_goodness = [
    ('terveellisyyspuristi',
        'tuote tarjoaa\nvälitöntä iloa ja rauhaa\nerityisesti joulun aikaan'),
    ('terveellisyysneutraali',
        'tuote on yleishyödyllinen\nfyysiselle tai henkiselle\nhyvinvoinnille'),
    ('terveellisyysradikaali',
        'tuote on vähintäänkin kyseenalainen,\naiheuttanee välitöntä tai pitkäaikaista\nterveyshaittaa'),
]

alignments = [
    'lawful good', 'neutral good', 'chaotic good',
    'lawful neutral', 'true neutral', 'chaotic neutral',
    'lawful evil', 'neutral evil', 'chaotic evil',
]

filenames = [
    'suklaa', 'tee', 'lelu',
    'puuro', 'pillerit', 'chanel',
    'karkki', 'viina', 'tyhjyys',
]

explanations = [
    'suklaajoulukalenteri', '24-osainen teelajitelma', 'leikkikaluja lokeroissa',
    '24 puuron lajitelma', 'neljän viikon ehkäisypillerit', 'wannabe lokerikko\nkosmetiikkatuotteita',
    '30 gigajoulea karkkia päivässä\nalhaisella kilohinnalla', 'viski- tai muu\nviinalajitelma', 'pula-ajan mummon myymä\ntyhjä suklaakalenteri kirpputorilta',
]

if __name__ == "__main__":
    alignmentchart(output_file, chart_title, explainer, filenames, main_descs_lawfulness, main_descs_goodness, alignments, explanations)
