import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patheffects as pe
import matplotlib

debugmode = False
fontsize = 15
bigfont = 1.5 * fontsize
hugefont = 2 * fontsize

def spectext(ax, short, long):
    ax.text(0.5, 0.9, short, weight='bold',
            fontsize=bigfont, verticalalignment='top',
            horizontalalignment='center')
    ax.text(0.5, 0.1, long,
            horizontalalignment='center')

def alignmentchart(output_file, chart_title, explainer, filenames, main_descs_x, main_descs_y, alignments, explanations):
    matplotlib.rc('font', size=fontsize)
    peff = [pe.withStroke(linewidth=4, foreground="white")]
    images = [mpimg.imread('%s.jpg' % x) for x in filenames]

    fig, ax = plt.subplots(4, 4, figsize=(19.20, 10.80),
        gridspec_kw={
            'width_ratios':[0.8, 1, 1, 1],
            'height_ratios':[0.8, 1, 1, 1]
        }
    )
    fig.tight_layout()
    plt.subplots_adjust(left=0.01, bottom=0.01, wspace=0.01, hspace=0.01)

    ax[0][0].text(0, 1, chart_title,
            weight='black',
            verticalalignment='top',
            fontsize=hugefont)

    for (i, (img, alig, expl)) in enumerate(zip(images, alignments, explanations)):
        a = ax[1 + i // 3][1 + i % 3]
        (h, w, _) = img.shape
        a.imshow(img)
        a.text(w/2, 0.05, alig,
                path_effects=peff,
                weight='bold',
                verticalalignment='top',
                horizontalalignment='center')
        a.text(w/2, 0.95*h, expl + explainer,
                path_effects=peff,
                horizontalalignment='center')

    for (i, (short, long)) in enumerate(main_descs_x):
        spectext(ax[0][1 + i], short, long)

    for (i, (short, long)) in enumerate(main_descs_y):
        spectext(ax[1 + i][0], short, long)

    if not debugmode:
        for a in ax:
            for b in a:
                b.set_axis_off()

    plt.savefig(output_file)
    plt.show()
