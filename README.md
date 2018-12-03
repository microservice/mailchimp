# MailChimp as a microservice

## Installation and Build
```

npm install -g omg
omg build

```


## Usage

### Add subscriber to a list

```

omg exec add -a list_name=<list_name> -a user_email=<user_email> -a status="subscribed" -a first_name=<f_name> -a last_name=<L_name> -e API_KEY=<API_KEY> -e USERNAME= <username>

```

### Delete subscriber from a list

```

omg exec delete -a list_name=<list_name> -a user_email=<user_email> -e API_KEY=<API_KEY> -e USERNAME= <username>

```

### Add Tags to a subcriber

```

omg exec add_tag -a list_name=<list_name> -a user_email=<user_email> -a tag= <tag_name> -e API_KEY=<API_KEY> -e USERNAME= <username>

```

### Update a subcriber

```

omg exec update_subscriber -a list_name=<list_name< -a user_email= <user_email> -a last_name= <last_name> -a phone=<phone_number> -a new_email=<new_email> -e API_KEY= <API_KEY> -e USERNAME= <username>

```
