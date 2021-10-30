import scrapy
from ..items import *
from bs4 import BeautifulSoup
import requests as req


class SpecializationSpider(scrapy.Spider):
    name = "specialization"

    def start_requests(self):
        urls = [
            'https://www.coursera.org/account/accomplishments/specialization/ALQTJWC4EXQP',
            'https://www.coursera.org/account/accomplishments/specialization/ZK736PZ8HQ3F',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        specialisation = {}
        specialisations = []

        certificat = {}
        certificatss = []
        url = response.url
        rep = req.get(url)

        soup = BeautifulSoup(rep.text, 'html.parser')
        # //features="lxml")
        titres = soup.find_all('h2')

        etudiants = soup.find_all('h3')
        descriptions = soup.find_all('p')
        liens = soup.find_all('a')

        date = soup.find_all('div', {'class': 'course-details'})[0].p.text
        specialisation['date'] = date

        duree = soup.find_all(
            'div', {'class': 'course-details'})[0].find_all('span')[1].text
        specialisation['duree'] = duree

        certificats = soup.find_all(
            'div', {'class', 'course-record-tile-details'})

        for cert in certificats:
            nom = cert.find('h3').text
            certificat['nom'] = nom

            lien = cert.find_all(
                'a', {'class': 'view-certificate'})[0].attrs['href']
            certificat['lien'] = lien

            for i, c in enumerate(cert.find_all('div', {'class': 'course-details'})[0]):
                if i == 0:
                    universite = c.text
                    certificat['universite'] = universite

                if i == 1:
                    formateur = c.text.replace('Taught by: ', '')
                    certificat['formateur'] = formateur

                if i == 2:
                    etudiant = c.text.replace(
                        'Completed by: ', '')[: c.text.index('by ')+3]

                    certificat['etudiant'] = etudiant

                    date_obtention = c.text.replace(
                        'Completed by: ', '')[len(etudiant) + len('by '):]

                    certificat['date_obtention'] = date_obtention

                if i == 3:
                    duree = c.text
                    certificat['duree'] = duree

                if i == 4:
                    score = c.text
                    certificat['score'] = score
                certificatss.append(certificat)
                specialisation['certificats'] = certificatss

        for h2 in titres:
            if 'course-name' in h2["class"]:
                titre = h2.text
                specialisation['titre'] = titre

        for h3 in etudiants:
            if '_lriijlm' in h3["class"]:
                etudiant = h3.text
                specialisation['etudiant'] = etudiant

        for p in descriptions:
            try:
                if 'account-verification-description' in p["class"]:
                    description = p.text
                    specialisation['description'] = description
            except:
                pass

        for a in liens:
            try:
                if 'product-link' in a["class"]:
                    lien = a.attrs['href']
                    specialisation['lien'] = lien
            except:
                pass

        yield specialisation
