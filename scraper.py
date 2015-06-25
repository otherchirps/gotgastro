# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("http://www.foodauthority.nsw.gov.au/penalty-notices/default.aspx?template=results&searchname=Added%20this%20month&inthelast=31")
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)

for tr in root.cssselect("#myTable tr"):
    td = tr.findall("td")
    if td is None or len(td) == 0:
        continue
    #import pdb; pdb.set_trace()
    record={}
    record["penaltynotice"]=td[3].text_content()
    record["tradename"]=td[0].text_content()
    record["suburb"]=td[1].text_content()
    scraperwiki.sqlite.save(unique_keys=['penaltynotice'], data=record)

