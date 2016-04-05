from unittest import TestCase

from kik.messages import TextMessage, LinkMessage, UnknownMessage, messages_from_json


class MessageUtilsTest(TestCase):
    def test_empty_array(self):
        input = []
        output = messages_from_json(input)
        self.assertEqual(output, [])

    def test_single_element(self):
        input = [{'type': 'text', 'from': 'aleem', 'body': 'Yo text message!'}]
        output = messages_from_json(input)
        self.assertEqual(len(output), 1)
        self.assertIsInstance(output[0], TextMessage)
        self.assertEqual(output[0].type, 'text')
        self.assertEqual(output[0].from_user, 'aleem')
        self.assertEqual(output[0].body, 'Yo text message!')

    def test_multiple_elements(self):
        input = [{'type': 'text', 'from': 'aleem', 'body': 'Yo text message!'},
                 {'type': 'link', 'from': 'laura', 'url': 'http://yo.text/message'}]
        output = messages_from_json(input)
        self.assertEqual(len(output), 2)
        self.assertIsInstance(output[0], TextMessage)
        self.assertEqual(output[0].type, 'text')
        self.assertEqual(output[0].from_user, 'aleem')
        self.assertEqual(output[0].body, 'Yo text message!')
        self.assertIsInstance(output[1], LinkMessage)
        self.assertEqual(output[1].type, 'link')
        self.assertEqual(output[1].from_user, 'laura')
        self.assertEqual(output[1].url, 'http://yo.text/message')

    def test_unknown_message(self):
        input = [{'type': 'some-unknown-type', 'from': 'aleem', 'to': 'laura', 'someProperty': 'aValue'}]
        output = messages_from_json(input)
        self.assertEqual(len(output), 1)
        self.assertIsInstance(output[0], UnknownMessage)
        self.assertEqual(output[0].type, 'some-unknown-type')
        self.assertEqual(output[0].from_user, 'aleem')
        self.assertEqual(output[0].to, 'laura')
        self.assertEqual(output[0].raw_message, input[0])
