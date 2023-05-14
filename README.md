# Web-Scrapping using Beautifulsoup

Projek ini dikembangkan sebagai salah satu capstone project dari Algoritma Academy Data Analytics Specialization. Deliverables yang diharapkan dari projek ini adalah melakukan simple webscrapping untuk mendapatkan informasi. Untuk step by step guide, Bapak Ibu dipersilahkan untuk membuka git saya [Click here](https://github.com/t3981-h/Webscrapping-with-BeautifulSoup "Webscrapping with Beautiful Soup"). Kita juga akan memanfaatkan flask dashboard sederhana untuk menampilkan hasil scrap dan visualisasi kita.

## Dependencies

- beautifulSoup4
- pandas
- flask
- matplotlib

Library yang diperlukan dapat di install dengan requirements2.txt sebagaimana environments yang digunakan yaitu vulcan_da atau minimal dengan requirements.txt dengan cara berikut

```python
pip install -r requirements.txt
```

## Rubics

- Environment preparation (2 points)
- Finding the right key to scrap the data  & Extracting the right information (5 points)
- Creating data frame & Data wrangling (5 points)
- Creating a tidy python notebook as a report. (2 points)
- Implement it on flask dashboard (2 points)


## What Need to Do

* Scraping soal di bawah menggunakan `beautiful soup` di notebook terlebih dahulu.
* Dapat melakukan -clone repo ini.
* Melengkapi code Skeletone pada notebook termasuk mengisi background dan Kesimpulan serta analisa
* Membuat flask dashboard sederhana.

```python
table = soup.find(___)
tr = table.find_all(___)
```

* Isi bagian ini untuk menyimpan hasil scrap  menjadi sebuah dataframe.

```python
df = pd.DataFrame(name of your tupple, columns = (name of the columns))
```

* Terakhir menggunakan fungsi `scrap` dengan cara mengisi bagian berikut dengan link web yang Bapak/Ibu scrap.

```python
df = scrap(___) #insert url here
```

* Bermain dengan UI nya pada `index.html` serta mengikuti comment yang ada untuk mengetahui bagian mana yang dapat diubah. 

### The Final Mission

Pada captsone kali ini, soal yang dikerjakan adalah :

Data kurs US Dollar ke rupiah dari `https://www.exchange-rates.org/history/IDR/USD/T`

    * `harga harian`, dan `tanggal`
    * plot pergerakan kurs USD 
    * plot frekuensi/sebaran kurs USD (extra challenge)
    

Happy learning! 
