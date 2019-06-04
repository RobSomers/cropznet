from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import BmonBlog

def index(request):
	response = redirect("brokemon")
	return response

def brokemon(request, name="latest"):
	bloglist = [blog.name for blog in BmonBlog.objects.order_by("date")]
	firstblog = bloglist[0]
	latestblog = bloglist[-1]
	
	try:
		name = BmonBlog.objects.get(name__iexact=name)
	except:
		name = BmonBlog.objects.get(name__iexact=latestblog)
	date = name.date
	intro = name.intro
	par_one = name.par_one
	par_two = name.par_two
	par_three = name.par_three
	par_four = name.par_four
	par_five = name.par_five
	par_six = name.par_six
	par_seven = name.par_seven
	par_eight = name.par_eight
	par_nine = name.par_nine
	par_ten = name.par_ten

	title_intro = name.title_intro
	title_one = name.title_one
	title_two = name.title_two
	title_three = name.title_three
	title_four = name.title_four
	title_five = name.title_five
	title_six = name.title_six
	title_seven = name.title_seven
	title_eight = name.title_eight
	title_nine = name.title_nine
	title_ten = name.title_ten
	
	nickname = name.nickname
	type_one = name.type_one
	type_two = name.type_two
	nature = name.nature
	ability = name.ability
	item = name.item
	move_one = name.move_one
	move_two = name.move_two
	move_three = name.move_three
	move_four = name.move_four
	hp = name.hp
	attack = name.attack
	defense = name.defense
	spAtk = name.spAtk
	spDef = name.spDef
	speed = name.speed

	pic_one = name.pic_one
	pic_two = name.pic_two
	pic_three = name.pic_three
	pic_four = name.pic_four
	pic_five = name.pic_five
	pic_six = name.pic_six
	pic_seven = name.pic_seven
	pic_eight = name.pic_eight
	pic_nine = name.pic_nine
	pic_ten = name.pic_ten

	thisblog = bloglist.index(name.name)
	try:
		nextblog = bloglist[thisblog+1]
	except:
		nextblog = latestblog
	if thisblog == 0:
		prevblog = firstblog
	else:
		prevblog = bloglist[thisblog-1]
	
	return render(request, "brokemon/brokemon.html", {"PageName":name, "Date":date, "Intro":intro, 
	"IntroTitle":title_intro, "TitleOne":title_one, "ParOne":par_one, "TitleTwo":title_two, "ParTwo":par_two,
	"TitleThree":title_three, "ParThree":par_three, "TitleFour":title_four, "ParFour":par_four, "TitleFive":title_five, "ParFive":par_five,
	"TitleSix":title_six, "ParSix":par_six, "TitleSeven":title_seven, "ParSeven":par_seven, "TitleEight":title_eight, "ParEight":par_eight,
	"TitleNine":title_nine, "ParNine":par_nine, "TitleTen":title_ten, "ParTen":par_ten,
	"NickName":nickname, "TypeOne":type_one, "TypeTwo":type_two, "Nature":nature, "Ability":ability, "Item":item,
	"Move1":move_one, "Move2":move_two, "Move3":move_three, "Move4":move_four, 
	"HP":hp, "Attack":attack, "Defense":defense, "SpAtk":spAtk, "SpDef":spDef, "Speed":speed, 
	"Pic1":pic_one, "Pic2":pic_two, "Pic3":pic_three, "Pic4":pic_four, "Pic5":pic_five, "Pic6":pic_six,
	"Pic7":pic_seven, "Pic8":pic_eight, "Pic9":pic_nine, "Pic10":pic_ten,
	"NextBlog":nextblog, "PrevBlog":prevblog, "FirstBlog":firstblog, "LatestBlog":latestblog})

