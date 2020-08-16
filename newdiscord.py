import os
import discord
from urllib.request import urlopen
from bs4 import BeautifulSoup

app = discord.Client() #클라이언트 변수

@app.event
async def on_message(message):
    # < 시간 출력 >
    if message.content.startswith("!시간"):
        text = message.content
        flag = False

        # < 지역 검색 >
        if "한국" in text or "서울" in text:
            Time_url = "https://www.timeanddate.com/worldclock/south-korea/seoul"
            area = "한국(서울)"
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

            classData2 = soup.select('#ctdat')[0]
            Date = classData2.text

            temp = Date.split()
            temp[0] = temp[0].replace(',', '')
            temp[2] = temp[2].replace(',', '')

            if temp[1] == "January":
                temp[1] = "1"
            elif temp[1] == "February":
                temp[1] = "2"
            elif temp[1] == "March":
                temp[1] = "3"
            elif temp[1] == "April":
                temp[1] = "4"
            elif temp[1] == "May":
                temp[1] = "5"
            elif temp[1] == "June":
                temp[1] = "6"
            elif temp[1] == "July":
                temp[1] = "7"
            elif temp[1] == "August":
                temp[1] = "8"
            elif temp[1] == "September":
                temp[1] = "9"
            elif temp[1] == "October":
                temp[1] = "10"
            elif temp[1] == "November":
                temp[1] = "11"
            elif temp[1] == "December":
                temp[1] = "12"

            if temp[0] == "Monday":
                temp[0] = "월"
            elif temp[0] == "Tuesday":
                temp[0] = "화"
            elif temp[0] == "Wednesday":
                temp[0] = "수"
            elif temp[0] == "Thursday":
                temp[0] = "목"
            elif temp[0] == "Friday":
                temp[0] = "금"
            elif temp[0] == "Saturday":
                temp[0] = "토"
            elif temp[0] == "Sunday":
                temp[0] = "일"

            Date = temp[3] + "년 " + temp[1] + "월 " + temp[2] + "일 " + temp[0] + "요일"

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
            embed.add_field(
                name="날짜",
                value=Date,
                inline=False
            )
            await message.channel.send(embed=embed)
     
access_token = os.environ["BOT_TOKEN"]
app.run(access_token)
