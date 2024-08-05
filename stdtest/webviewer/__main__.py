from stdtest import *
from .webviewerx import WebViewerX

if __name__ == "__main__":
    # app = QApplication(['', '--no-sandbox'])
    # w = WebViewerX()
    # w.resize(640, 480)
    # w.set_htmlbody("""
    #     <p>$$ e = mc^2 $$</p>
    #                """)
    # w.show()
    # sys.exit(app.exec())

    import webview

    window = webview.create_window('', url="file:///Users/dy/gits/cc/alegs/index.html")
    webview.start()