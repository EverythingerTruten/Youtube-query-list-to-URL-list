# Youtube-query-list-to-URL-list
This python code processess a txt file with each line being a possible youtube search query with the URL corresponding to the first result when looking up that query on youtube. There are probably different ways of using it but I personally use it as a way to quickly write playlists for the java Discord music bo that jagrosh created. (https://jmusicbot.com/)

Before running this program make sure that you have both the "os" and "googleapiclient.discovery" libraries installed. You can do so by following these steps:

1. Open a terminal or command prompt.
2. To install the os library, type the following command and press Enter: "pip install os"
This will install the os library, which provides a way to work with the operating system in Python.
3. To install the googleapiclient.discovery library, type the following command and press Enter: "pip install google-api-python-client"
This will install the google-api-python-client package, which includes the googleapiclient.discovery module. This module provides a way to interact with Google APIs using Python.

If you do not have pip installed, the installation process will not work. You can install it by following the steps this article gives you: https://www.activestate.com/resources/quick-reads/how-to-install-pip-on-windows/

For people who cannot find their youtube API key, follow these steps:

Go to the Google Developers Console (https://console.developers.google.com/).

1. If you're not already signed in, sign in with your Google account.
2. Click the project drop-down and select or create the project for which you want to add the API key.
3. Click the navigation menu and select APIs & Services > Credentials.
4. On the Credentials page, click the Create credentials button and select API key.
5. In the Create a new API key dialog, select the type of API key you want to create. In this case, you will want to select "YouTube Data API v3".
6. Copy the generated API key.

Once you have your API key, you can paste it into your Python program in the correct place to access the YouTube Data API.

Remember to enable the "Youtube Data API V3" by visiting this link: https://console.developers.google.com/apis/api/youtube.googleapis.com/overview?project=707005156301

Sometimes you have to wait for the API to propagate in Google's servers, so wait a couple minutes before running the program.
