#Basit Discord Botu Örnek Kodlar
import discord 
from discord.ext import commands, tasks
from random import randint as ras
#Bunları yazmadan önce terminale "pip install discord.py" yazın.
 
Bot = commands.Bot(command_prefix="!tt ", intents=discord.Intents.all())
#!tt bizim botumuza vereceğimiz komutlardan önce yazmamız gereken bir şey olarak düşünün.İsterseniz değiştirebilirsiniz.

@Bot.event  
async def on_ready():
    await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name="FİLM ADI"))
    await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name="MÜZİK ADI"))
    await Bot.change_presence(activity=discord.Game(name="OYUN ADI"))
    #Eğer botunuz aktivitesini ayarlamak istiyorsanız(izliyor,dinliyor,oynuyor v.b) bu komutlardan birisini kullanın.

@Bot.event
async def on_member_join(member): #Bu fonksiyon sunucuya bir kullanıcı girdiğinde çalışır.
    channel = discord.utils.get(member.guild.text_channels, name ="KANAL ADI")#"KANAL ADI" yerine sizin sunucunuzdaki bir kanalı yazın.
    await channel.send(f"{member.mention} Giriş Yaptı.")#"Giriş Yaptı." yerine istediğinizi yazın. 

@Bot.event
async def on_member_remove(member): #Bu fonksiyon sunucudan bir kullanıcı çıktığında çalışır.
    channel = discord.utils.get(member.guild.text_channels, name ="KANAL ADI")#"KANAL ADI" yerine sizin sunucunuzdaki bir kanalı yazın.
    await channel.send(f"{member.mention} Ayrıldı.")#"Ayrıldı." yerine istediğinizi yazın. 

@Bot.event
async def on_message(message): #Bu fonksiyon sunucuya bir mesaj yazıldığında çalışır.
    print(message) #Bu kodu burası boş kalmasın diye yazdım.İhtiyacınıza göre burayı değiştirebilirsiniz.
    
@Bot.command() #Botunuz için örnek bir komut yapımı.
async def nbr(msg):
    await msg.send("iyi senden naber")
#eğer "!tt nbr" yazarsanız bu koda göre "iyi senden naber" yazıcaktır.

@Bot.command(aliases = ["zarat"]) #Örnek zar atma komudu.
async def zar(msg):
    await msg.send(str(ras(1,7)) + " Çıktı.")
#eğer "!tt zar" yada "!tt zarat" yazarsanız "0 ile 7 arasında(1,2,3,4,5,6)Çıktı." yazıcaktır.

@Bot.command() #Örnek mesajları silme komudu
async def temizle(ctx,amount = 2):
    await ctx.channel.purge(limit = amount)
#eğer örnek olarak "!tt temizle 100" yazarsanız yazdığınız mesajla birlikte 100 mesajı silecektir. 
@Bot.command() #Örnek kanal kopyalama komudu
@commands.has_role("ROL ADI") #"ROL ADI" yerine sunucunuzdaki adminlere özel rolün adını yazabilirsiniz.
async def kanalkopyala(ctx):
    await ctx.channel.clone()
#eğer "!tt kanalkopyala" yazarsanız komutu yazdığınız kanalı kopyalarsınız.
@Bot.command() #Örnek sunucundan insan atma komudu
@commands.has_role("ROL ADI") #"ROL ADI" yerine sunucunuzdaki adminlere özel rolün adını yazabilirsiniz.
async def at(ctx,member:discord.Member,*args,reason = "Yok"):
    await ctx.member.kick(reason=reason)
#eğer "!tt at @kamil" yazarsanız "kamil" kişisi sunucudan atarsınız.
@Bot.command() #Örnek sunucudan insan yasaklama komudu
@commands.has_role("ROL ADI") #"ROL ADI" yerine sunucunuzdaki adminlere özel rolün adını yazabilirsiniz.
async def ban(ctx,member:discord.Member,*args,reason = "Yok"):
    await ctx.member.ban(reason=reason)
#eğer "!tt ban @kamil" yazarsanız "kamil" kişisi sunucudan yasaklarsınız.
@Bot.command() #Örnek sunucudan yasaklanan insanın yasağını kaldırma komudu
@commands.has_role("ROL ADI") #"ROL ADI" yerine sunucunuzdaki adminlere özel rolün adını yazabilirsiniz.
async def unban(ctx, *,member):
    banned_users = await ctx.guild.bans()
    member_name, member_disciriminator = member.spilit("#")
    for bans in banned_users:
        user = bans.user
        if(user.name, user.disciriminator) == (member_name, member_disciriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Banı Kaldırılmıştır{user.mention}.')
            return
#eğer "!tt unban @kamil" yazarsanız "kamil" kişisi sunucudaki yasağını kaldırırsınız.        
@Bot.command() #Örnek Mesaja Emoji verme komudu
async def emoji(ctx):
    await ctx.message.add_reaction("KULLANMAK İSTEDİĞİN EMOJİ")
#eğer "!tt emoji" yazarsa yazdığı mesaja "KULLANMAK İSTEDİĞİN EMOJİ" emojisi kullanır.    
#bu komudu başka yerlerde kullanmanız daha faydalı olacaktır.
@tasks.loop(seconds=600) #Örnek belirli saniyelerde mesaj atma komudu.
async def tekrarmsj():
    for c in Bot.get_all_channels():
        if c.id == 00000000000000000000: #Buraya sunucudaki kanalınızın ID'sini yapıştırın.
            await c.send('YAZMAK İSTEDİĞİNİZ MESAJ')
#koda göre artık 600 saniyede bir "00000000000000000000" ID'ye sahip olan kanalı "YAZMAK İSTEDİĞİNİZ MESAJ" mesajı gönderilecek.

Bot.run('00000000000000000000000000') #Buraya kendi Discord botunuzun ID'sini yapıştırın.

#Eğer yazdığım kodlarda bir hata varsa şimdiden özür dilerim
#Made by h0taf