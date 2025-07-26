import requests
import time


def get_tiktok_video_url(url):
    time.sleep(1)
    api = "https://tikwm.com/api/?url=" + url
    response = requests.get(api).json()

    if response["code"] == 0:
        if 'images' in response["data"]:
            images = []
            for image in response["data"]["images"]:
                images.append(image)

            return 'img', images
        else:
            video_url = response["data"]["play"]

            return 'url', video_url
    else:
        print(f"Ошибка (get_tiktok_video_url): {response["msg"]}")
        return False

