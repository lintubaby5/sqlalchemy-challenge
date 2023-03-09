# sqlalchemy-challenge

# Surfs_up
Weather analysis using SQLite and SQLAlchemy. Climate App building using Flask. Other tools include Python and Jupyter Notebooks.

## Overview of Surfs Up Analysis

The purpose of this analysis is to review a dataset pertaining to weather conditions that has been stored in a [SQLite database] to do a climate analysis about Honolulu,Hawaii to help with a trip planning. 

In order to explore the data in the `SQLite` database, we used `SQLAlchemy` to connect and generate queries to pull the necessary information needed for our analysis. Throughout this module, we used `Jupiter notebook` to import dependencies and create the commands to pull the data from the `SQLite` database.

We also used `Visual Studio Code` to create Python applications to share the results via a webpage by creating `Flask` routes and using Terminal to run the `Flask` app. When running the `Flask` app in `Terminal`, it generated the `Flask` routes in a web address `http://127.0.0.1:5000` that could be shared.

![web](https://github.com/amylio/Surfs_up/blob/main/MOD9_Challenge_Submission/Images/FlaskWebpage.png)

## Results

When we pulled the data, we first looked at the the precipitation for a one year timeframe. We reviewed the activity from August 23, 2016 - August 23, 2017. The average was 18% based on 2,021 observations. This tells us that throughout the year, Oahu was mostly sunny throughout the day and experienced low rainfall. 

![precipstats](https://github.com/amylio/Surfs_up/blob/main/MOD9_Challenge_Submission/Images/PrecipStats.png) 
![precipgraph](https://github.com/amylio/Surfs_up/blob/main/MOD9_Challenge_Submission/Images/PrecipGraph.png)

We also looked at the number of weather stations that were actively collecting precipitation data and focus on one station that had the most observations recorded. In total, there were (9) stations with `USC00519281` showing the highest amount of observations at 2,772 entries. We used the information from this station to review the temperature for the same time period. The results showed that the average temperature throughout the year was **72°F** with a low of **54°F** and a high of **85°F**. 

![tempgraph](https://github.com/amylio/Surfs_up/blob/main/MOD9_Challenge_Submission/Images/tempgraph.png)

## Summary

In summary, the temperature in Oahu is relatively the same throughout the year and the chances of continuous rainfall is low. 

