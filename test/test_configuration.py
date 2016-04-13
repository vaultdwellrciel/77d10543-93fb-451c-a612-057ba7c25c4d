from unittest import TestCase

from kik import Configuration


class KikCodeTest(TestCase):
    def test_from_json(self):
        config = Configuration.from_json({
            'webhook': 'https://mybot.com/incoming',
            'features': {
                'manuallySendReadReceipts': True
            }
        })
        self.assertEqual(config.webhook, 'https://mybot.com/incoming')
        self.assertEqual(config.features, {'manuallySendReadReceipts': True})

    def test_to_json(self):
        config = Configuration(
            webhook='https://mybot.com/incoming',
            features={'manuallySendReadReceipts': True}
        )

        self.assertEqual(config.to_json(), {
            'webhook': 'https://mybot.com/incoming',
            'features': {
                'manuallySendReadReceipts': True
            }
        })

    def test_to_json_no_features(self):
        config = Configuration(
            webhook='https://mybot.com/incoming'
        )

        self.assertEqual(config.to_json(), {
            'webhook': 'https://mybot.com/incoming',
            'features': {}
        })
