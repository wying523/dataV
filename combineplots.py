import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.cbook import get_sample_data
from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage,
                                  AnnotationBbox)


Ima = get_sample_data("D:\Ying\Cummins_dada\sized\SET11_new.png", asfileobj=False)
arr_img = plt.imread(Ima)

fig= plt.figure(figsize=(20, 20))


newax = fig.add_axes([0, 0, 0.35, 0.35], anchor='NE')
newax.imshow(arr_img)
newax.axis('off')

Ima12 = get_sample_data("D:\Ying\Cummins_dada\sized\SET12_new.png", asfileobj=False)
arr_img12 = plt.imread(Ima12)
newax = fig.add_axes([0.25,0, 0.35, 0.35], anchor='NE')
newax.imshow(arr_img12)
newax.axis('off')

Ima13 = get_sample_data("D:\Ying\Cummins_dada\sized\SET13_new.png", asfileobj=False)
arr_img13 = plt.imread(Ima13)
newax = fig.add_axes([0.5, 0, 0.35, 0.35], anchor='NE')
newax.imshow(arr_img13)
newax.axis('off')

Ima21 = get_sample_data("D:\Ying\Cummins_dada\sized\SET21_new.png", asfileobj=False)
arr_img21 = plt.imread(Ima21)
newax = fig.add_axes([0, 0.3, 0.35, 0.35], anchor='NE')
newax.imshow(arr_img21)
newax.axis('off')

Ima22 = get_sample_data("D:\Ying\Cummins_dada\sized\SET22_new.png", asfileobj=False)
arr_img22 = plt.imread(Ima22)
newax = fig.add_axes([0.25, 0.3, 0.35, 0.35], anchor='NE')
newax.imshow(arr_img22)
newax.axis('off')

Ima23 = get_sample_data("D:\Ying\Cummins_dada\sized\SET23_new.png", asfileobj=False)
arr_img23 = plt.imread(Ima23)
newax = fig.add_axes([0.5, 0.3, 0.35, 0.35], anchor='NE')
newax.imshow(arr_img23)
newax.axis('off')

Ima31 = get_sample_data("D:\Ying\Cummins_dada\sized\SET31_new.png", asfileobj=False)
arr_img31 = plt.imread(Ima31)
newax = fig.add_axes([0, 0.65, 0.35, 0.35], anchor='NE')
newax.imshow(arr_img31)
newax.axis('off')

Ima32 = get_sample_data("D:\Ying\Cummins_dada\sized\SET32_new.png", asfileobj=False)
arr_img32 = plt.imread(Ima32)
newax = fig.add_axes([0.25, 0.65, 0.35, 0.35], anchor='NE')
newax.imshow(arr_img32)
newax.axis('off')

Ima33 = get_sample_data("D:\Ying\Cummins_dada\sized\SET33_new.png", asfileobj=False)
arr_img33 = plt.imread(Ima33)
newax = fig.add_axes([0.5, 0.65, 0.35, 0.35], anchor='NE')
newax.imshow(arr_img33)
newax.axis('off')


'''
v = np.linspace(-.5, 2.0, 20, endpoint=True)
cbar = plt.colorbar(ticks=v)
'''
plt.savefig('Contour.png')
