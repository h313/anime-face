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
    i = 0
    
    print(g.get_rate_limit())
    for github_id in range(1200000, 1201000):
        try:
            user = g.get_user(github_id)
        except Exception:
            continue
        print('Remaining queries: ' + str(g.get_rate_limit().core.remaining))
        print('Current user_id: ' + str(user.id))

        # Add every event ever into the list
        event_count = 0
        for event in user.get_events():
            event_count += 1

        print('event_count: ' + str(event_count))
        # If they only no events, that's an inactive user. Don't count them
        if event_count >= 1:
            user_activity.append(event_count)

            # Check if profile picture is anime
            if check_image(get_profile_image(user.avatar_url, "img.png")):
                has_anime_propic.append(True)
                has_anime_propic_bool = True
            else:
                has_anime_propic.append(False)
                has_anime_propic_bool = False

            print('has_anime_propic: ' + str(has_anime_propic_bool) + '\n')
            f.write(str(user.id) + ',' + str(has_anime_propic_bool) + ',' + str(event_count) + '\n')
            f.flush()

    f.close


if __name__ == '__main__':
    main()
