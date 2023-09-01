# setting-up-github for CTP
0. Create a fork of this repo. ![forking](https://raw.githubusercontent.com/zd123/images-for-class/main/forking-image-instructions/01-fork-button.png)

0. Name that fork `my-fork-2023-fall-data-science` ![enter image description here](https://github.com/zd123/images-for-class/blob/main/forking-image-instructions/02-naming-fork.png?raw=true)
	
0. Copy the link of your forked repo.  ![enter image description here](https://github.com/zd123/images-for-class/blob/main/forking-image-instructions/03-getting-fork-link.png?raw=true)

0. Open your terminal

0. Clone your forked version of the original version by typing in `git clone` then pasting the link you just copied. 
	* `git clone https://github.com/[YOUR-GITHUB-USER-NAME]/my-fork-2023-fall-data-science.git`

## Setting it up to listen for updates. 

0. Navigate to inside that repo. 
	* `cd my-fork-2023-fall-data-science`

0. Set the upstream (Note this is the link of the CUNY Tech Preps version of the repo, not your fork)
	* IF YOU ARE IN __TUESDAYS__ CLASS:  
		* `git remote add upstream https://github.com/CUNYTechPrep/2023-fall-data-science-tuesday`
	* IF YOU ARE IN __FRDIAYS__ CLASS: 
		* `git remote add upstream https://github.com/CUNYTechPrep/2023-fall-data-science-fridays`



## Modifying the Exercise-DONT-EDIT-MAKE-COPY.ipynb file

0. __FIRST OFF MAKE A COPY OF THE Exercise-DONT-EDIT-MAKE-COPY.ipynb, Rename it as Exercise-[YOUR-INITIALS].ipynb__

0. In your terminal run 
	* `jupyter notebook`
	* If that doesn't work, run `jupyter lab`

0. This should have launched a web page.  In that page, navigate to Week-01/Exercise-[YOUR-INITIALS].ipynb notebook.

0. In the first cell print your name
	* `print('YOUR NAME HERE')`

0. Save the file by clicking the disk icon in the top right. 



## Adding your changes and pushing them to the internet

0. In your terminal that is in repo where you just edited the Exercise file....
0. Add your changes 
	* `git add Week-01-Pandas/Exercise-[YOUR-INITIALS].ipynb`
0. Commit your changes
	* `git commit -m 'YOUR COMMIT MESSAGE HERE'`
0. Push your changes
	* `git push`

## Sanity check
0. Go to your forked github repo. 
0. Navigate to Week-01 and click on the Exercise-[YOUR-INITIALS].ipynb file.
0. Make sure you can see the changes you made. 
0. Copy that exact URL.
0. Paste that URL next to your name in the HW Submission Sheet. 
	* [Tuesday's HW Submission Sheet](https://docs.google.com/spreadsheets/d/1HJb_Hf0dVCOWhw-jimE-E9bnFCROZ1Hx_GLRlQhQ8lA/edit#gid=0)
	* [Friday's 12:30 HW Submission Sheet](https://docs.google.com/spreadsheets/d/1JjyMHmS0n8IuCcYihp5Z9YtTDwsE2ygwIPUqT0tEowE/edit#gid=0)
	* [Friday's 3:30 HW Submission Sheet](https://docs.google.com/spreadsheets/d/1PbQ1JI9cC9WZUnJoEgfoFWhXw7a5wx-53p7bmQmKhKI/edit#gid=0)


## If youre having auth issues... 
* First try to update git: https://git-scm.com/downloads 

If you're still having issues... Follow these instructions CAREFULLY.
* https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

* https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
