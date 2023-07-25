Pascal's triangle is the triangular array of numbers that begins with 1 on the top and with 1's running down the two sides of a triangle. Each new number lies between two numbers and below them, and its value is the sum of the two numbers above it.

Create a Flask API endpoint that takes in an integer as a parameter in a POST request. Use that integer to generate Pascal's triangle in a separate function call. The function should be located in a separate module inside a separate Python package and must be imported from the package, not directly from the module. The function should return a Python dictionary to the controller, which in turn should return the dictionary as an HTTP response to the client.

The structure of the dictionary, and in turn the response, should be as follows:

```
{
    "row_1": [1],
    "row_2": [1, 1],
    "row_3": [1, 2, 1],
    "row_4": [1, 3, 3, 1]
    "row_5": [1, 4 , 6, 4, 1]
}
```

Assuming the number of rows requested in the HTTP request is 4, the number of rows should be 4.

Do not statically type your solution. Generate the dictionary/response dynamically. The folder structure will accompany this email in the form of a zip file.

This application should be dockerized and should run on port 8080.

Here are some additional details about the requirements:

- The function to generate Pascal's triangle should be recursive.
- The Flask API endpoint should be able to handle multiple concurrent requests.
- The application should be dockerized. Create a docker file and enable port 8080 to be accessed over a network.
- Push your solution to a github repository.
- Use Postman to test your API endpoints against dynamic input.

hints:

- Use this tutorial to get started. https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/
- Research on how to create modules and packages in python. https://www.w3schools.com/python/python_modules.asp
- Research on how to return json data from a dictionary in flask. https://www.geeksforgeeks.org/how-to-return-a-json-response-from-a-flask-api/
