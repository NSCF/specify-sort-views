## Sorting and formatting [Specify 6](specifysoftware.com) forms XML files

A simple command line script for formatting the views.xml files that define Specify data entry forms. Doing so makes form customization a little easier. 

This tool uses Click, see instructions there to create and run this tool in a virtual environment, or else from a terminal / "black window that hackers use" run, just run

`pip install -r requirements.txt`

...and then

`pip install --editable .`

Then to format a file, run

`sortviews --file "viewsfileyouwanttoformat"`

`viewsfileyouwanttoformat` needs to be the full filename and path, and must have double quotes. The easiest is to open the terminal above in your Specify/config folder where all the files reside, and then you won't have to add long path names, just the subfolders. For example,

`sortviews --file "insect/guest/ento.views.xml"`

...will format that one file for the entomology discipline. 

You may have to open your terminal as an administrator on your system to be able to run this command. 

If you find problems, please add them here in the issues :-)

