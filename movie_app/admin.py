from django.contrib import admin
import movie_app.models as m_a

# Register your models here.
admin.site.register(m_a.Director)
admin.site.register(m_a.Movie)
admin.site.register(m_a.Review)
