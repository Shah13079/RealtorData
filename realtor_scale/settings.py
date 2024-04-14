# Scrapy settings for realtor_scale project

BOT_NAME = 'realtor_scale'

SPIDER_MODULES = ['realtor_scale.spiders']
NEWSPIDER_MODULE = 'realtor_scale.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
FEED_EXPORT_ENCODING = 'utf-8-sig'

CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16
DOWNLOAD_DELAY = 0.1
RETRY_HTTP_CODES = [502,500, 503, 504, 408, 429, 403]
RETRY_TIMES = 500

# Enable autothrottle to adjust crawling speed based on server responses
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10
AUTOTHROTTLE_TARGET_CONCURRENCY = 4

# Lower download timeout to reduce waiting time for unresponsive servers
DOWNLOAD_TIMEOUT = 80

# Disable cookies to avoid potential issues with session management
COOKIES_ENABLED = False



