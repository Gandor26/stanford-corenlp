import zipfile
import os, sys, glob
from urllib import request

version = '2017-06-09'

def download_lib(directory):
    url = 'http://nlp.stanford.edu/software/stanford-corenlp-full-%s.zip' % version
    filepath, _ = request.urlretrieve(url, directory+'corenlp.zip')
    arxiv = zipfile.ZipFile(filepath)
    arxiv.extractall(directory)
    folder = arxiv.namelist()[0]
    for ff in os.listdir(directory+folder):
        os.rename(directory+folder+ff, directory+ff)
    os.rmdir(directory+folder)

def download_model(directory, lang):
    directory = os.path.abspath(directory)+os.path.sep
    if len(glob.glob(directory+'stanford-corenlp-[0-9].[0-9].[0-9].jar')) <= 0:
        download_lib(directory)
    lang_dict = {'en': 'english',
                'en-kbp': 'english-kbp',
                'zh': 'chinese',
                'ar': 'arabic',
                'fr': 'french',
                'de': 'german',
                'es': 'spanish'}
    filename = 'stanford-%s-corenlp-%s-models.jar' % (lang_dict[lang], version)
    url = 'http://nlp.stanford.edu/software/%s' % (filename)
    file_path, _ = request.urlretrieve(url, directory+filename)
    return file_path

