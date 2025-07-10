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
        if film not in self.film_ids:
            self.film_ids.append(film)
            film_list = ast.literal_eval(film)  # Assuming film is a string representation of a list or dict
            title = film_list[0] # Extract title or use film as
            self.film_titles.append(title)  # Assuming film is a title or ID
            self.save()
    
    def remove_film(self, film):
        if film in self.film_ids:
            self.film_ids.remove(film)
            film_list = ast.literal_eval(film)
            title = film_list[0]  # Assuming film is a string representation of a list
            self.film_titles.remove(title)
            self.save()
            
    def get_film_count(self):
        return len(self.film_ids)