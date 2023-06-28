import numpy as np
from skimage.feature import peak_local_max
from skimage.filters import threshold_otsu
from skimage.measure import label, regionprops
from skimage.morphology import binary_closing, disk
from bioformats import load_image

# Cargar imagen de huella
image_path = 'huella.png'
img = load_image(image_path)

# Binarizar la imagen utilizando umbral de Otsu
threshold_value = threshold_otsu(img)
binary_image = img > threshold_value

# Cerrar agujeros en la imagen binaria
closed_image = binary_closing(binary_image, disk(3))

# Etiquetar regiones conectadas
labeled_image = label(closed_image)

# Encontrar coordenadas de los picos locales en la imagen etiquetada
peaks = peak_local_max(img, min_distance=20, labels=labeled_image, num_peaks_per_label=1)

# Extraer características (minucias) de los picos encontrados
minutiae = []
for peak in peaks:
    y, x = peak
    minutiae.append({'x': x, 'y': y})

# Imprimir las coordenadas de las minucias
for m in minutiae:
    print("Coordenadas: ({}, {})".format(m['x'], m['y']))

print('Minucias extraídas.')
