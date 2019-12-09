from reportlab.lib.units import *
from CharacterSheetLayout import CharacterSheetLayout, Skills
from itertools import *

percent = 1.0/100.0;

class OriginalCharacterSheetLayout(CharacterSheetLayout):
    def __init__(self, canvas):
        self._line_spacing = (3.85*mm)/(11.0*inch)
        super(OriginalCharacterSheetLayout, self).__init__(
            canvas,
            "C:\\Users\\Matt\\Documents\\dev\\character-sheet-generator\\resources\\official.png")


    def Draw_Character_Info(self, name, level, class_5e, background, player_name, race, alignment):
        base_x = 44.7*percent
        x_step = (1.5/8.5)
        y_1 = 89*percent
        y_2 = 92.3*percent

        self.Set_Font_Size(16)
        self.draw_string((9*percent, 90*percent), name)

        self.Set_Font_Size(12)
        self.draw_string((base_x,            y_2), class_5e + ' - ' + str(level))
        self.draw_string((base_x + x_step,   y_2), background)
        self.draw_string((base_x + 2*x_step, y_2), player_name)

        self.draw_string((base_x,          y_1), race)
        self.draw_string((base_x + x_step, y_1), alignment)


    def Draw_Stats(self, scores, modifiers):
        x = 9.45*percent
        step = 9*percent
        score_iter = iter(count(30*percent, step))
        modifier_iter = iter(count(32.5*percent, step))
        self.Set_Font_Size(8)
        self.draw_centered_string((x, next(score_iter)), str(scores[Skills.Charisma]))
        self.draw_centered_string((x, next(score_iter)), str(scores[Skills.Wisdom]))
        self.draw_centered_string((x, next(score_iter)), str(scores[Skills.Intelligence]))
        self.draw_centered_string((x, next(score_iter)), str(scores[Skills.Constitution]))
        self.draw_centered_string((x, next(score_iter)), str(scores[Skills.Dexterity]))
        self.draw_centered_string((x, next(score_iter)), str(scores[Skills.Strength]))

        self.Set_Font_Size(18)
        self.draw_centered_string((x, next(modifier_iter)), str(modifiers[Skills.Charisma]))
        self.draw_centered_string((x, next(modifier_iter)), str(modifiers[Skills.Wisdom]))
        self.draw_centered_string((x, next(modifier_iter)), str(modifiers[Skills.Intelligence]))
        self.draw_centered_string((x, next(modifier_iter)), str(modifiers[Skills.Constitution]))
        self.draw_centered_string((x, next(modifier_iter)), str(modifiers[Skills.Dexterity]))
        self.draw_centered_string((x, next(modifier_iter)), str(modifiers[Skills.Strength]))


    def Draw_Skills(self, saving_throws, proficiencies):
        skill_step = 1.7*percent
        x = 19.1*percent
        stats_base_y = 64.55*percent
        skills_base_y = 29.55*percent
        proficiency_x_offset = -1.9*percent
        proficiency_y_offset = 0.015 / 11.0
        skills_y = {
            Skills.Strength:        stats_base_y + 5*skill_step,
            Skills.Dexterity:       stats_base_y + 4*skill_step,
            Skills.Constitution:    stats_base_y + 3*skill_step,
            Skills.Intelligence:    stats_base_y + 2*skill_step,
            Skills.Wisdom:          stats_base_y + skill_step,
            Skills.Charisma:        stats_base_y,
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
        self.Set_Font_Size(8)
        for skill in Skills:
            self.draw_string((x, skills_y[skill]), "%+d" % saving_throws[skill])
            if skill in proficiencies:
                self.draw_circle((x + proficiency_x_offset, skills_y[skill] + proficiency_y_offset), 1*mm)

    def Draw_Details(self, initiative, speed, hp_maximum, hit_dice, proficiency_bonus, passive_perception):
        self.Set_Font_Size(16)
        self.draw_centered_string((17.9*percent, 76.8*percent), "%+d" % proficiency_bonus)
        self.draw_centered_string((7*percent, 23.6*percent), str(passive_perception))

        self.Set_Font_Size(18)
        self.draw_centered_string((49.7*percent, 79*percent), "%+d" % initiative)
        self.draw_centered_string((59.3*percent, 79*percent), str(speed))

        self.Set_Font_Size(8)
        self.draw_string((50*percent, 74*percent), str(hp_maximum))
        self.draw_string((41.7*percent, 58.8*percent), hit_dice)


    def Draw_Other_Proficiencies(self, other_proficiencies):
        proficiencies_string = ""
        for title, proficiencies in other_proficiencies.items():
            proficiencies_string += title
            proficiencies_string += ':\n'
            for proficiency in proficiencies:
                proficiencies_string += '    '
                proficiencies_string += proficiency
                proficiencies_string += '\n'
        self.Set_Font_Size(8)
        self.draw_strings((0.6/8.5, 20*percent), self._line_spacing, proficiencies_string)


    def Draw_Equipment(self, equipment):
        self.Set_Font_Size(8)
        self.draw_strings((3.85/8.5, 2.66/11.0), self._line_spacing, equipment)


    def Draw_Features_And_Traits(self, features_and_traits):
        self.Set_Font_Size(8)
        self.draw_strings((5.75/8.5, 5.55/11.0), self._line_spacing, features_and_traits)


    def Draw_Characteristics(self, personality_traits, ideals, bonds, flaws):
        self.Set_Font_Size(8)
        characteristics_line_spacing = (4.5*mm)/(11.0*inch)
        self.draw_strings((5.85/8.5, 8.95/11.0), characteristics_line_spacing, personality_traits)
        self.draw_strings((5.85/8.5, 7.98/11.0), characteristics_line_spacing, ideals)
        self.draw_strings((5.85/8.5, 7.22/11.0), characteristics_line_spacing, bonds)
        self.draw_strings((5.85/8.5, 6.45/11.0), characteristics_line_spacing, flaws)