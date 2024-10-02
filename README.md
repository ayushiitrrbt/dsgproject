# SortYourCodeforces

SortYourCodeforces is a handy tool that helps you find and practice Codeforces problems in a structured and sorted manner. Whether you're preparing for competitive programming contests or just want to improve your problem-solving skills, SortYourCodeforces allows you to customize your practice sessions by sorting problems based on:

Tags: Focus on specific topics or problem types you want to improve.
Rating: Practice problems that match your current skill level, or challenge yourself with more difficult ones.
Name: Quickly locate specific problems or work through them alphabetically.
With SortYourCodeforces, you can efficiently tailor your problem-solving journey according to your preferences, making it easier to track your progress and enhance your competitive programming skills.


#How it works
SortYourCodeforces leverages a cutting-edge Retrieval-Augmented Generation (RAG) system to provide an efficient and flexible way to query Codeforces problems. Here's a breakdown of how it functions:
Data Retrieval: The application maintains a comprehensive database of Codeforces problems, including details such as tags, ratings, and problem names. When you make a query, the RAG system retrieves the most relevant problems from this dataset based on your specified criteria.
Query Processing: You can ask questions or provide sorting instructions in natural language (e.g., "Show me problems with a rating above 1600 tagged with 'graphs'"). The RAG model processes this query and understands your intent, allowing it to fetch the most suitable problems for you.
Response Generation: After retrieving the relevant problems, the system sorts them according to your specified parameters (tags, rating, or name) and generates a structured response. The result is an organized list of Codeforces problems tailored to your needs, making it easy for you to start practicing right away.

By combining the power of retrieval with the intelligence of a language model, SortYourCodeforces delivers a seamless experience, helping you find the right problems faster and more accurately.

``` wsl/linux
git clone https://github.com/ayushiitrrbt/dsgproject
```
Navigate to civil civic
``` wsl/linux
cd examples/pipelines/demo-questuion-answering
```
create you gemini-apikey and paste it in .env file

Build the Docker Image
```wsl/linus
docker build -t rag .
```

Run the Docker Container
```wsl/linux
docker run -v "$(pwd)/data:/app/data" -p 8000:8000 --env-file .env rag
```
install streamlit
```wsl/linux
pip-install streamlit
```
navigate to ui directory and run streamlit and run streamlitweb.py
``` wsl/linux
cd examples/pipelines/demo-question-answering/ui/streamlit run streamlitweb.py
```
get to streamlit web page via link given on wsl and just ask query there.

now setup is completed and you can just ask question there webpage

Here below is demo video of it working



https://github.com/user-attachments/assets/0d259ccc-01f3-462b-bdc8-e6cb01b1ca1f

