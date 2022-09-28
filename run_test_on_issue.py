import time


def run_test_on_issue():
    while True:
        print("Start running tests")
        issue_list = get_issue_list_from_db()
        if len(issue_list) == 0:
            time.sleep(5)
        else:
            while len(issue_list) > 0:
                task_name = issue_list.pop
                get_file(task_name)
                try:
                    result = run_test()
                except:
                    print("Error while trying to run test")

                try:
                    put_test_result_to_db(result)
                except:
                    print("Error while trying to put test result to DB")

                delete_file(task_name)


def get_file():
    pass


def delete_file():
    pass


def get_issue_list_from_db():
    issue_list = []
    return issue_list


def run_test():
    return 0


def put_test_result_to_db(test_result):
    pass


if __name__ == '__main__':
    run_test_on_issue()
