from reportlab.pdfgen import canvas
from reportlab.lib.units import mm, inch
from reportlab.lib.pagesizes import *
from CharacterSheetLayout import CharacterSheetLayout, Skills
from OriginalCharacterSheetLayout import OriginalCharacterSheetLayout

pagesize = LETTER
name = 'Schlage'
level = 9
class_5e = 'Warlock'
background = 'Urchin'
player_name = 'Matt'
race = 'Tefling'
alignment = 'CN'
speed = 30
hp_maximum = 91
hit_dice = "9d8"
scores = {
    Skills.Strength:     15,
    Skills.Dexterity:    18,
    Skills.Constitution: 18,
    Skills.Intelligence: 15,
    Skills.Wisdom:       16,
    Skills.Charisma:     20,
}
stat_proficiencies = [
    Skills.Wisdom,
    Skills.Charisma,
    Skills.Deception,
    Skills.Investigation,
    Skills.Slight_Of_Hand,
    Skills.Stealth,
]
other_proficiencies = """
Armor:
    Light
Weapons:
    Simple
Languages:
    Common
    Infernal
Tools:
    Disguise Kit
    Theives' Tools
"""
features_and_traits = """Urchin Features:
    City Secrets
Racial Features:
    Darkvision
    Hellish Resistance
        (Resistance to fire damage)
    Infernal Legacy
Warlock Features:
    Pact of the Tome
Invocations:
    Agonizing Blast
    Armor of Shadows
    Book of Ancient Secrets
    Mask of Many Faces
    Ghostly Gaze
Patron Features:
    Awakened Mind
    Entropic Ward
Feats:
    Warcaster"""
equipment = """None
None
None"""
personality_traits = ("I eat like a pig and have bad manners", "I don't like to bathe")
ideals = "I help people who help me - That's what \nkeeps us alive"
bonds = "No one else should have to endure the \nhardships I've been through"
flaws = "It's not stealing if I need it more than \nsomeone else"


proficiency_bonus = (level - 1)//4 + 2;

def modifier(proficiency):
    return (scores[proficiency.Stat()] - 10)//2

def saving_throw(proficiency):
    saving_throw_value = modifier(proficiency)
    if proficiency in stat_proficiencies:
        saving_throw_value += proficiency_bonus
    return saving_throw_value

modifiers = {skill: modifier(skill) for skill in Skills}
saving_throws = {skill: saving_throw(skill) for skill in Skills}

passive_perception = 10 + modifiers[Skills.Perception]
initiative = modifiers[Skills.Dexterity]


c = canvas.Canvas("test.pdf", pagesize)
sheet = OriginalCharacterSheetLayout(c);
c.drawInlineImage(sheet.Background, 0, 0, pagesize[0], pagesize[1])

sheet.Draw_Character_Info(name, level, class_5e, background, player_name, race, alignment)
sheet.Draw_Stats(scores, modifiers)
sheet.Draw_Skills(saving_throws, stat_proficiencies)
sheet.Draw_Details(initiative, speed, hp_maximum, hit_dice, proficiency_bonus, passive_perception)
sheet.Draw_Other_Proficiencies(other_proficiencies)
sheet.Draw_Equipment(equipment)
sheet.Draw_Features_And_Traits(features_and_traits)
sheet.Draw_Characteristics(personality_traits, ideals, bonds, flaws)

c.showPage()
c.save()

import subprocess
subprocess.call(["start", "test.pdf"], shell=True)
