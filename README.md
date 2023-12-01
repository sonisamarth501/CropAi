
# CropAI - Crop image classification.

CropAI is a cutting-edge Flask web application powered by machine learning, designed to accurately classify uploaded images and identify the specific type of plant or crop depicted in the image.

# Key Features
Input data collection:
The system allows to save the images uploaded in static section in the directory for future usage and several predictions.

Data preprocessing:
In order to train our ML model effectively, the uploaded images undergo a rigorous preprocessing phase, where they are transformed into multiple arrays, creating several distinct input sets. These input sets are then further divided into various test and validation subsets, ensuring that our model receives comprehensive and diverse data for accurate predictions.

Machine Learning Models:
Our approach leverages a Sequential model, harnessing the power of Convolutional Neural Networks (CNNs) enriched with multiple layers, including Dense, Softmax, MaxPooling, and Convolutional layers. This architectural configuration empowers our model to effectively capture intricate patterns within the data.
For model training and evaluation, we utilize historical data as our training dataset. We meticulously evaluate model performance using a range of appropriate performance metrics to guarantee accuracy and reliability in our predictions. This rigorous process ensures that our model not only learns from the past data but also generalizes well to make accurate predictions on new, unseen data.

Prediction:
Based on the trained model, the system recommends the most suitable crop for the given input parameter.

User-Friendly Interface:
The system provides a user-friendly interface where users can easily input their data, view recommendations, and explore additional information.

#Technology Used

Kaggle:
Enabling direct access to multiple image datasets hosted on Kaggle. This integration simplifies the data retrieval process, making it convenient for users to tap into Kaggle's extensive collection of tech-related image datasets.

Google extensions:
Extensions to collect several images from google and creating an image dataset from scratch.

Google colab:
Virtual notebook/plateform for training the image classification model.

Python: Programming language used for model development, data preprocessing, and web application development. 

Tensorflow and keras:
Used for image classification model prepration building several image classification layers.

Scikit-learn: Machine learning library used for model training, evaluation, and prediction. Pandas: Data manipulation library used for data preprocessing and analysis. 

NumPy: Library for numerical computing used for handling arrays and mathematical operations. 

Flask: Web framework used for building the user interface and handling HTTP requests. 

HTML/CSS: Markup and styling languages used for designing the web interface. JavaScript: Scripting language used for client-side interactions and enhancing the user interface.

# Installation and Usage

- Clone the repository
- Install the required dependencies: pip install -r requirements.txt.
- Run the application: python app.py.

# Future Enhancements

Integration of real-time weather data to improve the accuracy of recommendations. Incorporation of crop market prices and profitability analysis to assist farmers in making economically viable decisions. Development of a mobile application for convenient access and usage on smartphones and tablets. Integration of user feedback and data collection to continuously enhance the recommendation system's performance. Contributing Contributions to the project are welcome. If you have any suggestions, bug reports, or feature requests, please submit them through the issue tracker on the GitHub repository.

# Acknowledgements

I would like to express my gratitude to the agricultural research community, farmers, and organizations for providing valuable insights, data, and domain knowledge that contributed to the development of this Crop Recommendation System.

# Contact
For any inquiries or questions, please contact at 

## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/samarth-soni-b62933182/)

