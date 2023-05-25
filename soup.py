from bs4 import BeautifulSoup

gpx = open("broken_data.gpx")
soup = BeautifulSoup(gpx.read(), features="xml")
