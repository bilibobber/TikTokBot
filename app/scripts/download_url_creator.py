import requests


def get_download_url(url):
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
        print("Ошибка:", response["msg"])
        return False

