from os.path import exists
import asyncio
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import _thread
import requests


def fire_and_forget(f):
    """対象関数を非同期で投げっぱなしにするためのデコレータ"""
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)
    return wrapped


class TestWebserver:

    @classmethod
    @fire_and_forget
    def start_web_server(cls, port_num: int, test_class_name: str):
        """テスト用のWEBサーバを起動する"""
        document_root: str = f'document_roots/{test_class_name}'
        if not exists(document_root):
            raise FileNotFoundError(f'document root is not exists. document_root: {document_root}')

        class __Handler(SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, directory=document_root, **kwargs)

            def do_POST(self):
                if self.path.startswith('/kill_server'):
                    def kill_me_please(server):
                        server.shutdown()
                    _thread.start_new_thread(kill_me_please, (httpd,))
                    self.send_error(500)
                    print(f'webserver stopped. port_num: {port_num}, document_root: {document_root}')

        TCPServer.allow_reuse_address = True
        with TCPServer(('', port_num), __Handler) as httpd:
            print(f'webserver started. port_num: {port_num}, document_root: {document_root}')
            httpd.serve_forever()

    @classmethod
    def stop_web_server(cls, port_num: int):
        """テスト用のWEBサーバを停止する"""
        requests.post(f'http://localhost:{port_num}/kill_server')
