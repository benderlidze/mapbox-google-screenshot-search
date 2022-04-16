# import PythonMagick as Magick
# img = Magick.Image("test.png")
# img.backgroundColor('rgba(0,0,0,0)')
# img.rotate(45) 
# img.magick('PNG')
# img.write("testOut.png")
from PIL import Image
import numpy

# im = Image.open('test.png')
# img = im.rotate(45, expand=True)
# img = img.transform((800, 800), Image.PERSPECTIVE, (1, 0, 0, 0, 2, 0, 0, 0) )
# img.save("12345.png")
def find_coeffs(source_coords, target_coords):
    matrix = []
    for s, t in zip(source_coords, target_coords):
        matrix.append([t[0], t[1], 1, 0, 0, 0, -s[0]*t[0], -s[0]*t[1]])
        matrix.append([0, 0, 0, t[0], t[1], 1, -s[1]*t[0], -s[1]*t[1]])
    A = numpy.matrix(matrix, dtype=numpy.float)
    B = numpy.array(source_coords).reshape(8)
    res = numpy.dot(numpy.linalg.inv(A.T * A) * A.T, B)
    return numpy.array(res).reshape(8)


img = Image.open("test.png")
img = img.rotate(45, expand=True)


coeffs = find_coeffs(
    [(0, 0), (1134, 0), (1134, 1134), (0, 1134)],
    [(150, 150), (984, 150), (1134, 600), (0, 600)])

img = img.transform((1134, 1134), Image.PERSPECTIVE, coeffs,Image.BICUBIC)
img.save("12345.png")

