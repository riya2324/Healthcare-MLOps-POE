# Viva preparation: Healthcare ML DevOps project

**1. What is your problem statement?**  
I built a healthcare machine-learning application that predicts whether a breast tumour is benign or malignant from numerical measurements.

**2. Why did you choose this dataset?**  
It is a built-in, small, labelled healthcare dataset. It has numerical features and a clear classification target, so it is suitable for demonstrating the complete ML workflow.

**3. Is this a real medical diagnosis system?**  
No. It is only an educational demonstration and must not be used for patient diagnosis.

**4. What is the target variable?**  
The target is the diagnosis class: malignant or benign.

**5. What is classification?**  
Classification predicts a category or class label.

**6. Which model did you use and why?**  
I used Logistic Regression. It is a simple classification algorithm, trains quickly and is suitable as a baseline model.

**7. Why did you use StandardScaler?**  
The features have different numeric scales. StandardScaler puts them on a comparable scale, which helps Logistic Regression.

**8. Why split the dataset?**  
Training data is used to learn the model. Test data checks how well it performs on unseen examples.

**9. What is accuracy?**  
Accuracy is the number of correct predictions divided by the total number of predictions.

**10. What is precision?**  
Precision tells us, out of all samples predicted positive, how many were actually positive.

**11. What is recall?**  
Recall tells us, out of all actual positive samples, how many the model correctly found.

**12. Why MLflow?**  
MLflow tracks experiment parameters, evaluation metrics and model artifacts so experiments can be compared and reproduced.

**13. What is an experiment in MLflow?**  
An experiment is a group of related runs.

**14. What is a run in MLflow?**  
A run is one execution of model training with its parameters, metrics and artifacts.

**15. Why FastAPI?**  
FastAPI lets us expose the trained model through REST API endpoints.

**16. What is an API?**  
An API allows two software applications to communicate with each other.

**17. What is Uvicorn?**  
Uvicorn is an ASGI server that runs the FastAPI application.

**18. What is the difference between FastAPI and Uvicorn?**  
FastAPI defines the API and its endpoints. Uvicorn serves the application.

**19. What is the /predict endpoint?**  
It accepts feature values and returns the predicted class.

**20. Why Pytest?**  
Pytest runs automated tests to check that the application behaves as expected.

**21. Why HTTPX?**  
HTTPX provides the HTTP client used by FastAPI's TestClient to send requests to the API during tests.

**22. What do your tests check?**  
They check the health endpoint, home endpoint, successful prediction and handling of missing features.

**23. What is an assertion?**  
An assertion checks whether an expected condition is true. If it is false, the test fails.

**24. Why Evidently?**  
Evidently compares reference data with current data and helps identify data drift.

**25. What is data drift?**  
Data drift means the distribution of input data changes over time.

**26. What is the reference dataset?**  
It is the baseline dataset used for comparison.

**27. What is the current dataset?**  
It is the newer data being compared with the reference data.

**28. What is Jenkins?**  
Jenkins is an automation server used to run software development tasks such as building, testing and deployment.

**29. What is CI?**  
Continuous Integration means regularly integrating code changes and automatically checking them.

**30. What does your Jenkinsfile do?**  
It installs dependencies, trains the model, runs tests and creates the Evidently report.

**31. What is Git?**  
Git is a version control system that tracks changes in source code.

**32. What is GitHub?**  
GitHub is an online platform for hosting Git repositories and collaborating.

**33. Why Java JDK?**  
Jenkins is Java-based, so Java is required to run the Jenkins server.

**34. What is the role of Pandas?**  
Pandas loads, organises and manipulates tabular data using DataFrames.

**35. Explain your project flow.**  
I load the dataset, split it, train Logistic Regression, track the run in MLflow, expose predictions using FastAPI, test the API using Pytest and HTTPX, and monitor data drift using Evidently. GitHub stores the code and Jenkins automates the workflow.

**36. What happens if a test fails?**  
Pytest reports the failed test. In the Jenkins pipeline, the test stage fails and later stages do not run.

**37. What is the difference between testing and monitoring?**  
Testing checks whether code or an API works correctly. Monitoring checks whether data or model behaviour changes over time.

**38. What is model deployment?**  
Deployment means making a trained model available for use, for example through an API.

**39. What is a REST API?**  
A REST API is a web API that uses HTTP methods and resource-based endpoints.

**40. What is Swagger UI?**  
FastAPI provides interactive API documentation at `/docs`, where we can try endpoints.

## Honest demonstration note
Do not claim that you used Jenkins or GitHub in a completed pipeline unless you actually run and configure them. You can explain the included Jenkinsfile and demonstrate the local steps. Also do not claim the model is clinically approved.
