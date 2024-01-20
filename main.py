from zillow_rent import Rent
from sheet import FillSheet

google_form = "https://docs.google.com/forms/d/e/1FAIpQLSeaOH8tSjEUvExhkuVyTLZXIB1Vj3-8G9Ev7I3wlnzdlP294g/viewform?vc=0&c=0&w=1&flr=0"

place = Rent()
detail = place.get_detail()
print(detail)

form = FillSheet(detail, google_form)
