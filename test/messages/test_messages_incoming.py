from unittest import TestCase

from kik.messages import VideoMessage, UnknownMessage, TextMessage, StartChattingMessage, StickerMessage, \
    ScanDataMessage, PictureMessage, LinkMessage, IsTypingMessage, ReadReceiptMessage, DeliveryReceiptMessage


class KikBotMessagesIncomingTest(TestCase):
    def test_text_message_incoming(self):
        message = TextMessage.from_json({
            'from': 'aleem',
            'participants': ['aleem'],
            'mention': None,
            'chatId': 'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2',
            'body': 'Some text',
            'id': '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0',
            'timestamp': 1458336131,
            'readReceiptRequested': True
        })

        self.assertEqual(message.from_user, 'aleem')
        self.assertEqual(message.participants, ['aleem'])
        self.assertIs(None, message.mention)
        self.assertEqual(message.chat_id, 'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2')
        self.assertEqual(message.body, 'Some text')
        self.assertEqual(message.id, '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0')
        self.assertEqual(message.timestamp, 1458336131)
        self.assertIs(True, message.read_receipt_requested)

    def test_link_message_incoming(self):
        message = LinkMessage.from_json({
            'from': 'aleem',
            'participants': ['aleem'],
            'mention': None,
            'chatId': 'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2',
            'url': 'http://foo.bar',
            'title': 'A Title',
            'text': 'Some text',
            'noForward': True,
            'kikJsData': 'somedata',
            'attribution': {
                'name': 'Webpage',
                'iconUrl': 'http://foo.bar/icon'
            },
            'id': '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0',
            'timestamp': 1458336131,
            'readReceiptRequested': True
        })

        self.assertEqual(message.from_user, 'aleem')
        self.assertEqual(message.participants, ['aleem'])
        self.assertIs(None, message.mention)
        self.assertEqual(message.chat_id, 'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2')
        self.assertEqual(message.url, 'http://foo.bar')
        self.assertEqual(message.title, 'A Title')
        self.assertEqual(message.text, 'Some text')
        self.assertEqual(message.no_forward, True)
        self.assertEqual(message.kik_js_data, 'somedata')
        self.assertEqual(message.attribution.name, 'Webpage')
        self.assertEqual(message.attribution.icon_url, 'http://foo.bar/icon')
        self.assertEqual(message.id, '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0')
        self.assertEqual(message.timestamp, 1458336131)
        self.assertIs(True, message.read_receipt_requested)

    def test_picture_message_incoming(self):
        message = PictureMessage.from_json({
            'from': 'aleem',
            'participants': ['aleem'],
            'mention': None,
            'chatId': 'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2',
            'picUrl': 'http://foo.bar/image',
            'attribution': {
                'name': 'Webpage',
                'iconUrl': 'http://foo.bar/icon'
            },
            'id': '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0',
            'timestamp': 1458336131,
            'readReceiptRequested': True
        })

        self.assertEqual(message.from_user, 'aleem')
        self.assertEqual(message.participants, ['aleem'])
        self.assertIs(None, message.mention)
        self.assertEqual(message.chat_id, 'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2')
        self.assertEqual(message.pic_url, 'http://foo.bar/image')
        self.assertEqual(message.attribution.name, 'Webpage')
        self.assertEqual(message.attribution.icon_url, 'http://foo.bar/icon')
        self.assertEqual(message.id, '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0')
        self.assertEqual(message.timestamp, 1458336131)
        self.assertIs(True, message.read_receipt_requested)

    def test_video_message_incoming(self):
        message = VideoMessage.from_json({
            'from': 'aleem',
            'participants': ['aleem'],
            'mention': None,
            'chatId': 'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2',
            'videoUrl': 'http://foo.bar/vid',
            'muted': False,
            'autoplay': True,
            'loop': False,
            'attribution': {
                'name': 'Webpage',
                'iconUrl': 'http://foo.bar/icon'
            },
            'id': '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0',
            'timestamp': 1458336131,
            'readReceiptRequested': True
        })

        self.assertEqual(message.from_user, 'aleem')
        self.assertEqual(message.participants, ['aleem'])
        self.assertIs(None, message.mention)
        self.assertEqual(message.chat_id, 'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2')
        self.assertEqual(message.video_url, 'http://foo.bar/vid')
        self.assertIs(False, message.muted)
        self.assertIs(True, message.autoplay)
        self.assertIs(False, message.loop)
        self.assertEqual(message.attribution.name, 'Webpage')
        self.assertEqual(message.attribution.icon_url, 'http://foo.bar/icon')
        self.assertEqual(message.id, '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0')
        self.assertEqual(message.timestamp, 1458336131)
        self.assertIs(True, message.read_receipt_requested)

    def test_start_chatting_incoming(self):
        message = StartChattingMessage.from_json({
            'from': 'aleem',
            'participants': ['aleem'],
            'mention': None,
            'chatId': 'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2',
            'id': '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0',
            'timestamp': 1458336131,
            'readReceiptRequested': False
        })

        self.assertEqual(message.from_user, 'aleem')
        self.assertEqual(message.participants, ['aleem'])
        self.assertIs(None, message.mention)
        self.assertEqual(message.chat_id, 'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2')
        self.assertEqual(message.id, '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0')
        self.assertEqual(message.timestamp, 1458336131)
        self.assertIs(False, message.read_receipt_requested)

    def test_sticker_message_incoming(self):
        message = StickerMessage.from_json({
            'from': 'aleem',
            'participants': ['aleem'],
            'mention': None,
            'chatId': 'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2',
            'stickerPackId': 'memes',
            'stickerUrl': 'http://cards-sticker-dev.herokuapp.com/stickers/memes/okay.png',
            'id': '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0',
            'timestamp': 1458336131,
            'readReceiptRequested': False
        })

        self.assertEqual(message.from_user, 'aleem')
        self.assertEqual(message.participants, ['aleem'])
        self.assertIs(None, message.mention)
        self.assertEqual(message.chat_id, 'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2')
        self.assertEqual(message.sticker_pack_id, 'memes')
        self.assertEqual(message.sticker_url, 'http://cards-sticker-dev.herokuapp.com/stickers/memes/okay.png')
        self.assertEqual(message.id, '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0')
        self.assertEqual(message.timestamp, 1458336131)
        self.assertIs(False, message.read_receipt_requested)

    def test_scan_data_message_incoming(self):
        message = ScanDataMessage.from_json({
            'from': 'aleem',
            'participants': ['aleem'],
            'mention': None,
            'chatId': 'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2',
            'data': 'foobar',
            'id': '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0',
            'timestamp': 1458336131,
            'readReceiptRequested': False
        })

        self.assertEqual(message.from_user, 'aleem')
        self.assertEqual(message.participants, ['aleem'])
        self.assertIs(None, message.mention)
        self.assertEqual(message.chat_id, 'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2')
        self.assertEqual(message.data, 'foobar')
        self.assertEqual(message.id, '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0')
        self.assertEqual(message.timestamp, 1458336131)
        self.assertIs(False, message.read_receipt_requested)

    def test_is_typing_incoming(self):
        message = IsTypingMessage.from_json({
            'from': 'aleem',
            'participants': ['aleem'],
            'mention': None,
            'chatId': 'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2',
            'isTyping': True,
            'id': '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0',
            'timestamp': 1458336131,
            'readReceiptRequested': False
        })

        self.assertEqual(message.from_user, 'aleem')
        self.assertEqual(message.participants, ['aleem'])
        self.assertIs(None, message.mention)
        self.assertEqual(message.chat_id, 'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2')
        self.assertIs(True, message.is_typing)
        self.assertEqual(message.id, '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0')
        self.assertEqual(message.timestamp, 1458336131)
        self.assertIs(False, message.read_receipt_requested)

    def test_read_receipt_incoming(self):
        message = ReadReceiptMessage.from_json({
            'from': 'aleem',
            'participants': ['aleem'],
            'mention': None,
            'chatId': 'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2',
            'messageIds': ['ff3ea373-576c-45d4-bdcd-9956a156301d'],
            'id': '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0',
            'timestamp': 1458336131,
            'readReceiptRequested': False
        })

        self.assertEqual(message.from_user, 'aleem')
        self.assertEqual(message.participants, ['aleem'])
        self.assertIs(None, message.mention)
        self.assertEqual(message.chat_id, 'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2')
        self.assertEqual(message.message_ids, ['ff3ea373-576c-45d4-bdcd-9956a156301d'])
        self.assertEqual(message.id, '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0')
        self.assertEqual(message.timestamp, 1458336131)
        self.assertIs(False, message.read_receipt_requested)

    def test_delivery_receipt_incoming(self):
        message = DeliveryReceiptMessage.from_json({
            'from': 'aleem',
            'participants': ['aleem'],
            'mention': None,
            'chatId': 'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2',
            'messageIds': ['ff3ea373-576c-45d4-bdcd-9956a156301d'],
            'id': '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0',
            'timestamp': 1458336131,
            'readReceiptRequested': False
        })

        self.assertEqual(message.from_user, 'aleem')
        self.assertEqual(message.participants, ['aleem'])
        self.assertIs(None, message.mention)
        self.assertEqual(message.chat_id, 'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2')
        self.assertEqual(message.message_ids, ['ff3ea373-576c-45d4-bdcd-9956a156301d'])
        self.assertEqual(message.id, '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0')
        self.assertEqual(message.timestamp, 1458336131)
        self.assertIs(False, message.read_receipt_requested)

    def test_unknown_message_incoming(self):
        message_json = {
            'type': 'some-unknown-type',
            'from': 'aleem',
            'participants': ['aleem'],
            'mention': None,
            'chatId': 'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2',
            'anUnknownProperty': ['With', 'Some', 'Values'],
            'id': '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0',
            'timestamp': 1458336131,
            'readReceiptRequested': False
        }
        message = UnknownMessage.from_json(message_json)

        self.assertEqual(message.type, 'some-unknown-type')
        self.assertEqual(message.from_user, 'aleem')
        self.assertEqual(message.participants, ['aleem'])
        self.assertIs(None, message.mention)
        self.assertEqual(message.chat_id, 'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2')
        self.assertEqual(message.raw_message, message_json)
        self.assertEqual(message.id, '8e7fc0ad-36aa-43dd-8c5f-e72f5f2ed7e0')
        self.assertEqual(message.timestamp, 1458336131)
        self.assertIs(False, message.read_receipt_requested)
