import discord

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	elif message.content.startswith('$01') or message.content.startswith('$02'):
		await message.channel.send('Roll on this table at the start of each of your turns ' 
			+ 'for the next minute ignoring this result on subsequent rolls.')

	elif message.content.startswith('$03') or message.content.startswith('$04'):
		await message.channel.send('For the next minute, you can see any invisible creature ' 
			+ 'if you have line of sight to it.')

	elif message.content.startswith('$05') or message.content.startswith('$06'):
		await message.channel.send('A modron chosen and controlled by the DM appears ' 
			+ 'in an unoccupied space with 5 feet of you, then disappears 1 minute later.')

	elif message.content.startswith('$07') or message.content.startswith('$08'):
		await message.channel.send('You cast Fireball as a 3rd-level spell centered on yourself.')

	elif message.content.startswith('$09') or message.content.startswith('$10'):
		await message.channel.send('You cast Magic Missle as a 5th-level spell.')

	elif message.content.startswith('$11') or message.content.startswith('$12'):
		await message.channel.send('Roll a d10. Your height changes by a number of inches equal ' 
			+ 'to the roll. If the roll is odd, you shrink. If the roll is is even, you grow.')

	elif message.content.startswith('$13') or message.content.startswith('$14'):
		await message.channel.send('You cast Confusion centered on yourself.')

	elif message.content.startswith('$15') or message.content.startswith('$16'):
		await message.channel.send('For the next minute, you regain 5 hit points at the start of each of your turns.')

	elif message.content.startswith('$17') or message.content.startswith('$18'):
		await message.channel.send('You grow a long beard made of feathers that remains until you sneeze, '
			+ 'at which point the feathers explode out from your face.')

	elif message.content.startswith('$19') or message.content.startswith('$20'):
		await message.channel.send('You cast Grease centered on yourself.')

	elif message.content.startswith('$21') or message.content.startswith('$22'):
		await message.channel.send('Creatures have disadvantage on saving throws against ' 
			+ 'the next spell you cast in the next minute that involves a saving throw.')

	elif message.content.startswith('$23') or message.content.startswith('$24'):
		await message.channel.send('Your skin turns a vibrant shade of blue. A Remove Curse spell can end this effect.')

	elif message.content.startswith('$25') or message.content.startswith('$26'):
		await message.channel.send('An eye appears on your forehead for the next minute. '
			+ 'During that time, you have advantage on Wisdom (Perception) checks that rely on sight.')

	elif message.content.startswith('$27') or message.content.startswith('$28'):
		await message.channel.send('For the next minute, all your spells with a casting time of 1 action '
			+ 'have a casting time of 1 bonus action.')

	elif message.content.startswith('$29') or message.content.startswith('$30'):
		await message.channel.send('You teleport up to 60 feet to an unoccupied space of your choice that you can see.')

	elif message.content.startswith('$31') or message.content.startswith('$32'):
		await message.channel.send('You are transported to the Astral Plane until the end of your next turn, '
			+ 'after which time you return to the space you previously occupied or the nearest unoccupied space if that space is occupied.')

	elif message.content.startswith('$33') or message.content.startswith('$34'):
		await message.channel.send('Maximize the damage of the next damaging spell you cast within the next minute.')

	elif message.content.startswith('$35') or message.content.startswith('$36'):
		await message.channel.send('Roll a d10. Your age changes by a number equal to the roll. '
			+ 'If the roll is odd, you get younger (minimum 1 year old). If the roll is even, you get older.')

	elif message.content.startswith('$37') or message.content.startswith('$38'):
		await message.channel.send('1d6 flumphs controlled by the DM appear in unoccupied spaces '
			+ 'within 60 feet of you and are frightened of you. They vanish after 1 minute.')

	elif message.content.startswith('$39') or message.content.startswith('$40'):
		await message.channel.send('You regain 2d10 hit points.')

	elif message.content.startswith('$41') or message.content.startswith('$42'):
		await message.channel.send('You turn into a potted plant until the start of your next turn. '
			+ 'While a plant, you are incapacitated and have vulnerability to all damage. '
			+ 'If you drop to 0 hit points, your pot breaks, and your form reverts.')

	elif message.content.startswith('$43') or message.content.startswith('$44'):
		await message.channel.send('For the next minute, you can teleport up to 20 feet as a bonus action on each of your turns.')

	elif message.content.startswith('$45') or message.content.startswith('$46'):
		await message.channel.send('You cast Levitate on yourself.')

	elif message.content.startswith('$47') or message.content.startswith('$48'):
		await message.channel.send('A unicorn controlled by the DM appears in a space within 5 feet of you, then disappears 1 minute later.')

	elif message.content.startswith('$49') or message.content.startswith('$50'):
		await message.channel.send('You can\'t speak for the next minute. Whenever you try, pink bubbles float out of your mouth.')

	elif message.content.startswith('$51') or message.content.startswith('$52'):
		await message.channel.send('A spectral shield hovers near you for the next minute, granting '
			+ 'you a +2 bonus to AC and immunity to Magic Missle.')

	elif message.content.startswith('$53') or message.content.startswith('$54'):
		await message.channel.send('You are immune to being intoxicated by alcohol for the next 5d6 days.')

	elif message.content.startswith('$55') or message.content.startswith('$56'):
		await message.channel.send('Your hair falls out but grows back within 24 hours.')

	elif message.content.startswith('$57') or message.content.startswith('$58'):
		await message.channel.send('For the next minute, any flammable object you touch that isn\'t being worn '
			+ 'or carried by another creature bursts into flame.')

	elif message.content.startswith('$59') or message.content.startswith('$60'):
		await message.channel.send('You regain your lowest level expended spell slot.')

	elif message.content.startswith('$61') or message.content.startswith('$62'):
		await message.channel.send('For the next minute, you must shout when you speak.')

	elif message.content.startswith('$63') or message.content.startswith('$64'):
		await message.channel.send('You cast Fog Cloud centered on yourself.')

	elif message.content.startswith('$65') or message.content.startswith('$66'):
		await message.channel.send('Up to three creatures you choose within 30 feet of you take 4d10 lightning damage.')

	elif message.content.startswith('$67') or message.content.startswith('$68'):
		await message.channel.send('You are frightened by the nearest creature until the end of your next turn.')

	elif message.content.startswith('$69') or message.content.startswith('$70'):
		await message.channel.send('Each creature within 30 feet of you becomes invisible for the '
			+ 'next minute. The invisible ends on a creature when it attacks or casts a spell.')

	elif message.content.startswith('$71') or message.content.startswith('$72'):
		await message.channel.send('You gain resistance to all damage for the next minute.')

	elif message.content.startswith('$73') or message.content.startswith('$74'):
		await message.channel.send('A random creature within 60 feet of you becomes poisoned for 1d4 hours.')

	elif message.content.startswith('$75') or message.content.startswith('$76'):
		await message.channel.send('You glow with bright light in a 30-foot radius for the next minute. '
			+ 'Any creature that ends its turn within 5 feet of you is blinded until the end of its next turn.')

	elif message.content.startswith('$77') or message.content.startswith('$78'):
		await message.channel.send('You cast Polymorph on yourself. If you fail the saving throw, you turn '
			+ 'into a sheep for the spell\'s duration.')

	elif message.content.startswith('$79') or message.content.startswith('$80'):
		await message.channel.send('Illusory butterflies and flower petals flutter in the air within 10 feet of you for the next minute.')

	elif message.content.startswith('$81') or message.content.startswith('$82'):
		await message.channel.send('You can take one additional action immediately.')

	elif message.content.startswith('$83') or message.content.startswith('$84'):
		await message.channel.send('Each creature within 30 feet of you takes 1d10 necrotic damage. '
			+ 'You regain hit points equal to the sum of the necrotic damage dealt.')

	elif message.content.startswith('$85') or message.content.startswith('$86'):
		await message.channel.send('You cast Mirror Image.')

	elif message.content.startswith('$87') or message.content.startswith('$88'):
		await message.channel.send('You cast Fly on a random creature within 60 feet of you.')

	elif message.content.startswith('$89') or message.content.startswith('$90'):
		await message.channel.send('You become invisible for the next minute. During that time, '
			+ 'other creatures can\'t hear you. The invisibility ends if you attack or cast a spell.')

	elif message.content.startswith('$91') or message.content.startswith('$92'):
		await message.channel.send('If you die within the next minute, you immediately come back '
			+ 'to life as if by the Reincarnate spell.')

	elif message.content.startswith('$93') or message.content.startswith('$94'):
		await message.channel.send('Your size increases by one size category for the next minute.')

	elif message.content.startswith('$95') or message.content.startswith('$96'):
		await message.channel.send('You and all creatures within 30 feet of you gain vulnerability '
			+ 'to piercing damage for the next minute.')

	elif message.content.startswith('$97') or message.content.startswith('$98'):
		await message.channel.send('You are surronded by faint, ethereal music for the next minute.')

	elif message.content.startswith('$99') or message.content.startswith('$$100'):
		await message.channel.send('You regain all expended sorcery points.')

client.run('Njg5MzI5OTYyNDY5MTYzMDI1.XnBVDQ.NBpERyuBSbRjVuLFyUneLnh6baE')