import coverage

cov = coverage.Coverage()
cov.start()
import modules.web.get_site
from modules.web.get_site import get_site
response = get_site('http://my-test-site.com')
cov.stop()
cov.save()
cov.html_report()
