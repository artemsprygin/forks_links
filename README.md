# Forks links

While I'm doing projects, forked from [https://github.com/devmanorg](https://github.com/devmanorg), after finishing a project I usually check how other people did same task to find most beautiful solution. I wrote this script to make it simple: just launch the script and you'll have an HTML page with list of all links, opened in your browser!

# How it works

* You can launch it with parameter -l or --link — link to the original repository. If you run script without parameters, it will ask you to write it.

* The link can be to a whole repo: `https://github.com/devmanorg/10_coursera` or link to a specific file: `https://github.com/devmanorg/10_coursera/blob/master/coursera.py`. You'll have list of links to repos or to a specific file in other repos respectively.

* Script will generate HTML file with list of all links to a forked repos or files and save it in the same directory with itself.

* Script will ask you whether you want automatically open generated file in browser or not. If you type 'y' or 'yes', page will be opened in your browser.

# Usage example

```bash
$ python forks_links.py -l https://github.com/devmanorg/10_coursera/blob/master/coursera.py
Would you like to open generated HTML file in browser? y/n
n
https://github.com/kostyaeremin/10_coursera/blob/master/coursera.py
https://github.com/xdass/10_coursera/blob/master/coursera.py
https://github.com/vitalib/10_coursera/blob/master/coursera.py
https://github.com/Tonycrosss/10_coursera/blob/master/coursera.py
https://github.com/sergeikhrustalev/10_coursera/blob/master/coursera.py
https://github.com/AntonGorynya/10_coursera/blob/master/coursera.py
https://github.com/IrinaNizova/10_coursera/blob/master/coursera.py
https://github.com/BioshokMe/10_coursera/blob/master/coursera.py
https://github.com/a-savinov/10_coursera/blob/master/coursera.py
https://github.com/gaisin/10_coursera/blob/master/coursera.py
https://github.com/StMrKirk/10_coursera/blob/master/coursera.py
https://github.com/dathbezumniy/10_coursera/blob/master/coursera.py
https://github.com/p-well/10_coursera/blob/master/coursera.py
https://github.com/erlong15/10_coursera/blob/master/coursera.py
https://github.com/m0dusX/10_coursera/blob/master/coursera.py
https://github.com/mechanicalmachine/10_coursera/blob/master/coursera.py
https://github.com/voron434/10_coursera/blob/master/coursera.py
https://github.com/jusnikolaev/10_coursera/blob/master/coursera.py
https://github.com/andeniel/10_coursera/blob/master/coursera.py
https://github.com/mcproger/10_coursera/blob/master/coursera.py
https://github.com/DM45/10_coursera/blob/master/coursera.py
https://github.com/evgeny-shestakov/10_coursera/blob/master/coursera.py
https://github.com/velios/10_coursera/blob/master/coursera.py
https://github.com/maksart72/10_coursera/blob/master/coursera.py
https://github.com/alpden550/10_coursera/blob/master/coursera.py
https://github.com/romabiker/10_coursera/blob/master/coursera.py
https://github.com/netolyrg/10_coursera/blob/master/coursera.py
https://github.com/piterskikhsa/10_coursera/blob/master/coursera.py
https://github.com/KhorinVitaly/10_coursera/blob/master/coursera.py
https://github.com/Ildarik/10_coursera/blob/master/coursera.py
``` 