import discord#導入 Discord.py
client = discord.Client()   #client 是我們與 Discord 連結的橋樑

#調用 event 函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)

@client.event   #當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    #輸入密碼來獲取線索
    if message.content == '1q2': #童軍繩
        await message.channel.send('一條童軍繩???__________好像被使用過的痕跡??') 
    elif message.content == '8e6': #藥包
        await message.channel.send('一包藥__________這好像是憂鬱症的藥??') 
    elif message.content == '9a2': #另一個藥包
        await message.channel.send('一包藥________這包藥的顏色跟杯子裡的好像') 
    elif message.content == '4t8': #備取通知書
        await message.channel.send('備取通知書________上面寫著裕祥的名字')
    elif message.content == '8p9': #手電筒
        await message.channel.send('一支手電筒')
    elif message.content == '6e5': #屍體描述_勒痕
        await message.channel.send('梓晨的脖子上有一條長長的勒痕')
    elif message.content == '7d3': #hello kitty
        await message.channel.send('一隻背後被剪開裡面剩下少許棉花的hello kitty')
    elif message.content == '9d8': #hello kitty的棉花
        await message.channel.send('一團棉花')
    elif message.content == '5q9': #照片
        await message.channel.send('一張濕掉的照片________裡面是巴德和梓晨的合照')
    elif message.content == '6h2': #葉夢給巴德的情書
        await message.channel.send('一封信________竟然事是葉  夢寫給巴德的')
    elif message.content == '3s5': #照片
        await message.channel.send('一張的照片________裡面是樂夢和梓晨的合照')
    elif message.content == '9a3': #獎狀
        await message.channel.send('一張模範生獎狀________上面有著梓晨的照片')
    

client.run('OTgxNzQ2NDI0NzEyNjg3NjY3.GkP1nG.kLORpM3hjYFh-tyIkivjOSzUsywHZQb9s4d42o') #TOKEN