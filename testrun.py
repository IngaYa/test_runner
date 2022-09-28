import time


def testrunner():
    while True:
        issues = get_issue_list()
        if len(issues) > 0:
            pass
        else:
            time.sleep(5)

def get_issue_list():
    pass

if __name__ == '__main__':
    testrunner()
