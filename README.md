# fastapi-balance-agent
Agent deployment

**Render web service deployment:** 

Puplic repo: https://github.com/lux21298/fastapi-balance-agent.git

Branch: main

Runtime: Python3

Build Command: pip install -r requirements.txt

Start Command: uvicorn main:app --host 0.0.0.0 --port 10000


**Test api though postman** 

Download: https://www.postman.com/ 

- **Post**: https://fastapi-balance-agent1.onrender.com/register
- 
In Body, choose "raw". In content:

{
  "username": "user_name",
  "password": "1234"
}

Then send

**Get**: https://fastapi-balance-agent1.onrender.com/balance

In Authorization, choose "Basic Auth" 

Username: user_name

Password: 1234

Then send

