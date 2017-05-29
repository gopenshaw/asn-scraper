import urllib2
import bs4

def fun():
    print('hey')

def url_to_soup(url):
    # bgp.he.net filters based on user-agent.
    req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
    html = urllib2.urlopen(req).read()
    soup = bs4.BeautifulSoup(html)
    return soup

def get_asn_country_urls():
    ''' Return list of url strings '''
    base_url = 'http://bgp.he.net'
    world_asn_url = base_url + '/report/world'
    world_asn = url_to_soup(world_asn_url)
    country_table = world_asn.findAll('table')
    if len(country_table) > 1:
        raise RuntimeError('More than one table at {}'.format(
            world_asn_url))
    country_a_tags = country_table[0].findAll('a')
    country_urls = [base_url + c.get('href') for c in country_a_tags]
    return country_urls

def get_asns_from_country(asn_country_url):
    asn_country = url_to_soup(asn_country_url)
    asn_table = asn_country.findAll('table')
    if len(asn_table) > 1:
        raise RuntimeError('More than one table at {}'.format(
            asn_country_url))
    asn_tr_tags = asn_table[0].findAll('tr')
    asn_tr_tags = asn_tr_tags[1:] # remove headers
    # TODO get real country code
    asns = [build_asn_from_tag(a, 'US') for a in asn_tr_tags]
    return asns

def build_asn_from_tag(asn_tr_tag, country_code):
    tds = asn_tr_tag.findAll('td')
    asn_number = tds[0].getText().strip('AS')
    name = tds[1].getText()
    v4_routes = tds[3].getText()
    v6_routes = tds[5].getText()
    return (asn_number, {'Country': country_code,
        'Name': name, 'Routes v4': v4_routes, 'Routes v6': v6_routes})
    
