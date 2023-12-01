# The Final Stretch


## Agenda: Not writing spaghetti code and making a pretty GitHub Repo

### Making a marketable github repo.
0. Making a [good README.md](https://github.com/georgiosioannoucoder/realesrgan)
0. Code and file structure [(cookie-cutter format)](https://drivendata.github.io/cookiecutter-data-science/#cookiecutter-data-science). Good deeper [here](https://towardsdatascience.com/how-to-structure-a-data-science-project-for-readability-and-transparency-360c6716800).
0. How to write [pretty code and docstrings](https://www.dataquest.io/blog/documenting-in-python-with-docstrings/). 

### Tech that might REALLY help you.
0. Serverless GPUs via https://www.banana.dev/
    * aka if your streamlit app is super slow. 
0. Another way to run clould GPUs with streamlit or locally via [modal.ai](https://modal.com/docs/guide/gpu)
0. Fuck around with LLMs locally for free with a GUI via https://lmstudio.ai/ 




<br>
<img src="images/file-structure.png" width="300" height="300">

~~THIS IS FROM SOME WEBSITE THAT GEORGIOS FOUND BUT CANT REMEMBER WHERE.  SO ITS NOT OURS, BUT LIKE, ITS GOOD AND IMPORTANT.~~



```
# THIS IS FROM 🚀 Jeremy ARANCIO POST ON LINKED IN 
1. Notebooks

Maybe you figured it out, but I hate Jupyter Notebooks: messy, hard to version, cannot be deployed...

However, for exploratory data analysis (EDA), notebooks are Kings, under certain conditions...

First, no feature engineering in a notebook. 
It should be only done in Python scripts to facilitate its integration into a pipeline.

Second, once a cell is written, it cannot be modified. This way, when I go back to the notebook, I understand my thought process. 
If I need to explore the data again, I just create new cells or a new notebook.

Third, each notebook is enumerated and named appropriately. I usually create a new notebook at every phase of the project: 
* first exploration, 
* after feature engineering, 
* improvement of the data for model v2, etc...
2. Src/ folder

The core of the repository. 
It should contain the different scripts, such as the feature engineering, training, evaluation, inference, algorithms, etc...

If I plan to deploy the solution or model, I build an API in src/app/, which calls all the scripts located in src/. This way, anybody who checks the code can start from the app/ and explore each piece of the code structure.

I also add unitests and integration tests to src/ to ensure the continuous development of the application/algorithm.
3. A distinct front-end to host the Streamlit / Gradio app

As a data scientist, it is essential to showcase our work in an interactive manner. Thus, it is pretty common to create a Streamlit application over the model/application.

However, building a front-end is also a way for me to test the API and ensure that everything goes well when other developers call my endpoints.

Therefore, I reproduce how my code would work in production by running two servers: one for the front end (Streamlit) and one for the API. 

The best way would be to create two Docker Images and run the containers like in production. No more excuses such as "But it runs on my computer" anymore!
```
<br>
<br>







# Other stuff
#### This week is in class demos and the rest project time.

#### Next week is virtual in class demos, and more project time. 

#### Next next week is the big day == Demo Night
<br>



# Demo Night Details

### When is Demo Night
* Wed, Dec 13th, 6:00 - 8:00pm EST __Arrive by 5:15pm__

### Where is Demo Night
* In Person in [Building 92 @ Brooklyn Navy Yard](https://maps.app.goo.gl/BHJ4nvRvaPmp3pEz6)


IMPORTANT: If you are using GPS or an online mapping service to find BLDG 92, enter "Building 92, Flushing Avenue, Brooklyn, NY" or  “Flushing Ave and Carlton Ave, Brooklyn, NY”.  Do not just  use the street address, as there is only one address for the entire 300-acre Yard. 

![image](https://openlab.citytech.cuny.edu/macdonaldecon2505wed2016d728/files/2016/01/Brooklyn_Navy_Yard_Directions.jpeg)


Do not enter “63 Flushing Ave” or just “Brooklyn Navy Yard,” as you will end up in the wrong location.


Do not attempt to enter the Brooklyn Navy Yard through any of the other security entrances, as you will be turned away.

If you plan on taking the subway, the closest stops are York Street (F) and High St (A/C). Alternative transportation options, as well as driving, biking, or ferry directions are here.

Here are more details on how to get there including subway, car shuttle, ferry, bike and bus: [Planning your trip to BNY](https://www.brooklynnavyyard.org/directions-map/)




Agenda
=========
**We will share with you ahead of time what group you have been assigned.

* 6:00pm - 6:50pm :: Group A Project Presentations 

* 6:55pm - 7:05pm Staff Speeches

* 7:10pm - 8:00pm Group B Project Presentations






