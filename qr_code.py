import sys
import qrcode
from optparse import OptionParser

Parser = OptionParser()
Parser.add_option("-n", dest="name", help="Enter the name of the object you want to create with qr code")
Parser.add_option("-d", dest="data", help="Enter the data you want to create with qr code")

try:
    (UI, arguments) = Parser.parse_args()
    name = UI.name
    data = UI.data

    image = qrcode.make(data)
    image.save( name + ".jpg")
    image.show()

except KeyboardInterrupt:
    print("pressed 'CTRL + C'")
    sys.exit()

except Exception as E:
    print(E)
    sys.exit()


