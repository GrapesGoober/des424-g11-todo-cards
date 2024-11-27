# DES424 G11 TodoCards
User Instruction:
1. If you haven't signed up, press sign up.
2. Otherwise, login to your account.
    - We have users `bob`, `cindy`, `fay`, and `ajarn`.
    - As for passwords, concatenate `123` after username; for example `bob123`
4. To create a deck, press the green plus button.
5. In each deck, if you have the editor permission or you are the owner, you can:
    - Modify the deck name and description.
    - Use the sharelink to add new members to the deck with predetermined permission.
    - Create new card with its name, description, deadlines, and colors.
    - Add subcards to breakdown the card into smaller tasks
    - Remove cards or mark them as done.
6. If you only have a viewer permission, you can only see the list of task and their deadline.

## Run App
1. Start the Docker engine.
2. Run `docker compose up`. This sets up 3 containers: 
    - `mysql` for port 3306 
    - `fastapi-app` for port 8000. You can visit FastAPI's auto docs via `http://localhost:8000/docs`
    - `svelte-app` for port 5173. Connect to frontend UI via `http://localhost:5173`

## Current Link
- Jira: https://nachatk.atlassian.net/jira/software/projects/DES424/boards/34
- Todo-Card Website: EC2 Public IP:5173 (However, since this is on EC2 learner lab, it terminates when lab ends)
- ECS Fargate Service: http://100.25.168.40

## Members
- Nachat Kaewmeesang 6422770774
- Pusit Eiamsook 6422772226
- Krittidech Paijitjinda 6422781664
- Supakorn Vannathong 6422782712
- Arkaravit Raksakaeo 6722800099
- Kittisak Wanganansukdee 6422781441
