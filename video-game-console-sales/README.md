# Worldwide Total Video Game Console Sales

## Data Source(s)

The source for the data used in this project can be located [here](https://www.vgchartz.com/charts/platform_totals/Hardware.php).

Further details have been obtained from the below:

- https://necretro.org/PC_Engine_SuperGrafx
- https://www.macrotrends.net/2575/us-dollar-yuan-exchange-rate-historical-chart
- https://www.videogameconsolelibrary.com
- https://www.computinghistory.org.uk/det/67123/Super-Cassette-Vision/
- https://en.wikipedia.org/

**NOTE** Pandora console was removed as it is mostly used for emulation and has no real native games.

Failure rate information:
https://www.squaretrade.com/htm/pdf/SquareTrade_Xbox360_PS3_Wii_Reliability_0809.pdf

Average determined to be ~7.5% (wii @ 2.7% rounded to 3 and end being PS3 @ 10. Halfway = 7.5%)

## Requirements

1. Scrape the table from the above link.
2. Convert it into a Pandas dataframe.
3. Add additional features to the dataframe as needed. For example:
   1. a source image for either the console or a logo for that console.
   2. Categorise the consoles as portable, traditional or other. Perhaps there are other categories that could be used as well.
   3. Year or release.
   4. Year of discontinuation.
   5. Failure rate of the system.
4. Perform some initial EDA to see what insights can be extracted from the data.
5. Save the dataframe contents to a CSV file.
6. Create a database after normalising the data and looking to see if there are any other useful data points. For example, have a table that lists details about each company.
7. Perform further EDA and finalise the insights to report on.
8. Create visualisations and reports.
9. Create a presentation with the findings.

## Requirements

