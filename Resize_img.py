import cv2
def resize_image(img):
    r = 300 / img.shape[1] # El atributo shape retorna las dimensiones del array. Si el array es (m,n) i.shape[1] retorna n
    dim = (300, int(img.shape[0] * r)) # 
    rimg = cv2.resize(img, dim, interpolation = cv2.INTER_AREA) #
    return rimg