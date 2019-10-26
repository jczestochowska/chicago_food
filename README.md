# ADA Milestone 1

# Title: Where (not) to eat in Chicago?  

# Abstract

With more than 14'000 restaurants, food is a serious business in Chicago. But choosing where to eat is not an easy task, especially when you want to avoid risky places. Our choices are usually affected by the reviews of other visitors and the location of the restaurant. But do we ever wonder if a restaurant fulfils all sanitary standards?

Using Chicago Food Inspection data, our goal is to provide insights into food quality in the Windy City. We want to explore what are the violations that restaurants make most often, how they change over time and are they connected to the area where restaurant is located. Moreover, we what to see if there is a link between the inspection results and user reviews for the particular restaurant.

If you want to eat out in Chicago, our data story should help you make the right choice and understand how social factors and food quality influence one another.

# Research questions
A list of research questions we would like to address during our analysis:

1. What are the most common reasons for a restaurant not passing an inspection?
2. Are there "safe to eat" areas or "dangerous to eat" areas in Chicago?
3. Checking restaurants history of inspections, how are restaurants or whole areas changing in their inspection scores? Can one see any patterns in improvements with respect to inspection results? Are there areas/restaurant chains/restaurant types that follow some trends?
4. How is restaurant performance in terms of inpection results related to geodemographic charactestics of the area (e.g. Life Quality Index)?
5. How are inspection results connected to customer reviews? Are the best scored restaurants the ones with the best inspection results as well? Which client-reported issues are also noticed by inspections? Which issues are only discovered by inspections?

# Dataset

Our main base dataset is a kaggle one [Chicago Food Inspections](https://www.kaggle.com/chicago/chicago-food-inspections) which contains information about sanitary inspections performed by staff from the Chicago Department of Public Health’s Food Protection Program in restaurants, grocery stores and other food related sites in city of Chicago. Data span is: since 1 January 2010 to the present. We want to focus specifically on restaurants. Dataset consists of various inspection related information like: inspection date, inspection type, results of inspection, violations a restaurant commited but also geographical data like zip code or area in which restaurant is located. To answer all our questions we will enrich it with:

1. Customers reviews about restaurant using e.g: [Yelp API](https://www.yelp.com/developers/documentation/v3/business_reviews), [Yelp Dataset](https://www.yelp.com/dataset/documentation/main), [Google Places API](https://developers.google.com/places/web-service/details) or others. Yelp Dataset is 9GB sized JSON dataset. We are not sure if all the restaurants from Chicaco Food Inspections are present there, therefore it might be easier to use Yelp API to query the restaurants we need. Yelp API can also provide information about restaurant price range, what kind of food it serves or opening hours. Those features could improve our knowledge base.
3. [Chicago districts geolocation](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-ZIP-Codes/gdcf-axmw) to use for visualization purposes in questions 2. and 4.
4. [PlaceILive](https://chicago.placeilive.com/map#41.80919639152055/-87.72926330566406/10) website which has information about Life Quality Index in neighborhoods of (mainly) US cities.
    

# A list of internal milestones up until project milestone 2

## Week 1 (28.10. - 4.11.)
1. **Getting the data:** fetching datasets, accessing APIs, web scraping.
2. **Exploratory analysis:** get the first feeling of what is included in the data, how can various datasets be combined - what data are we missing?
3. **Get the missing data:** find datasources for what we realized is missing for the coherent analysis&ast;.

## Week 2 (4.11. - 11.11.)
4. **Make data analysis-friendly:** clean datasets, make them compatible and suitable for joint analysis&ast;.
5. **Process violation notes:** categorize data from violations column in the main inspections dataset to extract clear reasons why some restaurants haven't passed inspections.

## Week 3 (11.11. - 18.11.)
6. **Exploring analysis possibilities:** NLP techniques on customer reviews (e.g. sentiment analysis, keyword extraction).
7. **Discovering and observing trends:** getting first answers to our questions.

## Week 4 (18.11. - 25.11.)
8. **Visualization of the results:** generating ideas for captivating visualizations and preparing first tryout versions that we will use in our data story: annotated maps, trend graphs etc.
9. **Preparing the notebook**: finishing the notebook and explaining the results.

&ast; Knowing the back-and-forths of data wrangling processs the above schedule is a rough outline of our main priorities for the upcoming weeks.
    

# Questions for TAs

1. Are we too broad with our research questions? Should we focus on one big conclusion, or can we do several general ones?
2. How final are the research questions? It's likely that we will discover something interesting during data analysis, which we didn't forsee coming up. We might want then to switch focus to this particular thing. Can the research questions be modified at that point?
3. What would be the best source for customer reviews?

