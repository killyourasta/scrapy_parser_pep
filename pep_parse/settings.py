from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

RESULTS = 'results'
RESULTS_DIR = BASE_DIR / RESULTS

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ('pep_parse.spiders')
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

FILE_NAME = 'status_summary_{}.csv'
