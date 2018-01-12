# home-env

Simple home environment monitor using the sense hat.

#### Description

Our home gets pretty cold and dry in the winter and I wanted to monitor how the temp and humidity changes over time. While the sesors provided by the sense hat are not extremely accurate I subscribed to the 'good nuf' philosophy here to gather some basic data I can analyze.

#### Instructions

The app has one piece that will simply wake up to take a reading on some interval and write that to a local text file. 
In addition to logging data continuously, I thought it would useful to create this as a simple web app using Flask so that I could also check it any time asychronously. In addition to getting the current reading, I want to show the historical graph of the readings over time in a basic webpage.

There are requirements to be able to run flask and I will not cover the setup here. More details can be found in the references below. Note: it is advisable to run in a virtual environment as well; details for this can also be found below.

#### Reference

[Flask info](http://flask.pocoo.org/)
[Virtualenv info](https://virtualenv.pypa.io/en/stable/)
