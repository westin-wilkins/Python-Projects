This code leverages Kaggle's video game sales data to generate actionable insights about the gaming market. 
The analysis includes identifying top-selling and underperforming genres, as well as correlating news articles with fluctuations in global sales numbers for Nintendo. 
It's worth noting that the dataframe initially contains 271 null values in the "Year" column. However, upon closer examination, 
most of these values correspond to game titles that contribute only a fraction of the total sales. Therefore, I have chosen to use the "dropna" function to remove these rows entirely from the dataframe.


The first two graphs illustrate the global sales distribution across different video game genres and publishers. The data reveals that action games have the highest sales, which aligns with the abundance of action games produced annually. Sports games secure the second position, most likely due to the dominance that EAs' FIFA series of games have on the sports game market. Consequently, on the second graph, EA emerges as the second top publisher, following Nintendo.

The third graph presents the global sales trends of Nintendo games over the years. Notably, there was a significant surge in sales from 2005 to 2006, which coincided with the release of the highly popular Wii console. However, the most intriguing aspect of this graph is the gradual decline in sales from 2006 to 2016. Through thorough research, I discovered an insightful article published by "The Economic Times" in 2010 that sheds light on this trend. The article highlights that, during this period, Nintendo faced fierce competition from other motion-controlled consoles in the market, such as Microsoft's "Kinect" and Sony's "PlayStation Move". Additionally, Nintendo experienced a decline in games produced for the Wii console (The Economic Times, 2010).

Reference:
https://economictimes.indiatimes.com/tech/software/nintendo-profits-fall-on-declining-wii-sales/articleshow/5898677.cms
