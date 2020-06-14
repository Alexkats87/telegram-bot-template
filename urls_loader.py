
import requests
import re
from random import randint


USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
HEADERS = { 'User-Agent': USER_AGENT }


def get_jpg_urls_by_query(query):

    """

        Args:
            query: search term as of what is input to search box.
        Returns:
            (list): list of url for respective images.
 
    """

    query = query.replace(' ','+')
    url = 'https://www.google.com.sg/search?q={}&tbm=isch&tbs=sbd:0'.format(query) # last part is the sort by relv
 
    s = requests.Session()
    r = s.get(url, headers = HEADERS)
    raw_urls_list = re.findall('(https?://\S+)', r.text)
    jpg_urls_list = [u.split('\",')[0] for u in raw_urls_list if (".jpg\"," in u)]

    return jpg_urls_list


def filter_by_stop_list(url_list, stop_list):

    """
        Remove  stop_list's url-s from url_list
    """

    if len(stop_list) == 0:
        return url_list

    filtered_list = [url for url in url_list if (all(s not in url for s in stop_list ))]

    print("Removed urls count: {}".format(len(url_list) - len(filtered_list)))

    return filtered_list




def get_image_url(q_list):

    """
        Returns urls for every query from q_list

    """

    urls_list = []

    for q in q_list:
        cur_urls_list = get_jpg_urls_by_query(q)
        urls_list.extend(cur_urls_list)

    return urls_list
  


def get_urls_to_show(config):

    """
    
        Random selection N urls to show according to config

    """

    jpg_urls_list = get_image_url(config['query_list'])

    filtered_urls_list = filter_by_stop_list(url_list=jpg_urls_list, stop_list=config['stop_list'])

    url_list_to_show = [filtered_urls_list[randint(0, len(filtered_urls_list)-1)] for i in range(5)]

    return url_list_to_show



 ######################################################


if __name__ == '__main__':

    config = {'stop_list':['static.fjcdn', 'images-na'],
            'query_list':['cats'],
            'urls_count': 5}

    urls = get_urls_to_show(config)

    for i, u in enumerate(urls):
        print(i, u)
