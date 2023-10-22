from django.db import models


class PartyMaster(models.Model):
    city_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    gst_number = models.CharField(max_length=15)
    party_type = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email_id = models.EmailField()
    landline_number = models.CharField(max_length=10)
    contact_person = models.CharField(max_length=100)

    def __str__(self):
        return (
            self.city_name,
            self.mobile_number,
            self.gst_number,
            self.party_type,
            self.address,
            self.email_id,
            self.landline_number,
            self.contact_person,
        )
