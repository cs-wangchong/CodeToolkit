'''
constants: constants used in Spiral splitters.
'''

common_suffix_numbers = {'16', '32', '64', '128', '256', '512', '1024'}
'''
List of numbers that are commonly put after some other strings, to form
symbols such as "int32", "float64", etc.
'''

# General principles for the following:
# 1. Only put in terms that at least one digit in them.
# 2. Avoid 2-character sequences, because they match too many things and
#    cause too many bad splits.
# 3. Stick to computing terms that many people use or have used, not stuff
#    that a particular program happens to use.
# 4. Generally, avoid packages for particular languages, like "urllib3".
#
# Sources for the following:
# - https://en.wikipedia.org/wiki/List_of_computing_and_IT_abbreviations
# - https://en.wikipedia.org/wiki/List_of_codecs
# - https://en.wikipedia.org/wiki/Comparison_of_video_codecs
# - the book 'The Definitivei Guide to iReport' by Toffoli, 2007
# - various lists and dictionaries of computing terms found by Googling
# - personal experience
 
common_terms_with_numbers = {
    '1st',
    '1to1',
    '2fa',
    '2nd',
    '2of7',
    '3d',
    '3of9',
    '3ivx',
    '3rd',
    '88k',
    'a52',
    'ac2',
    'ac3',
    'ada83',
    'ada95',
    'amd64',
    'asn1',
    'avs1',
    'avs2',
    'b2b',
    'b2c',
    'b2e',
    'b8zs',
    'base64',
    'bit7',
    'bzip2',
    'bz2',
    'c2a',
    'c3p0',
    'c4s',
    'cast5',
    'ciks1',
    'coconut98',
    'code128',
    'code128a',
    'code128b',
    'code128c',
    'code39',
    'color16',
    'color32',
    'com1',
    'com2',
    'com3',
    'com4',
    'crc32',
    'cvv2',
    'ddr2',
    'ddr3',
    'ddr4',
    'd2d',
    'd2d2t',
    'd3d',
    'db2',
    'db9',
    'des3',
    'ds0',
    'ds1',
    'ean128',
    'ean13',
    'e2e',
    'e3cp',
    'ec2',
    'f2f',
    'f95',
    'fat32',
    'float128',
    'float32',
    'float64',
    'float96',
    'fma99',
    'fs1015',
    'fs1016',
    'fs1023',
    'g711',
    'g718',
    'g719',
    'g721',
    'g722',
    'g723',
    'g726',
    'g728',
    'g729',
    'g729a',
    'g729d',
    'gtk3',
    'h261',
    'h262',
    'h263',
    'h264',
    'h265',
    'h323',
    'hdf5',
    'hi10p',
    'hi422p',
    'hi444pp',
    'hl7',
    'html3',
    'html4',
    'html40',
    'html5',
    'i10n',
    'i18n',
    'i2c',
    'i386',
    'ia32',
    'ia64',
    'id10t',
    'ie10',
    'ie11',
    'ie12',
    'ie13',
    'ie6',
    'ie7',
    'ie8',
    'ie9',
    'imap4',
    'int128',
    'int16',
    'int2of5',
    'int32',
    'int64',
    'int8',
    'jpa2',
    'ipv4',
    'ipv6',
    'ipv6cp',
    'iso[0-9]{2,}',
    'ix86',
    'j2ee',
    'j2me',
    'j2se',
    'java10',
    'java6',
    'java7',
    'java8',
    'java9',
    'jdk10',
    'jdk11',
    'jdk12',
    'jdk13',
    'jdk14',
    'jdk15',
    'jdk16',
    'jpeg2000',
    'koi8r',
    'l10n',
    'l2f',
    'l2s',
    'l2tp',
    'l2tp',
    'l3f',
    'l3s',
    'l3tp',
    'log10',
    'log2',
    'log4j',
    'lpt1',
    'lpt2',
    'lpt4',
    'lpt4',
    'md5',
    'md5sum',
    'mp3',
    'mp4',
    'mpeg1',
    'mpeg2',
    'mpeg25',
    'mpeg3',
    'mpeg4',
    'multi2',
    'ns3',
    'nw7',
    'o2o',
    'oauth1',
    'oauth2',
    'os10',
    'os11',
    'os12',
    'os13',
    'os7',
    'os8',
    'os9',
    'p2p',
    'p2sc',
    'p3p',
    'p4m',
    'pep8',
    'perl5',
    'pop3',
    'px64',
    'python2',
    'python3',
    'qt4',
    'r2d2',
    'rc5',
    'rc6',
    'rfc[0-9]{3,}',
    'rj11',
    'rj45',
    'rot13',
    'scc14shippingcode',
    'sha0',
    'sha1',
    'sha1024',
    'sha1sum',
    'sha224sum',
    'sha224',
    'sha256sum'
    'sha256',
    'sha384sum',
    'sha384',
    'sha512sum',
    'sha512',
    'sint16',
    'sint32',
    'sint64',
    'sint8',
    'sm4',
    'smb2',
    'socks4',
    'ss7',
    'sscc18',
    'std2of5',
    'sys32',
    'uint16',
    'uint32',
    'uint64',
    'uint8',
    'usd3',
    'usd4',
    'utf16',
    'utf32',
    'utf8',
    'v2p',
    'vc1',
    'vc3',
    'vcard3',
    'vcard4',
    'vp3',
    'vp4',
    'vp5',
    'vp6',
    'vp6e',
    'vp6s',
    'vp7',
    'vp8',
    'vp9',
    'w3af',
    'w3c',
    'win32',
    'win64',
    'windows7',
    'windows10',
    'windows11',
    'x11',
    'x11r4',
    'x11r5',
    'x11r6',
    'x208',
    'x209',
    'x21',
    'x214',
    'x215',
    'x216',
    'x217',
    'x219',
    'x224',
    'x225',
    'x226',
    'x227',
    'x229',
    'x25',
    'x264',
    'x265',
    'x28',
    'x29',
    'x3d',
    'x3j16',
    'x3t10',
    'x400',
    'x409',
    'x500',
    'x509',
    'x64',
    'x680',
    'x75',
    'x86',
    'xfree86',
    'xga2',
    'xml10',
    'xml11',
    'y2k',
}
'''
Set of common abbreviations and symbols that contain numbers. Entries can be
regular expressions.
'''

special_computing_terms = {
    'adware',
    'ascii',
    'autoexec',
    'autosave',
    'autocommit',
    'backend',
    'backlink',
    'backprop',
    'backreference',
    'barcode',
    'bboard',
    'bitblt',
    'bitbucket',
    'bitcoin',
    'bitmap',
    'blocklist',
    'bnf',
    'btree',
    'builtin',
    'bytecode',
    'bzip',
    'callback',
    'camelcase',
    'charset',
    'chipset',
    'cgi',
    'checkbox',
    'classpath',
    'copyleft',
    'crosshair',
    'dataflow',
    'datastore',
    'deadlock',
    'defragment',
    'denoise',
    'deprecated',
    'devop',
    'devops',
    'distro',
    'dns',
    'dram',
    'ebnf',
    'ecmascript',
    'eeprom',
    'embeddable',
    'esata',
    'exec',
    'ext',
    'facebook',
    'fifo',
    'fn',
    'fs',
    'github',
    'gmail',
    'gnupg',
    'groupware',
    'gzip',
    'hardwire',
    'hardwired',
    'hashmap',
    'hashset',
    'hmac',
    'hostname',
    'hyperscale',
    'inode',
    'instagram',
    'intel',
    'intra',
    'icq',
    'io',
    'ipfs',
    'iscsi',
    'itunes',
    'javabean',
    'javadoc',
    'javascript',
    'jdbc',
    'jmeter',
    'json',
    'jvm',
    'linker',
    'listserv',
    'llvm',
    'logon',
    'macos',
    'malware',
    'memoization',
    'metamodel',
    'microcode',
    'microkernel',
    'middleware',
    'millis',
    'mmx',
    'mpegts',
    'multipass',
    'multitasking',
    'msata',
    'nan',
    'ndn',
    'newline',
    'nvme',
    'online',
    'opcode',
    'opendocument',
    'overclock',
    'overclocked',
    'parallelizable',
    'petaflop',
    'petaflops',
    'phish',
    'phishing',
    'pickling',
    'prefill',
    'popup',
    'pos',
    'pseudocode',
    'ptr',
    'quickbasic',
    'quicktime',
    'refactoring',
    'regex',
    'req',
    'rmi',
    'scrollbar',
    'segfault',
    'shebang',
    'signedness',
    'socks',
    'sourceforge',
    'sunos',
    'str',
    'symlink',
    'sysop',
    'tarball',
    'thread',
    'throwable',
    'todo',
    'trackpad',
    'txt',
    'usec',
    'underclock',
    'voip',
    'warez',
    'worklist',
    'xml',
    'xterm',
    'xwindows',
    'zlib',
    # 2021/08/06: add identifiers
    'seperated',
    'seperator',
    'publickey',
    'privatekey',
    'instantiator',
    'abilities',
    'wikidata',
    'micro',
    'clob',
    'zxing',
    'securities'
}
'''
Terms that are not usually found in dictionaries, and should be considered
single words rather than split.  These tend to be specialized computing
terms, including terms that contain one or more dictionary words inside
them; for example, "checkbox" would in normal English be considered two
words, but has come to be accepted as a common neologism in computing.
Additional entries include very common abbreviations such as "str" which
are not found in dictionaries.
'''

# The following list of prefixes and suffixes started as the lists from the
# web page for Samurai, https://hiper.cis.udel.edu/Samurai/Samurai.html
#
# Enslen, E., Hill, E., Pollock, L., & Vijay-Shanker, K. (2009).
# Mining source code to automatically split identifiers for software analysis.
# In Proceedings of the 6th IEEE International Working Conference on Mining
# Software Repositories (MSR'09) (pp. 71-80).
#
# I made additions to the prefixes.

prefixes = {'afro', 'ambi', 'amphi', 'ana', 'anglo', 'apo', 'astro', 'bi',
            'bio', 'circum', 'cis', 'co', 'col', 'com', 'con', 'contra',
            'cor', 'cryo', 'crypto', 'de', 'de', 'demi', 'di', 'dif',
            'dis', 'du', 'duo', 'eco', 'electro', 'em', 'en', 'epi',
            'euro', 'ex', 'franco', 'geo', 'hemi', 'hetero', 'homo',
            'hydro', 'hypo', 'ideo', 'idio', 'il', 'im', 'infra', 'inter',
            'intra', 'ir', 'iso', 'macr', 'mal', 'maxi', 'mega', 'megalo',
            'micro', 'midi', 'mini', 'mis', 'mon', 'multi', 'neo', 'omni',
            'paleo', 'para', 'ped', 'peri', 'poly', 'pre', 'preter',
            'proto', 'pyro', 're', 'retro', 'semi', 'socio', 'supra',
            'sur', 'sy', 'syl', 'sym', 'syn', 'tele', 'trans', 'tri',
            'twi', 'ultra', 'un', 'uni', 'non'}

suffixes = {'a', 'ac', 'acea', 'aceae', 'acean', 'aceous', 'ade', 'aemia',
            'agogue', 'aholic', 'al', 'ales', 'algia', 'amine', 'ana',
            'anae', 'ance', 'ancy', 'androus', 'andry', 'ane', 'ar',
            'archy', 'ard', 'aria', 'arian', 'arium', 'ary', 'ase',
            'athon', 'ation', 'ative', 'ator', 'atory', 'biont', 'biosis',
            'cade', 'caine', 'carp', 'carpic', 'carpous', 'cele', 'cene',
            'centric', 'cephalic', 'cephalous', 'cephaly', 'chory',
            'chrome', 'cide', 'clast', 'clinal', 'cline', 'coccus',
            'coel', 'coele', 'colous', 'cracy', 'crat', 'cratic',
            'cratical', 'cy', 'cyte', 'derm', 'derma', 'dermatous', 'dom',
            'drome', 'dromous', 'eae', 'ectomy', 'ed', 'ee', 'eer', 'ein',
            'eme', 'emia', 'en', 'ence', 'enchyma', 'ency', 'ene', 'ent',
            'eous', 'er', 'ergic', 'ergy', 'es', 'escence', 'escent',
            'ese', 'esque', 'ess', 'est', 'et', 'eth', 'etic', 'ette',
            'ey', 'facient', 'fer', 'ferous', 'fic', 'fication', 'fid',
            'florous', 'foliate', 'foliolate', 'fuge', 'ful', 'fy',
            'gamous', 'gamy', 'gen', 'genesis', 'genic', 'genous', 'geny',
            'gnathous', 'gon', 'gony', 'grapher', 'graphy', 'gyne',
            'gynous', 'gyny', 'ia', 'ial', 'ian', 'iana', 'iasis',
            'iatric', 'iatrics', 'iatry', 'ibility', 'ible', 'ic',
            'icide', 'ician', 'ick obsolete', 'ics', 'idae', 'ide', 'ie',
            'ify', 'ile', 'ina', 'inae', 'ine', 'ineae', 'ing', 'ini',
            'ious', 'isation', 'ise', 'ish', 'ism', 'ist', 'istic',
            'istical', 'istically', 'ite', 'itious', 'itis', 'ity', 'ium',
            'ive', 'ization', 'ize', 'kinesis', 'kins', 'latry', 'lepry',
            'ling', 'lite', 'lith', 'lithic', 'logue', 'logist', 'logy',
            'ly', 'lyse', 'lysis', 'lyte', 'lytic', 'lyze', 'mancy',
            'mania', 'meister', 'ment', 'merous', 'metry', 'mo', 'morph',
            'morphic', 'morphism', 'morphous', 'mycete', 'mycetes',
            'mycetidae', 'mycin', 'mycota', 'mycotina', 'ness', 'nik',
            'nomy', 'odon', 'odont', 'odontia', 'oholic', 'oic', 'oid',
            'oidea', 'oideae', 'ol', 'ole', 'oma', 'ome', 'ont', 'onym',
            'onymy', 'opia', 'opsida', 'opsis', 'opsy', 'orama', 'ory',
            'ose', 'osis', 'otic', 'otomy', 'ous', 'para', 'parous',
            'pathy', 'ped', 'pede', 'penia', 'phage', 'phagia', 'phagous',
            'phagy', 'phane', 'phasia', 'phil', 'phile', 'philia',
            'philiac', 'philic', 'philous', 'phobe', 'phobia', 'phobic',
            'phony', 'phore', 'phoresis', 'phorous', 'phrenia', 'phyll',
            'phyllous', 'phyceae', 'phycidae', 'phyta', 'phyte',
            'phytina', 'plasia', 'plasm', 'plast', 'plasty', 'plegia',
            'plex', 'ploid', 'pode', 'podous', 'poieses', 'poietic',
            'pter', 'rrhagia', 'rrhea', 'ric', 'ry', 's', 'scopy',
            'sepalous', 'sperm', 'sporous', 'st', 'stasis', 'stat',
            'ster', 'stome', 'stomy', 'taxy', 'th', 'therm', 'thermal',
            'thermic', 'thermy', 'thon', 'thymia', 'tion', 'tome', 'tomy',
            'tonia', 'trichous', 'trix', 'tron', 'trophic', 'tropism',
            'tropous', 'tropy', 'tude', 'ty', 'ular', 'ule', 'ure',
            'urgy', 'uria', 'uronic', 'urous', 'valent', 'virile',
            'vorous', 'xor', 'y', 'yl', 'yne', 'zoic', 'zoon', 'zygous',
            'zyme'}
