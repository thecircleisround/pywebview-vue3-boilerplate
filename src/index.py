import os
import threading
import webview
import requests

from time import time


class Api:
    def fullscreen(self):
        webview.windows[0].toggle_fullscreen()

    def save_content(self, content):
        filename = webview.windows[0].create_file_dialog(webview.SAVE_DIALOG)
        if not filename:
            return

        with open(filename, 'w') as f:
            f.write(content)

    def ls(self):
        return os.listdir('.')

    def showCount(self, count):
        print(f'Current Count{count}')
        return


def get_entrypoint():
    def exists(path):
        return os.path.exists(os.path.join(os.path.dirname(__file__), path))

    if exists('../gui/index.html'):  # unfrozen development
        try:
            url = 'http://localhost:1234'
            get = requests.get(url)
            if get.status_code == 200:
                return url
        except requests.exceptions.RequestException:
            print('Parcel server not running. Trying static files')
        return '../gui/index.html'

    if exists('../Resources/gui/index.html'):  # frozen py2app
        return '../Resources/gui/index.html'

    if exists('./gui/index.html'):
        return './gui/index.html'

    raise Exception('No index.html found')



entry = get_entrypoint()

if __name__ == '__main__':
    api = Api()
    window = webview.create_window('pywebview-vue boilerplate', entry, js_api=api)
    webview.start(debug=True)
