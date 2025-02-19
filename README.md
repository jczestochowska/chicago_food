# Title: Where (not) to eat in Chicago?

# Milestone 3 

Check out our data story [here](https://jczestochowska.github.io/)

In order to see all the plots, check out the `project_milestione_3.html` (HTML version of the notebook).

We also provide nbviewer [here](https://nbviewer.jupyter.org/github/jczestochowska/chicago_food/blob/master/project_milestone3.ipynb) (but it seems that not all the plots are shown).

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
5. ~~How are inspection results connected to customer reviews? Are the best scored restaurants the ones with the best inspection results as well? Which client-reported issues are also noticed by inspections? Which issues are only discovered by inspections?~~

# Dataset

Our main base dataset is a kaggle one [Chicago Food Inspections](https://www.kaggle.com/chicago/chicago-food-inspections) which contains information about sanitary inspections performed by staff from the Chicago Department of Public Health’s Food Protection Program in restaurants, grocery stores and other food related sites in city of Chicago. Data span is: since 1 January 2010 to the present. We want to focus specifically on restaurants. Dataset consists of various inspection related information like: inspection date, inspection type, results of inspection, violations a restaurant commited but also geographical data like zip code or area in which restaurant is located. To answer all our questions we will enrich it with:

1. Customers reviews and ratings about restaurant using [Google Places API](https://developers.google.com/places/web-service/details). Google Places API can also provide information about restaurant price range. Those features could improve our knowledge base. **As described in the notebook, we drop the question number 5 and we won't use the reviews**
2. [Chicago zip codes geolocation](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-ZIP-Codes/gdcf-axmw) to use for visualization purposes in questions 2. and 4.
3. [Chicago community areas geolocation](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Community-Areas-current-/cauq-8yn6)
4. [PlaceILive](https://chicago.placeilive.com/map#41.80919639152055/-87.72926330566406/10) website which has information about Life Quality Index in neighborhoods of (mainly) US cities.

# Group members

- Justyna Czestochowska: scrapping data from Google, Life Quality index analysis, Descriptive Analysis, Jekyll setup, plotting, Data story
- Maja Stamenkovic: Classification of violations, Analysis of Safe and Dangerous neighborhoods, working with Community areas, Data story
- Jakub Gwizdala: Data cleaning, Map plotting, Violations encoding and visualization, Data story
- Elias Hariz: Evolution of restaurants, Restaurant-chain analysis, Analysis by risk, Data story

Final presentation: Elias Hariz, Maja Stamenkovic

# Previous milestone

## Progress done up until milestone 2

Up until milestone 2 we managed to familirize ourselves with the data we're working with and obtain some first results that form the first answers to the research questions we posed. We decided to drop one research question. Also, we started visualizing our results in the form that will be the target one, which are maps of Chicago with marked neighborhoods.

## Internal milestones up until project milestone 3
**The same list can be also found at the end of the `project_milestone2` notebook**

The plans are split by research queations to which they apply:

**Question 1:** 
 - visualize and analyze spatial patterns of most common violations, 
 - use violations as a source for "safe to eat" metric for a neighborhood (e.g. with percentage of inspections passed without violations concerning food or a trend in such pass rate).

**Question 2:** 
 - build a better heuristic to evaluate restaurant safety, 
 - use other available features to determine "safe or dangerous" neighborhood (e.g. use the Risk column, narrow down the analysis to certain inspection type).

**Question 3:** 
 - study more indicators of restaurant quality, such as the risk level and violation categories, and their evolution over time,
 - find areas with potential future improvement,
 - inspect whether some restaurant chains follow certain trends.

**Question 4:** 
 - check if there is a relationship between "safe or dangerous" neighborhoods to eat and life quality index in those neighborhoods.


## Data story plan
**The same plan can be also found at the end of the `project_milestone2` notebook**

1. We begin it by general statistics and results based on simple metrics that should bring suspected results (such as the ones we obtained, where the city center and the airport proved to be the safest places to eat).
2. We dive deeper by constructing more complicated metrics based on inspection results and violations.
3. We inspect the trends that can tell us more about how neighborhoods are evolving. It *can* allow for forecasting which neighborhoods might be promising in the near future. This analysis can focus also on certain interesting restaurant chains.
4. We conclude our data story with recommendations of neighborhoods where one may be more interested to eat based on the previously presented metrics and analysis.

Throught our data story we want to make an extensive use of maps to visualize our metrics.

The final presentation will follow the pattern similar to the data story but limited to the most relevant/interesting information and findings.

