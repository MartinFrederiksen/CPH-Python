import wget
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import os

class NotFoundException(ValueError):
    def __init__(self, *args, **kwargs):
        ValueError.__init__(self, *args, **kwargs)


class Module():
    def __init__(self, urlList):
        self.urlList = urlList
        self.files = []
        self.avgVowel = []

    def download(self, url, filename=None):
        try:
            wget.download(url, filename)
        except:
            raise NotFoundException('url returned 404')

    def multiDownload(self):
        def multithreading(func, args, workers=5):
            with ThreadPoolExecutor(workers) as ex:
                res = ex.map(func, args)
            return list(res)
        self.files = multithreading(self.download, self.urlList)

    def __iter__(self):
        self.idx = 0
        return self
    def __next__(self):
        cidx = self.idx
        self.idx += 1
        if cidx < len(self.urlList):
            return self.urlList[cidx]
        else:
            raise StopIteration

    def fileListGenerator(self):
        for name in self.urlList:
            yield name

    def avgVowels(self, text):
        return sum([*map(text.lower().count, "aeiouæøå")])/len(text.split())

    def hardestRead(self):
        texts = []
        names = []

        for url in self.urlList:
            names.append(url.split('/')[-1])
            with open(url.split('/')[-1], 'r') as file:
                texts.append(file.read())

        def multiprocessing(func, args, workers = os.cpu_count()):
            with ProcessPoolExecutor(workers) as ex:
                    res = ex.map(func, args)
            return dict(zip(names, res))
            
        result = multiprocessing(self.avgVowels, texts)
        resultSorted = {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}
        return (list(resultSorted.keys())[0], list(resultSorted.values())[0])
        