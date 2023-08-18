from django.contrib import admin
from .models import Cards, utg_100bb, utg1_100bb, lj_100bb, hj_100bb, co_100bb, btn_100bb, scoring, report
# Register your models here.
admin.site.register(Cards)
admin.site.register(utg_100bb)
admin.site.register(utg1_100bb)
admin.site.register(lj_100bb)
admin.site.register(hj_100bb)
admin.site.register(co_100bb)
admin.site.register(btn_100bb)
admin.site.register(scoring)
admin.site.register(report)