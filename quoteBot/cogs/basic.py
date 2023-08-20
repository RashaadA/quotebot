import nextcord
from nextcord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import textwrap
import random
import requests
import sys
sys.path.append("..")
import config

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        await ctx.channel.send("Use the dq function followed by a string of text to generate a quote of e. Write mq followed by text for Morgan Freeman. The random function will generate a random quote by either one of the two.")

    #generates a quote of a friend of mine, information redacted for privacy purposes
    @commands.command()
    async def dq(self, ctx, mystr:str):
        image = Image.open("pictures/epic.png")
        font = ImageFont.truetype("arial.ttf", 80)
        cx, cy = (2150,800)

        lines = textwrap.wrap(mystr, width=30)
        width, height = font.getsize(mystr)
        y_offset = (len(lines)*height)/2
        y_text = cy-(height/2)-y_offset

        for line in lines:
            draw = ImageDraw.Draw(image)
            width, height = font.getsize(line)
            draw.text((cx-(width/2),y_text), line, font=font, fill=(0,0,0))
            image.save("epicture.png")
            y_text += height

        draw.text((1800,1400), "—— e ——", font=font, fill=(0,0,0))
        image.save("epicture.png")

        with open("epicture.png", "rb") as f:
            image = nextcord.File(f)
            await ctx.channel.send(file=image)

    @commands.command()
    async def mq(self, ctx, mystr:str):
        image = Image.open("pictures/morganpic.png")
        font = ImageFont.truetype("arial.ttf", 80)
        cx, cy = (2350,800)

        lines = textwrap.wrap(mystr, width=30)
        width, height = font.getsize(mystr)
        y_offset = (len(lines)*height)/2
        y_text = cy-(height/2)-y_offset

        for line in lines:
            draw = ImageDraw.Draw(image)
            width, height = font.getsize(line)
            draw.text((cx-(width/2),y_text), line, font=font, fill=(255,255,255))
            image.save("morganpicture.png")
            y_text += height

        draw.text((2000,1400), "—— Morgan Freeman ——", font=font, fill=(255,255,255))
        image.save("morganpicture.png")

        with open("morganpicture.png", "rb") as f:
            image = nextcord.File(f)
            await ctx.channel.send(file=image)

    @commands.command()
    async def random(self, ctx):
        api_url = 'https://api.api-ninjas.com/v1/quotes'
        response = requests.get(api_url, headers={'X-Api-Key': config.APIKEY})
        if response.status_code == requests.codes.ok:
            arg = response.json()
            functions = [
                self.dq,
                self.mq
            ]

            selected_function = random.choice(functions)
            await selected_function(ctx, arg[0]["quote"])
        else:
            await ctx.channel.send("Error:", response.status_code, response.text)




def setup(bot):
    bot.add_cog(Basic(bot))
