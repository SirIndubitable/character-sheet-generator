from enum import Enum, auto

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
	def __init__(self,
				 background_path,
				 name,
				 character_class,
				 background,
				 player_name,
				 race,
				 alignment,
				 speed,
				 str_score,
				 str_modifier,
				 dex_score,
				 dex_modifier,
				 con_score,
				 con_modifier,
				 int_score,
				 int_modifier,
				 wis_score,
				 wis_modifier,
				 cha_score,
				 cha_modifier,
				 proficiency_bonus,
				 passive_perception,
				 saving_throws,
				 proficiencies):
		self.Background_Path = background_path
		self.Name = name
		self.Class = character_class
		self.Background = background
		self.Player_Name = player_name
		self.Race = race
		self.Alignment = alignment
		self.Speed = speed
		self.Str_Score = str_score
		self.Str_Modifier = str_modifier
		self.Dex_Score = dex_score
		self.Dex_Modifier = dex_modifier
		self.Con_Score = con_score
		self.Con_Modifier = con_modifier
		self.Int_Score = int_score
		self.Int_Modifier = int_modifier
		self.Wis_Score = wis_score
		self.Wis_Modifier = wis_modifier
		self.Cha_Score = cha_score
		self.Cha_Modifier = cha_modifier
		self.Proficiency_Bonus = proficiency_bonus
		self.Passive_Perception = passive_perception
		self.Saving_Throws = saving_throws
		self.Proficiencies = proficiencies
		