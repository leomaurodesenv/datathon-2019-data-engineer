# Data Enginner - Datathon Example

Data Engineers are the data professionals who prepare the "big data" infrastructure to be analyzed. They often design, build, integrate data from various data resources. Also they, usually, run some ETL (Extract, Transform and Load) on top of big datasets.   

This repository present an example how to consume a web [API](https://dadosabertos.camara.leg.br/swagger/api.html) and develop a web crawler, in order to develop our own Data Lake (_i.e._ , data repository of blobs or raw files).   

As Data Lake was used Amazon S3. Also, the code was developed in Python 3.   

---
## Python

1. Example consuming the [API](https://dadosabertos.camara.leg.br/swagger/api.html).

```shell
python python/deputados_api.py
```

2. Example of a web crawler.

```shell
python python/noticias_crawler.py
```

3. Amazon S3 handler.
-   `python/s3_handler.py`

---
## Also look ~

-   Created by Leonardo Mauro ~ [leomaurodesenv](https://github.com/leomaurodesenv/)
-   Presented by [Itera](http://itera.com.br/) - [GitHub](https://github.com/iterasolucoes)