# MBTI

## Brief introduction
This application asks the user some questions. And users answer in good faith. The application uses a model trained on the data to guess and inform the user's MBTI.

## Used data set 
* [🔗 Link](https://www.kaggle.com/code/amishra527/mbti-500/data)
* This data is preprocessed texts: No punctuations, stopwords, URLs
* Reconstruct samples to be equal-sized chunks (500 words per sample)
* Personality types are 16 unique values

### Distribution by type in the used data set 
<img width="1317" alt="스크린샷 2022-05-29 오후 8 54 57" src="https://user-images.githubusercontent.com/33858991/170870819-33ef5600-63da-46eb-b9e5-9d64338e45f6.png">

## Analyze accuracy using test data
* Use 20% of the total data as test data

|  | precision | recall | f1-score |
| --- | --- | --- | --- |
| **ENFJ** | 0.84 | 0.58 | 0.69 |
| **ENFP** | 0.82 | 0.78 | 0.80 |
| **ENTJ** | 0.90 | 0.80 | 0.84 |
| **ENTP** | 0.86 | 0.83 | 0.84 |
| **ESFJ** | 0.83 | 0.45 | 0.59 |
| **ESFP** | 0.88 | 0.48 | 0.62 |
| **ESTJ** | 0.90 | 0.84 | 0.87 |
| **ESTP** | 0.95 | 0.90 | 0.92 |
| **INFJ** | 0.81 | 0.84 | 0.83 |
| **INFP** | 0.80 | 0.82 | 0.81 |
| **INTJ** | 0.83 | 0.87 | 0.85 |
| **INTP** | 0.84 | 0.87 | 0.86 |
| **ISFJ** | 0.80 | 0.61 | 0.69 |
| **ISFP** | 0.81 | 0.60 | 0.69 |
| **ISTJ** | 0.86 | 0.68 | 0.76 |
| **ISTP** | 0.89 | 0.79 | 0.84 |

### Overall accuracy of the model: 84%

## Execution example

### Q1: What happened today? Think of it as a diary and speak comfortably.
### A1: 
    I visited my grandmother's house today to commemorate my mother's birthday. 
    I went and ate fried fish. I had a stomach ache because I ate too much. 
    I was still very full, so I decided not to eat dinner. 
    So I'm working hard on my assignments.

### Q2: Do you have any favorite hobbies? Introduce your hobbies and tell us how you feel about doing them.
### A2:
    I play basketball as a hobby. basketball is so much fun It's hard, 
    but the desire to win and the desire to do better make me run even more. 
    In the future, I want to be educated in basketball at an academy and 
    play basketball with better skills.

### Q3: Now, the last question already. Tell me about what you need to do tomorrow and what you want to do tomorrow.
### A3: 
    I have to take a test called "Re-examined Korean History" tomorrow. 
    And after that, I decided to meet my girlfriend. I hope you have a happy day 
    tomorrow. And I hope you eat a lot of delicious things.
    
### Result
* My application's answer : **INFP**
* Real Answer : **ENFP**
* In this case, the accuracy was about 75%. 😃
