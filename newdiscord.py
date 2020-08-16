import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("하이")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
# client.run("NzQ0NDQ4MTgyMjQ2ODM0MjI3.XzjXZQ.PlijkNerOo91mRNjE6xQeMaKM30")




# import discord
# import os
# from bs4 import BeautifulSoup
# from urllib.request import urlopen
#
# app = discord.Client() #클라이언트 변수
#
# @app.event
# async def on_ready():
#     print("다음으로 로그인 합니다 : ")
#     print(app.user.name)
#     print(app.user.id)
#     print("-----------------")
#
# @app.event
# async def on_message(message):
#     #---- << 초기화 >> ----------------------------------------------------------------------------------------#
#
#     if message.content == "!초기화":
#         await app.change_presence(status=discord.Status.online, activity = None)
#         await message.channel.send("상태를 초기화 했다멍!")
#
#
#     #---- << 봇 상태설정 >> ---------------------------------------------------------------------------------------#
#
#     if message.content == "!poe" or message.content == "!POE" or message.content == "!패스오브엑자일":
#         activeGame = discord.Game(name="Path of Exile")
#         await app.change_presence(status=discord.Status.online, activity = activeGame)
#         await message.channel.send("패스 오브 엑자일을 플레이 할 거다멍!")
#
#
#     if message.content == "!롤" or message.content == "!롤체스" or message.content == "!lol" or message.content == "!LOL":
#         activeGame = discord.Game(name="League of Legends")
#         await app.change_presence(status=discord.Status.online, activity = activeGame)
#         await message.channel.send("리그 오브 레전드를 플레이 할 거다멍!")
#
#
#     #---- << 커맨드 명령어 >> ---------------------------------------------------------------------------------------#
#
#     # < 명령어 목록 >
#     if message.content == "!명령어":
#         await message.channel.send("명령어 목록 이다멍!")
#
#         embed = discord.Embed(
#             title="!롤 !롤체스 !lol !LOL",
#             description="아리가 롤플 플레이 합니다.",
#             color=discord.Colour.blue()
#             )
#
#         embed.add_field(
#             name="!poe !POE !패스오브엑자일",
#             value="아리가 poe를 플레이 합니다.",
#             inline=False
#             )
#
#         embed.add_field(
#             name="야리! 아리",
#             value="아리가 poe를 플레이 합니다.",
#             inline=False
#             )
#
#         embed.set_footer(text = "2019.07.03 최종수정본")
#         #embed.set_image(url="https://i.imgur.com/xzPCXp8.jpg")
#         await message.channel.send(embed=embed)
#
#     # < 아리 호출 >
#     if message.content.startswith("아리!") or message.content.startswith("아리 ") or message.content.startswith("아리야"):
#         text = message.content[3:]
#
#         # < 날씨 검색 >
#         if "날씨" in text:
#             url = ""
#             area = ""
#             flag = False
#
#             if "용인" in text:
#                 area = "용인"
#                 url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%9A%A9%EC%9D%B8+%EB%82%A0%EC%94%A8"
#                 flag = True
#
#             elif "서울" in text:
#                 area = "서울"
#                 url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
#                 flag = True
#
#             elif "분당" in text:
#                 area = "분당"
#                 url = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EB%B6%84%EB%8B%B9+%EB%82%A0%EC%94%A8"
#                 flag = True
#
#             else:
#                 await message.channel.send("지역을 같이 물어봐주라멍!")
#
#             if (flag == True):
#                 html = urlopen(url)
#                 source = html.read()
#                 html.close()
#                 soup = BeautifulSoup(source, "html.parser")
#                 nowTemp = soup.select('.todaytemp')[0].text
#                 todayCast = soup.select('.cast_txt')[0].text
#                 amRainRate = soup.select('.num')[7].text
#                 pmRainRate = soup.select('.num')[8].text
#
#                 await message.channel.send(area + "의 날씨 정보 입니다멍!")
#                 embed = discord.Embed(
#                 title = area + "날씨",
#                 description = "\u200b",
#                 color = discord.Colour.green()
#                 )
#                 embed.add_field(
#                 name="현재 온도",
#                 value=nowTemp + "℃ " + todayCast,
#                 inline=False
#                 )
#                 embed.add_field(
#                 name="비 올 확률",
#                 value="오전 " + amRainRate + "%, " + "오후 " + pmRainRate + "%",
#                 inline=False
#                 )
#                 embed.set_footer(text = "네이버 날씨")
#                 await message.channel.send(embed=embed)
#
#         else:
#             await message.channel.send("무슨 말인지 모르겠다멍!")
#
#
#     #--------------------------------------------------------------------------------------------------------------#
#
# app.run("NzQ0NDQ4MTgyMjQ2ODM0MjI3.XzjXZQ.PlijkNerOo91mRNjE6xQeMaKM30")
