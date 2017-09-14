from distutils.core import setup
from subprocess import call
from getpass import getuser


files =      [('/usr/share/theTranslator/translateapi',['translateapi/translator.py','translateapi/supportLanguage.py']),
              ('/usr/share/theTranslator/icon',['icon/magnifying.png','icon/america_flag.png','icon/fullscreen.png','icon/google_translate.png','icon/reload.png','icon/loading.gif','icon/more_translation.png','icon/reset_icon.png','icon/speak_icon.png','icon/syria_flag.png','icon/translate_icon.png','icon/upload.png','icon/yandex.png']),
              ('/usr/share/theTranslator/translate',['translate/Arabic.qm','translate/Arabic.ts']),
              ('/usr/share/theTranslator/ui',['ui/langDetect.ui','ui/license.ui','ui/mainUi.ui','ui/moreTranslationWindow.ui','ui/settings.ui']),
              ('/usr/share/theTranslator/widgets',['widgets/settingsWidget.py']),
              ('/usr/share/theTranslator/docs',['LICENSE']),
              ('/usr/share/theTranslator/',['version.txt']),
              ('/usr/share/pixmaps',['icon/translate_icon.png']),
              ('/usr/share/applications',['theTranslator.desktop'])
]



setup(name = "theTranslator",
      version = "0.1",
      description = "Translate your text with many amazing features",
      long_description = """A lightweight translator with many useful features such as file translation, translation and text translation, and many translation results.
Some of the advantages of the project:
1- Reading the translation results
2. Translation of text files
3. Save translation results
4 - Translation using more than one online translator
Another advantage of the project is that it does not require a lot of dependencies""",
      author = "Ahmad Nourallah",
      maintainer = "Ahmad Nourallah",
      author_email = "ahmadnurallah@gmail.com",
      maintainer_email = "ahmadnurallah@gmail.com",
      url = "https://github.com/ahmadnourallah/theTranslator",
      license='GPLv3',
      scripts=['theTranslator'],
      data_files=files
)
