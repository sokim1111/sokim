# -*- coding:utf-8 -*-

import discord, asyncio, random
token = "Njg2NDIyNzI1MTkxMDA4MjU4.XmXy3g.49HIrEpP0g6NGCStRF595zkZ5vM" # 아까 메모해 둔 토큰을 입력합니다
client = discord.Client() # discord.Client() 같은 긴 단어 대신 client를 사용하겠다는 선언입니다.
@client.event
async def on_ready(): # 봇이 준비가 되면 1회 실행되는 부분입니다.
    # discord.Status.online에서 online을 dnd로 바꾸면 "다른 용무 중", idle로 바꾸면 "자리 비움"으로 바뀝니다.
    await client.change_presence(status=discord.Status.online, activity=discord.Game("소원 성취"))

@client.event
async def on_message(message): # 메시지가 들어 올 때마다 가동되는 구문입니다.
    if message.content == "하나코 사랑해":
        rdlove=random.randint(1,3)
        if rdlove==1:
            await message.channel.send("나.. 나는.. 이만 가볼게!!")
        if rdlove==2:
            await message.channel.send("이런 거 좀 곤란한데..")
        if rdlove==3:
            await message.channel.send("... 고마워")   
    if message.content == "하나코 좋아해":
        rdlove=random.randint(1,3)
        if rdlove==1:
            await message.channel.send("내키진 않지만.. 나도")
        if rdlove==2:
            await message.channel.send("너라면 받아들일 수 있어.. 나도 좋아해")
        if rdlove==3:
            await message.channel.send("좋아해.. 말로 표현 할수 없을 만큼")

    if message.content == "하나코 안녕":
        await message.channel.send("어? 별일 이네. 안녕. 무슨 볼일이야?")
    if message.content == "하나코 이스터에그":
        await message.channel.send("❤")
    if message.content == "하나코 안녕":
        await message.channel.send("어? 별일 이네. 안녕. 무슨 볼일이야?")

client.run("Njg2NDIyNzI1MTkxMDA4MjU4.XmXy3g.49HIrEpP0g6NGCStRF595zkZ5vM") # 아까 넣어놓은 토큰 가져다가 봇을 실행하라는 부분입니다. 이 코드 없으면 구문이 아무리 완벽해도 실행되지 않습니다.


