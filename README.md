# MailChimp as a microservice: Add, Delete, and update a subscriber

### Add subscriber to a list

```coffee
# Storyscript
mailchimp add_subscriber list_name: 'Your_list_name' user_email: 'xxxx@gmail.com' first_name: 'John' last_name: 'Doe' status: 'subscribed/unsubscribed' address: 'user_address' phone: '+1xxxx' API_KEY: 'Mailchimp API key' USERNAME: 'Mailchimp Username'

# Required fields: list_name, list_id, user_email, first_name, last_name, status, API_Key, USERNAME
# Optional fields: address, phone

```

### Delete subscriber from a list
```coffee
# Storyscript
mailchimp delete_subscriber list_name: 'Your_list_name' user_email: 'xxxx@gmail.com' API_KEY: 'Mailchimp API key' USERNAME: 'Mailchimp Username'

```
### Update a subscriber

```coffee
# Storyscript
mailchimp update_subscriber list_name: 'Your_list_name' user_email: 'xxxx@gmail.com' first_name: 'John' last_name: 'Doe' status: 'subscribed/unsubscribed' new_email: 'xyz@gmail.com' address: 'user_address' phone: '+1xxxx' API_KEY: 'Mailchimp API key' USERNAME: 'Mailchimp Username'

# Required fields: list_name, list_id, user_email

```

### Add Tags to a subscriber

```coffee
# Storyscript
mailchimp add_subscriber_tags list_name: 'Your_list_name' user_email: 'xxxx@gmail.com' tags: 'tag1, tag2..' API_KEY: 'Mailchimp API key' USERNAME: 'Mailchimp Username'

```