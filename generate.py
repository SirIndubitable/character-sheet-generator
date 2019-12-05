from reportlab.pdfgen import canvas
from reportlab.lib.units import mm, inch
from reportlab.lib.pagesizes import *
from CharacterSheetLayout import CharacterSheetLayout, Skills

pagesize = LETTER
name = 'Schlage'
level = 9
class_5e = 'Warlock'
background = 'Urchin'
player = 'Matt'
race = 'Tefling'
alignment = 'CN'
speed = 30
hp_maximum = 91
hit_dice = "9d8"
scores = {
	Skills.Strength: 	 15,
	Skills.Dexterity: 	 18,
	Skills.Constitution: 18,
	Skills.Intelligence: 15,
	Skills.Wisdom: 		 16,
	Skills.Charisma: 	 20,
}
stat_proficiencies = [
	Skills.Wisdom,
	Skills.Charisma,
	Skills.Deception,
	Skills.Investigation,
	Skills.Slight_Of_Hand,
	Skills.Stealth,
]


proficiency_bonus = (level - 1)//4 + 2;
percent = 1.0/100.0;

#characterSheetPath = "C:\\Users\\Matt\\Documents\\dev\\character-sheet-generator\\resources\\background.png"

class OriginalCharacterSheetLayout(CharacterSheetLayout):
	def __init__(self):
		skill_step = 1.7*percent
		proficiencies_x = 17.2*percent
		saving_throws_x = 19.1*percent
		stats_base_y = 64.55*percent
		skills_base_y = 29.55*percent
		proficiency_y_offset = 0.015 / 11.0

		saving_throws = {
			Skills.Strength:		(saving_throws_x, stats_base_y + 5*skill_step),
			Skills.Dexterity:		(saving_throws_x, stats_base_y + 4*skill_step),
			Skills.Constitution:	(saving_throws_x, stats_base_y + 3*skill_step),
			Skills.Intelligence:	(saving_throws_x, stats_base_y + 2*skill_step),
			Skills.Wisdom:			(saving_throws_x, stats_base_y + skill_step),
			Skills.Charisma:		(saving_throws_x, stats_base_y),
			Skills.Acrobatics:		(saving_throws_x, skills_base_y + 17*skill_step),
			Skills.Animal_Handling:	(saving_throws_x, skills_base_y + 16*skill_step),
			Skills.Arcana:			(saving_throws_x, skills_base_y + 15*skill_step),
			Skills.Athletics:		(saving_throws_x, skills_base_y + 14*skill_step),
			Skills.Deception:		(saving_throws_x, skills_base_y + 13*skill_step),
			Skills.History:			(saving_throws_x, skills_base_y + 12*skill_step),
			Skills.Insight:			(saving_throws_x, skills_base_y + 11*skill_step),
			Skills.Intimidation:	(saving_throws_x, skills_base_y + 10*skill_step),
			Skills.Investigation:	(saving_throws_x, skills_base_y + 9*skill_step),
			Skills.Medicine:		(saving_throws_x, skills_base_y + 8*skill_step),
			Skills.Nature:			(saving_throws_x, skills_base_y + 7*skill_step),
			Skills.Perception:		(saving_throws_x, skills_base_y + 6*skill_step),
			Skills.Performance:		(saving_throws_x, skills_base_y + 5*skill_step),
			Skills.Persuasion:		(saving_throws_x, skills_base_y + 4*skill_step),
			Skills.Religion:		(saving_throws_x, skills_base_y + 3*skill_step),
			Skills.Slight_Of_Hand:	(saving_throws_x, skills_base_y + 2*skill_step),
			Skills.Stealth:			(saving_throws_x, skills_base_y + skill_step),
			Skills.Survival:		(saving_throws_x, skills_base_y)
		}
		proficiencies = {
			Skills.Strength:	   (proficiencies_x, proficiency_y_offset + stats_base_y + 5*skill_step),
			Skills.Dexterity:	   (proficiencies_x, proficiency_y_offset + stats_base_y + 4*skill_step),
			Skills.Constitution:   (proficiencies_x, proficiency_y_offset + stats_base_y + 3*skill_step),
			Skills.Intelligence:   (proficiencies_x, proficiency_y_offset + stats_base_y + 2*skill_step),
			Skills.Wisdom:		   (proficiencies_x, proficiency_y_offset + stats_base_y + skill_step),
			Skills.Charisma:	   (proficiencies_x, proficiency_y_offset + stats_base_y),
			Skills.Acrobatics:	   (proficiencies_x, proficiency_y_offset + skills_base_y + 17*skill_step),
			Skills.Animal_Handling:(proficiencies_x, proficiency_y_offset + skills_base_y + 16*skill_step),
			Skills.Arcana:		   (proficiencies_x, proficiency_y_offset + skills_base_y + 15*skill_step),
			Skills.Athletics:	   (proficiencies_x, proficiency_y_offset + skills_base_y + 14*skill_step),
			Skills.Deception:	   (proficiencies_x, proficiency_y_offset + skills_base_y + 13*skill_step),
			Skills.History:		   (proficiencies_x, proficiency_y_offset + skills_base_y + 12*skill_step),
			Skills.Insight:		   (proficiencies_x, proficiency_y_offset + skills_base_y + 11*skill_step),
			Skills.Intimidation:   (proficiencies_x, proficiency_y_offset + skills_base_y + 10*skill_step),
			Skills.Investigation:  (proficiencies_x, proficiency_y_offset + skills_base_y + 9*skill_step),
			Skills.Medicine:	   (proficiencies_x, proficiency_y_offset + skills_base_y + 8*skill_step),
			Skills.Nature:		   (proficiencies_x, proficiency_y_offset + skills_base_y + 7*skill_step),
			Skills.Perception:	   (proficiencies_x, proficiency_y_offset + skills_base_y + 6*skill_step),
			Skills.Performance:	   (proficiencies_x, proficiency_y_offset + skills_base_y + 5*skill_step),
			Skills.Persuasion:	   (proficiencies_x, proficiency_y_offset + skills_base_y + 4*skill_step),
			Skills.Religion:	   (proficiencies_x, proficiency_y_offset + skills_base_y + 3*skill_step),
			Skills.Slight_Of_Hand: (proficiencies_x, proficiency_y_offset + skills_base_y + 2*skill_step),
			Skills.Stealth:		   (proficiencies_x, proficiency_y_offset + skills_base_y + skill_step),
			Skills.Survival:	   (proficiencies_x, proficiency_y_offset + skills_base_y)
		}

		char_info_base_x = 44.7*percent
		char_info_x_step = (1.5/8.5)
		char_info_y_1 = 89*percent
		char_info_y_2 = 92.3*percent
		stat_x = 9.45*percent
		stat_step = 9*percent
		stat_score_base_y = 30*percent
		stat_modifier_base_y = 32.5*percent
		super(OriginalCharacterSheetLayout, self).__init__(
			"C:\\Users\\Matt\\Documents\\dev\\character-sheet-generator\\resources\\official.png",
			name=			(9*percent, 90*percent),
			character_class=(char_info_base_x, 						char_info_y_2),
			background=		(char_info_base_x + char_info_x_step, 	char_info_y_2),
			player_name=	(char_info_base_x + 2*char_info_x_step, char_info_y_2),
			race=			(char_info_base_x, 						char_info_y_1),
			alignment=		(char_info_base_x + char_info_x_step, 	char_info_y_1),
			initiative=		(49.7*percent, 79*percent),
			speed=			(59.3*percent, 79*percent),
			hp_maximum=     (50*percent, 74*percent),
			hit_dice=		(41.7*percent, 58.8*percent),
			str_score=		(stat_x, stat_score_base_y + 5*stat_step),
			dex_score=		(stat_x, stat_score_base_y + 4*stat_step),
			con_score=		(stat_x, stat_score_base_y + 3*stat_step),
			int_score=		(stat_x, stat_score_base_y + 2*stat_step),
			wis_score=		(stat_x, stat_score_base_y + stat_step),
			cha_score=		(stat_x, stat_score_base_y),
			str_modifier=	(stat_x, stat_modifier_base_y + 5*stat_step),
			dex_modifier=	(stat_x, stat_modifier_base_y + 4*stat_step),
			con_modifier=	(stat_x, stat_modifier_base_y + 3*stat_step),
			int_modifier=	(stat_x, stat_modifier_base_y + 2*stat_step),
			wis_modifier=	(stat_x, stat_modifier_base_y + stat_step),
			cha_modifier=	(stat_x, stat_modifier_base_y),
			proficiency_bonus=(17.9*percent, 76.9*percent),
			passive_perception=(7*percent, 23.6*percent),
			saving_throws=saving_throws,
			proficiencies=proficiencies)

layout = OriginalCharacterSheetLayout()

c = canvas.Canvas("test.pdf", pagesize)
c.drawInlineImage(layout.Background_Path, 0, 0, pagesize[0], pagesize[1])

def modifier(proficiency):
	return (scores[proficiency.Stat()] - 10)//2

def saving_throw(proficiency):
	saving_throw_value = modifier(proficiency)
	if proficiency in stat_proficiencies:
		saving_throw_value += proficiency_bonus
	return saving_throw_value

def draw_string(point, value):
	c.drawString(point[0] * pagesize[0], point[1] * pagesize[1], value)

def draw_centered_string(point, value):
	c.drawCentredString(point[0] * pagesize[0], point[1] * pagesize[1], value)

def draw_circle(point, radius):
	c.circle(point[0] * pagesize[0], point[1] * pagesize[1], radius, fill=1)

############################
#        The header
############################
c.setFontSize(16)
draw_string(layout.Name, name)

c.setFontSize(12)
draw_string(layout.Class, class_5e + ' - ' + str(level))
draw_string(layout.Background, background)
draw_string(layout.Player_Name, player)
draw_string(layout.Race, race)
draw_string(layout.Alignment, alignment)


############################
#        The Stats
############################
c.setFontSize(8)
draw_centered_string(layout.Str_Score, str(scores[Skills.Strength]))
draw_centered_string(layout.Dex_Score, str(scores[Skills.Dexterity]))
draw_centered_string(layout.Con_Score, str(scores[Skills.Constitution]))
draw_centered_string(layout.Int_Score, str(scores[Skills.Intelligence]))
draw_centered_string(layout.Wis_Score, str(scores[Skills.Wisdom]))
draw_centered_string(layout.Cha_Score, str(scores[Skills.Charisma]))

c.setFontSize(18)
draw_centered_string(layout.Str_Modifier, str(modifier(Skills.Strength)))
draw_centered_string(layout.Dex_Modifier, str(modifier(Skills.Dexterity)))
draw_centered_string(layout.Con_Modifier, str(modifier(Skills.Constitution)))
draw_centered_string(layout.Int_Modifier, str(modifier(Skills.Intelligence)))
draw_centered_string(layout.Wis_Modifier, str(modifier(Skills.Wisdom)))
draw_centered_string(layout.Cha_Modifier, str(modifier(Skills.Charisma)))

c.setFontSize(16)
draw_centered_string(layout.Proficiency_Bonus, "%+d" % proficiency_bonus)
draw_centered_string(layout.Passive_Perception, str(10 + saving_throw(Skills.Perception)))

c.setFontSize(18)
draw_centered_string(layout.Initiative, "%+d" % modifier(Skills.Dexterity))
draw_centered_string(layout.Speed, str(speed))

c.setFontSize(8)
draw_string(layout.Hp_Maximum, str(hp_maximum))
draw_string(layout.Hit_Dice, hit_dice)


############################
#      Saving Throws
############################
c.setFontSize(8)
for skill in Skills:
	draw_string(layout.Saving_Throws[skill], "%+d" % saving_throw(skill))


############################
#      Saving Throws
############################
for skill in stat_proficiencies:
	draw_circle(layout.Proficiencies[skill], 1*mm)



c.showPage()
c.save()
