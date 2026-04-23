# Orders Review Score Regression Analysis

##  Proje Amacı

Bu projede, e-ticaret sipariş verileri üzerinden müşteri memnuniyetini temsil eden **`review_score`** değişkenini analiz ettik.
Amaç, teslimat süresi ve gecikmenin müşteri puanı üzerindeki etkisini incelemek ve istatistiksel olarak yorumlamaktır.

---

#  Kullanılan Veri Seti

* `orders.csv`
* `order_reviews.csv`

Bu veri setleri birleştirilerek analiz için uygun hale getirilmiştir.

---

##  Kullanılan Teknolojiler

* Python
* Pandas
* NumPy
* Seaborn & Matplotlib
* Statsmodels (OLS Regression)
* Scikit-learn (Standardization)

---

##  Analiz Adımları

### 1️ Veri Hazırlama

* Sipariş ve review verileri birleştirildi
* Tarih değişkenlerinden:

  * `wait_time`
  * `delay_vs_expected`
    türetildi
* Eksik veriler temizlendi

---

### 2️ Keşifsel Veri Analizi (EDA)

* Korelasyon matrisi incelendi
* `review_score` ile:

  * `wait_time` → negatif ilişki
  * `delay_vs_expected` → negatif ilişki

 Ayrıca bu iki değişkenin kendi aralarında **yüksek korelasyon** gösterdiği gözlemlendi (~0.69)

---

### 3️ Tek Değişkenli Regresyon

#### Model 1:

```
review_score ~ wait_time
```

#### Model 2:

```
review_score ~ delay_vs_expected
```

 Sonuç:

* Her iki değişken de müşteri puanını negatif etkiler
* Gecikmenin etkisi daha güçlüdür

---

### 4️ Çok Değişkenli Regresyon

```
review_score ~ wait_time + delay_vs_expected
```

 Bulgular:

* `delay_vs_expected` daha baskın değişken olarak öne çıkar
* `wait_time` etkisi azalır (multicollinearity etkisi)

 **Kritik insight:**

> Müşteri memnuniyetini en çok düşüren faktör, uzun teslim süresi değil, beklenenden geç teslimattır.

---

### 5️ Feature Standardization

* Değişkenler z-score ile standardize edildi
* Amaç: katsayıları karşılaştırılabilir hale getirmek

 Sonuç:

* En önemli değişken yine **delay_vs_expected** olarak bulundu

---

### 6️ Model Performans Analizi

####  R-squared

* Düşük → model sınırlı açıklama gücüne sahip

####  RMSE

* ≈ **1.21**
* Model ortalama ~1 puan hata yapmaktadır

####  Residual Analizi

* Ortalama ≈ 0 → bias yok
* Dağılım normal değil

 Bunun nedeni:

* `review_score` değişkeninin **ayrık (1–5 arası)** olması
* Modelin **sürekli değerler üretmesi**

---

##  Sonuçlar

* Teslimat süresi müşteri memnuniyetini düşürür
* Ancak **gecikme (delay)** çok daha kritik bir faktördür
* Model performansı sınırlıdır çünkü:

  * Az sayıda feature kullanılmıştır
  * Müşteri memnuniyeti çok faktörlü bir değişkendir

---

##  Geliştirme Önerileri

* Daha fazla feature eklenebilir:

  * ürün fiyatı
  * ürün kategorisi
  * kargo mesafesi
  * sipariş içeriği

* Classification modelleri denenebilir:

  * çünkü `review_score` ayrık bir değişkendir

---

##  Kısa Özet (Sunum İçin)

Bu çalışmada müşteri puanlarını etkileyen faktörleri analiz ettik.
Teslimat süresi ve gecikmenin her ikisinin de negatif etkisi olduğu görülse de, gecikmenin çok daha güçlü bir faktör olduğu ortaya çıkmıştır.

Model performansı sınırlı kalmış olup, bunun temel nedeni hem veri setinin kısıtlı olması hem de hedef değişkenin ayrık yapıda olmasıdır.

---

## 👨 Author

Doruk Pamir
