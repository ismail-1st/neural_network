# neural_network

<h1>TO RUN DOCKER WITH COMPOSE</h1>
After cloning and changing directory to the repo directory, you will
<ol>
    <li>First build and start the containers in detached mode: 
        <code>docker-compose up -d</code></li>
    <li>If you want to rebuild the images (in case of code changes), use: 
        <code>docker-compose up --build -d</code></li>
    <li>If you want to enter the container and run commands interactively, use: 
        <code>docker-compose run -it --rm neural_network /bin/bash</code></li>
</ol>

<h1>TO RUN MAIN</h1>
<ol>
    <li>Run the command "run" inside the docker container to run the command "python main.py"</li>
</ol>
