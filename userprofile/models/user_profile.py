import logging

from django.db import models

from utils.base_models import BaseTimeStampModel

logger = logging.getLogger(__name__.split('.')[0])


class UserProfile(BaseTimeStampModel):
    OWNER = 'owner'
    SECONDARY_OWNER = 'secondary_owner'
    PROCESSING = 'processing'
    APPROVED = 'approved'
    REJECT = 'reject'

    USERTYPE = (
        (OWNER, 'Owner'),
        (SECONDARY_OWNER, 'SecondaryOwner')
    )

    STATUS = (
        (PROCESSING, 'Processing'),
        (APPROVED, 'Approved'),
        (REJECT, 'Reject')
    )

    fullname = models.CharField(max_length=30, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=30, null=False, blank=False)
    gender = models.BooleanField(default=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    dob = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS, default=PROCESSING)
    user_type = models.CharField(max_length=20, choices=USERTYPE, default=SECONDARY_OWNER)
    id_card = models.CharField(max_length=12, null=True, blank=True)
    permanent_residence = models.CharField(max_length=2000, null=True, blank=True)
    issued_by = models.CharField(max_length=1000, null=True, blank=True)
    issued_date = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return "%s" % self.fullname
