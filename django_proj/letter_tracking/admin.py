from django.contrib import admin
from .models import (Letter,
                    Legislator,
                    Topic,
                    Specific_Topic,
                    Recipient,
                    Caucus,
                    Legislature,
                    Action)

admin.site.register(Letter)
admin.site.register(Legislator)
admin.site.register(Topic)
admin.site.register(Specific_Topic)
admin.site.register(Recipient)
admin.site.register(Caucus)
admin.site.register(Legislature)
admin.site.register(Action)
