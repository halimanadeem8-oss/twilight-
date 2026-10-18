from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=80, default="Twilight's Magic")
    description = models.TextField()
    price = models.PositiveIntegerField(help_text="Price in Pakistani rupees (PKR).")
    emoji = models.CharField(max_length=12, default="✨", help_text="A simple decorative icon for the demo card.")
    is_featured = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-is_featured", "name"]

    def __str__(self):
        return self.name
