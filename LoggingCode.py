data_data = []
guild_data = []
category_data = []
channel_data = []
member_data = []
message_sent = []

@client.event
async def on_message(message):
   
    msg = (message.content, message.author.id, message.channel.id, message.channel.category.id, message.guild.id)

    # Channel
    channel_id = message.channel.id
    if msg[2] == channel_id:
        channel = []
        channel_info = {}
        channel.append(channel_info)
        channel_info["Name"] = message.channel.name
        channel_info["ID"] = message.channel.id
        channel_info["NSFW"] = message.channel.is_nsfw()
        #channel_info["Member"] = member

        for channel_info in channel:
            id = channel_info.get("ID")
            if msg[2] == id:
                channel_data.append(channel_info)

        new_channel_data = []
        for i in channel_data:
            if i not in new_channel_data:
                new_channel_data.append(i)

    # Category
    category_id = message.channel.category.id
    if msg[3] == category_id:
        category = []
        category_info = {}
        category.append(category_info)
        category_info["Name"] = message.channel.category.name
        category_info["ID"] = message.channel.category.id
        category_info["NSFW"] = message.channel.category.is_nsfw()
        category_info["Channel"] = new_channel_data
        
        for category_info in category:
            id = category_info.get("ID")
            if msg[3] == id:
                category_data.append(category_info)              

        new_category_data = []
        for i in category_data:
            if i not in new_category_data:
                new_category_data.append(i)
        
    # Guild 
    guild_id = message.guild.id
    if msg[4] == guild_id:
        guild = []
        guild_info = {}
        guild.append(guild_info)
        guild_info["Name"] = message.guild.name
        guild_info["ID"] = message.guild.id
        guild_info["Category"] = new_category_data

        for guild_info in guild:
            id = guild_info.get("ID")
            if msg[4] == id:
                guild_data.append(guild_info)

        new_guild_data = []
        for i in guild_data:
            if i not in new_guild_data:
                new_guild_data.append(i)
            #elif id == i.get("ID"):
                #print("Oh no!")

    # Data
    data = {}
    data["Guild"] = new_guild_data

    #JSON
    with open("logs.json", "w") as fp:
        lol = data

        json.dump(lol, fp, indent = 4)
        fp.close()
