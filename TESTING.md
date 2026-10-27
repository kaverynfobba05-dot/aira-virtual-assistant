Aira — Virtual AI Assistant



Manual Testing Report



1\. Testing Objective



The objective of this testing process is to verify that Aira responds correctly to supported commands, handles invalid inputs safely, and exits gracefully.



2\. Test Environment



\* Application: Aira — Virtual AI Assistant

\* Programming Language: Python

\* Interface: Command-line console

\* Testing Method: Manual testing



3\. Test Cases



| Test ID | Feature                   | Test Input                        | Expected Result                                 |

| ------- | ------------------------- | --------------------------------- | ----------------------------------------------- |

| TC-01   | Startup                   | Launch the program                | Aira greets the user and asks for their name    |

| TC-02   | Name storage              | Enter a name                      | Aira remembers the name during the session      |

| TC-03   | Greeting                  | hello                             | Aira greets the user                            |

| TC-04   | Assistant name            | name                              | Aira displays its name                          |

| TC-05   | User name                 |  my name                          | Aira displays the stored name                   |

| TC-06   | Current time              | time                              | Aira displays the current time                  |

| TC-07   | Current date              | date                              | Aira displays the current date                  |

| TC-08   | Calculator addition       | 'calculator', then '10', '+', '5' | Result is 15                                    |

| TC-09   | Calculator subtraction    | 'calculator', then '10', '-', '5' | Result is 5                                     |

| TC-10   | Calculator multiplication | 'calculator', then '4', '\*', '3'  | Result is 12                                    |

| TC-11   | Calculator division       | 'calculator', then '10', '/', '2' | Result is 5                                     |

| TC-12   | Division by zero          | 'calculator', then '10', '/', '0' | Aira displays an error message                  |

| TC-13   | Invalid calculator input  | Enter 'abc' instead of a number   | Aira reports invalid numerical input            |

| TC-14   | Invalid operator          | Enter '%' as the operator         | Aira reports an invalid operation               |

| TC-15   | Motivational quote        | 'quote'                           | Aira displays a motivational quote              |

| TC-16   | Joke                      | 'joke'                            | Aira displays a joke                            |

| TC-17   | Random fact               | 'fact'                            | Aira displays a fact                            |

| TC-18   | Guessing game             | 'game'                            | Aira starts the number-guessing game            |

| TC-19   | Invalid game input        | Enter 'abc' during the game       | Aira handles the invalid input                  |

| TC-20   | Out-of-range guess        | Enter '15' during the game        | Aira asks for a number between 1 and 10         |

| TC-21   | Activity recommendation   | 'activity'                        | Aira recommends an activity based on the time   |

| TC-22   | Perceptron valid input    | 'perceptron', then '1', '1'       | Weighted total is 0.3 and output is 1           |

| TC-23   | Perceptron invalid number | Enter '2' and '1'                 | Aira rejects the invalid input                  |

| TC-24   | Perceptron text input     | Enter 'abc' and '1'               | Aira rejects the invalid input without crashing |

| TC-25   | Help menu                 | 'help'                            | Aira lists available commands                   |

| TC-26   | Unknown command           | 'randomtext123'                   | Aira displays a friendly fallback message       |

| TC-27   | Exit                      | 'bye'                             | Aira exits gracefully                           |



4\. Test Results



After executing each test case, record its actual result and status.



| Test ID        | Actual Result                            | Status      |

| -------------- | ---------------------------------------- | ----------- |

| TC-01 to TC-27 | Record the observed output for each test | Pass / Fail |



Do not mark a test as passed until you have executed it and verified the actual result.



5\. Conclusion



Manual testing is used to verify Aira's supported commands, calculation behaviour, input validation, rule-based recommendations, perceptron demonstration, and graceful termination.



The final test status should be based on the results observed during execution.



