from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=120)
    
    def __str__(self):
        return self.name
    
### Article avec ces Attributs   
class Article(models.Model):
    title=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    desc=models.TextField()
    image=models.ImageField(blank=True,null=True)
    published=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title