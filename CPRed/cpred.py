from redbot.core import commands
import random

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


	# Informational commands

	@commands.command()
	async def roles(self, ctx):
		"""List the available roles in Cyberpunk Red"""
		await ctx.send("**Roles of Cyberpunk Red**\n1.Rockerboys\t6.Solos\n2.Netrunners\t7.Techs\n3.Medtechs\t  8.Medias\n4.Execs\t\t\t  9.Lawmen\n5.Fixers\t\t\t  10.Nomads")
