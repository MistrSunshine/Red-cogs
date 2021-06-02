from redbot.core import commands
from redbot.core.utils.chat_formatting import box, bold

import random

# Night market categories
nMarkets = ['Food and Drugs', 'Personal Electronics', 'Weapons and Armor', 'Cyberware', 'Clothing and Fashionware', 'Survival Gear']
# Night market shelf items
# Food and Drugs
fd = ['Canned Goods - 10E$', 'Packaged Goods - 10E$', 'Frozen Goods - 10E$', 'Bags of Grain - 20E$', 'Kibble Pack - 10E$', 'Bags of Prepak - 20E$', '*Street Drugs <20E$', 'Poor Quality Alcohol - 10E$', 'Alcohol - 20E$', 'Excellent Quality Alcohol - 100E$', 'MRE - 10E$', 'Live Chicken - 50E$', 'Live Fish - 50E$', 'Fresh Fruits - 50E$', 'Fresh Vegetables - 50E$', 'Root Vegetables - 20E$', 'Live Pigs - 100E$', 'Exotic Fruits - 100E$', 'Exotic Vegetables - 100E$', '*Street Drugs = 50E$']
# Personal Electronics
pe = ['Agent - 100E$', '*Programs or Hardware <100E$', 'Audio Recorder - 100E$', 'Bug Detector - 500E$', 'Chemical Analyzer - 1000E$', 'Computer - 50E$', 'Cyberdeck - 500E$', 'Disposable Cell Phone - 50E$', '*Instrument - 500E$', '*Programs or Hardware - 500E$', 'Medscanner - 1000E$', 'Homing Tracer - 500E$', 'Radio Communicator - 100E$', 'Techscanner - 1000E$', 'Smart Glasses - 500E$', 'Radar Detector - 500E$', 'Scrambler/Descrambler - 500E$', 'Radio Scanner - 50E$', 'Braindance Viewer - 1000E$', 'Virtuality Goggles - 100E$']
# Weapons and Armor
wa = []
# Cyberware
cw = []
# Clothing and Fashionware
cf = ['*Bag Lady Chic', '*Gang Colors', '*Generic Chic', '*Bohemian', '*Leisurewear', '*Nomad Leathers', '*Asia Pop', '*Urban Flash', '*Businesswear', '*High Fashion', 'Biomonitor - 100E$', 'Chemskin - 100E$', 'EMP Threading - 10E$', 'Light Tattoo - 100E$', 'Shift Tacts - 100E$', 'Skinwatch - 100E$', 'Techhair - 100E$', '*Generic Chic', '*Leisurewear', '*Gang Colors']
# Survival Gear
sg = []

class CPRed(commands.Cog):
	"""A Cyberpunk Red helper cog, with dice rolling and information about the game."""

	def __init__(self, bot):
		self.bot = bot 

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
		results = (
			"After looking around at a few stalls, it looks like this Night Market has {category1} and {category2} available."
			).format(
				category1=cat1,
				category2=cat2,
			)
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
