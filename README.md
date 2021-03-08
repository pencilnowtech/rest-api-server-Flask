This document lists the steps needed to run this API server, supplied
along with this document.

Steps to run API Server
-----------------------

*To run the alarm API server, it is assumed that python3 is already
installed in the system.*

1.  Go to the root folder

2. Install Python dependencies as:

   ```shell
   pip install -r requirements.txt
   ```

3.  Now, run the API Server from same folder as:

    ```shell
    python AlarmApp.py
    ```

    It will output, the location where API server is running:

    ```shell
    Running on <http://127.0.0.1:5000/>
    ```
    
    This location will be used for various REST requests as we will see
    soon

Issuing REST Requests
---------------------

Various REST requests can be issued through different tools such as
curl, etc:

- To list all the alarms:

  ```shell
  curl <http://127.0.0.1:5000//alarms>
  ```

-   To add a new alarm:

    ```shell
    curl -X POST -H "Content-Type: application/json" -d{\\"days\\":\[3,6\],\\"alarm\_id\\":4,\\"name\\":\\"deep-alarm\\",\\"status\\":1,\\"time\\":\\"05:00\\"}<http://127.0.0.1:5000//alarms>
    ```

-   To update an existing alarm:

    ```shell
    curl -X PUT -H "Content-Type: application/json" -d{\\"days\\":\[3,6\],\\"alarm\_id\\":1,\\"name\\":\\"new-alarm\\",\\"status\\":1,\\"time\\":\\"05:00\\"}<http://127.0.0.1:5000//alarms/1>
    ```

-   To delete an existing alarm:

    ```shell
    curl -X DELETE <http://127.0.0.1:5000//alarms/1>
    ```

Test Cases
----------

This application also covers some basic test cases, which are stored
inside tests/ directory.

To run the test cases:

1.  First, run the API server as was mentioned above

2.  In *separate command prompt*, run the test cases from the root
    folder of  project as:

    ```shell
    python -m pytest
    ```

    All test cases should run successfully.
    
    It tries to cover all the implemented scenarios. However, some edge
    cases are missing as discussed before.
