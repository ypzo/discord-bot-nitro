import discord
import random

class Bot(discord.Client):

    def __init__(self):
        super().__init__()

    async def on_ready(self):
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------")

    async def on_message(self, message):

        if(message.author == self.user):
            return

        if (message.content.startswith("-help")):
            embed = discord.Embed(title="𝑁𝐼𝑇𝑅𝑂", description="``-nitro`` send you 2 classic nitro codes in dm.\n``-boost`` send you 2 nitro boost codes in dm.", color=0xff00bb)
            embed.set_footer(text="By Asuma#9999")
            await message.channel.send(embed=embed)

        if (message.content.startswith("-nitro")):
            codelen = 16  # longueur du code nitro
            letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvxyz0123456789"
            author = message.author
            await author.send("https://discord.gift/" + ''.join(random.choice(letters) for i in range(codelen)) + "\n\nhttps://discord.gift/" + ''.join(random.choice(letters) for i in range(codelen)))
            embed = discord.Embed(title="𝑁𝐼𝑇𝑅𝑂", description="Look at your dms", color=0xff00bb)
            embed.set_footer(text="By Asuma#9999")
            await message.channel.send(embed=embed)

        if (message.content.startswith("-boost")):
            codelen = 24  # longueur du code nitro
            letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvxyz0123456789"
            author = message.author
            await author.send("https://discord.gift/" + ''.join(random.choice(letters) for i in range(codelen)) + "\n\nhttps://discord.gift/" + ''.join(random.choice(letters) for i in range(codelen)))
            embed = discord.Embed(title="𝑁𝐼𝑇𝑅𝑂", description="Look at your dms", color=0xff00bb)
            embed.set_footer(text="By Asuma#9999")
            await message.channel.send(embed=embed)


if __name__ == "__main__":

    bot = Bot()
    bot.run("ODI2NzM5NzAwMDkzMDI2MzE0.YGQ3WA.2bQ2aKPm8Cb3SEbxx9e1E-Phz1w")
