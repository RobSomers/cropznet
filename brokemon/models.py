from django.db import models

class BmonBlog(models.Model):
	types = [
		("Bug", "Bug"), ("Dark", "Dark"), ("Dragon", "Dragon"), ("Electric", "Electric"),
		("Fairy", "Fairy"), ("Fighting", "Fighting"), ("Fire", "Fire"), ("Flying", "Flying"),
		("Ghost", "Ghost"), ("Grass", "Grass"), ("Ground", "Ground"), ("Ice", "Ice"),
		("Normal", "Normal"), ("Poison", "Poison"), ("Psychic", "Psychic"), ("Rock", "Rock"),
		("Steel", "Steel"), ("Water", "Water"), ("None", "None")
	]

	name = models.CharField(max_length=100)
	date = models.DateTimeField('date published')

	title_intro = models.CharField(max_length=200, blank=True)
	intro = models.TextField(max_length=10000)
	title_one = models.CharField(max_length=200, blank=True)
	par_one = models.TextField(max_length=10000)
	title_two = models.CharField(max_length=200, blank=True)
	par_two = models.TextField(max_length=10000, blank=True)
	title_three = models.CharField(max_length=200, blank=True)
	par_three = models.TextField(max_length=10000, blank=True)
	title_four = models.CharField(max_length=200, blank=True)
	par_four = models.TextField(max_length=10000, blank=True)
	title_five = models.CharField(max_length=200, blank=True)
	par_five = models.TextField(max_length=10000, blank=True)
	title_six = models.CharField(max_length=200, blank=True)
	par_six = models.TextField(max_length=10000, blank=True)
	title_seven = models.CharField(max_length=200, blank=True)
	par_seven = models.TextField(max_length=10000, blank=True)
	title_eight = models.CharField(max_length=200, blank=True)
	par_eight = models.TextField(max_length=10000, blank=True)
	title_nine = models.CharField(max_length=200, blank=True)
	par_nine = models.TextField(max_length=10000, blank=True)
	title_ten = models.CharField(max_length=200, blank=True)
	par_ten = models.TextField(max_length=10000, blank=True)

	nickname = models.CharField(max_length=15, blank=True)
	type_one = models.CharField(max_length=15, choices=types)
	type_two = models.CharField(max_length=15, choices=types)
	nature = models.CharField(max_length=15, blank=True)
	ability = models.CharField(max_length=25, blank=True)
	item = models.CharField(max_length=25, blank=True)
	move_one = models.CharField(max_length=15, blank=True)
	move_two = models.CharField(max_length=15, blank=True)
	move_three = models.CharField(max_length=15, blank=True)
	move_four = models.CharField(max_length=15, blank=True)
	hp = models.IntegerField(default=0)
	attack = models.IntegerField(default=0)
	defense = models.IntegerField(default=0)
	spAtk = models.IntegerField(default=0)
	spDef = models.IntegerField(default=0)
	speed = models.IntegerField(default=0)

	pic_one = models.CharField(max_length=115, blank=True)
	pic_two = models.CharField(max_length=115, blank=True)	
	pic_three = models.CharField(max_length=115, blank=True)
	pic_four = models.CharField(max_length=115, blank=True)
	pic_five = models.CharField(max_length=115, blank=True)
	pic_six = models.CharField(max_length=115, blank=True)
	pic_seven = models.CharField(max_length=115, blank=True)
	pic_eight = models.CharField(max_length=115, blank=True)
	pic_nine = models.CharField(max_length=115, blank=True)
	pic_ten = models.CharField(max_length=115, blank=True)

	def __str__(self):
		return self.name