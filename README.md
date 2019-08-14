# MailChimp OMG Microservice

[![Open Microservice Guide](https://img.shields.io/badge/OMG%20Enabled-👍-green.svg?)](https://microservice.guide)
[![Build Status](https://travis-ci.com/omg-services/mailchimp.svg?branch=master)](https://travis-ci.com/omg-services/mailchimp)
[![codecov](https://codecov.io/gh/omg-services/mailchimp/branch/master/graph/badge.svg)](https://codecov.io/gh/omg-services/mailchimp)

### Add subscriber to a list

```coffee
# Storyscript
mailchimp addSubscriber listName: 'Your_list_name' userEmail: 'xxxx@gmail.com' firstName: 'John' lastName: 'Doe' status: 'subscribed/unsubscribed' address: 'user_address' phone: '+1xxxx'
{ "id": "id","email_address": "abc@example.com","unique_email_id": "unique_email_id","web_id": 3620xxxxx,"email_type": "html","status": "subscribed","merge_fields": {"merge_fields details"},"stats": {"stats details"},"ip_opt": "103.204.163.26",    "timestamp_opt": "2019-08-13T14:16:53+00:00","member_rating": 2,"last_changed": "2019-08-13T14:16:53+00:00","language": "","vip": false,"email_client": "","location": {"location details"},"source": "API - Generic","tags_count": 0,"tags": [],"list_id": "f7babfb748","_links": ["list of links"]
}
```

### Delete subscriber from a list

```coffee
# Storyscript
mailchimp deleteSubscriber listName: 'Your_list_name' userEmail: 'xxxx@gmail.com'
{"message": "list deleted successfully","success": true}
```

### Update a subscriber

```coffee
# Storyscript
mailchimp updateSubscriber listName: 'Your_list_name' userEmail: 'xxxx@gmail.com'   firstName: 'John' lastName: 'Doe' status: 'subscribed/unsubscribed' new_email:'xyz@gmail.com'
address: 'user_address' phone: '+1xxxx'
{ "id": "id","email_address": "abc@example.com","unique_email_id": "unique_email_id",   "web_id": 3620xxxxx,"email_type": "html","status": "subscribed","merge_fields": {"merge_fields details"},"stats": {"stats details"},"ip_opt": "103.204.163.26",    "timestamp_opt": "2019-08-13T14:16:53+00:00","member_rating": 2,"last_changed": "2019-08-13T14:16:53+00:00","language": "","vip": false,"email_client": "","location": {"location details"},"source": "API - Generic","tags_count": 0,"tags": [],"list_id": "f7babfb748","_links": ["list of links"]
}
```

### Add Tags to a subscriber

```coffee
# Storyscript
mailchimp addSubscriberTags listName: 'Your_list_name' userEmail: 'xxxx@gmail.com' tags: 'tag1, tag2..'
{"message": "Tag added successfully","success": true}

```

### Obtaining MailChimp credentials:

* MailChimp API key can be retrived from your MailChimp Account -> Extras -> API keys.
Checkout - [How to find or generate API Key](https://mailchimp.com/help/about-api-keys/#find+or+generate+your+api+key)

* MailChimp Username: Same as MailChimp account User ID.

Curious to [learn more](https://docs.storyscript.io/)?

✨🍰✨

## Usage with [OMG CLI](https://www.npmjs.com/package/omg)

##### Add Subscriber
```shell
$ omg run addSubscriber -a listName=<LIST_NAME> -a userEmail=<USER_EMAIL> -a status=<STATUS> -a firstName=<FRIST_NAME> -a lastName=<LAST_NAME> -e MAILCHIMP_API_KEY=<MAILCHIMP_API_KEY> -e MAILCHIMP_USERNAME=<MAILCHIMP_USERNAME>
```

##### Delete Subscriber
```shell
$ omg run deleteSubscriber -a listName=<LIST_NAME> -a userEmail=<USER_EMAIL> -e MAILCHIMP_API_KEY=<MAILCHIMP_API_KEY> -e MAILCHIMP_USERNAME=<MAILCHIMP_USERNAME>
```

##### Update Subscriber
```shell
$ omg run updateSubscriber -a listName=<LIST_NAME> -a userEmail=<USER_EMAIL> -a status=<STATUS> -a firstName=<FRIST_NAME> -a lastName=<LAST_NAME> -a newEmail=<NEW_EMAIL> -e MAILCHIMP_API_KEY=<MAILCHIMP_API_KEY> -e MAILCHIMP_USERNAME=<MAILCHIMP_USERNAME>
```

##### Add Subscriber Tags
```shell
$ omg run addSubscriberTags -a listName=<LIST_NAME> -a userEmail=<USER_EMAIL> -a tags=<TAGS> -e MAILCHIMP_API_KEY=<MAILCHIMP_API_KEY> -e MAILCHIMP_USERNAME=<MAILCHIMP_USERNAME>
```

**Note**: The OMG CLI requires [Docker](https://docs.docker.com/install/) to be installed.

## License
[MIT License](https://github.com/omg-services/mailchimp/blob/master/LICENSE).