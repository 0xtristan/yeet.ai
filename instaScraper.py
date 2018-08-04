import subprocess
from instagram_scraper.app import InstagramScraper
import os
import subprocess
from argparse import ArgumentParser

def scrape_insta(ig_location_id):

    args = '''-u "jamesjames12344kajs" -p "qwerty12345" --location {0} --include-location --maximum 5 --media-types "image" --destination "images/{1}" -v'''.format(ig_location_id,ig_location_id)
    #1027421101

    cmd = 'python app.py '

    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(str(dir_path)+"/instagram_scraper/")

    print(cmd+args)

    p = subprocess.Popen(cmd+args, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    result = out.split('\n')


# subprocess.call(["instagram-scraper","-u","jamesjames12344kajs", "-p", "qwerty12345", "--location", "1027421101",
#                  "--include-location", "--maximum", "5", "--media-types", "image",
#                  "--destination", "/Volumes/Samsung 250GB SSD/Downloads/BarLuca_scrape2", "-v"])

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--name", required=True)

    args = parser.parse_args()
    print(args)

    ig_location_id = '1027421101'

    scrape_insta(ig_location_id)