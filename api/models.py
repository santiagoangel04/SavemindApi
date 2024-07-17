from django.db import models
from translate import Translator

# Create your models here.
#language choice enum
class FromLanguage(models.TextChoices):
    ESPAÑOL = "ESP","Español"
    INGLES = "ENG", "Ingles"


class SavemindTranlate(models.Model):
    from_language = models.CharField(max_length= 5,choices=FromLanguage.choices, default=FromLanguage.ESPAÑOL, null= False)
    to_language = models.CharField(max_length=5,choices=FromLanguage.choices,default=FromLanguage.INGLES, null= False)
    word = models.CharField(max_length=100,null=False)
    translated_Word = models.CharField(max_length=100,null=False)
    context_word_use = models.TextField()
    status = models.BooleanField(null=False,default=True)

    def __str__(self):
        return "traduccion: \n de {} -> a {}, palabra a traducir {}, traduccion de la palabra {}, contexto de uso {}".format(self.from_language,self.to_language,self.word,self.translated_Word,self.context_word_use)
    

    def translate_word(self):
        translater = Translator(to_lang=self.to_language,from_lang=self.from_language)
        self.translated_Word = translater.translate(self.word)
        self.save()