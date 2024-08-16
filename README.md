
# **Market Analysis Lab for the Automotive Sector**

Below you will find a script for parsing data from the [Mashina.kg](https://m.mashina.kg/search/all) website. There is also a parsing script `mparsing(Aidana edition).py` that you can run. 
Original script is parsing_original.py from https://github.com/simonlobgromov/Mashina_KG_Parsing
Retrieve new data and compare the market conditions with historical data `machina_kg{date}.csv` from August 2024 and Mashina_kg_10K.csv (April 2023) Perform in-depth analytics and visualization.
```
Folder structure
.
└── main folder/
    ├── completed_urls.txt # number of all urls of cars to the moment of parsing
    ├── Mashina_kg_10k.csv # old database of cars
    ├── mashina_kg_2024-08-15.csv # new database of cars
    ├── mparsing(Aidana edition).py #upgraded script by Aidana and little upgrade by me
    ├── parsing_original.py # original script
    ├── py_log.log # log file of process (thanks Aidana)
    ├── README.md 
    ├── test.py # just testing script file
    └── urls.csv # urls to parsing
```
When running the script, you need to specify the number of pages you want to parse. Each page on the website contains 20 listings.
There can be around 1500 pages in total, but verify this number on the [website](https://m.mashina.kg/search/all).

Great thanks to Den our mentor and Aidana for code and for me for a little coding and waiting for 20 hours of parsing and praying :)

```
git clone https://github.com/thereisnoI/machinekg
cd machinekg

python mparsing(Aidana edition).py
```
