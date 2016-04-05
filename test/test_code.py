from unittest import TestCase

from kik import Code


class KikCodeTest(TestCase):
    def test_from_json(self):
        code = Code.from_json({'id': 'ba7a319394f912ccad1ac42770529bd5cb0e9783'})
        self.assertEqual(code.id, 'ba7a319394f912ccad1ac42770529bd5cb0e9783')

    def test_url(self):
        code = Code('ba7a319394f912ccad1ac42770529bd5cb0e9783')
        self.assertEqual(code.url(), 'https://api.kik.com/v1/code/ba7a319394f912ccad1ac42770529bd5cb0e9783')
        self.assertEqual(code.url(color=Code.Colors.TURQUOISE),
                         'https://api.kik.com/v1/code/ba7a319394f912ccad1ac42770529bd5cb0e9783?c=1')
