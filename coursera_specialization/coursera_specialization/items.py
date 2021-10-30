# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CertificatItem(scrapy.Item):
    nom: scrapy.Field()
    universite: scrapy.Field()
    formateur: scrapy.Field()
    duree: scrapy.Field()
    score: scrapy.Field()
    date_obtention: scrapy.Field()


class CourseraSpecializationItem(scrapy.Item):
    titre: scrapy.Field()
    auteur: scrapy.Field()
    etudiant: scrapy.Field()
    image: scrapy.Field()
    lien: scrapy.Field()
    duree: scrapy.Field()
    date_obtention: scrapy.Field()
    objectif: scrapy.Field()
    dateObtention: scrapy.Field()
    description: scrapy.Field()
    certificats: list()
