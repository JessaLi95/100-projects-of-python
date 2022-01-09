from bs4 import BeautifulSoup
import requests

############## 100 best movies list ###################
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best"
                        "-movies-2/")
empire_100_mov_page = response.text
soup = BeautifulSoup(empire_100_mov_page, "html.parser")
title = [title.getText() for title in soup.find_all(name="h3", class_="title")[::-1]]
intro = [intro.getText() for intro in soup.find_all(name="p", class_="description")[::-1]]

with open('100-best-movies.txt', 'w') as f:
    for i in range(100):
        f.write(title[i])
        f.write('\n')
        f.write(intro[i])
        f.write('\n')


################ Extract from ycombinator #############
# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text
# soup = BeautifulSoup(yc_web_page, "html.parser")
# news_title = soup.select(".titlelink")
# title = []
# link = []
# records = []
# for tags in news_title:
#     title.append(tags.getText())
#     link.append(tags.get("href"))
#
# score = [int(vote_point.getText().split(" ")[0]) for vote_point in soup.select(".score")]
# record_dic = {"title": title, "link": link, "score": score}
#
# max_index = score.index(max(score))
# print(record_dic["title"][max_index], record_dic["link"][max_index], record_dic["score"][max_index])



################ Beautiful Soup essential ################
# # import lxml
# with open("website.html") as files:
#     contents = files.read()
#
# soup = BeautifulSoup(contents, "html.parser")   # Or lxml
# print(soup.title)
# print(soup.title.string)    # Title of the website
# print(soup.prettify())  # Indented html
# print(soup.a)   # First anchor
# all_anchor_tags = soup.find_all(name="a")   # p
# print(all_anchor_tags)
# for tags in all_anchor_tags:
#     print(tags.getText())   # Get the string of anchor
#     print(tags.get("href"))  # Get the link of anchor
#
# heading = soup.find(name="h1", id="name")   # Get specific h1
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText(), section_heading.name, section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")   # Locate to an Anchor inside a Paragraph
# print(company_url)
#
# company_name = soup.select_one(selector="#name")    # Use "#" to specify ID
# print(company_name)
#
# heading_class = soup.select(selector=".heading")    # Use "." to specify Class
# print(heading_class)