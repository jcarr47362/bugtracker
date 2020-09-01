from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class MyUser(AbstractUser):
    pass


class Ticket(models.Model):
    title = models.TextField(max_length=80)
    description = models.CharField(max_length=240)
    time_dates = models.DateTimeField(default=timezone.now)
    assigned_to = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='assigned_to', blank=True, null=True)
    completed_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='completed_by', blank=True, null=True)
    ticket_maker = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='ticket_maker')
    New = 'N'
    In_progress = 'IP'
    Done = 'D'
    Invalid = 'Inv'

    Ticket_Status = [
        (New, 'New'),
        (In_progress, 'In_progress'),
        (Done, 'Done'),
        (Invalid, 'Invalid')
    ]

    status = models.CharField(
        max_length=3,
        choices=Ticket_Status,
        default=New
    )

