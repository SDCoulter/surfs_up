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

| June Temperatures | December Temperatures |
:------------------:|:----------------------:
![June Temperature Statistics](Images/june_temps_stat_summary.png) | ![December Temperature Statistics](Images/dec_temps_stat_summary.png)

### Query Takeaways

- The **mean** temperature is 5 degrees higher in June than in December. It's not unexpected that June is warmer on average than December, as Oahu is an island in the Norther Hemisphere.
- The **minimum temperature** statistic shows the largest difference between the two months, with June a full 8 degrees higher than December. For December this minimum temperature is 4 standard deviations from the mean though, so this may be an outlier and would need to be investigated further. For June the minimum is only about 3 standard deviations from the mean, likely meaning a tighter spread of temperatures.
- The **maximum temperature** has a difference of only 2 degrees, again this could be an outlier, as the differences in the other temperature measurements are much larger when comparing months. We would need to investigate how often temperatures were getting near the max, which given how far from the mean it is likely means it's a rare occurance.
- The **quartile spread** of temperatures seems similar for both June and December, with half of the temperatures falling in a 4-5 degree range. This would mean that you could, on a random day on either of those months, have a 50% chance of having a the temperature fall in these ranges. This would allow you to plan around the weather with a good deal of accuracy.

## Challenge - Summary

--missing--

## Context

This is the result of Module 8 of the University of Toronto School of Continuing Studies Data Analysis Bootcamp Course - **Python and SQLite** - Advanced Data Storage and Retrieval. Following the guidance of the module we end up pushing this selection of files to GitHub.
