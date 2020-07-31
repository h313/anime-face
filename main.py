#!/usr/bin/env python3
from github import Github
import numpy as np
import argparse

from profile_tester import get_profile_image, check_image

parser = argparse.ArgumentParser(description='Run the test!')
parser.add_argument('api_key', metavar='KEY', type=str, nargs='+',
                    help='An API key for GitHub')

has_anime_propic = []
user_activity = []


def main():
    g = Github("")
    f = open("data.csv", "a")
    # Loop through the first fifty thousand users
    for i in range(0, 1000):
        print(str(i) + ': ' + str(g.get_rate_limit().core.remaining))
        user = g.get_user(str(i))

        # Add every event ever into the list
        event_count = 0
        for event in user.get_events():
            event_count += 1

        # If they only have one event, that's an inactive user. Don't count them
        if event_count > 1:
            user_activity.append(event_count)

            # Check if profile picture is anime
            if check_image(get_profile_image(user.avatar_url, "img.png")):
                has_anime_propic.append(True)
                has_anime_propic_bool = True
            else:
                has_anime_propic.append(False)
                has_anime_propic_bool = False

            print(str(has_anime_propic_bool) + ',' + str(event_count) + '\n')
            f.write(str(has_anime_propic_bool) + ',' + str(event_count) + '\n')

    f.close


if __name__ == '__main__':
    main()
