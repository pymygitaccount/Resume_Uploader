from django.db import models

STATE_CHOICE = (
  ('maharastra', 'Maharashtra'),
  ('gujarat', 'Gujarat')
)


class Profile(models.Model):
  name = models.CharField(max_length=20)
  email = models.EmailField()
  dob = models.DateField(auto_now=False, auto_now_add=False)
  state = models.CharField(max_length=30, choices=STATE_CHOICE)
  gender = models.CharField(max_length=10)
  location = models.CharField(max_length=20)
  profile_image = models.ImageField(upload_to='profile_img', blank=True)
  resume_file = models.FileField(upload_to='resume_data', blank=True)


  def __str__(self):
      return self.name
  