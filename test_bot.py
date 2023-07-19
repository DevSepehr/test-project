# api bot on Telegram
import time
import os
import json
import requests as req
from pyrogram import Client
from pyrogram import filters
import random

my_token = '5251404430:AAGtimfjjI_H5v2dQvvkcfJIgNOVijUY2o0'
api_hash = 'e672c81d47063219249eac3cdd94bf0c'
api_id = 3940019
app = Client('myacc', api_id=5501261, api_hash="63402a3b7e875edfee3786e911744dd5")
# app = Client('myacc2', api_id=api_id, api_hash=api_hash)


qalb = ["🤍","🖤","🤎","💜","💙","💚","💛","🧡","❤️"]
emoji = ['🦁', '🐯', '🌼', '🌗', '🌓', '🪐', '💫', '⭐️', '✨','⚡️', '🔥', '🌈', '☃️', '❄️', '🍔', '🍕', '🍓', '🍉','🍟', '🧁', '🍰',  '🦊', '🦄', '🐝', '🐺', '🦋', '🐞','🐳', '🐬', '🐼', '🦚', '🎄', '🌲', '🍄', '🍁', '🌷','🌹', '🌺', '🌸','🍭', '🍬', '🍫', '🍿', '🍩', '🍪','🥂', '🍸', '🍹', '🧉', '🍾', '⚽️', '🏀', '🏈', '⚾️','🥎', '🎾', '🎖', '🎗', '🥁', '🎸', '🎺', '🎷', '🏎', '🚀','✈️', '🚁', '🛸', '🏰', '🗼', '🎡', '🛩', '📱', '💻', '🖥','💰', '🧨', '💣', '🪓', '💎', '⚱️', '🔮', '🩸', '🦠', '🛎','🧸', '🎉', '💌', '📯', '❤️', '🧡', '💛', '💚', '💙', '💜','🖤', '🤍', '🤎', '❣️', '💕', '💞', '💝','⚜️', '🔱', '📣','♥️', '😍', '🥰', '🥳', '🤩', '🤪', '👾', '😻', '💋', '👑', '💍', '🎩']

ez_emoji = ["😀", "😃", "😄", "😁", "😆", "😅", "🗿", "🤣", "😭", "😗", "😙", "😚", "😘", "🥰", "😍", "🤩", "🥳", "🤗", "🙃", "🙂", "☺️", "😊", "😏", "😌", "😉", "🤭", "😶", "🤔", "🤪", "😜", "😝", "😛", "😋", "😔", "😑", "😐", "🤨", "🧐", "🙄", "😒", "😤", "😠", "😡", "🤬", "☹️", "😰", "🤫", "🤐", "😬", "😳", "🥺", "😟", "😕", "🙁", "😨", "😧", "😦", "😮", "😯", "😲", "😱", "🤯", "😢", "😥", "😓", "😞", "😣", "😖", "😩", "😫", "🤤", "😇", "😵", "🤥", "🤓", "😎", "🤑", "🤠"]
bot = True
if bot:

    @app.on_message(filters.user('agparianabot'))
    async def tools(app, Message):
 
        if Message.media:
            if Message.voice.mime_type == "audio/mpeg":
    
            
                user_id = open('voicechat','r').read()
                await app.send_audio(int(user_id),vfile := await Message.download(),caption="ᴅᴏɴᴇ⟮✅⟯")
                os.remove(vfile)
            
    @app.on_message(filters.me)
    async def tools(app, Message):
        text = Message.text
        #
        if text.startswith('/music '):
            await Message.edit("wait ...")
            music_name = text.replace('/music ','')
            music_info = await app.get_inline_bot_results("@deezermusicbot", music_name)
            print(music_info)
            await app.send_inline_bot_result(
                Message.chat.id, music_info.query_id,
                music_info.results[0].id)
        
        elif text.startswith('/text_voice'):
      
            v_text = text.replace('/text_voice ','')
            if v_text.startswith('1') or v_text.startswith('2') or v_text.startswith('3'):
                
                await Message.edit("wait...")
            
                open('voicechat','w').write(str(Message.chat.id))
                
                try:
                    await app.join_chat('asrgooyeshpardaz')
                except:
                    pass
                if v_text.startswith('1'):
                    v_text = v_text.replace('1 ','')
                
                    await app.send_message('@AgpArianaBot','/start')
                    time.sleep(0.5)
                    
                    await app.send_message('@AgpArianaBot','👸 زن:رایگان')
                    time.sleep(0.5)
                    
                    await app.send_message('@AgpArianaBot',f'{v_text}')
                    time.sleep(0.5)
                    await app.send_message('agparianabot', '🔉 خواندن متن و کسر 1 سکه')
                
                elif v_text.startswith('2 '):
                    v_text = v_text.replace('2 ','')
                
                    await app.send_message('@AgpArianaBot','/start')
                    time.sleep(0.5)
                    
                    await app.send_message('@AgpArianaBot','🕵 مرد۱:رایگان')
                    time.sleep(0.5)
                    
                    await app.send_message('@AgpArianaBot',f'{v_text}')
                    time.sleep(0.5)
                    await app.send_message('agparianabot', '🔉 خواندن متن و کسر 1 سکه')
                elif v_text.startswith('3 '):
                    v_text = v_text.replace('3 ','')
                    
                    await app.send_message('@AgpArianaBot','/start')
                    time.sleep(0.5)
                    
                    await app.send_message('@AgpArianaBot','🕵 مرد۲:رایگان')
                    time.sleep(0.5)
                    
                    await app.send_message('@AgpArianaBot',f'{v_text}')
                    time.sleep(0.5)
                    await app.send_message('agparianabot', '🔉 خواندن متن و کسر 1 سکه')
                
                
                else:
                    await Message.edit('[⚡] Error Please try again .')
  
  
        
        text = Message.text
        
        if text.startswith('/spam'):
            spam = text.replace('/spam ','')
            spam = spam.split(',')
            for i in range(int(spam[0])):
                await app.send_message(Message.chat.id, spam[1])
        elif text.startswith('/id'):
            await Message.edit_text(f'Your id is: `{Message.chat.id}`')
        elif text.startswith('/font '):
      
      
            FontText = text.replace('/font ','')
      
            FontText = FontText.replace(' ','+')
        
            GetFonts = req.get(f'https://api.codebazan.ir/font/?type=en&text={FontText}').text
        
            GetFonts = json.loads(GetFonts)
        
        
        
            if GetFonts['ok'] == False:
                await Message.edit('⚠️[ only use letters , do not use anything else ]\n⚠️[ فقط از حروف استفاده کنید ، از چیز دیگری استفاده نکنید ]')
            elif GetFonts['ok'] == True:
            
                await Message.edit(f'''▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬
`{GetFonts['result']["1"]}`
`{GetFonts['result']["2"]}`
`{GetFonts['result']["3"]}`
`{GetFonts['result']["4"]}`
`{GetFonts['result']["5"]}`
`{GetFonts['result']["6"]}`
`{GetFonts['result']["7"]}`
`{GetFonts['result']["8"]}`
`{GetFonts['result']["9"]}`
`{GetFonts['result']["10"]}`‌
`{GetFonts['result']["11"]}`
`{GetFonts['result']["12"]}`
`{GetFonts['result']["13"]}`
`{GetFonts['result']["14"]}`
`{GetFonts['result']["15"]}`
`{GetFonts['result']["16"]}`
`{GetFonts['result']["17"]}`
`{GetFonts['result']["18"]}`
`{GetFonts['result']["19"]}`
`{GetFonts['result']["20"]}`
`{GetFonts['result']["21"]}`‌
`{GetFonts['result']["22"]}`
`{GetFonts['result']["23"]}`
`{GetFonts['result']["24"]}`
`{GetFonts['result']["25"]}`
`{GetFonts['result']["26"]}`
`{GetFonts['result']["27"]}`
`{GetFonts['result']["28"]}`
`{GetFonts['result']["29"]}`
`{GetFonts['result']["30"]}`
`{GetFonts['result']["31"]}`
`{GetFonts['result']["32"]}`
`{GetFonts['result']["33"]}`
`{GetFonts['result']["34"]}`
`{GetFonts['result']["35"]}`
`{GetFonts['result']["36"]}`
`{GetFonts['result']["37"]}`
`{GetFonts['result']["38"]}`
`{GetFonts['result']["39"]}`
`{GetFonts['result']["40"]}`
`{GetFonts['result']["41"]}`
`{GetFonts['result']["42"]}`
`{GetFonts['result']["43"]}`
`{GetFonts['result']["44"]}`
`{GetFonts['result']["45"]}`
`{GetFonts['result']["46"]}`
`{GetFonts['result']["47"]}`
`{GetFonts['result']["48"]}`
`{GetFonts['result']["49"]}`
`{GetFonts['result']["50"]}`
`{GetFonts['result']["51"]}`
`{GetFonts['result']["52"]}`
`{GetFonts['result']["53"]}`
`{GetFonts['result']["54"]}`
`{GetFonts['result']["55"]}`
`{GetFonts['result']["56"]}`
`{GetFonts['result']["57"]}`
`{GetFonts['result']["58"]}`
`{GetFonts['result']["59"]}`
`{GetFonts['result']["60"]}`
`{GetFonts['result']["61"]}`
`{GetFonts['result']["62"]}`
`{GetFonts['result']["63"]}`
`{GetFonts['result']["64"]}`
`{GetFonts['result']["65"]}`‌
`{GetFonts['result']["66"]}`
`{GetFonts['result']["67"]}`
`{GetFonts['result']["68"]}`
`{GetFonts['result']["69"]}`
`{GetFonts['result']["70"]}`
`{GetFonts['result']["71"]}`
`{GetFonts['result']["72"]}`
`{GetFonts['result']["73"]}`
`{GetFonts['result']["74"]}`
`{GetFonts['result']["75"]}`
`{GetFonts['result']["76"]}`
`{GetFonts['result']["77"]}`
`{GetFonts['result']["78"]}`
`{GetFonts['result']["79"]}`
`{GetFonts['result']["80"]}`
`{GetFonts['result']["81"]}`
`{GetFonts['result']["82"]}`
`{GetFonts['result']["83"]}`
`{GetFonts['result']["84"]}`
`{GetFonts['result']["85"]}`
`{GetFonts['result']["86"]}`
`{GetFonts['result']["87"]}`
`{GetFonts['result']["88"]}`
`{GetFonts['result']["89"]}`
`{GetFonts['result']["90"]}`
`{GetFonts['result']["91"]}`
`{GetFonts['result']["92"]}`
`{GetFonts['result']["93"]}`‌
`{GetFonts['result']["94"]}`
`{GetFonts['result']["95"]}`
`{GetFonts['result']["96"]}`
`{GetFonts['result']["97"]}`
`{GetFonts['result']["98"]}`
`{GetFonts['result']["99"]}`
`{GetFonts['result']["100"]}`
`{GetFonts['result']["101"]}`
`{GetFonts['result']["102"]}`
`{GetFonts['result']["103"]}`
`{GetFonts['result']["104"]}`
`{GetFonts['result']["105"]}`
`{GetFonts['result']["106"]}`
`{GetFonts['result']["107"]}`
`{GetFonts['result']["108"]}`
`{GetFonts['result']["109"]}`
`{GetFonts['result']["110"]}`
`{GetFonts['result']["111"]}`
`{GetFonts['result']["112"]}`
`{GetFonts['result']["113"]}`
`{GetFonts['result']["114"]}`
`{GetFonts['result']["115"]}`
`{GetFonts['result']["116"]}`
`{GetFonts['result']["117"]}`
`{GetFonts['result']["118"]}`
`{GetFonts['result']["119"]}`
`{GetFonts['result']["120"]}`
`{GetFonts['result']["121"]}`
`{GetFonts['result']["122"]}`
`{GetFonts['result']["123"]}`
`{GetFonts['result']["124"]}`
`{GetFonts['result']["125"]}`
`{GetFonts['result']["126"]}`
`{GetFonts['result']["127"]}`
`{GetFonts['result']["128"]}`
`{GetFonts['result']["129"]}`
`{GetFonts['result']["120"]}`
`{GetFonts['result']["131"]}`
`{GetFonts['result']["132"]}`
`{GetFonts['result']["133"]}`
`{GetFonts['result']["134"]}`
`{GetFonts['result']["135"]}`
`{GetFonts['result']["135"]}`
`{GetFonts['result']["136"]}`
`{GetFonts['result']["137"]}`
`{GetFonts['result']["138"]}`

▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬''')
        
            
        elif text == '/down':
            if Message.reply_to_message and Message.reply_to_message.media:
                await Message.delete()
                try:
                    await app.send_video(
            'me',myfile := await Message.reply_to_message.download(),caption="""
  » ғɪʟᴇ sᴀᴠᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ⟮✅⟯
  =-=-=-=-=-=-=-=-=-=-=-=-=-=
  » ᴄᴏᴅᴇᴅ ʙʏ [ᴍʀ sᴇᴘᴇʜʀ](https://t.me/khodesepehram) ⟮🌪⟯
            """)
                    os.remove(myfile)
                except:
                    pass
        elif text =='عقاب':
            await Message.edit('''
☁️          ☁️            🌤
 🏔                                       🦅  
        🗻                          
              
    🍄            🥚     🌴
            ''')
            time.sleep(0.1)
            await Message.edit('''
☁️          ☁️            🌤
 🏔                                    🦅  
        🗻                          
              
    🍄            🥚     🌴
            ''')

            time.sleep(0.1)
            await Message.edit('''
☁️          ☁️             🌤
 🏔                                   
        🗻                         🦅  
              
    🍄            🥚     🌴
            ''')

            time.sleep(0.1)
            await Message.edit('''
☁️         ☁️             🌤
 🏔                                   
        🗻                  🦅  
              
    🍄            🥚     🌴
            ''')

            time.sleep(0.1)
            await Message.edit('''
☁️          ☁️            🌤
 🏔                                   
        🗻              🦅  
              
    🍄            🥚     🌴
            ''')
            time.sleep(0.1)
            await Message.edit('''
☁️          ☁️          ‌    🌤
 🏔                                   
        🗻               
                        🦅
    🍄            🥚     🌴
            ''')
            await Message.edit('''
☁️          ☁️          ‌    🌤
 🏔                                   
        🗻               
                    🦅      
    🍄         🥚          🌴
            ''')
            time.sleep(0.1)

            await Message.edit('''
☁️          ☁️          ‌    🌤
 🏔                                   
        🗻     🦅        
                  🥚      
    🍄                        🌴
            ''')
            time.sleep(0.1)

            await Message.edit('''
☁️          ☁️          ‌    🌤
 🏔       🦅                       
        🗻🥚        
                        
    🍄                        🌴
             ''')
            time.sleep(0.1)

            await Message.edit('''
☁️      🦅☁️          ‌     🌤
 🏔     🥚                       
        🗻        
                        
    🍄                        🌴
            ''')
            time.sleep(0.1)

            await Message.edit('''
☁️        🥚☁️          ‌     🌤
 🏔                            
        🗻        
                        
    🍄                        🌴
            ''')
            time.sleep(0.1)

            await Message.edit('''
☁️            ☁️          ‌     🌤
 🏔                            
        🗻        
                        
    🍄                        🌴
            ''')
            time.sleep(0.1)


        elif text == 'رقص' or text == 'dance':
            await Message.edit('''
🟦🟦🟥🟦🟦
🟦🟦🟥🟦🟦
🟥🟥🟥🟥🟥
🟦🟦🟥🟦🟦
🟦🟦🟥🟦🟦
    ''')
            time.sleep(0.1)

            await Message.edit('''
🟨🟦🟥🟦🟨
🟦🟦🟥🟦🟦
🟥🟥🟨🟥🟥
🟦🟦🟥🟦🟦
🟨🟦🟥🟦🟨
    ''')
            time.sleep(0.1)

            await Message.edit('''
🟩🟦🟥🟦🟦
🟦🟧🟥🟦🟦
🟥🟥🟨🟥🟥
🟦🟦🟥🟧🟦
🟦🟦🟥🟦🟩
    ''')
            time.sleep(0.1)

            await Message.edit('''
🟩🟦🟥🟦🟩
🟦🟧🟥🟧🟦
🟥🟥🟨🟥🟥
🟦🟧🟥🟧🟦
🟩🟦🟥🟦🟩
    ''')
            time.sleep(0.1)

            await Message.edit('''
🟩🟦⬜️🟦🟩
🟦🟧⬜️🟧🟦
⬜️⬜️⬜️⬜️⬜️
🟦🟧⬜️🟧🟦
🟩🟦⬜️🟦🟩
    ''')
            time.sleep(0.1)

            await Message.edit('''
🟩🟦⬜️🟦🟩
🟦🟧⬜️🟧🟦

🟦🟧⬜️🟧🟦
🟩🟦⬜️🟦🟩
      ''')
            time.sleep(0.1)

            await Message.edit('''
🟩🟦⬜️🟦🟩
🟦🟧⬜️🟧🟦
🟦🟧⬜️🟧🟦
🟩🟦⬜️🟦🟩
      ''')
            time.sleep(0.1)

            await Message.edit('''
🟩🟦🟦🟩
🟦🟧🟧🟦
🟦🟧🟧🟦
🟩🟦🟦🟩
      ''')
            time.sleep(0.1)

            await Message.edit('''
🟦🟦
🟦🟦
🟦🟦
🟦🟦
      ''')
            time.sleep(0.1)

            await Message.edit('''
◻️🟦
🟦🟦
🟦🟦
🟦🟦
      ''')
            time.sleep(0.1)

            await Message.edit('''
◻️◻️
🟦🟦
🟦🟦
🟦🟦
    ''')
            time.sleep(0.1)

            await Message.edit('''
◻️◻️
◻️🟦
🟦🟦
🟦🟦
    ''')
            time.sleep(0.1)

            await Message.edit('''
◻️◻️
◻️◻️
🟦🟦
🟦🟦
    ''')
            time.sleep(0.1)

            await Message.edit('''
◻️◻️
◻️◻️
◻️🟦
🟦🟦
    ''')
            time.sleep(0.1)
            await Message.edit('''
◻️◻️
◻️◻️
◻️◻️
🟦🟦
    ''')
            time.sleep(0.1)
            await Message.edit('''
◻️◻️
◻️◻️
◻️◻️
◻️🟦
    ''')
            time.sleep(0.1)
            await Message.edit('''
◽️◽️
◽️◽️
◽️◽️
◽️◽️
    ''')
            time.sleep(0.1)
            await Message.edit('''
◾️◾️
◾️◾️
◾️◾️
◾️◾️
    ''')
            time.sleep(0.1)
            await Message.edit('''
◽️◾️◾️◾️◾️◽️
◾️    𝙵𝙸𝙽𝙸𝚂𝙷    ◾️
◽️◾️◾️◾️◾️◽️
    ''')
        elif text == 'گلب' or text == 'heart':
            await Message.edit('''
❤️❤️❤️💖❤️❤️❤️
❤️❤️❤️💖❤️❤️❤️
❤️❤️❤️💖❤️❤️❤️
❤️❤️❤️💖❤️❤️❤️
❤️❤️❤️💖❤️❤️❤️
❤️❤️❤️💖❤️❤️❤️
❤️❤️❤️💖❤️❤️❤️
      ''')
            time.sleep(0.2)
            await Message.edit('''
❤️❤️❤️❤️❤️❤️💖
❤️❤️❤️❤️❤️💖❤️
❤️❤️❤️❤️💖❤️❤️
❤️❤️❤️💖❤️❤️❤️
❤️❤️💖❤️❤️❤️❤️
❤️💖❤️❤️❤️❤️❤️
💖❤️❤️❤️❤️❤️❤️
      ''')
            time.sleep(0.2)
            await Message.edit('''
❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️
💖💖💖💖💖💖💖
❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️
    ''')
            time.sleep(0.2)
            await Message.edit('''
💖❤️❤️❤️❤️❤️❤️
❤️💖❤️❤️❤️❤️❤️
❤️❤️💖❤️❤️❤️❤️
❤️❤️❤️💖❤️❤️❤️
❤️❤️❤️❤️💖❤️❤️
❤️❤️❤️❤️❤️💖❤️
❤️❤️❤️❤️❤️❤️💖
      ''')
            time.sleep(0.2)
            await Message.edit('''
❤️❤️❤️💖❤️❤️❤️
❤️❤️❤️💖❤️❤️❤️
❤️❤️❤️💖❤️❤️❤️
💖💖💖💖💖💖💖
❤️❤️❤️💖❤️❤️❤️
❤️❤️❤️💖❤️❤️❤️
❤️❤️❤️💖❤️❤️❤️
    ''')
            time.sleep(0.2)
            await Message.edit('''
❤️💖❤️💖❤️💖❤️
💖❤️💖❤️💖❤️💖
❤️💖❤️💖❤️💖❤️
💖❤️💖❤️💖❤️💖
❤️💖❤️💖❤️💖❤️
💖❤️💖❤️💖❤️💖
❤️💖❤️💖❤️💖❤️
    ''')
            time.sleep(0.2)
            await Message.edit('''
💖💖💖💖💖💖💖
💖💖💖💖💖💖💖
💖💖💖💖💖💖💖
💖💖💖💖💖💖💖
💖💖💖💖💖💖💖
💖💖💖💖💖💖💖
💖💖💖💖💖💖💖
    ''')
            time.sleep(0.2)
            await Message.edit('𝙸 𝙻𝙾𝚅𝙴 𝚈𝙾𝚄 💫 ')
        elif text == 'fuck' or text == 'فاک':
            await Message.edit('''
🖕🖕🖕🖕🖕🖕🖕
🖕🖕🖕🖕🖕🖕🖕
🖕🖕🖕🖕🖕🖕🖕
🖕🖕🖕🖕🖕🖕🖕
🖕🖕🖕🖕🖕🖕🖕
🖕🖕🖕🖕🖕🖕🖕
🖕🖕🖕🖕🖕🖕🖕
    ''')
            time.sleep(0.2)
            await Message.edit('''
🖕🏿🖕🖕🖕🖕🖕🖕
🖕🖕🏿🖕🖕🖕🖕🖕
🖕🖕🖕🏿🖕🖕🖕🖕
🖕🖕🖕🖕🏿🖕🖕🖕
🖕🖕🖕🖕🖕🏿🖕🖕
🖕🖕🖕🖕🖕🖕🏿🖕
🖕🖕🖕🖕🖕🖕🖕🏿
    ''')
            time.sleep(0.2)
            await Message.edit('''
🖕🏿🖕🖕🖕🖕🖕🖕🏿
🖕🖕🏿🖕🖕🖕🖕🏿🖕
🖕🖕🖕🏿🖕🖕🏿🖕🖕
🖕🖕🖕🖕🏿🖕🖕🖕
🖕🖕🖕🏿🖕🖕🏿🖕🖕
🖕🖕🏿🖕🖕🖕🖕🏿🖕
🖕🏿🖕🖕🖕🖕🖕🖕🏿
    ''')
            time.sleep(0.2)
            await Message.edit('''
🖕🏿🖕🖕🖕🏿🖕🖕🖕🏿
🖕🖕🏿🖕🖕🏿🖕🖕🏿🖕
🖕🖕🖕🏿🖕🏿🖕🏿🖕🖕
🖕🖕🖕🖕🏿🖕🖕🖕
🖕🖕🖕🏿🖕🏿🖕🏿🖕🖕
🖕🖕🏿🖕🖕🏿🖕🖕🏿🖕
🖕🏿🖕🖕🖕🏿🖕🖕🖕🏿
    ''')


            time.sleep(0.2)
            await Message.edit('''
🖕🏿🖕🏿🖕🏿🖕🏿🖕🏿🖕🏿🖕🏿
🖕🏿🖕🏿🖕🖕🖕🖕🏿🖕🏿
🖕🏿🖕🖕🏿🖕🖕🏿🖕🖕🏿
🖕🏿🖕🖕🖕🏿🖕🖕🖕🏿
🖕🏿🖕🖕🏿🖕🖕🏿🖕🖕🏿
🖕🏿🖕🏿🖕🖕🖕🖕🏿🖕🏿
🖕🏿🖕🏿🖕🏿🖕🏿🖕🏿🖕🏿🖕🏿
      ''')

            time.sleep(0.2)
            await Message.edit('''
🖕🖕🖕🖕🖕🖕🖕
🖕🖕🖕🏿🖕🏿🖕🏿🖕🖕
🖕🖕🏿🖕🖕🏿🖕🖕🏿🖕
🖕🖕🏿🖕🏿🖕🖕🏿🖕🏿🖕
🖕🖕🏿🖕🖕🏿🖕🖕🏿🖕
🖕🖕🖕🏿🖕🏿🖕🏿🖕🖕
🖕🖕🖕🖕🖕🖕🖕
      ''')
            time.sleep(0.2)
            await Message.edit('ғᴜᴄᴋ ʏᴏᴜ 🖕🏻')
        elif text == 'fuck you' or text == 'فاک یو' :
            await Message.edit('🖕🏿🖕🖕🖕🖕🖕🖕')
            time.sleep(0.1)
            await Message.edit('🖕🖕🏿🖕🖕🖕🖕🖕')
            time.sleep(0.1)
            await Message.edit('🖕🖕🖕🏿🖕🖕🖕🖕')
            time.sleep(0.1)
            await Message.edit('🖕🖕🖕🖕🏿🖕🖕🖕')
            time.sleep(0.1)
            await Message.edit('🖕🖕🖕🖕🖕🏿🖕🖕')
            time.sleep(0.1)
            await Message.edit('🖕🖕🖕🖕🖕🖕🏿🖕')
            time.sleep(0.1)
            await Message.edit('🖕🖕🖕🖕🖕🖕🖕🏿')
            time.sleep(0.1)
            await Message.edit('🖕🖕🖕🖕🖕🖕🏿🖕')
            time.sleep(0.1)
            await Message.edit('🖕🖕🖕🖕🖕🏿🖕🖕')
            time.sleep(0.1)
            await Message.edit('🖕🖕🖕🖕🏿🖕🖕🖕')
            time.sleep(0.1)
            await Message.edit('🖕🖕🖕🏿🖕🖕🖕🖕')
            time.sleep(0.1)
            await Message.edit('🖕🖕🏿🖕🖕🖕🖕🖕')
            time.sleep(0.1)
            await Message.edit('🖕🏿🖕🖕🖕🖕🖕🖕')
            time.sleep(0.1)
            await Message.edit('🖕🖕🏿🖕🖕🏿🖕🖕🏿🖕')
            time.sleep(0.1)
            await Message.edit('🖕🏿🖕🖕🏿🖕🖕🏿🖕🖕🏿')
            time.sleep(0.1)
            await Message.edit('𝐟𝐮𝐜𝐤 𝐲𝐨𝐮 🖕🏼🦦')
        elif text == 'کبص' or text=='کوبص':

            await Message.edit('🚶‍♀              🚶‍♂')
            await Message.edit('🚶‍♀             🚶‍♂')
            await Message.edit('🚶‍♀            🚶‍♂')
            await Message.edit('🚶‍♀           🚶‍♂')
            await Message.edit('🚶‍♀          🚶‍♂')
            await Message.edit('🚶‍♀         🚶‍♂')
            await Message.edit('🚶‍♀        🚶‍♂')
            await Message.edit('🚶‍♀       🚶‍♂')
            await Message.edit('🚶‍♀      🚶‍♂')
            await Message.edit('🚶‍♀     🚶‍♂')
            await Message.edit('🚶‍♀    🚶‍♂')
            await Message.edit('🚶‍♀   🚶‍♂')
            await Message.edit('🚶‍♀  🚶‍♂')
            await Message.edit('🚶‍♀ 🚶‍♂')
            await Message.edit('🚶‍♀🚶‍♂')
            await Message.edit('🧎‍♀🚶‍♂')
            await Message.edit('💦🔞')
        elif text == 'ساک' and len(text) == 3:



            await Message.edit('🗣<=======Ѽ')
            await Message.edit('🗣=======Ѽ')
            await Message.edit('🗣======Ѽ')
            await Message.edit('🗣=====Ѽ')
            await Message.edit('🗣====Ѽ')
            await Message.edit('🗣===Ѽ')
            await Message.edit('🗣==Ѽ')
            await Message.edit('🗣=Ѽ')
            await Message.edit('🗣Ѽ')
            await Message.edit('🗣=Ѽ')
            await Message.edit('🗣==Ѽ')
            await Message.edit('🗣===Ѽ')
            await Message.edit('🗣====Ѽ')
            await Message.edit('🗣=====Ѽ')
            await Message.edit('🗣======Ѽ')
            await Message.edit('🗣=======Ѽ')
            await Message.edit('🗣<=======Ѽ')
            await Message.edit('💦💦😈')
        elif text == 'bk' or text== 'بکیرم':

            await Message.edit('''
🤤🤤🤤
🤤         🤤
🤤           🤤
🤤        🤤
🤤🤤🤤
🤤         🤤
🤤           🤤
🤤           🤤
🤤        🤤
🤤🤤🤤
    ''')
            await Message.edit('''
💦         💦
💦       💦
💦     💦
💦   💦
💦💦
💦   💦
💦      💦
💦        💦
💦          💦
💦            💦
    ''')

            await Message.edit('''
🍆🍆🍆          🍆        🍆
🍆         🍆      🍆       🍆
🍆           🍆    🍆     🍆
🍆        🍆       🍆   🍆
🍆🍆🍆          🍆🍆
🍆         🍆      🍆   🍆
🍆           🍆    🍆      🍆
🍆           🍆    🍆        🍆
🍆        🍆       🍆          🍆
🍆🍆🍆          🍆            🍆
    ''')

            await Message.edit('''
🖕🏻🖕🏻🖕🏻          🖕🏻        🖕🏻
🖕🏻         🖕🏻      🖕🏻       🖕🏻
🖕🏻           🖕🏻    🖕🏻     🖕🏻
🖕🏻        🖕🏻       🖕🏻   🖕🏻
🖕🏻🖕🏻🖕🏻          🖕🏻🖕🏻
🖕🏻         🖕🏻      🖕🏻   🖕🏻
🖕🏻           🖕🏻    🖕🏻      🖕🏻
🖕🏻           🖕🏻    🖕🏻        🖕🏻
🖕🏻        🖕🏻       🖕🏻          🖕🏻
🖕🏻🖕🏻🖕🏻          🖕🏻            🖕🏻
    ''')

            await Message.edit('''
⚡⚡⚡          ⚡        ⚡
⚡         ⚡      ⚡       ⚡
⚡           ⚡    ⚡     ⚡
⚡        ⚡       ⚡   ⚡
⚡⚡⚡          ⚡⚡
⚡         ⚡      ⚡   ⚡
⚡           ⚡    ⚡      ⚡
⚡           ⚡    ⚡        ⚡
⚡        ⚡       ⚡          ⚡
⚡⚡⚡          ⚡            ⚡
    ''')

            await Message.edit('''
💩💩💩          💩        💩
💩         💩      💩       💩
💩           💩    💩     💩
💩        💩       💩   💩
💩💩💩          💩💩
💩         💩      💩   💩
💩           💩    💩      💩
💩           💩    💩        💩
💩        💩       💩          💩
💩💩💩          💩            💩
    ''')

            await Message.edit('''
🤬🤬🤬          🤬        🤬
🤬         🤬      🤬       🤬
🤬           🤬    🤬     🤬
🤬        🤬       🤬   🤬
🤬🤬🤬          🤬🤬
🤬         🤬      🤬   🤬
🤬           🤬    🤬      🤬
🤬           🤬    🤬        🤬
🤬        🤬       🤬          🤬
🤬🤬🤬          🤬            🤬
    ''')

            await Message.edit('''
😐😐😐          😐        😐
😐         😐      😐       😐
😐           😐    😐     😐
😐        😐       😐   😐
😐😐😐          😐😐
😐         😐      😐   😐
😐           😐    😐      😐
😐           😐    😐        😐
😐        😐       😐          😐
😐😐😐          😐            😐
بکیرم 
    ''')

        elif text == 'انگشت':

            await Message.edit('👌🏻=======👈🏻')
            await Message.edit('👌🏻======👈🏻')
            await Message.edit('👌🏻=====👈🏻')
            await Message.edit('👌🏻====👈🏻')
            await Message.edit('👌🏻===👈🏻')
            await Message.edit('👌🏻==👈🏻')
            await Message.edit('👌🏻=👈🏻')

            time.sleep(0.1)
            await Message.edit('انگشت شد😂👌')
        elif text == 'جغ' or text== 'جق':

            await Message.edit('ѼΞΞΞΞΞΞΞD🤌🏻')


            await Message.edit('ѼΞΞΞΞΞΞΞ🤌🏻D')


            await Message.edit('ѼΞΞΞΞΞΞ🤌🏻ΞD')


            await Message.edit('ѼΞΞΞΞΞ🤌🏻ΞΞD')


            await Message.edit('ѼΞΞΞΞ🤌🏻ΞΞΞD')


            await Message.edit('ѼΞΞΞ🤌🏻ΞΞΞΞD')
          #

            await Message.edit('ѼΞΞ🤌🏻ΞΞΞΞΞD')


            await Message.edit('ѼΞ🤌🏻ΞΞΞΞΞΞD')


            await Message.edit('Ѽ🤌🏻ΞΞΞΞΞΞΞD')


            await Message.edit('ѼΞ🤌🏻ΞΞΞΞΞΞD')


            await Message.edit('ѼΞΞ🤌🏻ΞΞΞΞΞD')


            await Message.edit('ѼΞΞΞ🤌🏻ΞΞΞΞD')


            await Message.edit('ѼΞΞΞΞ🤌🏻ΞΞΞD')

            await Message.edit('ѼΞΞΞΞΞ🤌🏻ΞΞD')

            await Message.edit('ѼΞΞΞΞΞΞ🤌🏻ΞD')

            await Message.edit('ѼΞΞΞΞΞΞΞ🤌🏻D')

            await Message.edit('ѼΞΞΞΞΞΞΞD🤌🏻')

            await Message.edit('ѼΞΞΞΞΞΞΞD💦')
            time.sleep(0.1)

            await Message.edit('ѼΞΞΞΞΞΞΞD💦💦')
            time.sleep(0.2)

            await Message.edit(' تو صورت بدخاه😂✊')

        elif text == 'جوجه':
            await Message.edit('''🌧🌧⛈🌧🌧

🥚    🍄‌''')
            time.sleep(0.2)


            await Message.edit('''🌧☁️⛈🌧🌧

🐣    🍄‌''')
            time.sleep(0.2)
            await Message.edit('''🌧☁️🌧🌧☁️

🐓    🍄‌‌''')
            time.sleep(0.2)

            await Message.edit('🍗😋')
        # delete
        elif text == 'food':
            await Message.edit('《=====🥚')
            time.sleep(0.2)
            await Message.edit('《=====🐣')
            time.sleep(0.2)
            await Message.edit('《=====🐥')
            time.sleep(0.2)
            await Message.edit('《=====🐓')
            time.sleep(0.2)
            await Message.edit('🍗😋')
            time.sleep(0.2)
            await Message.edit('نوش جان☺️😇')
            time.sleep(0.2)
            await Message.edit('نوش جان☺️😇')
            time.sleep(0.2)
        if text == 'you':
            love = ['🄻🄾🅅🄴 🅈🄾🅄','𝒍𝒐𝒗𝒆 𝒚𝒐𝒖','ʟᴏᴠᴇ ʏᴏᴜ','ʟᴏᴠᴇ ʏᴏᴜ','𝓵𝓸𝓿𝓮 𝔂𝓸𝓾','Ŀ♡ѴƐ Y♡Ʊ','‌𝕝𝕠𝕧𝕖 𝕪𝕠𝕦']
            for i in love:
                await Message.edit(f'{i} [{Message.chat.first_name}](tg://{Message.chat.id}) {random.choice(qalb)}')
                time.sleep(0.2)
        elif text == 'time':
            fonts = {
        
                 ':':':','0':'⓪','1':'➊','2':'②','3':'➌','4':'④','5':'➎','6':'⑥','7':'➐','8':'⑧','9':'➒'
            }
            
            for i in range(30):
                qal = random.choice(qalb)
                qal2 = random.choice(qalb)
                qal3 = random.choice(qalb)
                qal4 = random.choice(qalb)
                
                t = time.localtime()
                tme = time.strftime("%H:%M:%S", t)
                currect = ''
                for char in tme:
                    currect += fonts[char]
                
                await Message.edit(f'{qal3}{qal}{qal4} {currect} {qal2}{qal4}{qal}')
                time.sleep(0.9)
           

app.run()