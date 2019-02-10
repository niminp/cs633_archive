from django.db import models
from django.contrib import admin
from django.apps import apps
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.html import format_html
# import jsonfield, json

class Project(models.Model):
	SEMESTER_CHOICES = [
		("SPRING I", "SPRING I"),
		("SPRING II", "SPRING II"),
		("SUMMER I", "SUMMER I"),
		("SUMMER II", "SUMMER II"),
		("FALL I", "FALL I"),
		("FALL II", "FALL II"),
	]

	name = models.CharField(max_length=255)
	description = models.TextField()
	year = models.IntegerField()
	semester = models.CharField(max_length=255, choices=SEMESTER_CHOICES)
	instructor = models.ForeignKey(User, on_delete=models.PROTECT)
	facilitator = models.ManyToManyField(User, related_name='projects')
	team_member = models.ManyToManyField('TeamMember', related_name='projects')
	keyword = models.ManyToManyField('Keyword', related_name='projects')
	language = models.ManyToManyField('Language', related_name='projects')
	github = models.URLField(null=True, blank=True)
	project_management = models.URLField(null=True, blank=True)
	website = models.URLField(null=True, blank=True)
	is_hidden = models.BooleanField()
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	last_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{}".format(self.name)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	fields = ['name', 'description', 'year', 'semester', 'instructor', 'facilitator', 'team_member', 'keyword', 'language', 'github', 'project_management', 'website', 'is_hidden', 'last_modified', 'created']
	readonly_fields = ['last_modified', 'created']
	list_display = ['id', 'name', 'description', 'year', 'semester', 'instructor_link', 'facilitator_link', 'github', 'project_management', 'website', 'is_hidden', 'last_modified', 'created']
	list_filter = ['is_hidden', 'instructor', 'facilitator', 'team_member', 'keyword', 'semester', 'year']
	search_fields = ['name', 'year', 'semester']

	def instructor_link(self, obj):
		return format_html('<a href="{}">{}</a>', reverse('admin:auth_user_change', args=[obj.instructor.id]), obj.instructor)
	instructor_link.short_description = 'Instructor'
	instructor_link.admin_order_field = 'instructor'

	def facilitator_link(self, obj):
		return format_html(", ".join(['<a href="{}">{}</a>'.format(reverse('admin:auth_user_change', args=[facilitator.id]), facilitator) for facilitator in obj.facilitator.all()]))
	facilitator_link.short_description = 'Facilitator'
	facilitator_link.admin_order_field = 'facilitator'

	def team_member_link(self, obj):
		return format_html(", ".join(['<a href="{}">{}</a>'.format(reverse('admin:auth_user_change', args=[team_member.id]), team_member.name) for team_member in obj.team_member.all()]))
	team_member_link.short_description = 'TeamMember'
	team_member_link.admin_order_field = 'team_member'

class TeamMember(models.Model):
	name = models.CharField(max_length=255)
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	last_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{}".format(self.name)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
	fields = ['name',  'last_modified', 'created']
	readonly_fields = ['last_modified', 'created']
	list_display = ['id', 'name', 'last_modified', 'created']
	search_fields = ['name']

class Keyword(models.Model):
	word = models.CharField(max_length=255)
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	last_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{}".format(self.word)

@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
	fields = ['word',  'last_modified', 'created']
	readonly_fields = ['last_modified', 'created']
	list_display = ['id', 'word', 'last_modified', 'created']
	search_fields = ['word']

class Language(models.Model):
	name = models.CharField(max_length=255)
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	last_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{}".format(self.name)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
	fields = ['name',  'last_modified', 'created']
	readonly_fields = ['last_modified', 'created']
	list_display = ['id', 'name', 'last_modified', 'created']
	search_fields = ['name']