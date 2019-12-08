from enum import Enum, auto
from reportlab.lib.units import *

class Skills(Enum):
    Strength = auto()
    Dexterity = auto()
    Constitution = auto()
    Intelligence = auto()
    Wisdom = auto()
    Charisma = auto()
    Acrobatics = auto()
    Animal_Handling = auto()
    Arcana = auto()
    Athletics = auto()
    Deception = auto()
    History = auto()
    Insight = auto()
    Intimidation = auto()
    Investigation = auto()
    Medicine = auto()
    Nature = auto()
    Perception = auto()
    Performance = auto()
    Persuasion = auto()
    Religion = auto()
    Slight_Of_Hand = auto()
    Stealth = auto()
    Survival = auto()

    def Stat(self):
        switcher = {
            Skills.Strength: Skills.Strength, 
            Skills.Dexterity: Skills.Dexterity, 
            Skills.Constitution: Skills.Constitution, 
            Skills.Intelligence: Skills.Intelligence, 
            Skills.Wisdom: Skills.Wisdom, 
            Skills.Charisma: Skills.Charisma, 
            Skills.Acrobatics: Skills.Dexterity,
            Skills.Animal_Handling: Skills.Wisdom,
            Skills.Arcana: Skills.Intelligence,
            Skills.Athletics: Skills.Strength,
            Skills.Deception: Skills.Charisma,
            Skills.History: Skills.Intelligence,
            Skills.Insight: Skills.Wisdom,
            Skills.Intimidation: Skills.Charisma,
            Skills.Investigation: Skills.Intelligence,
            Skills.Medicine: Skills.Wisdom,
            Skills.Nature: Skills.Intelligence,
            Skills.Perception: Skills.Wisdom,
            Skills.Performance: Skills.Charisma,
            Skills.Persuasion: Skills.Charisma,
            Skills.Religion: Skills.Intelligence,
            Skills.Slight_Of_Hand: Skills.Dexterity,
            Skills.Stealth: Skills.Dexterity,
            Skills.Survival: Skills.Wisdom
        }
        return switcher[self]

class CharacterSheetLayout():
    def __init__(self, canvas, background):
        self.Canvas = canvas
        self.PageSize = canvas._pagesize
        self.Background = background
        self._font_size_scale = self.PageSize[1] / (11*inch)

    def Set_Font_Size(self, size):
        self.Canvas.setFontSize(size * self._font_size_scale)

    def draw_strings(self, point, spacing, strings):
        font_size_to_points = 0.75
        x = point[0]
        if isinstance(strings,(tuple,list)):
            x += spacing
            bullet_x = (x + point[0])/2.0
            for i in range(len(strings)):
                bullet_y_offset = (self.Canvas._fontsize * font_size_to_points * 0.5 / self.PageSize[1]) - (spacing * i)
                self.draw_circle((bullet_x, point[1] + bullet_y_offset), (self.Canvas._fontsize * font_size_to_points) / 8.0)
        text_block = self.Canvas.beginText(x * self.PageSize[0], point[1] * self.PageSize[1])
        text_block.setLeading(spacing * self.PageSize[1])
        text_block.textLines(strings, trim=0)
        self.Canvas.drawText(text_block)

    def draw_string(self, point, value):
        self.Canvas.drawString(point[0] * self.PageSize[0], point[1] * self.PageSize[1], value)

    def draw_centered_string(self, point, value):
        self.Canvas.drawCentredString(point[0] * self.PageSize[0], point[1] * self.PageSize[1], value)

    def draw_circle(self, point, radius):
        self.Canvas.circle(point[0] * self.PageSize[0], point[1] * self.PageSize[1], radius * self._font_size_scale, fill=1)

    def Draw_Character_Info(self, name, level, class_5e, background, player_name, race, alignment):
        pass

    def Draw_Stats(self, scores, modifiers):
        pass

    def Draw_Skills(self, saving_throws, proficiencies):
        pass

    def Draw_Details(self, initiative, speed, hp_maximum, hit_dice, proficiency_bonus, passive_perception):
        pass

    def Draw_Other_Proficiencies(self, other_proficiencies):
        pass

    def Draw_Equipment(self, equipment):
        pass

    def Draw_Features_And_Traits(self, features_and_traits):
        pass

    def Draw_Characteristics(self, personality_traits, ideals, bonds, flaws):
        pass
