'''
mapping ISO 639_1/2 language Codes, used by Googel Trnaslate v3 API, to corresponding ISO 639_3 Codes for maximum
 coverage for both by GlotLID and the WALS library.   
'''
CUSTOM_MAPPING = {
    'fil': 'tgl',  # Filipino (Tagalog)
    'tl': 'tgl',  # Tagalog (Filipino)
    'sm': 'smo',  # Samoan
    'mk': 'mkd',  # Macedonian
    'gu': 'guj',  # Gujarati
    'haw': 'haw',  # Hawaiian
    'fi': 'fin',  # Finnish
    'mn': 'mon',  # Mongolian
    'bm': 'bam',  # Bambara
    'ta': 'tam',  # Tamil
    'ur': 'urd',  # Urdu
    'nso': 'nso',  # Sepedi
    'mni-Mtei': 'mni',  # Meiteilon (Manipuri)
    'hy': 'hye',  # Armenian
    'nl': 'nld',  # Dutch
    'tk': 'tuk',  # Turkmen
    'en': 'eng',  # English
    'bg': 'bul',  # Bulgarian
    'gd': 'gla',  # Scots Gaelic
    'pt': 'por',  # Portuguese (Portugal, Brazil)
    'ko': 'kor',  # Korean
    'kri': 'kri',  # Krio
    'ga': 'gle',  # Irish
    'eu': 'eus',  # Basque
    'sv': 'swe',  # Swedish
    'bs': 'bos',  # Bosnian
    'co': 'cos',  # Corsican
    'fr': 'fra',  # French
    'gn': 'gug',  # Guarani
    'doi': 'dgo',  # Dogri
    'ro': 'ron',  # Romanian
    'it': 'ita',  # Italian
    'dv': 'div',  # Dhivehi
    'ku': 'ckb',  # Kurdish
    'ckb': 'ckb',  # Kurdish (Sorani)
    'ak': 'aka',  # Twi (Akan)
    'eo': 'epo',  # Esperanto
    'bho': 'bho',  # Bhojpuri
    'zu': 'zul',  # Zulu
    'id': 'ind',  # Indonesian
    'gom': 'knn',  # Konkani
    'te': 'tel',  # Telugu
    'sl': 'slv',  # Slovenian
    'lv': 'lav',  # Latvian
    'ceb': 'ceb',  # Cebuano
    'pa': 'pan',  # Panjabi
    'ru': 'rus',  # Russian
    'si': 'sin',  # Sinhala (Sinhalese)
    'ee': 'ewe',  # Ewe
    'yi': 'ydd',  # Yiddish
    'ilo': 'ilo',  # Ilocano
    'ny': 'nya',  # Nyanja (Chichewa)
    'az': 'azb',  # Azerbaijani
    'mai': 'mai',  # Maithili
    'sw': 'swh',  # Swahili
    'hi': 'hin',  # Hindi
    'mt': 'mlt',  # Maltese
    'sr': 'hbs',  # Serbian
    'hr': 'hbs',  # Croatian
    'ka': 'kat',  # Georgian
    'ug': 'uig',  # Uyghur
    'tt': 'tat',  # Tatar
    'lg': 'lug',  # Luganda
    'kn': 'kan',  # Kannada
    'fy': 'fry',  # Frisian
    'kk': 'kaz',  # Kazakh
    'ca': 'cat',  # Catalan
    'lb': 'ltz',  # Luxembourgish
    'jw': 'jav',  # Javanese
    'jv': 'jav',  # Javanese alternativ
    'et': 'ekk',  # Estonian
    'la': 'lat',  # Latin
    'tr': 'tur',  # Turkish
    'ps': 'pst',  # Pashto
    'km': 'khm',  # Khmer
    'zh-TW': 'zho',  # Chinese (Traditional) ################ NO CLEAR ISO CODE
    'zh': 'zho',  # Chinese (Simplified) ################### NO CLEAR ISO CODE
    'zh-CN': 'zho',  # Chinese (Simplified) alternativ #################### NO CLEAR ISO CODE
    'uk': 'ukr',  # Ukrainian
    'as': 'asm',  # Assamese
    'he': 'heb',  # Hebrew
    'iw': 'heb',  # Hebrew alternativ
    'yo': 'yor',  # Yoruba
    'sq': 'sqi',  # Albanian
    'da': 'dan',  # Danish
    'gl': 'glg',  # Galician
    'vi': 'vie',  # Vietnamese
    'ay': 'ayr',  # Aymara
    'is': 'isl',  # Icelandic
    'ln': 'lin',  # Lingala
    'mr': 'mar',  # Marathi
    'st': 'sot',  # Sesotho
    'xh': 'xho',  # Xhosa
    'cs': 'ces',  # Czech
    'ky': 'kir',  # Kyrgyz
    'ml': 'mal',  # Malayalam
    'ht': 'hat',  # Haitian Creole
    'mi': 'mri',  # Maori
    'so': 'som',  # Somali
    'uz': 'uzn',  # Uzbek
    'lus': 'lus',  # Mizo
    'el': 'ell',  # Greek
    'ti': 'tir',  # Tigrinya
    'be': 'bel',  # Belarusian
    'cy': 'cym',  # Welsh
    'am': 'amh',  # Amharic
    'ig': 'ibo',  # Igbo
    'or': 'ory',  # Odia (Oriya)
    'fa': 'pes',  # Persian
    'ms': 'zsm',  # Malay
    'su': 'sun',  # Sundanese
    'de': 'deu',  # German
    'lo': 'lao',  # Lao
    'ha': 'hau',  # Hausa
    'ts': 'tso',  # Tsonga
    'om': 'gaz',  # Oromo
    'ar': 'arb',  # Arabic
    'my': 'mya',  # Myanmar (Burmese)
    'es': 'spa',  # Spanish
    'hmn': 'mww',  # Hmong
    'qu': 'quh',  # Quechua
    'no': 'nor',  # Norwegian
    'th': 'tha',  # Thai
    'sa': 'san',  # Sanskrit
    'mg': 'plt',  # Malagasy
    'pl': 'pol',  # Polish
    'sd': 'snd',  # Sindhi
    'sk': 'slk',  # Slovak
    'bn': 'ben',  # Bengali
    'rw': 'kin',  # Kinyarwanda
    'af': 'afr',  # Afrikaans
    'ne': 'npi',  # Nepali
    'lt': 'lit',  # Lithuanian
    'tg': 'tgk',  # Tajik
    'ja': 'jpn',  # Japanese
    'sn': 'sna',  # Shona
    'hu': 'hun',  # Hungarian
}