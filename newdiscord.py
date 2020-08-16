import os
import discord
from urllib.request import urlopen
from bs4 import BeautifulSoup

app = discord.Client() #클라이언트 변수

@app.event
async def on_message(message):
    # < 봇 호출 >
    if message.content.startswith("!시간"):
        text = message.content
        flag = False

        # < 지역 검색 >
        if "한국" in text:
            Time_url = "https://www.timeanddate.com/worldclock/south-korea/seoul"
            area = "한국"
            flag = True

        elif "시애틀" in text:
            Time_url = "https://www.timeanddate.com/worldclock/usa/seattle"
            area = "시애틀"
            flag = True

        else:
            await message.channel.send("지역명을 같이 입력해주세요.")

        if flag == True:
            html = urlopen(Time_url)
            source = html.read()
            html.close()
            soup = BeautifulSoup(source, "html.parser")

            classData = soup.select('.h1')[0]
            Time = classData.text
            Time = Time.replace('.', '')
            Time = Time(3:4) + "시 " + Time(6:7) + "분 " + Time(9:10) + "초"

            embed = discord.Embed(
                title=area + " 시간 정보",
                description="\u200b",
                color=discord.Colour.green()
            )
            embed.add_field(
                name="시간",
                value=Time,
                inline=False
            )
            await message.channel.send(embed=embed)


access_token = os.environ["BOT_TOKEN"]
app.run(access_token)
