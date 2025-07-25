import ast
from django.db import models

# Create your models here.
class UserFilmList(models.Model):
    username = models.CharField(max_length=150)
    film_ids = models.JSONField(default=list, blank=True)
    film_titles = models.JSONField(default=list, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"UserFilmList(user_id={self.username}, film_ids={self.film_ids})"
    
    def add_film(self, film):
        film_list = ast.literal_eval(film)
        if film_list not in self.film_ids and len(self.film_ids) < 20:
            self.film_ids.append(film_list)
            title = film_list[0]
            self.film_titles.append(title)
            self.save()
    
    def remove_film(self, film):
        film_list = ast.literal_eval(film)
        if film_list in self.film_ids:
            self.film_ids.remove(film_list)
            title = film_list[0]
            if title in self.film_titles:
                self.film_titles.remove(title)
            self.save()
            
    def get_film_count(self):
        return len(self.film_ids)