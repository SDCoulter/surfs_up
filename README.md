# Challenge - Surfs Up Analysis

## Challenge - Overview

The module walks us through creating and running analysis on weather data for the island of Oahu, using Python, SQLite/SQLAlchemy, Pandas, and for displaying the findings, Flask. We look at the type of weather on this Hawaiian island as a precursor to opening a Surf and Ice Cream store. We are running the analysis to show to the investor that the weather throughout the year will not affect this business being profitable year-round. Our goal being to convince the investor that investing is a wise choice and to support us creating our business.

For the challenge portion of the module we run two queries to find all the temperatures for the months of June and December from the dataset. Then we use Pandas to display a summary statistics table for each month. These results are detailed below.

## Challenge - Results

We find the temperatures for June using the following query:

```py
results = session.query(Measurement.tobs)\
            .filter(extract('month', Measurement.date) == 6)
```

And similarly for December, but with the extracted month matching `12` rather than `6`. Here we have used the query method on the Python-SQLite session with a filter. For the filter we have employed the use of the SQLAlchemy function `extract` which allows us to extract the month from the date string and compare it to a month value of our choosing. `6` for the sixth month June, and `12` as December.

After the query is returned we turn it into a list with `.all()`, and then a DataFrame with `pd.DataFrame()`, before showing a table of statistical values with `.describe()`. Below you can see the returned statistics:

![June Temperature Statistics](Images/june_temps_stat_summary.png) | ![December Temperature Statistics](Images/dec_temps_stat_summary.png)

### Query Takeaways

- one
- two
- three






Results: Provide a bulleted list with three major points from the two analysis deliverables. Use images as support where needed.
There is a bulleted list that addresses the three key differences in weather between June and December. (6 pt)

## Challenge - Summary



Summary: Provide a high-level summary of the results and two additional queries that you would perform to gather more weather data for June and December.
There is a high-level summary of the results and there are two additional queries to perform to gather more weather data for June and December. (5 pt)

## Context

This is the result of Module 8 of the University of Toronto School of Continuing Studies Data Analysis Bootcamp Course - **Python and SQLite** - Advanced Data Storage and Retrieval. Following the guidance of the module we end up pushing this selection of files to GitHub.
