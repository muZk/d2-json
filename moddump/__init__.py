import glob

__version__ = '0.8'
__locales__ = glob.glob('moddump/locales/*.json')

from . import dump
from . import heroes
from . import addon