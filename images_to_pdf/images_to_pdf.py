import os
import img2pdf

path = 'C:/Users/Hoffmann/OneDrive/Backupdropbox/UNOESC/python'
with open("out.pdf", "wb") as file:
   file.write(img2pdf.convert([i for i in os.listdir(path) if i.endswith(".jpg")]))
