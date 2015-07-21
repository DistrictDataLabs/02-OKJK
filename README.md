# 02-OKJK

Summary of Problem: There are a lot of economic indicators being captured by the Bureau of Labor Statistics (BLS). However, there is only a small set of the population that understands what these indicators mean. OKJK tried to combine multiple economic indicators into a single score. The core idea behind the app is that it allows disparate economic indicators (like age, price of grapefruits, and unemployment) be combined into one single economic score. Their app is really about normalizing and displaying more than it is about analyzing any particular pattern. As age, unemployment, and the price of a grapefruit increase, states’ economic scores decrease. To demonstrate this, OKJK created an interactive web application that rates economic development based on user input relating to age, unemployment rate, and price of an average grapefruit. OKJK uses requests to get data from the Bureau. OKJK implements a pandas DataFrame which allows them to quickly combine, normalize, and fill in data. Their website runs on Heruko, a platform that allows developers to run applications entirely in the cloud. It uses Vincent for visualization and Flask for its framework. 


[Check it out](http://floating-plains-7989.herokuapp.com)


#software architecture diagram
![alt text](http://i61.tinypic.com/2vifeh5.jpg)
[software architecture link](http://i61.tinypic.com/2vifeh5.jpg)

#data flow diagram
![alt text](http://i58.tinypic.com/oswv3m.jpg)
[data flow link](http://i58.tinypic.com/oswv3m.jpg)
