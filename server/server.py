import pusher
from yandex_translate import YandexTranslate


pusher_client = pusher.Pusher(
  app_id='',
  key='',
  secret='',
  cluster='eu',
  ssl=True
)

yandex_api = "" # yandex translate API key here

translate = YandexTranslate(yandex_api)

from_lang = raw_input("Select the source language (e.g. en): ")
to_lang = raw_input("Select the target language (e.g. fr): ")

gen = from_lang.lower()+"-"+to_lang.lower()

print "Set source lang: {} | target lang: {}".format(from_lang, to_lang)

while True:
	text = raw_input("Enter a phrase to translate: ")
	if text == "stop":
		break
	translated = translate.translate(text, gen)
	pusher_client.trigger('test_channel', 'my_event', {'message': translated.get("text")[0]})

print "Session complete."
