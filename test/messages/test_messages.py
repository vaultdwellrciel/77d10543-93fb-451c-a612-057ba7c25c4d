from unittest import TestCase

from kik.messages import IsTypingMessage, LinkMessage, PictureMessage, ReadReceiptMessage, TextMessage, VideoMessage, \
    SuggestedResponseKeyboard, TextResponse, CustomAttribution, PresetAttributions


class KikBotMessagesTest(TestCase):
    def test_text_message(self):
        message = TextMessage(body='Some text', to='aleem').to_json()
        self.assertEqual(message, {
            'type': 'text',
            'to': 'aleem',
            'body': 'Some text'
        })

    def test_text_message_id(self):
        message = TextMessage(body='Some text', to='aleem', id='8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0').to_json()
        self.assertEqual(message, {
            'type': 'text',
            'to': 'aleem',
            'body': 'Some text',
            'id': '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0'
        })

    def test_text_message_with_keyboard(self):
        message = TextMessage(
            body='Some text',
            to='aleem',
            id='8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0',
            keyboards=[
                SuggestedResponseKeyboard(
                    hidden=True,
                    responses=[
                        TextResponse('Foo')
                    ]
                )
            ]
        ).to_json()
        self.assertEqual(message, {
            'type': 'text',
            'to': 'aleem',
            'body': 'Some text',
            'id': '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0',
            'keyboards': [
                {
                    'type': 'suggested',
                    'hidden': True,
                    'responses': [
                        {'type': 'text', 'body': 'Foo'}
                    ]
                }
            ]
        })

    def test_text_message_delay(self):
        message = TextMessage(body='Some text', to='aleem', delay=1500).to_json()
        self.assertEqual(message, {
            'type': 'text',
            'to': 'aleem',
            'body': 'Some text',
            'delay': 1500
        })

    def test_link_message(self):
        message = LinkMessage(url='http://foo.bar', to='aleem').to_json()
        self.assertEqual(message, {
            'type': 'link',
            'to': 'aleem',
            'url': 'http://foo.bar'
        })

    def test_link_message_complete(self):
        message = LinkMessage(
            url='http://foo.bar',
            to='aleem',
            mention='anotherbot',
            chat_id='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
            title='A Title',
            text='Some Text',
            pic_url='http://foo.bar/image',
            no_forward=True,
            kik_js_data='foobar',
            keyboards=[
                SuggestedResponseKeyboard(
                    hidden=True,
                    responses=[
                        TextResponse('Foo')
                    ]
                )
            ],
            attribution=CustomAttribution(name='Foobar'),
            delay=100
        ).to_json()

        self.assertEqual(message, {
            'type': 'link',
            'to': 'aleem',
            'url': 'http://foo.bar',
            'mention': 'anotherbot',
            'chatId': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
            'title': 'A Title',
            'text': 'Some Text',
            'picUrl': 'http://foo.bar/image',
            'noForward': True,
            'kikJsData': 'foobar',
            'keyboards': [
                {
                    'type': 'suggested',
                    'hidden': True,
                    'responses': [
                        {'type': 'text', 'body': 'Foo'}
                    ]
                }
            ],
            'attribution': {
                'name': 'Foobar'
            },
            'delay': 100
        })

    def test_picture_message(self):
        message = PictureMessage(pic_url='http://foo.bar/image', to='aleem').to_json()
        self.assertEqual(message, {
            'type': 'picture',
            'to': 'aleem',
            'picUrl': 'http://foo.bar/image'
        })

    def test_picture_message_preset_attribution(self):
        message = PictureMessage(
            pic_url='http://foo.bar/image',
            attribution=PresetAttributions.CAMERA,
            to='aleem'
        ).to_json()

        self.assertEqual(message, {
            'type': 'picture',
            'to': 'aleem',
            'picUrl': 'http://foo.bar/image',
            'attribution': 'camera'
        })

    def test_picture_message_complete(self):
        message = PictureMessage(
            pic_url='http://foo.bar/image',
            to='aleem',
            mention='anotherbot',
            chat_id='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
            keyboards=[
                SuggestedResponseKeyboard(
                    hidden=True,
                    responses=[
                        TextResponse('Foo')
                    ]
                )
            ],
            attribution=CustomAttribution(name='Foobar'),
            delay=100
        ).to_json()

        self.assertEqual(message, {
            'type': 'picture',
            'to': 'aleem',
            'mention': 'anotherbot',
            'chatId': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
            'picUrl': 'http://foo.bar/image',
            'keyboards': [
                {
                    'type': 'suggested',
                    'hidden': True,
                    'responses': [
                        {'type': 'text', 'body': 'Foo'}
                    ]
                }
            ],
            'attribution': {
                'name': 'Foobar'
            },
            'delay': 100
        })

    def test_video_message(self):
        message = VideoMessage(video_url='http://foo.bar/vid', to='aleem').to_json()
        self.assertEqual(message, {
            'type': 'video',
            'to': 'aleem',
            'videoUrl': 'http://foo.bar/vid'
        })

    def test_video_message_preset_attribution(self):
        message = VideoMessage(
            video_url='http://foo.bar/vid',
            attribution=PresetAttributions.GALLERY,
            to='aleem'
        ).to_json()

        self.assertEqual(message, {
            'type': 'video',
            'to': 'aleem',
            'videoUrl': 'http://foo.bar/vid',
            'attribution': 'gallery'
        })

    def test_video_message_complete(self):
        message = VideoMessage(
            video_url='http://foo.bar/vid',
            to='aleem',
            mention='anotherbot',
            chat_id='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
            autoplay=True,
            muted=True,
            loop=True,
            no_save=True,
            keyboards=[
                SuggestedResponseKeyboard(
                    hidden=True,
                    responses=[
                        TextResponse('Foo')
                    ]
                )
            ],
            attribution=CustomAttribution(name='Foobar'),
            delay=100
        ).to_json()

        self.assertEqual(message, {
            'type': 'video',
            'to': 'aleem',
            'mention': 'anotherbot',
            'chatId': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
            'videoUrl': 'http://foo.bar/vid',
            'muted': True,
            'loop': True,
            'autoplay': True,
            'noSave': True,
            'keyboards': [
                {
                    'type': 'suggested',
                    'hidden': True,
                    'responses': [
                        {'type': 'text', 'body': 'Foo'}
                    ]
                }
            ],
            'attribution': {
                'name': 'Foobar'
            },
            'delay': 100
        })

    def test_is_typing_message(self):
        message = IsTypingMessage(is_typing=True, to='aleem').to_json()
        self.assertEqual(message, {
            'type': 'is-typing',
            'to': 'aleem',
            'isTyping': True
        })

    def test_read_receipt_message(self):
        message = ReadReceiptMessage(message_ids=['ff3ea373-576c-45d4-bdcd-9956a156301d'], to='aleem').to_json()
        self.assertEqual(message, {
            'type': 'read-receipt',
            'to': 'aleem',
            'messageIds': ['ff3ea373-576c-45d4-bdcd-9956a156301d']
        })

    def test_message_equality(self):
        message1 = PictureMessage(
            pic_url='http://foo.bar/image',
            to='aleem',
            mention='anotherbot',
            chat_id='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
            keyboards=[
                SuggestedResponseKeyboard(
                    hidden=True,
                    responses=[
                        TextResponse('Foo')
                    ]
                )
            ],
            attribution=CustomAttribution(name='Foobar'),
            delay=100
        )

        message2 = PictureMessage(
            pic_url='http://foo.bar/image',
            to='aleem',
            mention='anotherbot',
            chat_id='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
            keyboards=[
                SuggestedResponseKeyboard(
                    hidden=True,
                    responses=[
                        TextResponse('Foo')
                    ]
                )
            ],
            attribution=CustomAttribution(name='Foobar'),
            delay=100
        )

        self.assertEqual(message1, message2)

    def test_message_inequality(self):
        message1 = PictureMessage(
            pic_url='http://foo.bar/image',
            to='aleem',
            mention='anotherbot',
            chat_id='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
            keyboards=[
                SuggestedResponseKeyboard(
                    hidden=True,
                    responses=[
                        TextResponse('Foo')
                    ]
                )
            ],
            attribution=CustomAttribution(name='Foobar Not The Same'),
            delay=100
        )

        message2 = PictureMessage(
            pic_url='http://foo.bar/image',
            to='aleem',
            mention='anotherbot',
            chat_id='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
            keyboards=[
                SuggestedResponseKeyboard(
                    hidden=True,
                    responses=[
                        TextResponse('Foo')
                    ]
                )
            ],
            attribution=CustomAttribution(name='Foobar'),
            delay=100
        )

        self.assertNotEqual(message1, message2)
