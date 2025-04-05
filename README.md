# Moodify – Project Documentation

## Project Description

Moodify is a Python-based API that provides song recommendations tailored to different moods. Users can specify their mood through an HTTP GET request, and the API will respond with a curated list of songs. The project is designed to bring joy, inspiration, or comfort to users by matching music with their emotional states.

## Project Phases

### 1. Planning:
- **Goal:** To create an API that delivers personalized song recommendations based on a user's mood, enhancing their music-listening experience.
- Define the features, design the mood-based song database, and outline the project structure.

### 2. Development:
- Write the code for the API using Python and set up mood-based song recommendations.
- Implement robust error handling for seamless user interaction.

### 3. Testing:
- Use tools like Postman to validate the API functionality.
- Ensure accurate responses for valid requests and proper error handling for invalid inputs.

### 4. Deployment:
- Host the API on a local or cloud server to make it accessible to users.
- Optimize performance for reliability and scalability.

### 5. Documentation:
- Prepare a user guide detailing how to run and test the API.
- Include a summary of the endpoints, parameters, and expected responses.

## Requirements

### Software:
- Python 3.x
- Postman (for testing)

### Libraries:
- http.server
- json
- urllib.parse

## How to Run the Project

1. Clone or download the project files.
2. Open a terminal and navigate to the project directory.
3. Run the following command to start the server:

   ```bash
   python moodify_server.py

4. The server will start on port 8080 by default.

# Song Recommendation API

This API provides song recommendations based on the mood provided by the user.

## Endpoints

### GET `/recommend`

Fetches a list of song recommendations based on the mood.

#### Query Parameters:

| Parameter | Type    | Description                             |
|-----------|---------|-----------------------------------------|
| `mood`    | integer | Represents the mood (1-5)               |

#### Mood Values:

| Value | Mood Description |
|-------|------------------|
| `1`   | Happy            |
| `2`   | Sad              |
| `3`   | Motivational     |
| `4`   | Party            |
| `5`   | Gym Freak        |

## Steps to Test Using Postman

1. Open Postman and create a new `GET` request.
2. Enter the URL:

    ```
    http://localhost:8080/recommend?mood=[number]
    ```

    Replace `[number]` with a mood number (e.g., `1` for Happy).

![postman](https://github.com/user-attachments/assets/5aa02f07-9ef2-43ea-ae27-f5113a1a0a86)

3. Send the request.
4. Verify the response contains song recommendations.
5. Test invalid or missing parameters to verify error handling.









