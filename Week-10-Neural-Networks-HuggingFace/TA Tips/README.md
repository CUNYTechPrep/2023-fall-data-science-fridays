# Hugging Face Spaces Tutorial

The following instructions are a guide to create a simple machine learning app on Hugging Face's Spaces platform that allow data scientists, developers, and researchers to host, share, and collaborate on their machine learning models and applications.

## Step 1
Navigate to the [Hugging Face](https://huggingface.co/) homepage that'll look like the below screenshot. Create an account by selecting `Sign Up` on the top right

![Step1](https://github.com/CUNYTechPrep/2023-fall-DS-dev/blob/main/2023-curriculum/Week-10-Neural-Networks-HuggingFace/TA%20Tips/huggingface%20space%20screenshots/mainpage.png)
## Step 2
Go to the `Spaces` tab on top that should lead you to a page similiar to below. This is the main platform where developers deploy their creative apps using Hugging Face's library of pre-trained models
### Examples
- [AI Comic Factory](https://huggingface.co/spaces/jbilcke-hf/ai-comic-factory)
- [Face Swap](https://huggingface.co/spaces/tonyassi/face-swap)
- [Image Animation USing Thin Plate Spline Motion Model](https://huggingface.co/spaces/CVPR/Image-Animation-using-Thin-Plate-Spline-Motion-Model)

![Step2](https://github.com/CUNYTechPrep/2023-fall-DS-dev/blob/main/2023-curriculum/Week-10-Neural-Networks-HuggingFace/TA%20Tips/huggingface%20space%20screenshots/spacespage.png)
## Step 3
Select `Create new Space`, leading you to the following page:

![Step3](https://github.com/CUNYTechPrep/2023-fall-DS-dev/blob/main/2023-curriculum/Week-10-Neural-Networks-HuggingFace/TA%20Tips/huggingface%20space%20screenshots/createspace.png)

`Owner` should be the username you assigned yourself after creating your account. `Space name` is whatever you want to call the app; in this example we'll call our app, `image-caption-app`, since we're utilizing [this](https://huggingface.co/nlpconnect/vit-gpt2-image-captioning) image captioning model. Finally, choosing your Space SDK (Software Development Kit) is dependant on what you're comfortable with and project necessities; in this example we'll be selecting the `Streamlit` option.

- [Streamlit](https://streamlit.io/) - helps us create web apps for data science and machine learning in a short time
- [Gradio](https://gradio.app/) - create an interactive app that allows users to try out the demo in their browsers
- [Docker](https://www.docker.com/) - allows us to build, test, and deploy applications quickly using 'containers' that have everything we need to run our app
- [Static](https://www.w3schools.com/howto/howto_website_static.asp) - web page with fixed HTML content

## Step 4
After creating the space, the following page will show up that resembles a typical GitHub repository:

![Step4](https://github.com/CUNYTechPrep/2023-fall-DS-dev/blob/main/2023-curriculum/Week-10-Neural-Networks-HuggingFace/TA%20Tips/huggingface%20space%20screenshots/navigatetofiles.png)


## Step 5
Navigate to the `App` tab on the top right to get started on your code. In addtion to following along on the Spaces platform, you can clone this copy of the app by pasting:

**Terminal**:
- `git lfs install`
- `git clone https://huggingface.co/spaces/sms07/image-caption-app`

**SSH**:

- `git lfs install`
- `git clone git@hf.co:spaces/sms07/image-caption-app`


![Step5](https://github.com/CUNYTechPrep/2023-fall-DS-dev/blob/main/2023-curriculum/Week-10-Neural-Networks-HuggingFace/TA%20Tips/huggingface%20space%20screenshots/apppage.png)

## Step 6
Under the `Files` tab, let's start our app by creating a text file detailing the libraries we need. Call the file `requirements.txt` and note `transformers` and `streamlit` as the two libraries we'll be using this example

![Step6](https://github.com/CUNYTechPrep/2023-fall-DS-dev/blob/main/2023-curriculum/Week-10-Neural-Networks-HuggingFace/TA%20Tips/huggingface%20space%20screenshots/createrequtxt.png)
## Step 7
After committing the requirements file, create another file called `app.py` that'll contain our code leveraging the image captioning model

**Our Code**:
```
from transformers import pipeline
import streamlit as st

pipe = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

url = st.text_area("enter image address:")

if url:
    out = pipe(url)
    st.json(out)
```

![Step7](https://github.com/CUNYTechPrep/2023-fall-DS-dev/blob/main/2023-curriculum/Week-10-Neural-Networks-HuggingFace/TA%20Tips/huggingface%20space%20screenshots/createapppy.png)

After committing `app.py` to the main branch, we can use our app. To commit using the terminal, do the following:
- `git add app.py`
- `git commit -m "first edit"`
- `git push`
## Step 8
Our app page should look like the screenshot below, a text box asking for an image address. Perhaps paste `https://gray-wowt-prod.cdn.arcpublishing.com/resizer/FAzqkVcPX-lKa-B5Th-WtPfuYds=/1200x675/smart/filters:quality(85)/cloudfront-us-east-1.images.arcpublishing.com/gray/4ORTTBVIXBMZDKJJFDWGRUQR3U.jpg` as our example image

![Step8](https://github.com/CUNYTechPrep/2023-fall-DS-dev/blob/main/2023-curriculum/Week-10-Neural-Networks-HuggingFace/TA%20Tips/huggingface%20space%20screenshots/code.png)
## Step 9
Our generated text is returned in JSON as a standard format for storing and transporting data. In this example, we receive the following response:
```
[
   0 : {
        "generated_text":"a man in a suit and tie smiling"
       }
]
```
![Step9](https://github.com/CUNYTechPrep/2023-fall-DS-dev/blob/main/2023-curriculum/Week-10-Neural-Networks-HuggingFace/TA%20Tips/huggingface%20space%20screenshots/codewresult.png)
