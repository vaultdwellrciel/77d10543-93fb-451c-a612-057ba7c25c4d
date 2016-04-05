.. _api:

API Documentation
=================

API Client
----------

Client for interacting with the Kik API.

.. autoclass:: kik.KikApi
   :members:

User Model
----------

Model for working with user profiles

.. autoclass:: kik.User
   :members:

Code Model
----------

Model for working with Kik Codes

.. autoclass:: kik.Code
   :members:

Configuration Model
-------------------

Model for working with your bot's configuration.

.. autoclass:: kik.Configuration
   :members:

Messages
--------

These classes directly mirror the `message types used by the API <https://dev.kik.com/#/docs/messaging#message-formats>`_.

.. autoclass:: kik.messages.Message

.. autoclass:: kik.messages.TextMessage

.. autoclass:: kik.messages.LinkMessage

.. autoclass:: kik.messages.PictureMessage

.. autoclass:: kik.messages.VideoMessage

.. autoclass:: kik.messages.StartChattingMessage

.. autoclass:: kik.messages.ScanDataMessage

.. autoclass:: kik.messages.StickerMessage

.. autoclass:: kik.messages.IsTypingMessage

.. autoclass:: kik.messages.ReceiptMessage

.. autoclass:: kik.messages.DeliveryReceiptMessage

.. autoclass:: kik.messages.ReadReceiptMessage

.. autoclass:: kik.messages.UnknownMessage

Message Utilities
-----------------

.. autofunction:: kik.messages.messages_from_json

Attribution
-----------

.. autoclass:: kik.messages.attribution.Attribution

.. autoclass:: kik.messages.CustomAttribution
   :members:
   :show-inheritance:

.. autoclass:: kik.messages.attribution.PresetAttribution
   :members:
   :show-inheritance:

.. autoclass:: kik.messages.attribution.PresetAttributions
   :members:

.. autoclass:: kik.messages.attributable_message.AttributableMessage

Keyboards and Responses
-----------------------

.. autoclass:: kik.messages.keyboards.Keyboard

.. autoclass:: kik.messages.SuggestedResponseKeyboard
   :members:
   :show-inheritance:

.. autoclass:: kik.messages.responses.SuggestedResponse

.. autoclass:: kik.messages.TextResponse
   :members:
   :show-inheritance:

.. autoclass:: kik.messages.keyboard_message.KeyboardMessage

Exceptions
----------

.. autoexception:: kik.KikError
