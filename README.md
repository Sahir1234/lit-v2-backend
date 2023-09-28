# lit-v2-backend


TODO:

1. Finish setting up app as Flask script with all of the updates
    a. there should be API endpoints for basic updates
    b. the web socket should only be used for the lobby and game states
    c. we may be able to use Flask-SocketIO
    d. TEMPORARY ARCHITECTURE: everything through restful API, later convert to other stuff
2. Dockerize start up script
3. Can test deployment on elastic benstalk


FLOW:

create 8 digit identifier code -> map that to a uuid code