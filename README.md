# ADA Milestone 2

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
5.~~How are inspection results connected to customer reviews? Are the best scored restaurants the ones with the best inspection results as well? Which client-reported issues are also noticed by inspections? Which issues are only discovered by inspections?~~

# Dataset

Our main base dataset is a kaggle one [Chicago Food Inspections](https://www.kaggle.com/chicago/chicago-food-inspections) which contains information about sanitary inspections performed by staff from the Chicago Department of Public Health’s Food Protection Program in restaurants, grocery stores and other food related sites in city of Chicago. Data span is: since 1 January 2010 to the present. We want to focus specifically on restaurants. Dataset consists of various inspection related information like: inspection date, inspection type, results of inspection, violations a restaurant commited but also geographical data like zip code or area in which restaurant is located. To answer all our questions we will enrich it with:

1. Customers reviews and ratings about restaurant using [Google Places API](https://developers.google.com/places/web-service/details). Google Places API can also provide information about restaurant price range. Those features could improve our knowledge base.
3. [Chicago districts geolocation](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-ZIP-Codes/gdcf-axmw) to use for visualization purposes in questions 2. and 4.
4. [PlaceILive](https://chicago.placeilive.com/map#41.80919639152055/-87.72926330566406/10) website which has information about Life Quality Index in neighborhoods of (mainly) US cities.

    

# A list of internal milestones up until project milestone 3

1. For the next milestone we are going to analyze spatial patterns within Chicago for the most common violations per neighborhood. Also, violations discovered during inspections can serve as another measure for ranking places where to eat in Chicago, i.e. we can use percentage of passed inspections or (more detailed) percentage of passed inspections with no food related violations for gauging the quality and safety of restaurants in particular neighbourhood. Establishing such additional measures may help us in responding to the main project question based on not that commonly analyzed aspects and propose safe to eat neighbourhoods based on such measure.
2. We plan to explore further the "safe vs. dangerous" areas by choosing several criteria. We plan to check how Risk feature impacts that separation, as well as try to find other metrics which could be relevant for this analysis.
3. Our goal for the next milestone is to study more indicators of restaurant quality, such as the risk level and violation categories, and their evolution over time. Particularly, it would be interesting to find which areas show the most potential for future improvement. We could also check whether certain restaurant chains (Subway, Starbucks...) follow certain trends.
4. Our aim in the next milestone will be to check if there is a relationship between "safe or dangerous" neighborhoods to eat and life quality index in those neighborhoods.


 Plan of the data story : 
1. Are there "safe to eat" areas or "dangerous to eat" areas in Chicago? Areas classified by inspection results. (different criteria: inspection score, percentage of restaurant failing inspections, risk)
2. The most common reasons for a restaurant not passing an inspection. Most common reasons per area, classification of areas per most common violation categories, most common violations in Chicago and per inspection type (Canvas, License, customer complaint). Visualizing violation patterns in Chicago.
3. Checking restaurants history of inspections, how are restaurants or whole areas changing in their inspection results? Which areas show the highest potential for improvement? Are there areas/restaurant chains/restaurant types that follow some trends?
4. How is restaurant performance in terms of inpection results related to geodemographic charactestics of the area (e.g. Life Quality Index)?

Goals until milestone 3 : 
- Build a better heuristic to evaluate restaurant safety

