from bs4 import BeautifulSoup
import requests

#inhalt_seite = requests.get('https://heise.de/').content
#soup = BeautifulSoup(inhalt_seite , 'html.parser')
#print(soup.title.get_text(strip=True))

homepage_will = 'https://daserste.ndr.de/annewill/index.html'
stamm_will = 'https://daserste.ndr.de'
liste_termine_will = ['Sendetermin noch nicht bekannt']
liste_gaeste_will = ['Gäste noch nicht bekannt']
liste_beschreibung_will = ['Gästebeschreibung noch nicht bekannt']
thema_will = 'Thema noch nicht bekannt'
aktuell_will = None

req_homepage_will = requests.get(homepage_will).content
soup_homepage_will = BeautifulSoup(req_homepage_will, 'html.parser')

liste_termine_will = soup_homepage_will.select_one('div[class="timetable"] span').get_text(strip=True)
liste_termine_will = liste_termine_will.replace('|', '').replace(',', '').replace('Uhr', '').replace('So', 'Sonntag').split()
liste_termine_will[3:5] = [' '.join(liste_termine_will[3:5])]

if soup_homepage_will.select_one('div[class="media mediaA"] span[class="icon icon_video"]') == None:
    aktuell_will = True
else:
    aktuell_will = False

aktuell_will = True #Aktivieren

if aktuell_will == True:
    #thema_will = soup_homepage_will.select_one('div[class="media mediaA"]').get_text
    thema_will = soup_homepage_will.select_one('div[class="media mediaA"] a[class="imglink"]')['title']
#print(thema_will) # "Zum Video: " aus dem String entfernen

sendeseite_will = stamm_will + soup_homepage_will.select_one('div[class="media mediaA"] a[class="imglink"]')['href']

req_sendeseite_will = requests.get(sendeseite_will).content
soup_sendeseite_will = BeautifulSoup(req_sendeseite_will, 'html.parser')

gaesteseite_will = stamm_will + soup_sendeseite_will.select_one('a[title*="Gäste"]')['href']

req_gaesteseite_will = requests.get(gaesteseite_will).content
soup_gaesteseite_will = BeautifulSoup(req_gaesteseite_will, 'html.parser')

#liste_gaeste_will = []
#for gast in soup_gaesteseite_will.select('h3[class="subtitle small"]'):
#    liste_gaeste_will.append(gast.get_text(strip=True))
liste_gaeste_will  = [gast.get_text(strip=True) for gast in soup_gaesteseite_will.select('h3[class="subtitle small"]')]

liste_beschreibung_will = [beschreibung.get_text(strip=True) for beschreibung in soup_gaesteseite_will.select('h3[class="subtitle small"] + p' )]

#print('Termine Will:', liste_termine_will)
#print('Gäste Will:', liste_gaeste_will)
#print('Thema Will: ' + thema_will)
#print('Gäste Beschreibung Will:', liste_gaeste_will)


#Hartaberfair
homepage_hart = 'https://www1.wdr.de/daserste/hartaberfair/index.html'
liste_termin_hart = ['Sendetermin noch nicht bekannt']
liste_gaeste_hart = ['Gäste noch nicht bekannt']
liste_beschreibung_hart = ['Gästebeschreibung noch nicht bekannt']
thema_hart = 'Thema noch nicht bekannt'
aktuell_hart = None

req_homepage_hart = requests.get(homepage_hart).content
soup_homepage_hart = BeautifulSoup(req_homepage_hart, 'html.parser')

if soup_homepage_hart.select_one('div[class="con transparent infoBroadcastDateBox"] span').get_text(strip=True) == 'Nächster Sendetermin':
    liste_termin_hart = soup_homepage_hart.select_one('div[class="sendeterminText"]').get_text(strip=True)
    liste_termin_hart = liste_termin_hart.replace('|', '').replace(',', '').replace('Uhr', '').replace('Mo', 'Montag').split()
    liste_termin_hart.append('Das Erste')

#if soup_homepage_hart.select_one('div[class="media mediaA video"] span[class="icon icon_video"]') == None:
 #   aktuell_will = True
#else:
 #   aktuell_will = False

thema_hart = soup_homepage_hart.select('h4[class="headline"]')[1].get_text(strip=True)
print(thema_hart)