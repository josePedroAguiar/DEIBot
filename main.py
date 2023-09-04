import discord
import datetime as t
import asyncio
import days
import os
from keep_alive import keep_alive
client = discord.Client()
id=int(os.getenv('ID'))
async def my_background_task():
  await client.wait_until_ready()
  while not client.is_closed(): 
    tempo=t.localtime.now()
    print(tempo.strftime("%X"))
    dis=days.aulas(tempo)
    if (dis!=0):
      link1,link2=days.link_disciplina(dis)
      channel= client.get_channel(id)
      await channel.send(dis+'@everyone\nPresença: '+ link1+'\nLink ZOOM(T e TP): '+link2)
       
    await asyncio.sleep(35)

@client.event
async def on_ready():
  channel= client.get_channel(id)
  print('We have logged in as {0.user}'.format(client))


client.loop.create_task(my_background_task())


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  #channel
  if message.content.startswith('$'):
    link1,link2=days.link_disciplina(message.content)
    await message.channel.send('Presença: '+ link1)
    await message.channel.send('Link ZOOM(T e TP): '+link2)
  #privado
  if message.content.startswith('-'):
    link1,link2=days.info_disciplina(message.content)
    await message.author.send("\t\t"+message.content+'\nPresença: '+link1+'\nLink ZOOM(T e TP):'+link2)
  #PL privado
  if message.content.startswith('*'):
    link=days.links_pl(message.content)
    await message.author.send("\t\t"+message.content+'\nPresença: '+"https://ucstudent.uc.pt/")
    await message.author.send('Link ZOOM(PL): '+link)
  if message.content.startswith('!help'):
    await message.channel.send("$(ACRONIMO DA CADEIRA)- LINK\n-(ACRONIMO DA CADEIRA)- LINK)(privado)\n*(ACRONIMO DA CADEIRA)-Link PL só do admin :)")
keep_alive()   
client.run(os.getenv('TOKEN'))

