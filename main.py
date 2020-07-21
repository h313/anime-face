#!/usr/bin/env python3
from github import Github
import numpy as np
import argparse

from profile_tester import get_profile_image, check_image

parser = argparse.ArgumentParser(description='Run the test!')
parser.add_argument('api_key', metavar='KEY', type=str, nargs='+',
                    help='An API key for GitHub')

has_anime_propic = np.empty(1000000)
user_activity = np.zeros(1000000)


def main():
    # Loop through the first one million users
    for i in range(0, 1000000):
        g = Github("access_token")
        user = g.get_user(str(i))

        # Add every event ever into the list
        event_count = 0
        for event in user.get_events():
            event_count += 1

        # If they only have one event, that's an inactive user. Don't count them
        if event_count > 1:
            user_activity[i] = event_count

            # Check if profile picture is anime
            if check_image(get_profile_image(user.avatar_url, "img.png")):
                has_anime_propic[i] = True


if __name__ == '__main__':
    main()
