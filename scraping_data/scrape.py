from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

url = input("Masukkan URL toko disini : ")

if url :
  options = webdriver.ChromeOptions()
  options.add_argument("--start-maximized")
  driver = webdriver.Chrome(options=options)
  driver.get(url)

  data = []
  for i in range(0, 3):
    soup = BeautifulSoup(driver.page_source, "html.parser")
    containers = soup.findAll('article', attrs={'class':'css-1pr2lii'})

    for container in containers:
      try:
        review_r = container.find('span', attrs={'data-testid':'lblItemUlasan'}).text
        name = container.find('p', attrs={'class':'css-akhxpb-unf-heading e1qvo2ff8'}).text
        rating_e = container.find('div', attrs={'data-testid':'icnStarRating'})

        # ,Unnamed: 0,Ulasan,Rating,Kategori,Nama Produk,Id Produk,Terjual,Id_Toko,Url,label

        # PERBAIKAN KATA-KATA DARI ULASAN 
        review = review_r.replace('\n', ' ').replace('\r', ' ')
        review = " ".join(review.split())

        # PENCARIAN ANGKA RATING
        if rating_e:
          rating_r = rating_e.get('aria-label', '0')
          rating = rating_r.replace('bintang', '').strip()

        else:
          rating = "0"

        data.append(
          ({
            'Nama': name,
            'Ulasan': review,
            'Rating': rating
          })
        )
      except AttributeError:
        continue

    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button[aria-label^='Laman berikutnya']").click()
    time.sleep(3)

  print(data)
  df = pd.DataFrame(data, columns=["Nama", "Ulasan", "Rating"])
  df.to_csv("tokped.csv", index=True)