# Cric Genie <img src="https://t3.ftcdn.net/jpg/01/64/41/82/240_F_164418285_MLesgG4Ybzd3kmvY7FiS3gWMJonYvsf8.jpg" alt="Cricket Logo" width="50" height="50"/>
Cric Genie is a fantasy cricket application that aims to provide users with accurate predictions of Dream 11 players before the match begins. By leveraging machine learning algorithms and advanced feature engineering techniques, Cric Genie gives users an edge in the competition by helping them choose the best 11 players for their fantasy cricket teams.

## Problem Statement
The problem addressed by Cric Genie is the challenge faced by fantasy cricket players in selecting the most suitable players for their Dream 11 teams. With numerous players to choose from and limited resources, it becomes difficult for users, especially beginners, to make informed decisions. Cric Genie addresses this problem using machine learning, and optimization techniques to predict the top-performing players accurately.

## Key Features and Functionality
- **Data Collection:** Cric Genie manually scrapes cricket data from ESPN, check the code at [Meta_data_collector](https://github.com/Nayanjit-Sarkar/Cric-Genie/blob/main/Meta_data_collector.py). Also, I calculated the Dream point for each player you can see the code there itself.
- **Feature Engineering:** Advanced feature engineering techniques, including rolling functions and carefully selected features, are applied to extract meaningful insights from the data, enhancing the accuracy of the predictions, check the code at [Data_Pre-Processing](https://github.com/Nayanjit-Sarkar/Cric-Genie/blob/main/Data_Pre-Processing.ipynb). 
- **Machine Learning Models:** Cric Genie employs popular machine learning models such as XGBoost and Random Forest. These models are fine-tuned using techniques like Grid Search CV and Random Search CV to achieve optimal performance in predicting fantasy points,check the code at [Model](https://github.com/Nayanjit-Sarkar/Cric-Genie/blob/main/Model.py).
- **Optimization:** The Pulp library is utilized to optimize the selection of the top 11 players from the predicted pool of 22 players, considering constraints such as player positions and team limits, check the code at [get_prediction](https://github.com/Nayanjit-Sarkar/Cric-Genie/blob/main/get_prediction.py).

## Future Enhancements
In the future, we plan to incorporate the following enhancements to further improve Cric Genie:

- Integration with real-time match data to provide live updates and adjust predictions accordingly.
- Enhanced user interface with interactive visualizations and player statistics.
