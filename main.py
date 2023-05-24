import eel
import constructor

eel.init('web')


@eel.expose
def make_variants(count, th_mask, pr_mask):
    constructor.make_variants(count, th_mask, pr_mask)


eel.start('main.html', size=(800, 700))

