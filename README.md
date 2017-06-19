# Spiderman
*Spiders are invading El Mundo! You'd better hide, or they'll take your info.*

That's basically what's going on. I've built some basic spiders with the Scrapy library for python and got them crawl through the different sections of the Spanish digital newspaper 'El Mundo', getting into each article and taking both the title and body. These are then put into a pipeline, which sends the items to an ElasticSearch server (index: 'el-mundo', type: 'Article').

More info about the project in the following link:
https://www.youtube.com/watch?v=wLg318iEUPs
