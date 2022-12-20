import logging
logging.basicConfig(level = logging.DEBUG)

from codetoolkit.delimiter import Delimiter

if __name__ == "__main__":

    print(Delimiter.split_camel("codepoint"))
    print(Delimiter.split_camel("makelayer"))
    print(Delimiter.split_camel("dealwithread"))