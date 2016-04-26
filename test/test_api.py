import json
from unittest import TestCase

import mock
import requests

from kik import KikApi, KikError, Code, Configuration, User
from kik.messages import TextMessage


def _response(status_code, content):
    response = requests.Response()
    response.status_code = status_code
    response._content = content
    return response


def requests_raise_func(method, url, *args, **kwargs):
    raise Exception('Must mock {} request to {}'.format(method.upper(), url))


class KikBotApiTest(TestCase):
    def setUp(self):
        super(KikBotApiTest, self).setUp()

        self.requests_mock = mock.patch('requests.api.request', wraps=requests_raise_func)
        self.requests_mock.start()

        self.api = KikApi('mybotusername', 'mybotapikey')

    def tearDown(self):
        super(KikBotApiTest, self).tearDown()

        self.requests_mock.stop()

    @mock.patch('requests.post', return_value=_response(200, json.dumps({}).encode('utf-8')))
    def test_send_messages(self, post):
        msgs = [TextMessage(to='aleem', body='Sometext')]

        response = self.api.send_messages(msgs)

        post_call = post.call_args
        self.assertEqual(post_call[0][0], 'https://api.kik.com/v1/message')
        self.assertEqual(post_call[1]['auth'], ('mybotusername', 'mybotapikey'))
        self.assertEqual(post_call[1]['timeout'], 60)
        self.assertEqual(post_call[1]['headers'], {'Content-Type': 'application/json'})
        self.assertEqual(json.loads(post_call[1]['data']), {
            'messages': [{
                'type': 'text',
                'to': 'aleem',
                'body': 'Sometext',
            }]
        })
        self.assertEqual(response, {})

    @mock.patch('requests.post', return_value=_response(200, json.dumps({}).encode('utf-8')))
    def test_broadcast_messages(self, post):
        msgs = [TextMessage(to='aleem', body='Sometext')]

        response = self.api.send_broadcast(msgs)

        post_call = post.call_args
        self.assertEqual(post_call[0][0], 'https://api.kik.com/v1/broadcast')
        self.assertEqual(post_call[1]['auth'], ('mybotusername', 'mybotapikey'))
        self.assertEqual(post_call[1]['timeout'], 60)
        self.assertEqual(post_call[1]['headers'], {'Content-Type': 'application/json'})
        self.assertEqual(json.loads(post_call[1]['data']), {
            'messages': [{
                'type': 'text',
                'to': 'aleem',
                'body': 'Sometext'
            }]
        })
        self.assertEqual(response, {})

    @mock.patch('requests.post', return_value=_response(400, json.dumps({'error': 'BadRequest'}).encode('utf-8')))
    def test_send_messages_failure(self, post):
        msgs = [TextMessage(to='aleem', body='Sometext')]

        self.assertRaises(KikError, self.api.send_messages, msgs)

    @mock.patch('requests.post', return_value=_response(400, json.dumps({'error': 'BadRequest'}).encode('utf-8')))
    def test_send_broadcast_failure(self, post):
        msgs = [TextMessage(to='aleem', body='Sometext')]

        self.assertRaises(KikError, self.api.send_broadcast, msgs)

    @mock.patch('requests.get', return_value=_response(200, json.dumps({
        'firstName': 'First',
        'lastName': 'Last',
        'profilePicUrl': 'http://foo.bar/profile',
        'profilePicLastModified': 1458657367
    }).encode('utf-8')))
    def test_get_user_profile(self, get):
        user = self.api.get_user('aleem')

        get.assert_called_once_with(
            'https://api.kik.com/v1/user/aleem',
            auth=('mybotusername', 'mybotapikey'),
            timeout=60
        )

        self.assertIsInstance(user, User)
        self.assertEqual(user.first_name, 'First')
        self.assertEqual(user.last_name, 'Last')
        self.assertEqual(user.profile_pic_url, 'http://foo.bar/profile')
        self.assertEqual(user.profile_pic_last_modified, 1458657367)

    @mock.patch('requests.get', return_value=_response(400, json.dumps({'error': 'BadRequest'}).encode('utf-8')))
    def test_get_user_profile_failure(self, get):
        self.assertRaises(KikError, self.api.get_user, 'aleem')

    @mock.patch('requests.post', return_value=_response(
        200, json.dumps({'id': 'ba7a319394f912ccad1ac42770529bd5cb0e9783'}).encode('utf-8')
    ))
    def test_create_kik_code(self, post):
        code = self.api.create_code({'akey': 'avalue'})

        post.assert_called_once_with(
            'https://api.kik.com/v1/code',
            timeout=60,
            auth=('mybotusername', 'mybotapikey'),
            headers={
                'Content-Type': 'application/json'
            },
            data=json.dumps({'data': '{"akey": "avalue"}'})
        )

        self.assertIsInstance(code, Code)
        self.assertEqual(code.id, 'ba7a319394f912ccad1ac42770529bd5cb0e9783')

    @mock.patch('requests.post', return_value=_response(
        200, json.dumps({'id': 'ba7a319394f912ccad1ac42770529bd5cb0e9783'}).encode('utf-8')
    ))
    def test_create_kik_code_no_data(self, post):
        code = self.api.create_code()

        post.assert_called_once_with(
            'https://api.kik.com/v1/code',
            timeout=60,
            auth=('mybotusername', 'mybotapikey'),
            headers={
                'Content-Type': 'application/json'
            },
            data='{}'
        )

        self.assertIsInstance(code, Code)
        self.assertEqual(code.id, 'ba7a319394f912ccad1ac42770529bd5cb0e9783')

    @mock.patch('requests.post', return_value=_response(400, json.dumps({'error': 'BadRequest'}).encode('utf-8')))
    def test_create_kik_code_failure(self, post):
        self.assertRaises(KikError, self.api.create_code, {'akey': 'avalue'})

    @mock.patch('requests.get', return_value=_response(200, json.dumps({
        'webhook': 'https://example.com/incoming',
        'features': {
            'manuallySendReadReceipts': True
        }
    }).encode('utf-8')))
    def test_get_configuration(self, get):
        config = self.api.get_configuration()

        get.assert_called_once_with(
            'https://api.kik.com/v1/config',
            timeout=60,
            auth=('mybotusername', 'mybotapikey')
        )

        self.assertEqual(config.webhook, 'https://example.com/incoming')
        self.assertEqual(config.features, {'manuallySendReadReceipts': True})

    @mock.patch('requests.post', return_value=_response(200, json.dumps({
        'webhook': 'https://example.com/incoming',
        'features': {
            'manuallySendReadReceipts': True
        }
    }).encode('utf-8')))
    def test_set_configuration(self, post):
        config = Configuration(
            webhook='https://example.com/incoming',
            features={'manuallySendReadReceipts': True}
        )

        response = self.api.set_configuration(config)

        self.assertEqual(post.call_count, 1)
        self.assertEqual(post.call_args[0][0], 'https://api.kik.com/v1/config')
        self.assertEqual(post.call_args[1]['timeout'], 60)
        self.assertEqual(post.call_args[1]['auth'], ('mybotusername', 'mybotapikey'))
        self.assertEqual(post.call_args[1]['headers'], {'Content-Type': 'application/json'})
        self.assertEqual(json.loads(post.call_args[1]['data']), {
            'webhook': 'https://example.com/incoming',
            'features': {
                'manuallySendReadReceipts': True
            }
        })

        self.assertIsInstance(response, Configuration)
        self.assertEqual(response.webhook, 'https://example.com/incoming')
        self.assertEqual(response.features, {'manuallySendReadReceipts': True})

    def test_verify_signature(self):
        self.assertTrue(self.api.verify_signature('AC18D0105C2C257652859322B0499313342C6EB9', b'body'))
        self.assertFalse(self.api.verify_signature('fakesig', b'body'))
