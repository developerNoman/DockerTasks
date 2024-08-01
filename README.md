# DockerTasks
<p>The repo contains the docker tasks 1,2,3</p>
<h1>Task1:</h1>
<p>(Installation and basic usage)
<ul>
	<li>Install Docker on your local machine and verify that it is running correctly by running the hello-world example.</li>
<li>Pull and run the official nginx Docker image in detach mode and access the web server from your browser.</li>
<li>Stop and remove the nginx container.</li>
</ul>
</p>

<h1>Task2:</h1>
<p>(Building and running a custom Docker image)
<ul>
	<li>Create your own docker by creating a custom image that can install the following tools:
		<ol>
<li>CMake, Make</li>
<li>Python, Python3</li>
<li>Git</li>
<li>GCC</li>
		</ol>			
</li>
<li>Build and run a simple C++ application inside the Dockerfile</li>
<li>Build your image</li>
	<li>Map your source directory with the container - Volume mapping. (Remember to map your source directory from your user to the Docker's user, do not use Root user).
</li>
	<li>Run docker.</li>
	<li>Upload your custom image to Dockerhub.</li>
</ul>
</p>

<h1>Task3:</h1>
<p>(Create a Docker Compose setup for a Python server-client application where the client communicates with the server within a Docker network through different API/URI endpoints)

<ul>
	<li>Implement the Python server to handle:
		<ol>
<li>GET /health to return an OK status if the server is running.
</li>
<li>POST /ping to return a JSON response {"type": "pong", "time": "current_time"}.</li>
<li>POST /data to accept a JSON request {"jsonrpc": "2.0", "method": "message-1"} and respond with the original message with the current time {"jsonrpc": "2.0", "method": "message-1", “time”:"current_time"}.
</li>
		</ol>			
</li>
<li>Implement the Python client to handle:
		<ol>
<li>Perform a health check by sending a GET request to /health.
</li>
<li>Send a POST request to /ping with JSON {"type": "ping"} and handle the response.</li>
<li>Send a POST request {"jsonrpc": "2.0", "method": "message-1"} to /data and handle the response.
</li>
	<li>Repeat requests at 5 sec intervals in a while loop </li>
		</ol>			
</li>
	<li>Ensure the server is only accessible within the Docker network.</li>
	<li>Use Docker Compose <a href=https://docs.docker.com/compose/compose-file/05-services/#depends_on>depends_on</a> and condition for <a href="https://docs.docker.com/compose/startup-order/">services health checks</a>.</li>
</ul>
</p>
