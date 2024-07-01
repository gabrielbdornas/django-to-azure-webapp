
from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.role.name}"

from django.db import models

class Question(models.Model):
    question_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    answer_index = models.IntegerField()
    area = models.CharField(max_length=100)
    image_in_question = models.BooleanField(default=False)
    q_image_description = models.TextField(blank=True, null=True)
    image_in_answers = models.BooleanField(default=False)
    english_question = models.TextField()
    english_answer1 = models.TextField()
    english_answer2 = models.TextField()
    english_answer3 = models.TextField()
    description_of_answer_image1 = models.TextField(blank=True, null=True)
    description_of_answer_image2 = models.TextField(blank=True, null=True)
    description_of_answer_image3 = models.TextField(blank=True, null=True)
    v_text = models.TextField()
    v_image_steps = models.TextField()
    a_text = models.TextField()
    k_text = models.TextField()
    sinhala_question = models.TextField(blank=True, null=True)
    sinhala_answer1 = models.TextField(blank=True, null=True)
    sinhala_answer2 = models.TextField(blank=True, null=True)
    sinhala_answer3 = models.TextField(blank=True, null=True)
    sinhala_v_text = models.TextField(blank=True, null=True)
    #sinhala_v_image_steps = models.TextField(blank=True, null=True)
    sinhala_a_text = models.TextField(blank=True, null=True)
    sinhala_k_text = models.TextField(blank=True, null=True)
    tamil_question = models.TextField(blank=True, null=True)
    tamil_answer1 = models.TextField(blank=True, null=True)
    tamil_answer2 = models.TextField(blank=True, null=True)
    tamil_answer3 = models.TextField(blank=True, null=True)
    tamil_v_text = models.TextField(blank=True, null=True)
    #tamil_v_image_steps = models.TextField(blank=True, null=True)
    tamil_a_text = models.TextField(blank=True, null=True)
    tamil_k_text = models.TextField(blank=True, null=True)
    question_image_illustration = models.ImageField(upload_to='illustrations/', blank=True, null=True)
    answer1_image_illustration = models.ImageField(upload_to='illustrations/', blank=True, null=True)
    answer2_image_illustration = models.ImageField(upload_to='illustrations/', blank=True, null=True)
    answer3_image_illustration = models.ImageField(upload_to='illustrations/', blank=True, null=True)
    visual_instructions_illustration = models.ImageField(upload_to='illustrations/', blank=True, null=True)
    
    sinhala_status = models.CharField(max_length=20, choices=[
        ('incomplete', 'Incomplete'),
        ('complete', 'Complete'),
        ('approved', 'Approved')
    ], default='incomplete')
    
    tamil_status = models.CharField(max_length=20, choices=[
        ('incomplete', 'Incomplete'),
        ('complete', 'Complete'),
        ('approved', 'Approved')
    ], default='incomplete')
    
    illustrator_status = models.CharField(max_length=20, choices=[
        ('incomplete', 'Incomplete'),
        ('complete', 'Complete'),
        ('approved', 'Approved')
    ], default='incomplete')
    
    proofreader_status = models.CharField(max_length=20, choices=[
        ('incomplete', 'Incomplete'),
        ('complete', 'Complete'),
        ('approved', 'Approved'),
        ('pending', 'Pending')
    ], default='incomplete')
    
    def __str__(self):
        return self.english_question[:50]
