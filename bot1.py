import discord


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("!!도움말을 말한사람에게 설명")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on message(message):
 if message.content.startswith('!!안녕')
        await message.channel.send("안녕하다냥")

    if message.content.startswith("!!도움말"):
        embed = discord.Embed(color=0xff00ff)
        embed.add_field(name='냥 너에게 몇가지를 설명하겠다냥')
        embed.add_field(name='대화-안녕,반가워,잘가,누구세요,욕')
        embed.add_field(name='놀이-놀자,DM,아이스크림')
        embed.set_thumbnail(url=message.author.avarter_url)

    if message.content.startswith("!!"):
        await message.channel.send("명령어 모르냥?????바보같다냥..")


    if message.content.startswith("!!반가워"):
        await message.channel.send("이하동문이다냥")


    if message.content.startswith("!!누구세요"):
        await message.channel.send("난~~~하찮은~~~~~~고얭이라냐아아앙~~~")


    if message.content.startswith("!!욕"):
        await message.channel.send("넌 이 욕 모르지? WTF!!!!!!!!")

    if message.content.startwith("!!놀자"):
         await message.channel.send('난 먹는거랑 빈둥거리는거가 노는거다냥. @'message.author.name)

    if message.content.startswith("!!DM"):
        await message.channel.send("내가 그정도까지 똑똑하진 않다냥. 그래도 기다려봐냥")
        author = message.guild.get_number(int(message.content[4:22])
        msg = message.content[23:]
        await author.send(msg)

client.run("Njk1OTA5NTEwOTMzNTEyMjQy.XohCcg.qAMoZyS1__b24YJwfKSd_TstWAo")


