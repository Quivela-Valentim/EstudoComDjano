from django.db import models

# Create your models here.
class Topic(models.Model):
    """Um comentário do que a class faz"""
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        """Representação do texto em string no banco de dados"""
        return self.text
class Entry(models.Model):
    """Entra de dados dos topicos """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add= True)
    
    class Meta:
        verbose_name_plural= 'entries'
    def __str__(self):
        """Representação do modelo em string"""
        return self.text[:50] + '...'

        
    