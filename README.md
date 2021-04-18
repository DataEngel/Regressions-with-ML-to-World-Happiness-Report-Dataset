# Regularization
 
This technique consists of reducing the complexity of our model through a penalty applied to its most irrelevant variables.
 
So, regularization consists of introducing a bit of bias to reduce the variance of the data.
 
![3](https://user-images.githubusercontent.com/63415652/105785289-277d4980-5f40-11eb-8a6e-e9f96bd25307.PNG)
  
## What is this dataset about?

It is a classification of which countries in the world could be considered "happy". This report contains 155 countries from each continent to build an understanding of which countries can be the happiest. This classification is revered around the world as it could be an indication of the country's political decision-making skills. Experts from around the world (in economics, psychology and foreign affairs) have pointed out that these scores can be a good indication of the progress of a country, but of course, it is not the end and the progress of a country.

>**_Note:_** In this readme only the results will be shown, for more details see the code, in the code folder of this repo.

---

## Implementation of linear regression, lasso and ridge.

Now we are going to see which technique generates less loss for our analysis:
 
![15](https://user-images.githubusercontent.com/63415652/103431748-f147e680-4b9a-11eb-99f6-87e7442d845b.PNG) 
 
And as you can see, the linear generates less loss.
 
Now we will see the coefficients:
 
![16](https://user-images.githubusercontent.com/63415652/103431890-10e00e80-4b9d-11eb-808d-5f32015a455a.PNG) 
 
This is a numerical arrangement that has the same size as the columns that we use in our features, this is because each of the numbers correspond one by one to the columns that we are trying to evaluate and here where we can get more relevant information, because when We find the largest numbers, we can directly know that this column is the one that is having the most weight in the model we are training.

For example, in the case of the lasso regression, the economic factor has much more weight than the other variables than the happiness index that is calculated and in this case, the lasso regression decided to remove the other variables since it found them determining for us.
 
>**_Conclusion:_** This opens the door to many questions that we have to ask ourselves about our data, but that is already at our discretion to understand those complex relationships and do more tests to understand specifically what is happening.
 
# Robust regressions.
 
**Ransac:** selects a random sample of the data assuming that this sample is within the inliners values, with these data the model is trained and its behavior is compared with the other data. This procedure is repeated as many times as indicated and at the end of the algorithm it chooses the combination of data that has the best number of inliners, where the outliers can be effectively discriminated.
 
![17](https://user-images.githubusercontent.com/63415652/103431940-d75bd300-4b9d-11eb-9ba2-5d549e0b440e.PNG)
 
**Huber Reggresor:** does not remove outliers but penalizes them. Perform the training and if the absolute error of the loss reaches a certain threshold (epsilon) the data is treated as outliers. The default value for epsilon is 1.35 as it has been shown to achieve 95% statistical efficiency.
 
Now we will go on to do a robust regression introducing some corrupted data, to deal with it effectively.
 
![18](https://user-images.githubusercontent.com/63415652/103432212-09226900-4ba1-11eb-9def-deac0a86ca20.PNG)
 
The modification that was made was to add values in our dataset in zeros, in such a way this could confuse our models if they are not well trained or if we have not worked with those outliers before.
 
### Now we are going to apply Ransac and Huber:
 
![19](https://user-images.githubusercontent.com/63415652/103432432-4b00de80-4ba4-11eb-97df-38a34e4a0e6e.PNG) 
 
As we can see from the results, both RANSAC and HUBER have a much smaller error than SVR.
 
>**_Conclusion:_** Here we can clearly see how the outliers do affect the performance of our model, therefore it will always be important to take some precautionary measure to be able to deal with this process in a satisfactory way.  

## Data source: [World Happiness Report](https://www.kaggle.com/unsdsn/world-happiness)

Although the code is not proprietary and is free to use, the data is licensed, please read it before using this data.
This project is not for commercial purposes, it is for academic purposes only.

## You can check the main notebook in my kaggle profile and if you like, my other contributions too:

* [Robust Regressions in World Happiness Report DataSet](https://www.kaggle.com/dataengel/robust-regressions-in-world-happiness-report) 