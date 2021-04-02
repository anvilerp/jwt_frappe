## Jwt for Frappe

auth with token for mobile and frontend applications 
## How to get token use the same login api but with extra argument as explained :
curl -X POST https://{your frappe instance}/api/method/login \
     -H 'Content-Type: application/json' \
     -H 'Accept: application/json' \
     -d '{"usr":"Administrator","pwd":"admin","use_jwt",1}'

and ther response will be :

    "message": "Logged In",
    "home_page": "/desk",
    "full_name": "ahmad",
    "token": "eyJ0eXAiOiJqd3QiLC........."
}
## for requests use token in Header 
"Authorization" : "Bearer M72UK1a1SEiY1MUJ.........."


#### License

MIT
