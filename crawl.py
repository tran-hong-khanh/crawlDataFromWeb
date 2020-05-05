import bs4
import pandas
import requests

url = 'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating%27' # các bạn thay link của trang mình cần lấy dữ liệu tại đây
def get_page_content(url):
   page = requests.get(url,headers={"Accept-Language":"en-US"})
   return bs4.BeautifulSoup(page.text,"html.parser")
soup = get_page_content(url)

movies = soup.findAll('h3', class_='lister-item-header')
titles = [movie.find('a').text for movie in movies]
release = [rs.find('span',class_="lister-item-year text-muted unbold").text for rs in movies]
certificate = [ce.text for ce in soup.findAll('span',class_='certificate')]
runtime = [rt.text for rt in soup.findAll('span',class_='runtime')]
genre = [gr.text for gr in soup.findAll('span',class_="genre")]
rates = [rate['data-value'] for rate in soup.findAll('div',class_='inline-block ratings-imdb-rating')]


df = pandas.DataFrame.from_dict({'titles':titles, 
                  'release':release, 
                  'certificate':certificate,
                  'runtime':runtime,
                  'genre': genre,
                  'rates': rates}, orient='index')

lendf = len(dict(df))

from prettytable import PrettyTable
tb = PrettyTable()
tb.field_names = ["id","titles", "release", "certificate", "runtime", "genre", "rates"]
for x in range(lendf):
	tb.add_row([x,dict(df)[x]["titles"],dict(df)[x]["release"],dict(df)[x]["certificate"],dict(df)[x]["runtime"],dict(df)[x]["genre"],dict(df)[x]["rates"]])

print(tb)





