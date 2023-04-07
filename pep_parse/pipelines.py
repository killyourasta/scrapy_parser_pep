import csv
import datetime as dt
from pathlib import Path

from itemadapter import ItemAdapter

from .settings import DATETIME_FORMAT, FILE_NAME

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.__status_vocabulary = {}

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('status'):
            pep_status = adapter['status']
            self.__status_vocabulary[pep_status] = (
                self.__status_vocabulary.get(pep_status, 0) + 1
            )
            return item

    def close_spider(self, spider):
        # tests\test_main.py:17: AttributeError
        RESULTS_DIR = BASE_DIR / 'results'
        RESULTS_DIR.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_format = now.strftime(DATETIME_FORMAT)
        filename = FILE_NAME.format(now_format)
        with open(RESULTS_DIR / filename, mode='w', encoding='utf-8') as f:
            csv.writer(
                f, dialect=csv.unix_dialect, quoting=csv.QUOTE_NONE
            ).writerows(
                (
                    ("Статус", "Колличество"),
                    *self.__status_vocabulary.items(),
                    ("Total", sum(self.__status_vocabulary.values()))
                )
            )
