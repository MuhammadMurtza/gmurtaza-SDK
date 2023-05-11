# LOTR_SDK Design
The LOTR_SDK is designed to provide an easy-to-use interface for accessing the Lord of the Rings API endpoints for movies and quotes. The SDK is structured around a client class that handles making requests to the API, and a set of endpoint classes that provide methods for retrieving data from the API.

## Base Class
The LOTR_SDK class is the main entry point for the SDK. It is responsible for handling the bearer token and making requests to the API. The LOTR_SDK class contains the following methods:

### ```__init__(self, bearer_token: str) -> None```
This method initializes the LOTR_SDK object with the specified bearer token.

### ```_make_request(self, endpoint: str) -> dict```
This method is used to make HTTP GET requests to the API. It takes an endpoint string as input, and returns a JSON object with the response data.

### Endpoint Classes
The endpoint classes provide methods for retrieving data from the API. Each endpoint class corresponds to a different API endpoint. The endpoint classes contain the following methods:

### ```__init__(self, client: LOTR_SDK) -> None```
This method initializes the endpoint object with a reference to the LOTR_SDK client.

### ```<method_name>(self, <args>) -> dict```
These methods are used to retrieve data from the API. They take input parameters as necessary, and return a JSON object with the response data.

The endpoint classes should be implemented using a consistent design pattern. They should use the _make_request method of the LOTR_SDK client to make requests to the API. They should also include error handling to handle any exceptions that may be raised during the request.