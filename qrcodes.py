import qrcode, PIL
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import ImageColorMask

qr1 = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q)
qr1.add_data('https://spacetelescope.github.io/jdat_notebooks/')

logo_img = PIL.Image.open('stlogo_256.png')
c = logo_img.getchannel('A')
c.putdata([200 if i>200 else i for i in c.getdata()])
logo_img.putalpha(c)


# img = qr1.make_image(image_factory=StyledPilImage, color_mask=ImageColorMask(color_mask_image=logo_img))
# img.save("test1.png")
# img = qr1.make_image(image_factory=StyledPilImage, embeded_image=logo_img)
# img.save("test2.png")
# img = qr1.make_image()
# img.save('test3.png')
qr1.make_image(image_factory=StyledPilImage, embeded_image=logo_img).save("qr_jdat.png")


qr2 = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q)
qr2.add_data('https://spacetelescope.github.io/notebooks/')
qr2.make_image(image_factory=StyledPilImage, embeded_image=logo_img).save("qr_stnb.png")


qr3 = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q)
qr3.add_data('https://timeseries.science.stsci.edu/')
qr3.make_image(image_factory=StyledPilImage, embeded_image=logo_img).save("qr_tike.png")


qr4 = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q)
qr4.add_data('https://eteq.github.io/2023_AAS241_notebooks/aas241_notebook_links.html')
qr4.make_image(image_factory=StyledPilImage, embeded_image=logo_img).save("qr_links.png")