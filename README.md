# _Mailchimp_ Open Microservice

> This is a mailchimp service

[![Open Microservice Specification Version](https://img.shields.io/badge/Open%20Microservice-1.0-477bf3.svg)](https://openmicroservices.org)
[![Open Microservices Spectrum Chat](https://withspectrum.github.io/badge/badge.svg)](https://spectrum.chat/open-microservices)
[![Open Microservices Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](https://github.com/oms-services/.github/blob/master/CODE_OF_CONDUCT.md)
[![Open Microservices Commitzen](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

## Introduction

This project is an example implementation of the [Open Microservice Specification](https://openmicroservices.org), a standard
originally created at [Storyscript](https://storyscript.io) for building highly-portable "microservices" that expose the
events, actions, and APIs inside containerized software.

## Getting Started

The `oms` command-line interface allows you to interact with Open Microservices. If you're interested in creating an Open
Microservice the CLI also helps validate, test, and debug your `oms.yml` implementation!

See the [oms-cli](https://github.com/microservices/oms) project to learn more!

### Installation

```
npm install -g @microservices/oms
```

## Usage

### Open Microservices CLI Usage

Once you have the [oms-cli](https://github.com/microservices/oms) installed, you can run any of the following commands from
within this project's root directory:

#### Actions

##### addSubscriber

>

##### Action Arguments

| Argument Name      | Type     | Required | Default | Description                                                          |
| :----------------- | :------- | :------- | :------ | :------------------------------------------------------------------- |
| listName           | `string` | `true`   | None    | No description provided.                                             |
| userEmail          | `string` | `true`   | None    | No description provided.                                             |
| status             | `string` | `true`   | None    | Status of subscriber. Inputs - subscribed/unsubscribed               |
| firstName          | `string` | `true`   | None    | No description provided.                                             |
| lastName           | `string` | `true`   | None    | No description provided.                                             |
| address            | `string` | `false`  | None    | No description provided.                                             |
| phone              | `string` | `false`  | None    | No description provided.                                             |
| MAILCHIMP_API_KEY  | `string` | `false`  | None    | Please acquire your Mailchimp API from Account -> Extras -> API Keys |
| MAILCHIMP_USERNAME | `string` | `false`  | None    | Please provide your MailChimp username                               |

```shell
oms run addSubscriber \
    -a listName='*****' \
    -a userEmail='*****' \
    -a status='*****' \
    -a firstName='*****' \
    -a lastName='*****' \
    -a address='*****' \
    -a phone='*****' \
    -e MAILCHIMP_API_KEY=$MAILCHIMP_API_KEY \
    -e MAILCHIMP_USERNAME=$MAILCHIMP_USERNAME
```

##### deleteSubscriber

>

##### Action Arguments

| Argument Name      | Type     | Required | Default | Description                                                          |
| :----------------- | :------- | :------- | :------ | :------------------------------------------------------------------- |
| listName           | `string` | `true`   | None    | No description provided.                                             |
| userEmail          | `string` | `true`   | None    | No description provided.                                             |
| MAILCHIMP_API_KEY  | `string` | `false`  | None    | Please acquire your Mailchimp API from Account -> Extras -> API Keys |
| MAILCHIMP_USERNAME | `string` | `false`  | None    | Please provide your MailChimp username                               |

```shell
oms run deleteSubscriber \
    -a listName='*****' \
    -a userEmail='*****' \
    -e MAILCHIMP_API_KEY=$MAILCHIMP_API_KEY \
    -e MAILCHIMP_USERNAME=$MAILCHIMP_USERNAME
```

##### addSubscriberTags

>

##### Action Arguments

| Argument Name      | Type     | Required | Default | Description                                                          |
| :----------------- | :------- | :------- | :------ | :------------------------------------------------------------------- |
| listName           | `string` | `true`   | None    | No description provided.                                             |
| userEmail          | `string` | `true`   | None    | No description provided.                                             |
| tags               | `string` | `true`   | None    | No description provided.                                             |
| MAILCHIMP_API_KEY  | `string` | `false`  | None    | Please acquire your Mailchimp API from Account -> Extras -> API Keys |
| MAILCHIMP_USERNAME | `string` | `false`  | None    | Please provide your MailChimp username                               |

```shell
oms run addSubscriberTags \
    -a listName='*****' \
    -a userEmail='*****' \
    -a tags='*****' \
    -e MAILCHIMP_API_KEY=$MAILCHIMP_API_KEY \
    -e MAILCHIMP_USERNAME=$MAILCHIMP_USERNAME
```

##### updateSubscriber

>

##### Action Arguments

| Argument Name      | Type     | Required | Default | Description                                                          |
| :----------------- | :------- | :------- | :------ | :------------------------------------------------------------------- |
| listName           | `string` | `true`   | None    | No description provided.                                             |
| userEmail          | `string` | `true`   | None    | No description provided.                                             |
| status             | `string` | `false`  | None    | Status of subscriber. Inputs - subscribed/unsubscribed               |
| firstName          | `string` | `false`  | None    | No description provided.                                             |
| lastName           | `string` | `false`  | None    | No description provided.                                             |
| newEmail           | `string` | `false`  | None    | No description provided.                                             |
| address            | `string` | `false`  | None    | No description provided.                                             |
| phone              | `string` | `false`  | None    | No description provided.                                             |
| MAILCHIMP_API_KEY  | `string` | `false`  | None    | Please acquire your Mailchimp API from Account -> Extras -> API Keys |
| MAILCHIMP_USERNAME | `string` | `false`  | None    | Please provide your MailChimp username                               |

```shell
oms run updateSubscriber \
    -a listName='*****' \
    -a userEmail='*****' \
    -a status='*****' \
    -a firstName='*****' \
    -a lastName='*****' \
    -a newEmail='*****' \
    -a address='*****' \
    -a phone='*****' \
    -e MAILCHIMP_API_KEY=$MAILCHIMP_API_KEY \
    -e MAILCHIMP_USERNAME=$MAILCHIMP_USERNAME
```

## Contributing

All suggestions in how to improve the specification and this guide are very welcome. Feel free share your thoughts in the
Issue tracker, or even better, fork the repository to implement your own ideas and submit a pull request.

[![Edit mailchimp on CodeSandbox](https://codesandbox.io/static/img/play-codesandbox.svg)](https://codesandbox.io/s/github/oms-services/mailchimp)

This project is guided by [Contributor Covenant](https://github.com/oms-services/.github/blob/master/CODE_OF_CONDUCT.md).
Please read out full [Contribution Guidelines](https://github.com/oms-services/.github/blob/master/CONTRIBUTING.md).

## Additional Resources

- [Install the CLI](https://github.com/microservices/oms) - The OMS CLI helps developers create, test, validate, and build
  microservices.
- [Example OMS Services](https://github.com/oms-services) - Examples of OMS-compliant services written in a variety of
  languages.
- [Example Language Implementations](https://github.com/microservices) - Find tooling & language implementations in Node,
  Python, Scala, Java, Clojure.
- [Storyscript Hub](https://hub.storyscript.io) - A public registry of OMS services.
- [Community Chat](https://spectrum.chat/open-microservices) - Have ideas? Questions? Join us on Spectrum.
