from redbot.core import Config
from redbot.core import commands, bank, bot, checks
from redbot.core.utils.chat_formatting import box, bold
from redbot.core.utils import embed

import random
import discord

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

# Food and Drugs
streetDrugsLess20 = [
	'Blue Glass - 20E$',
	'Smash - 10E$',
	'Synthcoke - 20E$'
	]

streetDrugs50 = [
	'Black Lace - 50E$',
	'Boost - 50E$'
	]

# Personal Electronics
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

# Weapons and Armor
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

# Cyberware
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

# Fashion
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

# Survival
survival = [
	'Shovel - 50E$',
	'Axe - 50E$'
	]

# Drugs
drugs = [
	'Black Lace - 50E$',
	'Blue Glass - 20E$',
	'Boost - 50E$',
	'Smash - 10E$',
	'Synthcoke - 20E$',
	'Alcohol - 5E$',
	'Rohypnol - 20E$'
	]

class CPRed(commands.Cog):
	"""A Cyberpunk Red helper cog, with dice rolling and information about the game."""

	def __init__(self, bot):
		self.bot = bot 
		self.config = Config.get_conf(self, identifier=8465013279)

		self.config.register_global(
			nextDate = "Sun, Jun 13th",
			nextTime = "8:00PM",
			fixerLvl = 1,
			achList = {
				"Test": "Super cool tester"
			},
			graveyard = [],
			jackpot = 5000,
			lottopool = 0,
			prizes = [],
			assets = "",
			game = ""
			)
		self.config.register_user(
			currentip = 0,
			totalip = 0,
			awarded = {},
			tickets = []
			)

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
		# Add modifier ability and make result message nicer
		try:
			rolls, limit = map(int, dice.split('d'))
		except Exception:
			await ctx.send(box("Format must be NdN!"))
			return
		author = str(ctx.author)
		announce = " has rolled {} d{} dice. The results are:".format(rolls, limit)
		result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
		await ctx.send(box(author + announce + '\n\n' + result))

	@commands.command()
	async def birth(self, ctx):
		"""Character creation walkthrough *wip"""
		await ctx.send(box("This feature is not implemented yet"))

	@commands.command()
	async def nextgame(self, ctx):
		"""See when the next game is scheduled"""
		next_val = await self.config.nextDate() + ' at ' + await self.config.nextTime() + '.'
		await ctx.send(box("The next game is scheduled for {}".format(next_val)))

	@commands.command()
	@commands.is_owner()
	async def setnextdate(self, ctx, new_value):
		"""Set the date for the next scheduled game"""
		await self.config.nextDate.set(new_value)
		date = await self.config.nextDate()
		await ctx.send(box("The next scheduled game date has been set to {}.".format(date)))

	@commands.command()
	@commands.is_owner()
	async def setnexttime(self, ctx, new_value):
		"""Set the time for the next scheduled game"""
		await self.config.nextTime.set(new_value)
		time = await self.config.nextTime()
		await ctx.send(box("The time for the next scheduled game is set to {}.".format(time)))

	@commands.command()
	async def homebrew(self, ctx):
		"""WIP Homebrew rule suggestion and voting system"""
		embed=discord.Embed(title="Active Homebrew Rules", description="Homebrew rules being used for our CP Red games", color=0xff0f13)
		embed.add_field(name="Advantage/Disadvantage Rolls", value="When performing actions in stealth or before detected, players will perform two checks and use the higher of the two rolls. Alternatively, if the player is surprised, they may roll twice and take the lower roll.", inline=False)
		embed.set_footer(text="Suggest homebrew rules to make our games more exciting with the !suggest command.")
		await ctx.send(embed=embed)

	@commands.group()
	async def ip(self, ctx: commands.Context):
		"""
		Commands to control the Improvement Point System
		"""

	@ip.command(name="current")
	async def ip_current(self, ctx, user: discord.User=0):
		"""Check your characters IP balance"""
		try:
			# Call the config values
			currentIP = await self.config.user(user).currentip()
			totalIP = await self.config.user(user).totalip()
			# Stringify values
			sCurrentIP = str(currentIP)
			sTotalIP = str(totalIP)
			# Concatenate and send it
			ip_val = sCurrentIP + ' of ' + sTotalIP
			await ctx.send(box("{} currently has {} improvement points available.".format(user, ip_val)))
		except:
			# Call the config values
			currentIP = await self.config.user(ctx.author).currentip()
			totalIP = await self.config.user(ctx.author).totalip()
			# Stringify values
			sCurrentIP = str(currentIP)
			sTotalIP = str(totalIP)
			# Concatenate and send it
			ip_val = sCurrentIP + ' of ' + sTotalIP
			await ctx.send(box("You currently have {} improvement points available.".format(ip_val)))

	@ip.command(name="add")
	@commands.is_owner()
	async def ip_add(self, ctx, user: discord.User, amount: int):
		"""Add IP to a user's character"""
		# Increment the available IP
		init_val = await self.config.user(user).currentip()
		new_val = init_val + amount
		await self.config.user(user).currentip.set(new_val)
		# Also add to the total gained IP
		init_tot = await self.config.user(user).totalip()
		new_tot = init_tot + amount
		await self.config.user(user).totalip.set(new_tot)
		# Stringify
		new_val = str(new_val)
		new_tot = str(new_tot)
		# Reply to user
		await ctx.send(box("{} has been added to {} IP totals.".format(amount, user) + "\n\n" + "The new values are {} of {} IP.".format(new_val, new_tot)))

	@ip.command(name="use")
	async def ip_use(self, ctx, amount: int):
		"""Use the IP assigned to your character"""
		init_val = await self.config.user(ctx.author).currentip()
		if amount <= init_val:
			# Subtract the used IP
			new_val = init_val - amount
			await self.config.user(ctx.author).currentip.set(new_val)
			# Call total IP
			total = await self.config.user(ctx.author).totalip()
			# Stringify
			total = str(total)
			new_val = str(new_val)
			amount = str(amount)
			# Reply to user
			await ctx.send(box("You have successfully used {} IP.".format(amount) + "\n\n" + "Your new IP values are {} of {}.".format(new_val, total)))
		else:
			await ctx.send(box("You don't have enough IP for that."))

	@ip.command(name="reset")
	@commands.is_owner()
	async def ip_reset(self, ctx, user: discord.User):
		"""Reset a user's IP count after death"""
		await self.config.user(user).currentip.set(0)
		await self.config.user(user).totalip.set(0)
		await ctx.send(box("Improvement points have been reset for {}.".format(user)))

	@commands.group()
	async def lottery(self, ctx: commands.Context):
		"""
		Control the Lottery system
		"""

	@lottery.command(name="jackpot")
	async def lottery_jackpot(self, ctx):
		"""Get the current lottery jackpot amount"""
		pot = await self.config.jackpot()
		sPot = str(pot)
		await ctx.send(box("The current jackpot is at {}.".format(sPot)))

	@lottery.command(name="tickets")
	async def lottery_tickets(self, ctx):
		"""Check which numbers you've already bought"""
		ticks = await self.config.user(ctx.author).tickets()
		sTicks = str(ticks)
		await ctx.send("{} currently has tickets: {}".format(ctx.author, sTicks))

	@lottery.command(name="buy")
	async def lottery_buy(self, ctx, number: int=0):
		"""Buy a lottery ticket for 100E$"""
		if await bank.can_spend(ctx.author, 100):
			if number == 0:
				number = random.randint(1, 99)
			await bank.withdraw_credits(ctx.author, 100)
			pool = await self.config.lottopool()
			pool = pool + 100
			await self.config.lottopool.set(pool)
			nmbrs = await self.config.user(ctx.author).tickets()
			nmbrs.append(number)
			await self.config.user(ctx.author).tickets.set(nmbrs)
			sNumber = str(number)
			await ctx.send(box("You have purchased a ticket with the number: {}".format(sNumber)))
		else:
			await ctx.send(box("You do not appear to have enough E$ to purchase a lottery ticket. Tickets are 100E$ each."))

	@lottery.command(name="draw")
	@commands.is_owner()
	async def lottery_draw(self, ctx):
		"""Draw a winning number for the lottery"""
		winNum = random.randint(1, 99)
		users = await self.config.all_users()
		key = users.keys()
		win = []
		sWin = []
		jp = await self.config.jackpot()
		for member in key:
			name = self.bot.get_user(member)
			ticks = await self.config.user(name).tickets()
			if winNum in ticks:
				win.append(name)
				sWin.append(str(name))
			clr = []
			await self.config.user(name).tickets.set(clr)
		if len(win) < 1:
			jp += await self.config.lottopool()
			await self.config.jackpot.set(jp)
			await self.config.lottopool.set(0)
			await ctx.send(box("The winning number was: {}. There were no winners this drawing. The new jackpot is {}E$!".format(str(winNum), str(jp))))
		else:
			winnings = int(jp / len(win))
			for winner in win:
				await bank.deposit_credits(winner, winnings)
			new = 5000 + await self.config.lottopool()
			await self.config.jackpot.set(new)
			await self.config.lottopool.set(0)
			await ctx.send("The winning number was: {}. The winners of this drawing were: {}. Each winner won {}E$.".format(str(winNum), sWin, winnings))
			await ctx.send("Next weeks jackpot is set at {}E$.".format(new))

	@commands.group()
	async def prize(self, ctx: commands.Context):
		"""
		Prize selection commands
		"""

	@prize.command(name="add")
	@commands.is_owner()
	async def prize_add(self, ctx, prize: str):
		"""Add a prize to the prize list"""
		lst = await self.config.prizes() + prize
		await self.config.prizes.set(lst)
		await ctx.send(box("{} has been added to the prize list.".format(prize)))

	@prize.command(name="select")
	@commands.is_owner()
	async def prize_select(self, ctx, user: discord.User):
		"""Randomly select 3 raffle prizes"""
		options = await self.config.prizes()
		selection = random.sample(options, k=3)
		sSelection = '\n'.join(map(str, selection))
		await ctx.send("Congratulations {}! Please choose one prize from the following:\n\n".format(user) + sSelection)

	@commands.group()
	async def fixer(self, ctx: commands.Context):
		"""
		Control fixer level for Night Market generator
		"""

	@fixer.command(name="set")
	@commands.is_owner()
	async def fixer_set(self, ctx, level: int):
		"""Set the current fixer level for night market generation"""
		await self.config.fixerLvl.set(level)
		lvl = await self.config.fixerLvl()
		lvl = str(lvl)
		# Level should probably be between 1-6
		await ctx.send(box("The fixer is now set to level {}.".format(lvl)))

	@fixer.command(name="level")
	async def fixer_level(self, ctx):
		"""Show the current fixer level being used by the night market generator"""
		fixer = await self.config.fixerLvl()
		fixer = str(fixer)
		await ctx.send(box("Your current fixer is level {}.".format(fixer)))

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
		top = 5 + await self.config.fixerLvl()
		count1 = random.randint(1, top)
		count2 = random.randint(1, top)
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

	@commands.command()
	async def dealer(self, ctx):
		"""Generate drugs available at a dealer"""
		variety = random.randint(1, 3)
		available = random.sample(drugs, variety)
		msg = "The dealer has these available:\n\n"
		for item in available:
			amt = random.randint(1, 5)
			msg += str(amt) + ' ' + str(item) + '\n'
		await ctx.send(box(msg))

	@commands.group()
	async def achievements(self, ctx: commands.Context):
		"""
		Commands to control the Achievements system.
		"""

	@achievements.command(name="unlocked")
	async def achievements_unlocked(self, ctx, user: discord.User=0):
		"""Display player achievements"""
		try:
			awards = await self.config.user(user).awarded()
			sAwards = str(awards)
			await ctx.send(box("{}'s current achievements are:\n".format(user) + sAwards))
		except:
			awards = await self.config.user(ctx.author).awarded()
			sAwards = str(awards)
			await ctx.send(box("Your current achievements are:\n" + sAwards))

	@achievements.command(name="add")
	@commands.is_owner()
	async def achievements_add(self, ctx, achievement: str, desc: str):
		"""Add an achievement and desc to the achievement system"""
		achvDB = await self.config.achList()
		achvDB[achievement] = desc
		await self.config.achList.set(achvDB)
		await ctx.send(box("The {} achievement has been added to the catalogue.".format(achievement)))

	@achievements.command(name="award")
	@commands.is_owner()
	async def achievements_award (self, ctx, user: discord.User, achievement: str):
		"""Award an achievement to a player"""
		try:
			achvDB = await self.config.achList()
			desc = achvDB[achievement]
			awd = {}
			awd = await self.config.user(user).awarded()
			awd[achievement] = desc
			await self.config.user(user).awarded.set(awd)
			await ctx.send(box("The {} achievement has been unlocked by {}!".format(achievement, user)))
			await ctx.send(box("The description for {} is '{}'.".format(achievement, desc)))
		except:
			await ctx.send(box("The requested achievement was not found."))

	@achievements.command(name="list")
	async def achievements_list (self, ctx):
		"""List available achievements"""
		listAch = await self.config.achList()
		awards = []
		for key, value in listAch.items():
			awards.append(key + ' : ' + value)
		awards = awards.split(',')
		msg = '\n'.join(awards)
		await ctx.send("Available achievements are:\n{}".format(awards))

	# Informational commands

	@commands.command()
	async def source(self, ctx):
		"""Display the GitHub URL for the CP_AI cog"""
		await ctx.send("The CP_AI sourcecode can be found at: https://github.com/MistrSunshine/Red-cogs")

	@commands.command()
	async def graveyard(self, ctx):
		"""Visit the graves of those that have fallen"""
		graves = await self.config.graveyard()
		if len(graves) == 0:
			await ctx.send("The graveyard is empty.")
		else:
			msg = "Walking through the graveyard, you notice the following gravestones:\n"
			msg += graves
			await ctx.send("msg")

	@commands.command()
	async def addgrave(self, ctx, death):
		"""Bury a character in the graveyard"""
		# Format is Name - Quote - Date
		graves = await self.config.graveyard()
		graves.append(death)
		await self.config.graveyard.set(graves)
		await ctx.send("{} has been added to the graveyard.".format(death))

	@commands.command()
	async def assets(self, ctx):
		"""Display a link to the shared assets folder for map making"""
		link = await self.config.assets()
		await ctx.send("The shared files can be found at: " + link)

	@commands.command()
	@commands.is_owner()
	async def addassets(self, ctx, link: str):
		"""Add a link to the shared assets"""
		await self.config.assets.set(link)
		await ctx.send("The assets link has been set to: " + link)

	@commands.command()
	async def game(self, ctx):
		"""Display a link to the game server"""
		link = await self.config.game()
		await ctx.send("The game server can be found at: " + link)

	@commands.command()
	@commands.is_owner()
	async def addgame(self, ctx, link: str):
		"""Add a link to the game server"""
		await self.config.game.set(link)
		await ctx.send("The game link has been set to: " + link)

	@commands.command()
	@commands.is_owner()
	async def cmds(self, ctx):
		"""Lists relevant user commands"""
		# Money
		embed=discord.Embed(title="~ E$ Money E$ ~", description="Commands to control your E$", color=0xcaf0fe)
		embed.set_author(name="CP_AI", icon_url="https://cdn.discordapp.com/avatars/848331788270436372/d274fe90da1a000a4446401f3b73719b.png?size=1024")
		embed.set_thumbnail(url="https://ih1.redbubble.net/image.647035563.7656/st,small,845x845-pad,1000x1000,f8f8f8.u6.jpg")
		embed.add_field(name="!payday", value="Collect 200E$ from doing sidejobs during the week. This can be activated every 7 days.", inline=False)
		embed.add_field(name="!bank balance", value="Check your E$ balance, optionally, add a user at the end to check their balance.", inline=False)
		embed.add_field(name="!bank transfer [user] [amount]", value="Transfer [amount] of E$ from your account to [user].", inline=False)
		embed.add_field(name="!stocks list", value="List the stocks you currently own.", inline=False)
		embed.add_field(name="!stocks price [name]", value="Show the price of stock [name].", inline=False)
		embed.add_field(name="!stocks buy [name] [shares]", value="Buy [shares] shares of stock [name].", inline=False)
		embed.add_field(name="!stocks sell [name] [shares]", value="Sell [shares] shares of stock [name].", inline=False)
		await ctx.send(embed=embed)
		# Gambling
		embed=discord.Embed(title="~ Gambling ~", description="Commands to win big or lose all your E$", color=0x94e3fe)
		embed.set_author(name="CP_AI", icon_url="https://cdn.discordapp.com/avatars/848331788270436372/d274fe90da1a000a4446401f3b73719b.png?size=1024")
		embed.set_thumbnail(url="https://playlincoln.com/wp-content/uploads/2019/10/AdobeStock_290994991.jpeg")
		embed.add_field(name="!slot [bet]", value="Play a slot machine (bet 5-100).", inline=False)
		embed.add_field(name="!allin [multiplier]", value="Bet all your money. The higher the [multiplier] the worse your odds.", inline=False)
		embed.add_field(name="!blackjack [bet]", value="Play a game of blackjack (bet 50-500).", inline=False)
		embed.add_field(name="!coin [bet] [choice]", value="Flip a coin with a 50/50 chance. (bet 5-20) (choose heads or tails).", inline=False)
		embed.add_field(name="!craps [bet]", value="Play a modified version of craps (bet 50-500).", inline=False)
		embed.add_field(name="!cups [bet] [cup]", value="Guess the cup hiding the coin (bet 25-100) (cup = 1, 2, or 3)", inline=False)
		embed.add_field(name="!dice [bet]", value="Roll dice and win on a 2, 7, 11, and 12 (bet 25-100).", inline=False)
		embed.add_field(name="!double [bet]", value="Play a game of double or nothing (bet 10-250).", inline=False)
		embed.add_field(name="!hilo [bet] [choice]", value="Pick high, low, or 7 of a dice roll (bet 25-75) (choice = high, low, or 7).", inline=False)
		embed.add_field(name="!war [bet]", value="Play a modified game of war (bet 25-75).", inline=False)
		embed.add_field(name="!russian", value="Start a game of Russian Roulette for others to join. (Cost to enter is 500E$, last one standing takes all)", inline=False)
		await ctx.send(embed=embed)
		# Lottery
		embed=discord.Embed(title="~ Lottery ~", description="All that E$ sitting out there with no owner", color=0x53d5fd)
		embed.set_author(name="CP_AI", icon_url="https://cdn.discordapp.com/avatars/848331788270436372/d274fe90da1a000a4446401f3b73719b.png?size=1024")
		embed.set_thumbnail(url="https://www.wikihow.com/images/thumb/2/28/Choose-Lottery-Numbers-Step-20-Version-3.jpg/aid684371-v4-1200px-Choose-Lottery-Numbers-Step-20-Version-3.jpg")
		embed.add_field(name="!lottery buy [number]", value="Buy a lottery ticket with [number]. If no number is provided, a random number is chosen. (number between 1-99)", inline=False)
		embed.add_field(name="!lottery jackpot", value="Show the current lottery jackpot.", inline=False)
		embed.add_field(name="!lottery tickets", value="Show a list of your current lottery tickets.", inline=False)
		await ctx.send(embed=embed)
		# IP
		embed=discord.Embed(title="~ Improvement Points ~", description="Get that power level over 9000!", color=0x00c7fc)
		embed.set_author(name="CP_AI", icon_url="https://cdn.discordapp.com/avatars/848331788270436372/d274fe90da1a000a4446401f3b73719b.png?size=1024")
		embed.set_thumbnail(url="https://cdn1.vectorstock.com/i/1000x1000/13/00/level-up-neon-text-level-up-neon-sign-vector-22241300.jpg")
		embed.add_field(name="!ip current", value="Show your character's current IP.", inline=False)
		embed.add_field(name="!ip use [amount]", value="Spend [amount] of IP to improve your character.", inline=False)
		await ctx.send(embed=embed)
		# General
		embed=discord.Embed(title="~ General ~", description="A list of general commands.", color=0x00a3d7)
		embed.set_author(name="CP_AI", icon_url="https://cdn.discordapp.com/avatars/848331788270436372/d274fe90da1a000a4446401f3b73719b.png?size=1024")
		embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Information.svg/1024px-Information.svg.png")
		embed.add_field(name="!source", value="Display a link to the bot GitHub repository.", inline=False)
		embed.add_field(name="!assets", value="Display a link to the CP Red assets share.", inline=False)
		embed.add_field(name="!game", value="Display a link to the CP Red game server.", inline=False)
		embed.add_field(name="!achievements unlocked", value="Display a list of your player achievements, optionally, add a user at the end to check their achievements.", inline=False)
		embed.add_field(name="!fixer level", value="Shows the current level of the crews fixer.", inline=False)
		embed.add_field(name="!nightmarket", value="Generate a random night market encounter.", inline=False)
		embed.add_field(name="!dealer", value="Generate a random drug dealer encounter.", inline=False)
		embed.add_field(name="!nextgame", value="Display the next scheduled games date and time.", inline=False)
		embed.add_field(name="!roll [amount]d[sides]", value="Roll [amount] dice with [sides]. Ex. !roll 2d13", inline=False)
		embed.add_field(name="!homebrew", value="List the current implemented home rules for our game.", inline=False)
		embed.add_field(name="!roles", value="Show available character roles included with Cyberpunk Red.", inline=False)
		embed.add_field(name="!homes", value="Show available homes with corresponding prices.", inline=False)
		embed.add_field(name="!drugs", value="Show available drugs included with Cyberpunk Red.", inline=False)
		embed.add_field(name="!graveyard", value="Remember those that have fallen.", inline=False)
		embed.add_field(name="!tarot [option]", value="Receive a tarot reading from our Cyberpunk AI. (option can be: life, reading, or card)", inline=False)
		await ctx.send(embed=embed)
		# Help
		embed=discord.Embed(title="~ Help ~", description="Having trouble? Check here.", color=0x008cb4)
		embed.set_author(name="CP_AI", icon_url="https://cdn.discordapp.com/avatars/848331788270436372/d274fe90da1a000a4446401f3b73719b.png?size=1024")
		embed.set_thumbnail(url="https://contenthub-static.grammarly.com/blog/wp-content/uploads/2018/05/how-to-ask-for-help-437x230.jpg")
		embed.add_field(name="!help [command]", value="Get helpful information about a [command]. Ex. !help homes", inline=True)
		embed.add_field(name="!contact [message]", value="If you have other questions about a commands or use, send a [message] to the bot owner.", inline=True)
		await ctx.send(embed=embed)

	@commands.command()
	async def roles(self, ctx, select=0):
		"""List the available roles in Cyberpunk Red"""
		if select == 1:
			await ctx.send(bold("~~Rockerboys/Rockergirls~~"))
			await ctx.send("Rock-and-roll rebels who use performance, art, and rhetoric to fight authority. (p.30)")
			await ctx.send(bold("Role Ability: Charismatic Impact"))
			await ctx.send("With this ability, they can influence others by sheer presence of personality.")
		elif select == 2:
			await ctx.send(bold("~~Netrunners~~"))
			await ctx.send("Cybernetic master hackers of the post-NET world and brain-burning secret stealers. (p.32)")
			await ctx.send(bold("Role Ability: Interface"))
			await ctx.send("Allows them to interface with cyberdecks to control computers, electronics, and associated programming.")
		elif select == 3:
			await ctx.send(bold("~~Medtechs~~"))
			await ctx.send("Unsanctioned street doctors and cyberware medics, patching up meat and metal alike. (p.34)")
			await ctx.send(bold("Role Ability: Medicine"))
			await ctx.send("Can keep people alive who should be dead with their knowledge, tools, and training.")
		elif select == 4:
			await ctx.send(bold("~~Execs~~"))
			await ctx.send("Corporate power brokers and business raiders fighting to restore the rule of the Megacorps. (p.36)")
			await ctx.send(bold("Role Ability: Teamwork"))
			await ctx.send("Builds a team whose members help them accomplish their goals, whether legal or not, morale permitting.")
		elif select == 5:
			await ctx.send(bold("~~Fixers~~"))
			await ctx.send("Dealmakers, organizers, and information brokers in the post-War Midnight Markets of The Street. (p.38)")
			await ctx.send(bold("Role Ability: Operator"))
			await ctx.send("Know how to get things on the black market and are adept at navigating the complex social customs of The Street.")
		elif select == 6:
			await ctx.send(bold("~~Solos~~"))
			await ctx.send("Assassins, bodyguards, killers, and soldiers-for-hire in a lawless new world. (p.31)")
			await ctx.send(bold("Role Ability: Combat Awareness"))
			await ctx.send("Can call up their training to have an enhanced situational awareness of the battlefield.")
		elif select == 7:
			await ctx.send(bold("~~Techs~~"))
			await ctx.send("Renegade mechanics and supertech inventors; the people who make the Dark Future run. (p.33)")
			await ctx.send(bold("Role Ability: Maker"))
			await ctx.send("Can fix, improve, modify, make, and invent new items.")
		elif select == 8:
			await ctx.send(bold("~~Medias~~"))
			await ctx.send("Reporters, media stars, and social influencers risking it all for the truth - or glory. (p.35)")
			await ctx.send(bold("Role Ability: Credibility"))
			await ctx.send("Have greater levels of access to sources and information; they are always picking up rumors and information passively.")
		elif select == 9:
			await ctx.send(bold("~~Lawmen/Law-women~~"))
			await ctx.send("Maximum law enforcers patrolling the mean streets and barbarian warrior highways beyond. (p.37)")
			await ctx.send(bold("Role Ability: Backup"))
			await ctx.send("Can call upon the help of a group of fellow officers, based on rank and conditions.")
		elif select == 10:
			await ctx.send(bold("~~Nomad~~"))
			await ctx.send("Transport experts, ultimate road warriors, pirates, and smugglers who keep the world connected. (p.39)")
			await ctx.send(bold("Role Ability: Moto"))
			await ctx.send("Able to drive any type of vehicle with tremendous skill.")
		else:
			await ctx.send(box("**Roles of Cyberpunk Red**\n1.Rockerboys\t6.Solos\n2.Netrunners\t7.Techs\n3.Medtechs\t  8.Medias\n4.Execs\t\t 9.Lawmen\n5.Fixers\t\t10.Nomads"))
			await ctx.send("For more information about a particular role, run the !roles command with the role number at the end.")
			await ctx.send(bold("(Ex. !roles 3) (p.29)"))

	@commands.command()
	async def homes(self, ctx):
		"""List the available homes in Cyberpunk Red"""
		street = "Living on The Street  |  Rent:N/A  |  Buy:N/A\n"
		vehicle = "Living in a vehicle  |  Rent:N/A  |  Buy:N/A\n"
		cube = "Cube Hotel  |  Rent:500E$  |  Buy:N/A\n"
		cargo = "Cargo Container  |  Rent:1000E$  |  Buy:15000E$\n"
		studio = "Studio Apartment  |  Rent:1500E$  |  Buy:25000E$\n"
		twobr = "Two Bedroom Apt  |  Rent:2500E$  |  Buy:35000E$\n"
		cCon = "Corpo Conapt  |  Rent:Paid by Corp  |  Buy:N/A\n"
		upCon = "Upscale Conapt  |  Rent: 7500E$  |  Buy:85000E$\n"
		luxPent = "Luxury Penthouse  |  Rent:15000E$  |  Buy:150000E$\n"
		cHouse = "Corpo House  |  Rent:Paid by Corp  |  Buy:200000E$\n"
		cMansion = "Corpo Mansion  |  Rent:Paid by Corp  |  Buy:500000E$\n"
		await ctx.send(box(street + vehicle + cube + cargo + studio + twobr + cCon + upCon + luxPent + cHouse + cMansion + "(p.378)"))

	@commands.command()
	async def drugs(self, ctx, drug=0):
		"""List the available drugs and their effects in Cyberpunk Red"""
		if drug == 1:
			await ctx.send(box("Black Lace\nCost per Dose: 50E$\nLasts: 24h\n\nPrimary Effects:\n* The user takes 2d6 Humanity Loss upon taking a dose, which is returned if the user isn't affected by Black Lace's Secondary Effect.\n* For the duration of the Primary Effect, the user ignores the effects of the Seriously Wounded Wound State.\n\nSecondary Effect (DV17):\n* Humanity Loss from Primary Effect isn't returned.\n* You're addicted to Black Lace. While addicted, your REF is lowered by 2 points."))
		elif drug == 2:
			await ctx.send(box("Blue Glass\nCost per Dose: 20E$\nLasts: 4h\n\nPrimary Effects:\n* The GM will occasionally tell you when you are 'flashing out,' meaning you are hallucinating swirls of vibrant colors in short, powerful bursts. You lose your ability to do an Action on a Turn while in this state.\n\nSecondary Effect (DV15):\n* You're addicted to Blue Glass.\n* While addicted, The GM will occasionally tell you when you are 'flashing out,' hallucinating in short powerful bursts that cause you to lose your ability to do an Action on a Turn while in this state.\n* A Blue Glass Junkie will typically 'flash out' once every hour, but this can vary heavily from person to person.\n* While addicted to Blue Glass, its Primary Effect changes: Instead of causing you to 'flash out', you are instead immune to 'flashing out' while experiencing the Primary Effect of Blue Glass. Now, you take it for stability."))
		elif drug == 3:
			await ctx.send(box("Boost\nCost per Dose: 50E$\nLasts: 24h\n\nPrimary Effects:\n* The user's INT increases by 2 points. This can raise your INT above 8.\n\nSecondary Effect (DV17):\n* You're addicted to Boost. While addicted, your INT is lowered by 2 points."))
		elif drug == 4:
			await ctx.send(box("Smash\nCost per Dose: 10E$\nLasts: 4h\n\nPrimary Effects:\n* The user gets +2 to the following Skills: Dance, Contortionist, Conversation, Human Perception, Persuasion, and Acting.\n\nSecondary Effect (DV15):\n* You're addicted to Smash. While addicted, the user gets -2 to the following Skills: Dance, Contortionist, Conversation, Human Perception, Persuasion, and Acting.\n* While addicted to Smash, your GM will occasionally tell you when you crave more Smash, and you should do your best to roleplay accordingly."))
		elif drug == 5:
			await ctx.send(box("Synthcoke\nCost per Dose: 20E$\nLasts: 4h\n\nPrimary Effects:\n* The user's REF increases by 1 point. This can raise your REF above 8. In addition, they are prone to paranoid ideations.\n* Your GM will occasionally tell you when you feel paranoid, and you should do your best to roleplay accordingly.\n\nSecondary Effect (DV15):\n* You're addicted to Synthcoke. While addicted, your REF is lowered by 2 points, unless the user is currently experiencing the Primary Effect of Synthcoke.\n* While addicted to Synthcoke, your GM will occasionally tell you when you crave more Synthcoke, and you should do your best to roleplay accordingly."))
		elif drug == 6:
			await ctx.send(box("Alcohol\nCost per Dose: 5E$\nLasts: 2h\n\nPrimary Effects:\n* -1 REF\n* +3 to Dance, Contortionist, Conversation, Human Perception, Persuasion, and Acting\n\nSecondary Effects (DV11):\n* You are now an alcoholic, GM will let you know when alcohol is craved.\n* -1 REF, MOVE, DEX\n* -2 to Dance, Contortionist, Conversation, Human Perception, Persuasion, and Acting"))
		elif drug == 7:
			await ctx.send(box("Rohypnol\nCost per Dose: 20E$\nLasts: 4h\n\nPrimary Effects:\n* -2 REF, MOVE, DEX\n\nSecondary Effects:\nNONE"))
		else:
			await ctx.send(box("**Drugs of Cyberpunk Red**\n1.Black Lace\t6.Alcohol\n2.Blue Glass\t7.Rohypnol\n3.Boost\n4.Smash\n5.Synthcoke"))
			await ctx.send("For more information about a particular drug, run the !drugs command with the drug number at the end.")
			await ctx.send(bold("(Ex. !drugs 3) (p.227)"))

	@commands.command()
	async def test(self, ctx):
		"""Basic debugging function"""
		await ctx.send("No test code loaded at the moment.")
