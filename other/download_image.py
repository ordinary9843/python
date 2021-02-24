from bs4 import BeautifulSoup
import requests
import os


def main():
    url = input('請輸入網站連結：')

    print('開始下載')

    request = requests.get(url)
    html = BeautifulSoup(request.text, 'html.parser')
    title = html.select('.this-description-name')[0].get_text().strip()
    pictures = html.select('picture img')

    desktopPath = os.path.join(os.path.expanduser('~'), 'Desktop')
    productPath = desktopPath + '\\商品\\'
    itemPath = productPath + str(title) + '\\'

    if not os.path.exists(productPath):
        os.mkdir(productPath)

    if not os.path.exists(itemPath):
        os.mkdir(itemPath)

    for i, t in enumerate(pictures):
        url = 'https:' + t['src']
        img = requests.get(url)

        with open(itemPath + str(i + 1) + '.jpg', 'wb') as file:
            file.write(img.content)

    print('下載完成')


if __name__ == '__main__':
    main()
