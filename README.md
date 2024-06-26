# Castbox_erfan Podcast with Django Rest Framework

## Introduction
Welcome to the Castbox Podcast with Django Rest Framework! This project is designed to provide a seamless and enjoyable podcast listening experience using the power of Django Rest Framework.

## Features
- **User Authentication**: Users can create accounts, log in, and enjoy personalized podcast recommendations.
- **Podcast Streaming**: Seamless streaming of podcast episodes with high-quality audio.
- **Search Functionality**: Users can easily search for their favorite podcasts and episodes.
- **Episode Bookmarking**: Users can bookmark episodes to listen to later.

## Installation
To install and run the Castbox Podcast with Django Rest Framework, follow these steps:

1. Clone the repository from GitHub.
2. Create a virtual environment and activate it.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Set up the database by running `python manage.py migrate`.
5. Start the development server with `python manage.py runserver`.

## API Endpoints
The following are some of the API endpoints available in the Castbox Podcast with Django Rest Framework:

- api/ episodes/
- api/ episodes/<int:pk>/
- api/ episodes/<int:pk>/mention/
- api/ api/
- api/ users/register/
- api/ users/login/
- api/ users/profile/
- api/ users/<int:pk>/follow_channel/
- api/ users/<int:pk>/unfollow_channel/
- api/ users/<int:pk>/followed_channels/
- api/ channels/
- api/ channels/<int:pk>/
- api/ likes/
- api/ likes/<int:pk>/
- api/ comments/
- api/ comments/<int:pk>/
- api/ playlists/
- api/ playlists/<int:pk>/
## Feedback
We value your feedback! If you have any suggestions, feature requests, or bug reports, please feel free to open an issue on the GitHub repository.

Thank you for using the Castbox Podcast with Django Rest Framework. Happy podcast listening!