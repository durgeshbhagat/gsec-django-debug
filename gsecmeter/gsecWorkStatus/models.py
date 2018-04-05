# from django.db import models
#
# # Table for the candidate - VP, Cultural, Technical, Welfare, Sports, HAB
#
#
# class Candidate(models.Model):
#     post = models.CharField(max_length=50)
#     name = models.CharField(max_length=50)
#     pic = models.CharField(max_length=100)
#     video_link = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.post
#
#
# # Table for task's status - Completed, Not yet started, broken, In progress - short or long
#
#
# class Status(models.Model):
#     status = models.CharField(max_length=20)
#     candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.status
#
#
# # Table for headlines - Like Hostel Life, New Sac - Main headings
#
#
# class Headline(models.Model):
#     headline = models.CharField(max_length=100)
#     status = models.ForeignKey(Status, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.headline
#
# # Contains agenda points
#
#
# class Agenda(models.Model):
#     agenda = models.CharField(max_length=500)
#     progress = models.CharField(max_length=50)
#     headline = models.ForeignKey(Headline, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.agenda
