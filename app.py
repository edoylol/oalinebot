from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json


import errno
import os
import sys, random
import tempfile

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent,
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('HllzR7lQE3rKqkVx7QmFCTqQ2et2HaiQbKwKAQOeksfm4Ypg5xEdGcFva4qjtkhZqPrxg1S+V/ouHm3FOepJ7cdWm/imHI8gceuK1AxzcEgH3e/xW+ctwAdcaDSwjDOLoW59stZCbjSD+XR8OnGbcgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('e7130e1ea7d36818b3512cacb599d6a8')
#===========[ NOTE SAVER ]=======================
notes = {}

# Post Request
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text #simplify for receove message
    sender = event.source.user_id #get user_id
    gid = event.source.sender_id #get group_id
    
    def quickreply(*msgs, mode=('text',)*5):
        msgs = msgs[:5]
        content = []
        for idx, msg in enumerate(msgs):
            if mode[idx] == 'text':
                if isinstance(msg, (tuple, list)):
                    content = [TextSendMessage(text=item) for item in msg]
                    else:
                        content.append(TextSendMessage(text=msg))
                        elif mode[idx] == 'image':
                            if isinstance(msg, (tuple, list)):
                                content = [ImageSendMessage(original_content_url=item,preview_image_url=item)
                                           for item in msg]
                                else:
                                    content.append(ImageSendMessage(original_content_url=msg,preview_image_url=msg))
                                    elif mode[idx] == 'custimg':
                                        if isinstance(msg, (tuple, list)):
                                            content = [ImageSendMessage(original_content_url=item[0],preview_image_url=item[1])
                                                       for item in msg]
                                            else:
                                                content.append(ImageSendMessage(original_content_url=msg[0],preview_image_url=msg[1]))
                                                line_bot_api.reply_message(event.reply_token, content)
    

    

#=====[ LEAVE GROUP OR ROOM ]==========
    if text == 'profil':
        getprofile()
    if text == '/minggat':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='bye👌'))
            line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='good bye vroh👌'))
            line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))
#=====[ TEMPLATE MESSAGE ]=============
    elif text == '/template':
        buttons_template = TemplateSendMessage(
            alt_text='template',
            template=ButtonsTemplate(
                title='[ TEMPLATE MSG ]',
                text= 'Tap the Button',
                actions=[
                    MessageTemplateAction(
                        label='help menu',
                        text='/menu'
                    ),
                    MessageTemplateAction(
                        label='bot leave',
                        text='/minggat'
                    ),
                    MessageTemplateAction(
                        label='flex',
                        text='flex'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token, buttons_template)
#=====[ CAROUSEL MESSAGE ]==========
    elif text == '/menu':
        message = TemplateSendMessage(
            alt_text='OTHER MENU',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        title='ADD ME',
                        text='anu',
                        actions=[
                            URITemplateAction(
                                label='>TAP HERE<',
                                uri='https://line.me/ti/p/~vekok.'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Instagram',
                        text='FIND ME ON INSTAGRAM',
                        actions=[
                            URITemplateAction(
                                label='>TAP HERE!<',
                                uri='http://line.me/ti/p/~vekok.'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#=====[ FLEX MESSAGE ]==========
    elif text == 'flex':
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://lh5.googleusercontent.com/VoOmR6tVRwKEow0HySsJ_UdrQrqrpwUwSzQnGa0yBeqSex-4Osar2w-JohT6yPu4Vl4qchND78aU2c5a5Bhl=w1366-h641-rw',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='http://line.me/ti/p/~vekok.', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='vekok', weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            IconComponent(size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(size='sm', url='https://example.com/grey_star.png'),
                            IconComponent(size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(size='sm', url='https://example.com/grey_star.png'),
                            TextComponent(text='4.0', size='sm', color='#999999', margin='md',
                                          flex=0)
                        ]
                    ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Place',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='Tangerang, Indonesia',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Time',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="10:00 - 23:00",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='vekok', uri="https://line.me/ti/p/~vekok.")
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="hello", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
#=======================================================================================================================
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
