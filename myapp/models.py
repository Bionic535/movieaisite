from django.db import models

# Create your models here.
class UserFilmList(models.Model):
    user_id = models.CharField(max_length=100)
    film_ids = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"UserFilmList(user_id={self.user_id}, film_ids={self.film_ids})"
    
    def add_film(self, film_id):
        if film_id not in self.film_ids:
            self.film_ids.append(film_id)
            self.save()
    
    def remove_film(self, film_id):
        if film_id in self.film_ids:
            self.film_ids.remove(film_id)
            self.save()
            
    def get_film_count(self):
        return len(self.film_ids)