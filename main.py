import os
import discord
from discord.ui import Button, View
from discord.ext import commands
from discord import app_commands
from PIL import Image, ImageDraw, ImageFont
import datetime
import pytz

from myserver import server_on

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

MYGUILD_ID = 1270742905006325781  # GUILD ID à¹ÿà¸­à¸”à¸µà¹€à¸ÿà¸´à¸ÿà¹€à¸§à¸­à¸£à¹ÿ

class slipwallet_discord(discord.ui.Modal, title="SLIPWALLET"):
    name_user = discord.ui.TextInput(label="USERNAME", placeholder="à¸ÿà¸·à¹ÿà¸­à¸ÿà¸¹à¹ÿà¹ÿà¸­à¸ÿà¸ÿà¹ÿà¸²à¸¢", required=True, max_length=50, style=discord.TextStyle.short)
    name_me = discord.ui.TextInput(label="NAME", placeholder="à¸ÿà¸·à¹ÿà¸­à¸ÿà¸¹à¹ÿà¸£à¸±à¸ÿà¹€à¸ÿà¸´à¸ÿ", required=True, max_length=50, style=discord.TextStyle.short)
    phone_me = discord.ui.TextInput(label="PHONE", placeholder="à¹€à¸ÿà¸­à¸£à¹ÿà¹ÿà¸—à¸£à¸¨à¸±à¸ÿà¸—à¹ÿà¸ÿà¸¹à¹ÿà¸£à¸±à¸ÿ", required=True, max_length=10, style=discord.TextStyle.short)
    money = discord.ui.TextInput(label="MONEY", placeholder="à¸ÿà¸³à¸ÿà¸§à¸ÿà¹€à¸ÿà¸´à¸ÿ", required=True, max_length=4, style=discord.TextStyle.short)



    async def on_submit(self, interaction: discord.Interaction):
        name_user_id = self.name_user.value 
        name_me_id = self.name_me.value
        phone_me_id = self.phone_me.value
        money_id = self.money.value

        thailand_timezone = pytz.timezone('Asia/Bangkok')

        current_time_thailand = datetime.datetime.now(thailand_timezone)

        time =  current_time_thailand.strftime("%H:%M:%S")

        day =  current_time_thailand.strftime("%d")
        month = current_time_thailand.strftime("%m")
        year = current_time_thailand.strftime("%Y")

        image = Image.open("truemoney.png")
        draw = ImageDraw.Draw(image)

        font_size_money = 87
        font_size_user = 48
        font_size_me = 48
        font_size_phone = 40
        font_size_time = 37

        font_path_money = "Lato-Heavy.ttf" 
        font_path_user2 = "Kanit-Light.ttf"
        font_path_user = "Kanit-ExtraLight.ttf"
        font_path_phone = "Prompt-Light.ttf"

        font_money = ImageFont.truetype(font_path_money, font_size_money)
        font_user = ImageFont.truetype(font_path_user, font_size_user)
        font_me = ImageFont.truetype(font_path_user, font_size_me)
        font_phone = ImageFont.truetype(font_path_phone, font_size_phone)
        font_time = ImageFont.truetype(font_path_user2, font_size_time)
        font_order = ImageFont.truetype(font_path_user2, font_size_time)

        phone = phone_me_id
        text_money = money_id + ".00"
        text_name_user = name_user_id
        text_name_me = name_me_id
        text_name_phone = f"{phone[:3]}-xxx-{phone[6:]}"
        text_name_time = f"  {day}/{month}/{year} {time}"
        # text_name_time = f"{self.tim.value}"
        text_name_order = "50018935012188"

        text_position_money = (560, 270)  
        text_position_user = (302, 485)
        text_position_me = (302, 648)
        text_position_phone = (302, 720)
        text_position_time = (781, 885)
        text_position_order = (827, 953)

        text_color_money = (44, 44, 44) 
        text_color_user = (-20, -20, -20)
        text_color_me = (-20, -20, -20) 
        text_color_phone = (80, 80, 80)
        text_color_time = (60, 60, 60) 
        text_color_order = (60, 60, 60)  

        draw.text(text_position_money, text_money, font=font_money, fill=text_color_money)
        draw.text(text_position_user, text_name_user, font=font_user, fill=text_color_user)
        draw.text(text_position_me, text_name_me, font=font_me, fill=text_color_me)
        draw.text(text_position_phone, text_name_phone, font=font_phone, fill=text_color_phone)
        draw.text(text_position_time, text_name_time, font=font_time, fill=text_color_time)
        draw.text(text_position_order, text_name_order, font=font_order, fill=text_color_order)

        image.save("truemoney_with_text.png")
        user = interaction.user
        file = discord.File('truemoney_with_text.png')
        embed = discord.Embed(title="âÿ… à¸ªà¸£à¹ÿà¸²à¸ÿà¸ªà¸¥à¸µà¸ÿà¸ÿà¸¥à¸­à¸¡à¸ªà¸³à¹€à¸£à¹ÿà¸ÿ",description=f"à¸ÿà¸µà¹ÿà¹€à¸ÿà¹ÿà¸ÿà¸ªà¸¥à¸µà¸ÿà¸ÿà¸¥à¸­à¸¡à¸ÿà¸²à¸ÿà¸ÿà¹ÿà¸­à¸¡à¸¹à¸¥à¸—à¸µà¹ÿà¸ÿà¸¸à¸“à¸ÿà¸£à¸­à¸ÿ",color=0xFCE5CD)
        await interaction.response.send_message(embed=embed, file=file, ephemeral=True)



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord.Streaming(name='à¸£à¸°à¸ÿà¸ÿà¸ÿà¸¥à¸­à¸¡à¸ªà¸¥à¸´à¸ÿà¸§à¸­à¹€à¸¥à¹ÿà¸—', url='https://www.twitch.tv/'))
    
    # Registering slash command
    guild = client.get_guild(MYGUILD_ID)
    if guild is not None:
        await client.setup_hook()


@client.command(description="à¸ÿà¸¥à¸­à¸¡à¸ªà¸¥à¸´à¸ÿà¸—à¸£à¸¹à¸¡à¸±à¸ÿà¸ÿà¸µà¹ÿà¸§à¸­à¹€à¸¥à¹ÿà¸—")
async def slip_wallet(ctx):
    username = ctx.author.display_name

    button = Button(label="à¸ªà¸¥à¸´à¸ÿà¸§à¸­à¹€à¸¥à¹ÿà¸—", style=discord.ButtonStyle.grey, emoji="ðÿ“ÿ")
    
    async def button_callback(interaction: discord.Interaction):
        modal_view = slipwallet_discord()
        await interaction.response.send_modal(modal_view)
    
    button.callback = button_callback
    view = View(timeout=None)
    view.add_item(button)

    embed = discord.Embed(title="\nSLIPWALLET", description=f"**à¸ÿà¸£à¸´à¸ÿà¸²à¸£à¸ÿà¸¥à¸­à¸¡à¸ªà¸¥à¸´à¸ÿà¸§à¸­à¹€à¸¥à¹ÿà¸— !**", color=0x000000)
    embed.set_author(name=username, url="https://discord.com/channels/@me/"+username)
    embed.add_field(name="- ðÿ“ÿ __EXAMPLE ( à¸•à¸±à¸§à¸­à¸¢à¹ÿà¸²à¸ÿ )__", value="à¸ÿà¸£à¸­à¸ÿà¸ÿà¹ÿà¸­à¸¡à¸¹à¸¥à¸ÿà¸¥à¸­à¸¡à¹€à¹€à¸ÿà¸¥à¸ÿà¸—à¸µà¹ÿà¸ÿà¸¸à¸“à¸•à¹ÿà¸­à¸ÿà¸ÿà¸²à¸£à¸—à¸µà¹ÿà¸ÿà¸°à¸ÿà¸£à¸­à¸ÿà¸¥à¸ÿà¹ÿà¸«à¸ÿà¸ÿà¹ÿà¸­à¸ÿà¸ÿà¸£à¸­à¸ÿ à¸ÿà¸¹à¹ÿà¹ÿà¸ÿà¹ÿà¸ÿà¹ÿà¸²à¸¢à¹€à¸ÿà¸´à¸ÿ,à¸ÿà¸¹à¹ÿà¸£à¸±à¸ÿà¹€à¸ÿà¸´à¸ÿ,à¹€à¸ÿà¸­à¸£à¹ÿà¸ÿà¸¹à¹ÿà¸£à¸±à¸ÿà¹€à¸ÿà¸´à¸ÿ,à¸ÿà¸³à¸ÿà¸§à¸ÿà¹€à¸ÿà¸´à¸ÿ\nà¹€à¸§à¸¥à¸²à¸ÿà¸£à¸­à¸ÿà¸ÿà¸·à¹ÿà¸­à¹ÿà¸«à¹ÿà¹€à¸§à¹ÿà¸ÿà¸§à¸£à¸£à¸ÿà¸ÿà¸·à¹ÿà¸­à¹€à¹€à¸¥à¸°à¸ÿà¸²à¸¡à¸ªà¸ÿà¸¸à¸¥à¸ÿà¸­à¸ÿà¸ÿà¸¸à¸“à¸”à¹ÿà¸§à¸¢ ",inline=False)
    embed.set_image(url="https://images-ext-1.discordapp.net/external/4xDKAnuLeOoeFUhHfaFgDap5SgjCx_SlpQdtjMAPhqU/https/media.giphy.com/media/fecTAVKVVA2fSzg21J/giphy.gif")
    
    # Sending the interaction response
    await ctx.send(embed=embed, view=view)

server_on()

client.run(os.getenv('TOKEN'))
