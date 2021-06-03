from redbot.core import commands
from redbot.core.utils.chat_formatting import box, bold

import random

# Night market categories
nMarkets = [
	'Food and Drugs', 
	'Personal Electronics', 
	'Weapons and Armor', 
	'Cyberware', 
	'Clothing and Fashionware', 
	'Survival Gear'
	]
# Night market shelf items
# Food and Drugs
fd = [
	'Canned Goods - 10E$', 
	'Packaged Goods - 10E$', 
	'Frozen Goods - 10E$', 
	'Bags of Grain - 20E$', 
	'Kibble Pack - 10E$', 
	'Bags of Prepak - 20E$', 
	'Poor Quality Alcohol - 10E$', 
	'Alcohol - 20E$', 
	'Excellent Quality Alcohol - 100E$', 
	'MRE - 10E$', 
	'Live Chicken - 50E$', 
	'Live Fish - 50E$', 
	'Fresh Fruits - 50E$', 
	'Fresh Vegetables - 50E$', 
	'Root Vegetables - 20E$', 
	'Live Pigs - 100E$', 
	'Exotic Fruits - 100E$', 
	'Exotic Vegetables - 100E$'
	]
# Personal Electronics
pe = [
	'Agent - 100E$',  
	'Audio Recorder - 100E$', 
	'Bug Detector - 500E$', 
	'Chemical Analyzer - 1000E$', 
	'Computer - 50E$',  
	'Disposable Cell Phone - 50E$', 
	'Medscanner - 1000E$', 
	'Homing Tracer - 500E$', 
	'Radio Communicator - 100E$', 
	'Techscanner - 1000E$', 
	'Smart Glasses - 500E$', 
	'Radar Detector - 500E$', 
	'Scrambler/Descrambler - 500E$', 
	'Radio Scanner - 50E$', 
	'Braindance Viewer - 1000E$', 
	'Virtuality Goggles - 100E$'
	]
# Weapons and Armor
wa = [
	'Medium Pistol - 50E$',
	'SMG - 100E$',
	'Heavy SMG - 100E$',
	'Shotgun - 500E$',
	'Assault Rifle - 500E$', 
	'Sniper Rifle - 500E$',  
	'Light Melee Weapon - 50E$', 
	'Medium Melee Weapon - 50E$', 
	'Heavy Melee Weapon - 100E$', 
	'Very Heavy Melee Weapon - 100E$'
	]
# Cyberware
cw = [
	'Cybereye - 100E$',
	'Cyberaudio Suite - 500E$',
	'Neural Link - 500E$',
	'Cyberarm - 500E$',
	'Cyberleg - 100E$'
	]
# Clothing and Fashionware
cf = [
	'Biomonitor - 100E$', 
	'Chemskin - 100E$', 
	'EMP Threading - 10E$', 
	'Light Tattoo - 100E$', 
	'Shift Tacts - 100E$', 
	'Skinwatch - 100E$', 
	'Techhair - 100E$'
	]
# Survival Gear
sg = [
	'Anti-smog Breathing Mask - 20E$', 
	'Auto Level Dampening Ear Protectors - 1000E$', 
	'Binoculars - 50E$', 
	'Carryall - 20E$', 
	'Flashlight - 20E$', 
	'Duct Tape - 20E$', 
	'Inflatable Bed & Sleep-bag - 20E$', 
	'Lock Picking Set - 20E$', 
	'Handcuffs - 50E$', 
	'Medtech Bag - 100E$', 
	'Tent and Camping Equipment - 50E$', 
	'Rope (60m) - 20E$', 
	'Techtool - 100E$', 
	'Personal CarePak - 20E$', 
	'Radiation Suit - 1000E$', 
	'Road Flare - 10E$', 
	'Grapple Gun - 100E$', 
	'Tech Bag - 500E$',  
	'Airhypo - 50E$',
	'Glow Paint - 20E$'
	]

streetDrugsLess20 = [
	'Blue Glass - 20E$',
	'Smash - 10E$',
	'Synthcoke - 20E$'
	]

streetDrugs50 = [
	'Black Lace - 50E$',
	'Boost - 50E$'
	]

progsLess100 = [
	'Backup Drive - 100E$',
	'DNA Lock - 100E$',
	'Hardened Circuitry - 100E$',
	'Insulated Wiring - 100E$',
	'KRASH Barrier - 100E$',
	'Range Upgrade - 100E$',
	'Eraser - 20E$',
	'See Ya - 20E$',
	'Speedy Gonzalvez - 100E$',
	'Worm - 50E$',
	'Armor - 50E$',
	'Flak - 50E$',
	'Shield - 20E$',
	'Banhammer - 50E$',
	'Sword - 50E$',
	'DeckKRASH - 100E$',
	'Hellbolt - 100E$',
	'Nervescrub - 100E$',
	'Poison Flatline - 100E$',
	'Superglue - 100E$',
	'Vrizzbolt - 50E$',
	'Asp - 100E$',
	'Raven - 50E$',
	'Scorpion - 100E$',
	'Wisp - 50E$'
	]

progsMore500 = [
	'Giant - 1000E$',
	'Hellhound - 500E$',
	'Kraken - 1000E$',
	'Liche - 500E$',
	'Skunk - 500E$',
	'Dragon - 1000E$',
	'Killer - 500E$',
	'Sabertooth - 1000E$',
	'Imp - 1000E$',
	'Efreet - 5000E$',
	'Balron - 10000E$'
	]

instruments = [
	'Electric Guitar - 500E$',
	'Acoustic Guitar - 500E$',
	'Piano - 500E$',
	'Violin - 500E$',
	'Drums - 500E$',
	'Kazoo - 50E$',
	'Electric Kazoo - 100E$',
	'Portable Amplifier - 50E$',
	'Drum Synthesizer - 500E$'
	]

cyberdeck = [
	'Cyberdeck (5 slots) - 100E$',
	'Cyberdeck (7 slots) - 500E$',
	'Cyberdeck (9 slots) - 1000E$'
	]

pistols = [
	'H Pistol - 100E$',
	'VH Pistol - 100E$'
	]

bows = [
	'Bow - 100E$',
	'Crossbow - 100E$'
	]

launchers = [
	'Grenade Launcher - 500E$',
	'Rocket Launcher - 500E$'
	]

exotics = [
	'Air Pistol - 100E$',
	'Battleglove - 1000E$',
	'Hurricane Assault Weapon - 5000E$',
	'Dartgun - 100E$',
	'Flamethrower - 500E$',
	'Kendachi Mono-Three - 5000E$',
	'Malorian Arms 3516 - 10000E$',
	'Microwaver - 500E$',
	'Cowboy U-56 Grenade Launcher - 5000E$',
	'Rheinmetall EMG-86 Railgun - 5000E$',
	'Shrieker - 500E$',
	'Stun Baton - 100E$',
	'Stun Gun - 100E$',
	'Tsunami Arms Helix - 5000E$'
	]

ammo = [
	'Basic Ammo - 10E$',
	'AP Ammo - 100E$',
	'Biotoxin Ammo - 500E$',
	'EMP Grenade - 500E$',
	'Expansive Ammo - 100E$',
	'Flashbang Grenade - 100E$',
	'Incendiary Ammo - 100E$',
	'Poison Ammo - 100E$',
	'Rubber Ammo - 10E$',
	'Sleep Ammo - 500E$',
	'Smart Ammo - 500E$',
	'Smoke Grenade - 50E$',
	'Teargas Grenade - 50E$',
	'Vial of Biotoxin - 500E$',
	'Vial of Poison - 100E$'
	]

armorLess100 = [
	'Leathers - 20E$',
	'Kevlar - 50E$',
	'Light Armorjack - 100E$',
	'Medium Armorjack - 100E$',
	'Bulletproof Shield - 100E$'
	]

armor500 = [
	'Heavy Armorjack - 500E$',
	'Flak - 500E$'
	]

armorMore1000 = [
	'Bodyweight Suit - 1000E$',
	'Metalgear - 5000E$'
	]

weapLess100 = [
	'Bayonet - 100E$',
	'M Pistol Extended Magazine - 100E$',
	'H Pistol Extended Magazine - 100E$',
	'VH Pistol Extended Magazine - 100E$',
	'SMG Extended Magazine - 100E$',
	'H SMG Extended Magazine - 100E$',
	'Shotgun Extended Magazine - 100E$',
	'Assault Rifle Extended Magazine - 100E$',
	'Sniper Rifle Extended Magazine - 100E$',
	'Grenade Launcher Extended Magazine - 100E$',
	'Rocket Launcher Extended Magazine - 100E$',
	'Sniping Scope - 100E$'
	]

weapMore500 = [
	'M Pistol Drum Magazine - 500E$',
	'H Pistol Drum Magazine - 500E$',
	'VH Pistol Drum Magazine - 500E$',
	'SMG Drum Magazine - 500E$',
	'H SMG Drum Magazine - 500E$',
	'Shotgun Drum Magazine - 500E$',
	'Assault Rifle Drum Magazine - 500E$',
	'Sniper Rifle Drum Magazine - 500E$',
	'Grenade Launcher Drum Magazine - 500E$',
	'Rocket Launcher Drum Magazine - 500E$',
	'Underbarrel Grenade Launcher - 500E$',
	'Infrared Nightvision Scope - 500E$',
	'Underbarrel Shotgun - 500E$',
	'Smartgun Link - 500E$'
	]

externalLess500 = [
	'Hidden Holster - 500E$',
	'Skin Weave - 500E$',
	'Subdermal Pocket - 100E$'
	]

external1000 = [
	'Subdermal Armor - 1000E$'
	]

internalLess500 = [
	'AudioVox - 500E$',
	'Contraceptive Implant - 10E$',
	'Enhanced Antibodies - 500E$',
	'Midnight Lady Sexual Implant - 100E$',
	'Mr. Studd Sexual Implant - 100E$',
	'Nasal Filters - 100E$',
	'Toxin Binders - 100E$',
	'Vampyres - 500E$'
	]

internal1000 = [
	'Cybersnake - 1000E$',
	'Gills - 1000E$',
	'Grafted Muscle and Bone Lace - 1000E$',
	'Independent Air Supply - 1000E$',
	'Radar/Sonar Implant - 1000E$'
	]

fashionware = [
	'Biomonitor - 100E$',
	'Chemskin - 100E$',
	'EMP Threading - 10E$',
	'Light Tattoo - 100E$',
	'Shift Tacts - 100E$',
	'Skinwatch - 100E$',
	'Techhair - 100E$'
	]

borgware = [
	'Artificial Shoulder Mount - 1000E$',
	'Implanted Linear Frame Sigma - 1000E$',
	'Implanted Linear Fram Beta - 5000E$',
	'MultiOptic Mount - 1000E$',
	'Sensor Array - 1000E$'
	]

cybereyeLess500 = [
	'Anti-dazzle - 100E$',
	'Chyron - 100E$',
	'Color Shift - 100E$',
	'Dartgun - 500E$',
	'Image Enhance - 500E$',
	'Low Light/Infrared/UV - 500E$',
	'MicroOptics - 100E$',
	'MicroVideo - 500E$',
	'Targeting Scope - 500E$',
	'TeleOptics - 500E$',
	'Virtuality - 100E$'
	]

cybereye1000 = [
	'Radiation Detector - 1000E$'
	]

cyberaudioLess500 = [
	'Amplified Hearing - 100E$',
	'Audio Recorder - 100E$',
	'Bug Detector - 100E$',
	'Homing Tracer - 100E$',
	'Internal Agent - 100E$',
	'Level Damper - 100E$',
	'Radio Communicator - 100E$',
	'Radio Scanner - 50E$',
	'Scrambler/Descrambler - 100E$',
	'Voice Stress Analyzer - 100E$'
	]

cyberaudio1000 = [
	'Radar Detector - 500E$'
	]

neuralLess500 = [
	'Braindance Recorder - 500E$',
	'Chipware Socket - 500E$',
	'Interface Plugs - 500E$',
	'Kerenzikov - 500E$',
	'Sandevistan - 500E$',
	'Chemical Analyzer - 500E$',
	'Memory Chip - 10E$',
	'Olfactory Boost - 100E$',
	'Skill Chip (regular) - 500E$',
	'Tactile Boost - 100E$'
	]

neural1000 = [
	'Pain Editor - 1000E$',
	'Skill Chip (x2 Skills) - 1000E$'
	]

cyberArmLess500 = [
	'Big Knucks - 100E$',
	'Cyberdeck - 500E$',
	'Grapple Hand - 100E$',
	'Medscanner - 500E$',
	'Popup Grenade Launcher - 500E$',
	'Popup Melee Weapon - 500E$',
	'Popup Shield - 500E$',
	'Popup Ranged Weapon - 500E$',
	'Quick Change Mount - 100E$',
	'Rippers - 500E$',
	'Scratchers - 100E$',
	'Shoulder Cam - 500E$',
	'Slice n Dice - 500E$',
	'Subdermal Grip - 100E$',
	'Techscanner - 500E$',
	'Tool Hand - 100E$',
	'Wolvers - 500E$'
	]

cyberLegLess500 = [
	'Grip Foot - 500E$',
	'Jump Booster - 500E$',
	'Skate Foot - 500E$',
	'Talon Foot - 500E$',
	'Web Foot - 500E$',
	'Plastic Covering - 100E$',
	'Realskinn Covering - 500E$'
	]

cyberLeg1000 = [
	'Hardened Shielding - 1000E$',
	'Superchrome Covering - 1000E$'
	]

baglady = [
	'Bag Lady Chic Bottoms - 20E$',
	'Bag Lady Chic Top - 10E$',
	'Bag Lady Chic Jacket - 20E$',
	'Bag Lady Chic Footwear - 20E$',
	'Bag Lady Chic Jewelry - 20E$',
	'Bag Lady Chic Mirrorshades - 20E$',
	'Bag Lady Chic Glasses - 10E$',
	'Bag Lady Chic Contact Lenses - 10E$',
	'Bag Lady Chic Hats - 10E$'
	]

gang = [
	'Gang Colors Bottoms - 50E$',
	'Gang Colors Top - 20E$',
	'Gang Colors Jacket - 50E$',
	'Gang Colors Footwear - 20E$',
	'Gang Colors Jewelry - 50E$',
	'Gang Colors Mirrorshades - 20E$',
	'Gang Colors Glasses - 20E$',
	'Gang Colors Contact Lenses - 10E$',
	'Gang Colors Hats - 10E$'
	]

generic = [
	'Generic Chic Bottoms - 50E$',
	'Generic Chic Top - 20E$',
	'Generic Chic Jacket - 50E$',
	'Generic Chic Footwear - 20E$',
	'Generic Chic Jewelry - 50E$',
	'Generic Chic Mirrorshades - 20E$',
	'Generic Chic Glasses - 20E$',
	'Generic Chic Contact Lenses - 10E$',
	'Generic Chic Hats - 10E$'
	]

boho = [
	'Bohemian Bottoms - 50E$',
	'Bohemian Top - 20E$',
	'Bohemian Jacket - 50E$',
	'Bohemian Footwear - 50E$',
	'Bohemian Jewelry - 100E$',
	'Bohemian Mirrorshades - 50E$',
	'Bohemian Glasses - 50E$',
	'Bohemian Contact Lenses - 10E$',
	'Bohemian Hats - 10E$'
	]

leisure = [
	'Leisurewear Bottoms - 100E$',
	'Leisurewear Top - 20E$',
	'Leisurewear Jacket - 100E$',
	'Leisurewear Footwear - 50E$',
	'Leisurewear Jewelry - 100E$',
	'Leisurewear Mirrorshades - 50E$',
	'Leisurewear Glasses - 50E$',
	'Leisurewear Contact Lenses - 20E$',
	'Leisurewear Hats - 50E$'
	]

leathers = [
	'Nomad Leathers Bottoms - 100E$',
	'Nomad Leathers Top - 20E$',
	'Nomad Leathers Jacket - 100E$',
	'Nomad Leathers Footwear - 100E$',
	'Nomad Leathers Jewelry - 100E$',
	'Nomad Leathers Mirrorshades - 50E$',
	'Nomad Leathers Glasses - 50E$',
	'Nomad Leathers Contact Lenses - 20E$',
	'Nomad Leathers Hats - 100E$'
	]

asia = [
	'Asia Pop Bottoms - 100E$',
	'Asia Pop Top - 20E$',
	'Asia Pop Jacket - 100E$',
	'Asia Pop Footwear - 100E$',
	'Asia Pop Jewelry - 100E$',
	'Asia Pop Mirrorshades - 100E$',
	'Asia Pop Glasses - 100E$',
	'Asia Pop Contact Lenses - 100E$',
	'Asia Pop Hats - 100E$'
	]

urban = [
	'Urban Flash Bottoms - 100E$',
	'Urban Flash Top - 20E$',
	'Urban Flash Jacket - 100E$',
	'Urban Flash Footwear - 100E$',
	'Urban Flash Jewelry - 100E$',
	'Urban Flash Mirrorshades - 100E$',
	'Urban Flash Glasses - 100E$',
	'Urban Flash Contact Lenses - 100E$',
	'Urban Flash Hats - 100E$'
	]

business = [
	'Businesswear Bottoms - 500E$',
	'Businesswear Top - 50E$',
	'Businesswear Jacket - 500E$',
	'Businesswear Footwear - 500E$',
	'Businesswear Jewelry - 5000E$',
	'Businesswear Mirrorshades - 500E$',
	'Businesswear Glasses - 500E$',
	'Businesswear Contact Lenses - 100E$',
	'Businesswear Hats - 500E$'
	]

high = [
	'High Fashion Bottoms - 1000E$',
	'High Fashion Top - 500E$',
	'High Fashion Jacket - 1000E$',
	'High Fashion Footwear - 5000E$',
	'High Fashion Jewelry - 50000E$',
	'High Fashion Mirrorshades - 1000E$',
	'High Fashion Glasses - 1000E$',
	'High Fashion Contact Lenses - 1000E$',
	'High Fashion Hats - 5000E$'
	]

survival = [
	'Shovel - 50E$',
	'Axe - 50E$'
	]

class CPRed(commands.Cog):
	"""A Cyberpunk Red helper cog, with dice rolling and information about the game."""

	def __init__(self, bot):
		self.bot = bot 

	def foodDrugsBuild(self):
		fdBuilt = fd
		fdBuilt += random.sample(streetDrugsLess20, k=1)
		fdBuilt += random.sample(streetDrugs50, k=1)
		return fdBuilt

	def persElecBuild(self):
		peBuilt = pe
		peBuilt += random.sample(progsLess100, k=1)
		peBuilt += random.sample(progsMore500, k=1)
		peBuilt += random.sample(instruments, k=1)
		peBuilt += random.sample(cyberdeck, k=1)
		return peBuilt

	def weapArmoBuild(self):
		waBuilt = wa
		waBuilt += random.sample(pistols, k=1)
		waBuilt += random.sample(bows, k=1)
		waBuilt += random.sample(launchers, k=1)
		waBuilt += random.sample(exotics, k=1)
		waBuilt += random.sample(ammo, k=1)
		waBuilt += random.sample(armor500, k=1)
		waBuilt += random.sample(armorLess100, k=1)
		waBuilt += random.sample(armorMore1000, k=1)
		waBuilt += random.sample(weapLess100, k=1)
		waBuilt += random.sample(weapMore500, k=1)
		return waBuilt

	def cyberBuild(self):
		cwBuilt = cw
		cwBuilt += random.sample(externalLess500, k=1)
		cwBuilt += random.sample(external1000, k=1)
		cwBuilt += random.sample(internalLess500, k=1)
		cwBuilt += random.sample(internal1000, k=1)
		cwBuilt += random.sample(fashionware, k=1)
		cwBuilt += random.sample(borgware, k=1)
		cwBuilt += random.sample(cybereyeLess500, k=1)
		cwBuilt += random.sample(cybereye1000, k=1)
		cwBuilt += random.sample(cyberaudioLess500, k=1)
		cwBuilt += random.sample(cyberaudio1000, k=1)
		cwBuilt += random.sample(neuralLess500, k=1)
		cwBuilt += random.sample(neural1000, k=1)
		cwBuilt += random.sample(cyberArmLess500, k=1)
		cwBuilt += random.sample(cyberLegLess500, k=1)
		cwBuilt += random.sample(cyberLeg1000, k=1)
		return cwBuilt

	def clothFashBuild(self):
		cfBuilt = cf
		cfBuilt += random.sample(baglady, k=1)
		cfBuilt += random.sample(gang, k=1)
		cfBuilt += random.sample(generic, k=1)
		cfBuilt += random.sample(boho, k=1)
		cfBuilt += random.sample(leisure, k=1)
		cfBuilt += random.sample(leathers, k=1)
		cfBuilt += random.sample(asia, k=1)
		cfBuilt += random.sample(urban, k=1)
		cfBuilt += random.sample(business, k=1)
		cfBuilt += random.sample(high, k=1)
		return cfBuilt

	def survGearBuild(self):
		sgBuilt = sg
		sgBuilt += random.sample(survival, k=1)
		return sgBuilt

	@commands.command()
	async def roll(self, ctx, dice: str):
		"""Rolls a die/dice in NdN format. (Ex. 1d20 for 1 d20 die roll)"""
		try:
			rolls, limit = map(int, dice.split('d'))
		except Exception:
			await ctx.send("Format must be NdN!")
			return

		result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
		await ctx.send(result)

	@commands.command()
	async def birth(self, ctx):
		"""Character creation walkthrough"""
		await ctx.send("This feature is not implemented yet")

	@commands.command()
	async def nextgame(self, ctx):
		"""See when the next game is scheduled"""
		await ctx.send("This feature is not implemented yet")

	@commands.command()
	async def nightmarket(self, ctx):
		"""Generate a Night Market to visit"""
		cat1, cat2 = random.sample(nMarkets, k=2)
		# Assign items for first selected group
		if cat1 == 'Food and Drugs':
			items1 = self.foodDrugsBuild()
		elif cat1 == 'Personal Electronics':
			items1 = self.persElecBuild()
		elif cat1 == 'Weapons and Armor':
			items1 = self.weapArmoBuild()
		elif cat1 == 'Cyberware':
			items1 = self.cyberBuild()
		elif cat1 == 'Clothing and Fashionware':
			items1 = self.clothFashBuild()
		elif cat1 == 'Survival Gear':
			items1 = self.survGearBuild()
		# Assign items for second selected group
		if cat2 == 'Food and Drugs':
			items2 = self.foodDrugsBuild()
		elif cat2 == 'Personal Electronics':
			items2 = self.persElecBuild()
		elif cat2 == 'Weapons and Armor':
			items2 = self.weapArmoBuild()
		elif cat2 == 'Cyberware':
			items2 = self.cyberBuild()
		elif cat2 == 'Clothing and Fashionware':
			items2 = self.clothFashBuild()
		elif cat2 == 'Survival Gear':
			items2 = self.survGearBuild()
		# Select amount of items for each category
		count1 = random.randint(1, 6)
		count2 = random.randint(1, 6)
		# Select which items are available
		items = random.sample(items1, k=count1) + random.sample(items2, k=count2)
		# Build response
		categories = (
			"After looking around at a few stalls, it looks like this Night Market has {category1} and {category2} available.\n\n"
			).format(
				category1=cat1,
				category2=cat2,
			)
		sellItems = '\n'.join(map(str, items))
		results = categories + sellItems
		await ctx.send(box(results))


	# Informational commands

	# Need to enable config and clean this up
	@commands.command()
	async def roles(self, ctx, select=0):
		"""List the available roles in Cyberpunk Red"""
		if select == 1:
			await ctx.send(bold("~~Rockerboys/Rockergirls~~"))
			await ctx.send("Rock-and-roll rebels who use performance, art, and rhetoric to fight authority.")
			await ctx.send(bold("Role Ability: Charismatic Impact"))
			await ctx.send("With this ability, they can influence others by sheer presence of personality.")
		elif select == 2:
			await ctx.send(bold("~~Netrunners~~"))
			await ctx.send("Cybernetic master hackers of the post-NET world and brain-burning secret stealers.")
			await ctx.send(bold("Role Ability: Interface"))
			await ctx.send("Allows them to interface with cyberdecks to control computers, electronics, and associated programming.")
		elif select == 3:
			await ctx.send(bold("~~Medtechs~~"))
			await ctx.send("Unsanctioned street doctors and cyberware medics, patching up meat and metal alike.")
			await ctx.send(bold("Role Ability: Medicine"))
			await ctx.send("Can keep people alive who should be dead with their knowledge, tools, and training.")
		elif select == 4:
			await ctx.send(bold("~~Execs~~"))
			await ctx.send("Corporate power brokers and business raiders fighting to restore the rule of the Megacorps.")
			await ctx.send(bold("Role Ability: Teamwork"))
			await ctx.send("Builds a team whose members help them accomplish their goals, whether legal or not, morale permitting.")
		elif select == 5:
			await ctx.send(bold("~~Fixers~~"))
			await ctx.send("Dealmakers, organizers, and information brokers in the post-War Midnight Markets of The Street.")
			await ctx.send(bold("Role Ability: Operator"))
			await ctx.send("Know how to get things on the black market and are adept at navigating the complex social customs of The Street.")
		elif select == 6:
			await ctx.send(bold("~~Solos~~"))
			await ctx.send("Assassins, bodyguards, killers, and soldiers-for-hire in a lawless new world.")
			await ctx.send(bold("Role Ability: Combat Awareness"))
			await ctx.send("Can call up their training to have an enhanced situational awareness of the battlefield.")
		elif select == 7:
			await ctx.send(bold("~~Techs~~"))
			await ctx.send("Renegade mechanics and supertech inventors; the people who make the Dark Future run.")
			await ctx.send(bold("Role Ability: Maker"))
			await ctx.send("Can fix, improve, modify, make, and invent new items.")
		elif select == 8:
			await ctx.send(bold("~~Medias~~"))
			await ctx.send("Reporters, media stars, and social influencers risking it all for the truth - or glory.")
			await ctx.send(bold("Role Ability: Credibility"))
			await ctx.send("Have greater levels of access to sources and information; they are always picking up rumors and information passively.")
		elif select == 9:
			await ctx.send(bold("~~Lawmen/Law-women~~"))
			await ctx.send("Maximum law enforcers patrolling the mean streets and barbarian warrior highways beyond.")
			await ctx.send(bold("Role Ability: Backup"))
			await ctx.send("Can call upon the help of a group of fellow officers, based on rank and conditions.")
		elif select == 10:
			await ctx.send(bold("~~Nomad~~"))
			await ctx.send("Transport experts, ultimate road warriors, pirates, and smugglers who keep the world connected.")
			await ctx.send(bold("Role Ability: Moto"))
			await ctx.send("Able to drive any type of vehicle with tremendous skill.")
		else:
			await ctx.send(box("**Roles of Cyberpunk Red**\n1.Rockerboys\t6.Solos\n2.Netrunners\t7.Techs\n3.Medtechs\t  8.Medias\n4.Execs\t\t 9.Lawmen\n5.Fixers\t\t10.Nomads"))
			await ctx.send("For more information about a particular role, run the !role command with the role number at the end.")
			await ctx.send(bold("(ex. !roles 3)"))

	@commands.command()
	async def homes(self, ctx):
		"""List the available homes in Cyberpunk Red"""
		await ctx.send(bold("Real Estate\tCost per Month\tCost to Buy"))
		await ctx.send("Living on the Street\tN/A\tN/A\nLiving on the Street in a Vehicle\tN/A\tN/A\nCube Hotel\t500E$\tN/A\nCargo Container\t1000E$\t15000E$\nStudio Apartment\t1500E$\t25000E$\nTwo-bedroom Apartment\t2500E$\t35000E$\nCorporate Conapt\tPaid by Corp\tN/A\nUpscale Conapt\t7500E$\t85000E$\nLuxury Penthouse\t15000\t150000\nCorp Beaverville House\tPaid by Corp\t200000\nCorp Beaverville McMansion\tPaid by Corp\t500000E$")
