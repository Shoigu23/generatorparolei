from django.db import models

# Create your models here.
# class HorticlutureUpdateForm():
#          soil_type = format.MultipleChoiceField(
#                     required=False,
#                     widget=format.CheckboxSelectMultiple,
#                     choices=SOIL_TYPE_CHOICES,
#                 )
#          class Meta:
#               model = TreeDetails
#               exclude = ('created_by', 'client', 'is_deleted')
#               fieldsets = [
#         ["main", {
#             "fields": ['tree_name', 'common_name','description', 'part_number',
#                        'unit_price'],
#             "legend": "Main details",
#         }],
#         ["extra", {
#             "fields": [ 'quantity', 'height'
#                        'soil_type', ],
#             "legend": "Additional details",
#         }],
#     ]


class Pass(models.Model):
    password = models.CharField(max_length=30)
    is_complete = models.BooleanField(default=False)
