Project 1: Al-Powered Task Management System





Overview : 


Problem Statement  :  
Design and develop an intelligent system that leverages NLP and ML automatically classify, prioritize, and assign tasks to users based on their behavior, deadlines, and workloads.


Week-wise Plan 


Week 1  : 

Collect datasets related to tasks (e.g., Trello, Jira APIs, synthetic task datasets).

Perform exploratory data analysis (EDA) and clean data.

Apply NLP preprocessing on task descriptions (tokenization, stemming, stopword, removal)


Week 2 : 

Feature extraction using TF-IDF/word embeddings (Word2Vee/BERT).

Implement task classification using Naive Bayes and SVM.

Set up version control with GitHub.

Evaluate using accuracy, precision, recall.




Mid project review ( end of week 2 )  : 


Cleaned and preprocessed dataset

Task classifier (Naive Bayes/SVM) trained and evaluated
 
EDA visualizations completed


Week 3 : 

Implement priority prediction model using Random Forest/XGBoost. 

Integrate workload balancing logic using heuristic or ML approach.

Apply GridSearchCV for hyperparameter tuning.


Week 4 : 

Finalize models for task classification and priority prediction.

Prepare dashboard mockup or output summary.

Compile performance metrics, graphs, and results.


Final project review ( end of week 4 ) : 

Models finalized for task classification & prioritization








This project focuses on designing and developing an intelligent task management system
 that leverages NLP and ML techniques to automatically classify, prioritize, and assign
 tasks based on their descriptions, deadlines, and workloads










WEEK 1 – DATA COLLECTION AND PREPROCESSING


 During the first week, the primary focus was on gathering relevant data and preparing it for
 analysis. Datasets related to task management were collected, either through publicly
 available sources such as Trello or Jira APIs, or by generating synthetic task datasets that
 mimic real-world team workflows. Once the dataset was obtained, exploratory data
 analysis (EDA) was conducted to understand the structure of the data, identify missing
 values, and detect inconsistencies. Various visualizations such as bar graphs and
 histograms were used to observe task priority distribution and deadlines. Natural
 Language Processing (NLP) techniques were applied to clean the text data within task
 descriptions. This involved tokenization, removing punctuation, eliminating stopwords, and
 applying stemming or lemmatization to normalize the words. By the end of Week 1, a
 clean and preprocessed dataset was ready for feature extraction and model development.



 


WEEK 2 – FEATURE EXTRACTION AND TASK CLASSIFICATION

 The second week focused on transforming the preprocessed text data into a numerical
 format suitable for machine learning models. Feature extraction was performed using
 TF-IDF (Term Frequency–Inverse Document Frequency) to capture the importance of
 each word in the task descriptions. Alternatively, word embeddings such as Word2Vec or
 BERT could also be utilized for advanced semantic understanding. Two primary models —
 Naive Bayes and Support Vector Machine (SVM) — were implemented for classifying
 tasks based on their descriptions and priority levels. The models were trained and
 evaluated using metrics such as accuracy, precision, and recall to measure performance.
 In addition, version control was established through Git and GitHub to manage code
 updates efficiently and ensure collaborative development. By the end of Week 2, a
 working task classification model was developed, validated, and uploaded to GitHub as
 part of the mid-project deliverables






WEEK 3 – PRIORITY PREDICTION AND WORKLOAD BALANCING

 Week 3 was dedicated to enhancing the system’s intelligence by introducing task
 prioritization and workload balancing mechanisms. A predictive model using algorithms
 such as Random Forest or XGBoost was developed to estimate the priority of new or
 unlabelled tasks based on learned patterns. Additionally, workload balancing logic was
 incorporated to assign tasks to users depending on their existing workload and efficiency.
 This could be achieved using heuristic rules or a machine learning approach that learns
 from past assignment data. To improve model accuracy and generalization,
 hyperparameter tuning was conducted using GridSearchCV. By the end of this week, the
 system was capable of not only classifying tasks but also predicting their priority and
 recommending fair assignments to optimize productivity







WEEK 4 – MODEL FINALIZATION AND DASHBOARD CREATION

 The final week focused on refining the models, visualizing results, and summarizing
 findings. The best-performing models for both classification and prioritization were
 finalized based on evaluation metrics and cross-validation results. A dashboard mockup
 was prepared to present task insights such as task categories, predicted priorities, and
 workload distributions. This could be implemented using Streamlit or a simple Python
 visualization tool like Matplotlib or Seaborn to display graphs and charts. Finally, all the
 models, evaluation results, and EDA visualizations were compiled into a comprehensive
 project report. The project successfully demonstrated how NLP and ML can automate and
 enhance task management systems, improving team efficiency and decision-making
 processes






























Summary dashboard / mockup created 
Final report prepared
