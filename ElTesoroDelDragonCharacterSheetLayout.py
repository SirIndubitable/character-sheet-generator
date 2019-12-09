from reportlab.lib.units import *
from CharacterSheetLayout import CharacterSheetLayout, Skills
from itertools import *
import os.path
import errno

percent = 1.0/100.0;

class ElTesoroDelDragonCharacterSheetLayout(CharacterSheetLayout):
    def __init__(self, canvas):
        if not os.path.isfile("./resources/ElTesoroDelDragon.png"):
            print("The background image does not exist")
            print("Go to https://shoptly.com/eltesorodeldragon and get the character sheet")
            print("Then move the background.png into the resources folder and rename it ElTesoroDelDragon.png")
            print()
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), "./resources/ElTesoroDelDragon.png")
        self._line_spacing = (3.75*mm)/(11.0*inch)
        super(ElTesoroDelDragonCharacterSheetLayout, self).__init__(
            canvas,
            "./resources/ElTesoroDelDragon.png")


    def Draw_Character_Info(self, name, level, class_5e, background, player_name, race, alignment):
        base_x = 3.6/8.5
        x_step = (1.4/8.5)
        y_1 = 10.2/11.0
        y_2 = 10.48/11.0

        self.Set_Font_Size(16)
        self.draw_string((0.75/8.5, 10.25/11.0), name)

        self.Set_Font_Size(12)
        self.draw_string((3.6/8.5, y_2), class_5e + ' - ' + str(level))
        self.draw_string((5.08/8.5, y_2), background)
        self.draw_string((6.4/8.5, y_2), player_name)

        self.draw_string((3.6/8.5, y_1), race)
        self.draw_string((5.08/8.5, y_1), alignment)


    def Draw_Stats(self, scores, modifiers):
        self.Set_Font_Size(6)
        self.draw_centered_string((503.0/1223.0,  1 - (279.0/1576.0)), str(scores[Skills.Strength]))
        self.draw_centered_string((670.0/1223.0,  1 - (233.0/1576.0)), str(scores[Skills.Dexterity]))
        self.draw_centered_string((843.0/1223.0,  1 - (257.0/1576.0)), str(scores[Skills.Constitution]))
        self.draw_centered_string((980.0/1223.0,  1 - (350.0/1576.0)), str(scores[Skills.Intelligence]))
        self.draw_centered_string((1150.0/1223.0, 1 - (489.0/1576.0)), str(scores[Skills.Wisdom]))
        self.draw_centered_string((1157.0/1223.0, 1 - (643.0/1576.0)), str(scores[Skills.Charisma]))

        self.Set_Font_Size(22)
        self.draw_centered_string((3.79/8.5,  8.7/11.0),  "%+d" % modifiers[Skills.Strength])
        self.draw_centered_string((4.95/8.5, 9.01/11.0),  "%+d" % modifiers[Skills.Dexterity])
        self.draw_centered_string((6.16/8.5, 8.84/11.0), "%+d" % modifiers[Skills.Constitution])
        self.draw_centered_string((7.13/8.5, 8.2/11.0),  "%+d" % modifiers[Skills.Intelligence])
        self.draw_centered_string((7.7/8.5,  7.25/11.0), "%+d" % modifiers[Skills.Wisdom])
        self.draw_centered_string((7.75/8.5, 6.15/11.0), "%+d" % modifiers[Skills.Charisma])


    def Draw_Skills(self, saving_throws, proficiencies):
        skill_step = 0.133/11.0
        x = 1.95/8.5
        skills_base_y = 5.07/11.0
        proficiency_x_offset = -1.565/8.5
        proficiency_y_offset = 0.04/11.0
        skills_y = {
            Skills.Acrobatics:      skills_base_y + 17*skill_step,
            Skills.Animal_Handling: skills_base_y + 16*skill_step,
            Skills.Arcana:          skills_base_y + 15*skill_step,
            Skills.Athletics:       skills_base_y + 14*skill_step,
            Skills.Deception:       skills_base_y + 13*skill_step,
            Skills.History:         skills_base_y + 12*skill_step,
            Skills.Insight:         skills_base_y + 11*skill_step,
            Skills.Intimidation:    skills_base_y + 10*skill_step,
            Skills.Investigation:   skills_base_y + 9*skill_step,
            Skills.Medicine:        skills_base_y + 8*skill_step,
            Skills.Nature:          skills_base_y + 7*skill_step,
            Skills.Perception:      skills_base_y + 6*skill_step,
            Skills.Performance:     skills_base_y + 5*skill_step,
            Skills.Persuasion:      skills_base_y + 4*skill_step,
            Skills.Religion:        skills_base_y + 3*skill_step,
            Skills.Slight_Of_Hand:  skills_base_y + 2*skill_step,
            Skills.Stealth:         skills_base_y + skill_step,
            Skills.Survival:        skills_base_y,
        }
        self.Set_Font_Size(6)
        for skill in skills_y.keys():
            self.draw_string((x, skills_y[skill]), "%+d" % saving_throws[skill])
            if skill in proficiencies:
                self.draw_circle((x + proficiency_x_offset, skills_y[skill] + proficiency_y_offset), 1.1*mm)
        score_iter = iter(count(0.48/8.5, 0.395/8.5))
        abilities_x = {
            Skills.Strength:     next(score_iter),
            Skills.Dexterity:    next(score_iter),
            Skills.Constitution: next(score_iter),
            Skills.Intelligence: next(score_iter),
            Skills.Wisdom:       next(score_iter),
            Skills.Charisma:     next(score_iter),
        }
        self.Set_Font_Size(8)
        for skill in abilities_x.keys():
            self.draw_string((abilities_x[skill], 8.53/11.0), "%+d" % saving_throws[skill])

    def Draw_Details(self, initiative, speed, hp_maximum, hit_dice, proficiency_bonus, passive_perception):
        self.Set_Font_Size(12)
        self.draw_centered_string((370.0/1223.0,  1 - (244.0/1576.0)),  "%+d" % proficiency_bonus)
        self.draw_centered_string((470.0/1223.0,  1 - (890.0/1576.0)),  str(passive_perception))
        self.draw_centered_string((1055.0/1223.0, 1 - (874.0/1576.0)),  str(speed))
        self.draw_centered_string((990.0/1223.0,  1 - (212.0/1576.0)),  "%+d" % initiative)
        self.draw_centered_string((723.0/1223.0,  1 - (1105.0/1576.0)), str(hp_maximum))

        self.Set_Font_Size(5)
        self.draw_string((463.0/1223.0,  1 - (1109.0/1576.0)), hit_dice)


    def Draw_Other_Proficiencies(self, other_proficiencies):
        proficiencies_string = ""
        for title, proficiencies in other_proficiencies.items():
            proficiencies_string += title
            proficiencies_string += ': '
            proficiencies_string += ', '.join(proficiencies)
            proficiencies_string += '\n'
        self.Set_Font_Size(8)
        self.draw_strings((482.0/1223.0,  1 - (1397.0/1576.0)), self._line_spacing, proficiencies_string)


    def Draw_Equipment(self, equipment):
        pass


    def Draw_Features_And_Traits(self, features_and_traits):
        self.Set_Font_Size(8)
        self.draw_strings((5.95/8.5, 3.72/11.0), self._line_spacing, features_and_traits)


    def Draw_Characteristics(self, personality_traits, ideals, bonds, flaws):
        pass
