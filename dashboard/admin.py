from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Role, UserProfile, Question

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role']
    list_filter = ['role']
    search_fields = ['user__username']

from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'question_id', 'answer_index', 'area', 'image_in_question', 'q_image_description',
        'image_in_answers', 'english_question', 'english_answer1', 'english_answer2', 'english_answer3',
        'description_of_answer_image1', 'description_of_answer_image2', 'description_of_answer_image3',
        'v_text', 'v_image_steps', 'a_text', 'k_text', 'sinhala_question', 'sinhala_answer1',
        'sinhala_answer2', 'sinhala_answer3', 'sinhala_v_text', 'sinhala_a_text',
        'sinhala_k_text', 'tamil_question', 'tamil_answer1', 'tamil_answer2', 'tamil_answer3', 'tamil_v_text', 'tamil_a_text', 'tamil_k_text', 'question_image_illustration',
        'answer1_image_illustration', 'answer2_image_illustration', 'answer3_image_illustration',
        'visual_instructions_illustration', 'sinhala_status', 'tamil_status', 'illustrator_status', 'proofreader_status'
    )
    list_filter = (
        'sinhala_status', 'tamil_status', 'illustrator_status', 'proofreader_status'
    )

admin.site.register(Question, QuestionAdmin)
