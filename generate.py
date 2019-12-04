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

#characterSheetPath = "C:\\Users\\Matt\\Documents\\dev\\character-sheet-generator\\resources\\background.png"

class OriginalCharacterSheetLayout(CharacterSheetLayout):
	def __init__(self):
		skill_step = 4.766 * mm
		saving_throws = {
			Skills.Strength:		(1.62*inch, 7.1*inch + 5*skill_step),#8.05*inch),
			Skills.Dexterity:		(1.62*inch, 7.1*inch + 4*skill_step),#7.86*inch),
			Skills.Constitution:	(1.62*inch, 7.1*inch + 3*skill_step),#7.67*inch),
			Skills.Intelligence:	(1.62*inch, 7.1*inch + 2*skill_step),#7.48*inch),
			Skills.Wisdom:			(1.62*inch, 7.1*inch + skill_step),#7.29*inch),
			Skills.Charisma:		(1.62*inch, 7.1*inch),
			Skills.Acrobatics:		(1.62*inch, 3.25*inch + 17*skill_step),
			Skills.Animal_Handling:	(1.62*inch, 3.25*inch + 16*skill_step),
			Skills.Arcana:			(1.62*inch, 3.25*inch + 15*skill_step),
			Skills.Athletics:		(1.62*inch, 3.25*inch + 14*skill_step),
			Skills.Deception:		(1.62*inch, 3.25*inch + 13*skill_step),
			Skills.History:			(1.62*inch, 3.25*inch + 12*skill_step),
			Skills.Insight:			(1.62*inch, 3.25*inch + 11*skill_step),
			Skills.Intimidation:	(1.62*inch, 3.25*inch + 10*skill_step),
			Skills.Investigation:	(1.62*inch, 3.25*inch + 9*skill_step),
			Skills.Medicine:		(1.62*inch, 3.25*inch + 8*skill_step),
			Skills.Nature:			(1.62*inch, 3.25*inch + 7*skill_step),
			Skills.Perception:		(1.62*inch, 3.25*inch + 6*skill_step),
			Skills.Performance:		(1.62*inch, 3.25*inch + 5*skill_step),
			Skills.Persuasion:		(1.62*inch, 3.25*inch + 4*skill_step),
			Skills.Religion:		(1.62*inch, 3.25*inch + 3*skill_step),
			Skills.Slight_Of_Hand:	(1.62*inch, 3.25*inch + 2*skill_step),
			Skills.Stealth:			(1.62*inch, 3.25*inch + skill_step),
			Skills.Survival:		(1.62*inch, 3.25*inch)
		}
		proficiencies = {
			Skills.Strength:	   (1.465*inch, 7.115*inch + 5*skill_step),
			Skills.Dexterity:	   (1.465*inch, 7.115*inch + 4*skill_step),
			Skills.Constitution:   (1.465*inch, 7.115*inch + 3*skill_step),
			Skills.Intelligence:   (1.465*inch, 7.115*inch + 2*skill_step),
			Skills.Wisdom:		   (1.465*inch, 7.115*inch + skill_step),
			Skills.Charisma:	   (1.465*inch, 7.115*inch),
			Skills.Acrobatics:	   (1.465*inch, 3.265*inch + 17*skill_step),
			Skills.Animal_Handling:(1.465*inch, 3.265*inch + 16*skill_step),
			Skills.Arcana:		   (1.465*inch, 3.265*inch + 15*skill_step),
			Skills.Athletics:	   (1.465*inch, 3.265*inch + 14*skill_step),
			Skills.Deception:	   (1.465*inch, 3.265*inch + 13*skill_step),
			Skills.History:		   (1.465*inch, 3.265*inch + 12*skill_step),
			Skills.Insight:		   (1.465*inch, 3.265*inch + 11*skill_step),
			Skills.Intimidation:   (1.465*inch, 3.265*inch + 10*skill_step),
			Skills.Investigation:  (1.465*inch, 3.265*inch + 9*skill_step),
			Skills.Medicine:	   (1.465*inch, 3.265*inch + 8*skill_step),
			Skills.Nature:		   (1.465*inch, 3.265*inch + 7*skill_step),
			Skills.Perception:	   (1.465*inch, 3.265*inch + 6*skill_step),
			Skills.Performance:	   (1.465*inch, 3.265*inch + 5*skill_step),
			Skills.Persuasion:	   (1.465*inch, 3.265*inch + 4*skill_step),
			Skills.Religion:	   (1.465*inch, 3.265*inch + 3*skill_step),
			Skills.Slight_Of_Hand: (1.465*inch, 3.265*inch + 2*skill_step),
			Skills.Stealth:		   (1.465*inch, 3.265*inch + skill_step),
			Skills.Survival:	   (1.465*inch, 3.265*inch)
		}
		super(OriginalCharacterSheetLayout, self).__init__(
			"C:\\Users\\Matt\\Documents\\dev\\character-sheet-generator\\resources\\official.png",
			name=(inch, 9.9*inch),
			character_class=(3.8*inch, 10.15*inch),
			background=(5.3*inch, 10.15*inch),
			player_name=(6.8*inch, 10.15*inch),
			race=(3.8*inch, 9.8*inch),
			alignment=(5.3*inch, 9.8*inch),
			str_score=		(0.8*inch, 8.25*inch),
			str_modifier=	(0.8*inch, 8.55*inch),
			dex_score=		(0.8*inch, 7.25*inch),
			dex_modifier=	(0.8*inch, 7.55*inch),
			con_score=		(0.8*inch, 6.28*inch),
			con_modifier=	(0.8*inch, 6.55*inch),
			int_score=		(0.8*inch, 5.28*inch),
			int_modifier=	(0.8*inch, 5.56*inch),
			wis_score=		(0.8*inch, 4.3*inch),
			wis_modifier=	(0.8*inch, 4.58*inch),
			cha_score=		(0.8*inch, 3.3*inch),
			cha_modifier=	(0.8*inch, 3.58*inch),
			proficiency_bonus=(1.52*inch, 8.455*inch),
			passive_perception=(0.6*inch, 2.6*inch),
			saving_throws=saving_throws,
			proficiencies=proficiencies)

layout = OriginalCharacterSheetLayout()

def modifier(proficiency):
	return (scores[proficiency.Stat()] - 10)//2

def saving_throw(proficiency):
	saving_throw_value = modifier(proficiency)
	if proficiency in stat_proficiencies:
		saving_throw_value += proficiency_bonus
	return saving_throw_value

c = canvas.Canvas("test.pdf", pagesize)
c.drawInlineImage(layout.Background_Path, 0, 0, pagesize[0], pagesize[1])

############################
#        The header
############################
c.setFontSize(16)
c.drawString(layout.Name[0], layout.Name[1], name)

c.setFontSize(12)
c.drawString(layout.Class[0], layout.Class[1], class_5e + ' - ' + str(level))
c.drawString(layout.Background[0], layout.Background[1], background)
c.drawString(layout.Player_Name[0], layout.Player_Name[1], player)
c.drawString(layout.Race[0], layout.Race[1], race)
c.drawString(layout.Alignment[0], layout.Alignment[1], alignment)


############################
#        The Stats
############################
c.setFontSize(8)
c.drawCentredString(layout.Str_Score[0], layout.Str_Score[1], str(scores[Skills.Strength]))
c.drawCentredString(layout.Dex_Score[0], layout.Dex_Score[1], str(scores[Skills.Dexterity]))
c.drawCentredString(layout.Con_Score[0], layout.Con_Score[1], str(scores[Skills.Constitution]))
c.drawCentredString(layout.Int_Score[0], layout.Int_Score[1], str(scores[Skills.Intelligence]))
c.drawCentredString(layout.Wis_Score[0], layout.Wis_Score[1], str(scores[Skills.Wisdom]))
c.drawCentredString(layout.Cha_Score[0], layout.Cha_Score[1], str(scores[Skills.Charisma]))

c.setFontSize(18)
c.drawCentredString(layout.Str_Modifier[0], layout.Str_Modifier[1], str(modifier(Skills.Strength)))
c.drawCentredString(layout.Dex_Modifier[0], layout.Dex_Modifier[1], str(modifier(Skills.Dexterity)))
c.drawCentredString(layout.Con_Modifier[0], layout.Con_Modifier[1], str(modifier(Skills.Constitution)))
c.drawCentredString(layout.Int_Modifier[0], layout.Int_Modifier[1], str(modifier(Skills.Intelligence)))
c.drawCentredString(layout.Wis_Modifier[0], layout.Wis_Modifier[1], str(modifier(Skills.Wisdom)))
c.drawCentredString(layout.Cha_Modifier[0], layout.Cha_Modifier[1], str(modifier(Skills.Charisma)))

c.setFontSize(16)
c.drawCentredString(layout.Proficiency_Bonus[0], layout.Proficiency_Bonus[1], "+" + str(proficiency_bonus))
c.drawCentredString(layout.Passive_Perception[0], layout.Passive_Perception[1], str(10 + saving_throw(Skills.Perception)))


############################
#      Saving Throws
############################
c.setFontSize(8)
for skill in Skills:
	saving_throw_position = layout.Saving_Throws[skill]
	c.drawString(saving_throw_position[0], saving_throw_position[1], "+" + str(saving_throw(skill)))


############################
#      Saving Throws
############################
for skill in stat_proficiencies:
	proficiency_position = layout.Proficiencies[skill]
	c.circle(proficiency_position[0], proficiency_position[1], 1*mm, fill=1)



c.showPage()
c.save()
