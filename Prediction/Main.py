import sys

import app


def main():
    app.login_window.show()
    # app.page_window.show()
    sys.exit(app.app.exec_())


if __name__ == '__main__':
    main()
