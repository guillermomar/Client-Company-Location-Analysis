# Overview

![alt text](https://i.dlpng.com/static/png/6665186_preview.png "Gaming")

In this repo you will find an analysis of the best location to enplace the headquarters of a client company.

This is an academy exercise in wich a client demand from us to do an analysis to advice him in which city and place he should enplace the headquarters of his gaming design company. For this task we should take into consideration the following variables:

- Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.
- Developers like to be near successful tech startups that have raised at least 1 Million dollars.
- Executives like Starbucks A LOT. Ensure there's a starbucks not to far.
- All people in the company have between 25 and 40 years, give them some place to go to party.


# Methodology

I used two data bases:
    https://www.crunchbase.com/ for companies data in mongoDB

    https://www.kaggle.com/starbucks/store-locations to get the location of every starbucks store

One API:
    https://developer.foursquare.com/

The main libraries used are:
    pandas and geopandas for frames
    pymongo for mongo queries
    cartoframes for maps

To watch the analysis you can open the "Client company location anlysis.ipynb" in wich you will find a step by step explanation.

I hope you will enjoy it!
