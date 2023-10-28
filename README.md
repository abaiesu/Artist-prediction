# Text-Shazam
CSE204 project 2023 \
The goal of this project is to create a machine learning software which when given the lyrics to a song tries to predict the artist. There are plenty of reasons to do this but perhaps the most important one is to detect ghostwriters writing lyrics for multiple artists. This is why we cannot expect very high accuracies and machine learning is appropriate. \
Our system has been fed the lyrics from about 100 songs each of about 150 famous artists from about 10 genres and with a pool of 20 artists' works with over 60% accuracy. This was achieved after making 3 different models each of which improved on some shortcomings of the previous one: a kNN, a CNN, and a logistic regression.\
For a short overview of the system:\
Data Gathering: All our data has been scraped by us to make sure we have data according to some categories we determined to give the best results. The web scraper can be found in the web scraper folder.\
Pre Processing the data: #ANTONIA INSERT YOUR PART#\
Feature extraction: we extracted, from the lyrics, about 200 features such as the length or the number of emotional words, #ANTONIA INSERT YOUR WORK#. After this, we performed a POS which helped us to really reduce the storage requirements and process the data properly.\
kNN: the kNN is the base and initial model. It did not do so well but it gave us a very fair idea about the data and improvements that can be made.\
CNN: With not much success from that method we decided to move to CNN. After removing stop words, stemming and tokenizing the lyrics we used pre-trained GLoVe embeddings and truncated or padded the input to a certain length. Truncating was simply cutting off after a point and padding were random numbers following a normal with the mean and standard deviation seen from the previous data. This was put through multiple conv1D, pooling, and dropout layers before a flatten and 2 dense layers. This gave us an accuracy of about 35% for 15 artists however gave us little knowledge of why the classifications were done and the accuracy fell sharply for larger sets. This is why we moved on to the following.\
Logistic Regression: We used the same pre-processing and feature extraction as the kNN and then did binary classification on each artist and picked the artists with the highest probability. To boost the results we used bagging.\ 
Conclusions: We could see the effect of each feature and got much better accuracies \
\
The results can be seen in the logreg.ipynb file
