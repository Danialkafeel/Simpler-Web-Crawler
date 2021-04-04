import csv
from bs4 import BeautifulSoup as sp
from urllib.request import urlopen
import sys

pages = ["https://www.amazon.in/gp/bestsellers/books/","https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_2?ie=UTF8&pg=2"]

with open('output/in_book.csv','w',newline='') as out_file:	
	csvwriter = csv.writer(out_file, delimiter=";")
	row = ["Name","URL","Author","Price","Number of Ratings","Average Ratings"]
	csvwriter.writerow(row)
	for amz_url in pages:
		print("Yo")
		url_client = urlopen(amz_url)
		full_html = url_client.read()
		parsed_html = sp(full_html,"html.parser")
		url_client.close()
		books = parsed_html.findAll("span",{"class":"aok-inline-block zg-item"})
		print(len(books))
		# print(books)
		# break
		for book in books:
			# print(book.prettify())
			# sys.exit()
			try:
				title = book.find("div",{"class":"p13n-sc-truncate p13n-sc-line-clamp-1"}).string.strip()
			except AttributeError:
				title = "Not available"
			try:
				prefix = "https://www.amazon.in"
				b_url = book.find("a",href=True)
				b_url = b_url['href']
				b_url = prefix + b_url
			except AttributeError:
				b_url = "Not available"
			
			try:
				author = book.find("a",{"class":"a-size-small a-link-child"}).string.strip()
			except AttributeError:
				author = "Not available"
			try:
				price = book.find("span",{"class":"p13n-sc-price"}).string.strip()
			except AttributeError:
				price = "Not available"

			try:
				num_ratings = book.find("a",{"class":"a-size-small a-link-normal"}).string.strip()
			except AttributeError:
				num_ratings = "Not available"

			try:
				avg_ratings = book.find("span",{"class":"a-icon-alt"}).string.strip()
			except AttributeError:
				avg_ratings = "Not available"

			row = [title,b_url,author,price,num_ratings,avg_ratings]
			csvwriter.writerow(row)
			# print(title," ; ",b_url," ; ",author," ; ",price," ; ",avg_ratings," ; ",num_ratings)

print("Done!")

