# What is this?
The Course Hero website allows students to upload materials to assist other students. Unfortunately, this may include items which violate their instructors' intellectual property rights. Course Hero professes a commitment to protecting intellectual property and provides an easy to use webform (https://www.coursehero.com/copyright-infringement/) to request the removal of infringing materials.

However, the site does not seem to standardize the names / abbreviations for departments and courses, and it uses the uploading student's favored spelling of the instructor's name. This makes it difficult for an instructor to be sure they've checked all materials which might belong to them.

This is a tool which automates the process of searching the site to help me more easily keep tabs on my intellectual property.

It is thus extremely rough and probably not very user friendly. That said, I am making them public in case others find them useful.

These tools are provided in the hope that they will be useful to teachers seeking to protect their intellectual property, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

I am not a lawyer; nothing in here should be construed as legal advice. Make sure you understand your rights and responsibilities under the DCMA and other applicable laws before submitting takedown requests. These tools are provided with no warranty or claim that their use is consistent with any law, policy, terms of service, or any other constraint. IF YOU CHOOSE TO USE THEM, YOU AGREE TO REVIEW AND COMPLY WITH ALL RELEVANT POLICIES, INCLUDING SITE TERMS OF SERVICE, AND YOU AGREE THAT YOUR USE IS SOLELY AT YOUR OWN RISK.

Questions, requests, complaints, or other feedback (or pull-requests to improve it!) are welcome through this project's github page

    https://github.com/HatakoHaterson/CourseZero

Please understand that this is not an active project for me; I will monitor the project on github very infrequently.

-- 復讐者

#  Instructions
##  Startup

If you want to see what this looks like without running it, you can view a static image of the main notebook (though you won't be able to see the actual output) on Jupyter:

https://nbviewer.jupyter.org/github/HatakoHaterson/CourseZero/blob/master/Notebooks/IP_search_helper.ipynb?flush_cache=true

If you have Jupyter/iPython running on your computer, you don't need me to tell you what to do.

For most folks, it will be easiest to run it on your own free mini-server using Binder:

https://mybinder.org/v2/gh/HatakoHaterson/CourseZero/master?filepath=Notebooks%2FIP_search_helper.ipynb

##  Running

Once you've got the notebook open, select 'Run all' from the 'Cell' menu. Alternatively, press the run button in the toolbar repeatedly until you've reached the bottom of the page.

When the cells below run, they will display a selection menu of all CSU campuses. Use it to select the CSU you want to search.

NB, for now this will only work with CSU campuses. If there is a demand for covering more institutions, please leave a note on the github page

When the search starts it will display a message like "Searching for California State University Dominguez Hills". You may need to wait a few seconds for it to complete.

When the search completes, it will display buttons with all the departments found for the campus. Select all the departments you want to search for materials from. That will initiate a search for courses associated with those departments; from there you'll be able to select files students have uploaded for those courses.

Again, the site does not seem to standardize the names students enter. Thus you and your classes may be identified in some rather odd ways....

##  Troubleshooting

Please note that each step will take several seconds to run as the tool queries the Course Hero site. I didn't add any progress notifications, so it may seem to be frozen. Please be patient while it's working --if you click buttons before the previous search has finished, you may discover why I said it's not entirely user friendly.

If you have trouble, select 'Restart and clear output' from the 'Kernel' menu and try again.