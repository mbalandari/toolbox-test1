from bs4 import BeautifulSoup

gpx = open("broken_data.gpx")
soup = BeautifulSoup(gpx.read(), features="xml")
fixed = open("fixed_data.gpx", "w")
fixed.write(soup.prettify())
fixed.close()
