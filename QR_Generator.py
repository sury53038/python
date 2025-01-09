import qrcode as qr
img = qr.make("hello")
img.save("helloqr.png")

input("\npress any key")