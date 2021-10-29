# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Certificat(scrapy.Item):
    nom: Item()
    universite: Item()
    enseignant: Item()
    duree: Item()
    score: Item()


class CourseraSpecializationItem(scrapy.Item):
    titre: Item()
    auteur: Item()
    image: Item()
    url: Item()
    dateObtention: Item()
    description: Item()
    certificats: list()
