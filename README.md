[![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner-direct-single.svg)](https://stand-with-ukraine.pp.ua)

Unofficial and reverse-engineered Threads ([threads.net](https://www.threads.net/@zuck)) Python API wrapper. 
Supports read and write capabilities.

[![](https://github.com/dmytrostriletskyi/threads-net/actions/workflows/main.yaml/badge.svg?branch=main)](https://github.com/dmytrostriletskyi/threads-net/actions/workflows/main.yaml)
[![](https://img.shields.io/github/release/dmytrostriletskyi/threads-net.svg)](https://github.com/dmytrostriletskyi/threads-net/releases)
[![](https://img.shields.io/pypi/v/threads-net.svg)](https://pypi.python.org/pypi/threads-net)

[![](https://pepy.tech/badge/threads-net)](https://pepy.tech/project/threads-net)
[![](https://img.shields.io/pypi/l/threads-net.svg)](https://pypi.python.org/pypi/threads-net/)
[![](https://img.shields.io/pypi/pyversions/threads-net.svg)](https://pypi.python.org/pypi/threads-net/)

Table of content:

* [Disclaimer](#disclaimer)
* [Roadmap](#roadmap)
* [Getting started](#getting-started)
  * [How to install](#how-to-install)
  * [Examples](#examples)
* [API](#api)
  * [Troubleshooting](#troubleshooting)
    * [User Identifier](#user-identifier)
    * [Two-Factor Authentication (2FA)](#two-factor-authentication-2fa)
  * [Terminology](#terminology)
  * [Initialization](#initialization)
  * [Public](#api)
    * [User](#user)
      * [Get Identifier](#get-identifier)
      * [Get By Identifier](#get-by-identifier)
      * [Get Threads](#get-threads)
      * [Get Replies](#get-replies)
    * [Thread](#thread)
      * [Get Identifier](#get-identifier-1)
      * [Get By Identifier](#get-by-identifier-1)
      * [Get Likers](#get-likers)
  * [Private](#private)
    * [User](#user-1)
      * [Get Identifier](#get-identifier-2)
      * [Get By Identifier](#get-by-identifier-2)
      * [Get Followers](#get-followers)
      * [Get Following](#get-following)
      * [Search](#search)
      * [Follow](#follow)
      * [Unfollow](#unfollow)
    * [Thread](#thread-1)
      * [Get Identifier](#get-identifier-3)
      * [Get By Identifier](#get-by-identifier-3)
      * [Get Likers](#get-likers-1)
      * [Create](#create)
      * [Delete](#delete)
      * [Like](#like)
      * [Unlike](#unlike)

## Disclaimer

* As `Threads` are backed by `Instagram`, those are couples in terms of `APIs`. For example, there is a way to fetch a
  user or thread information from both `Threads` and `Instagram` `APIs`. But there are unique `API` endpoints that exist 
  only in one of the `APIs`, for instance, to create a post, there is only `Instagram API` endpoint.
* To interact with `Threads API` there is no need for any authorization. On the other hand, to interact with 
  `Instagram API`, you have to specify `Instagram` username and password (as like you do when you log in to `Threads` 
  mobile application). 
* This project is unofficial and reverse-engineered, it means: 
  * That the library would be pretending being a mobile phone or web user (via proper `HTTP` headers and other things). 
    Thus, you might face `rate limits` (because pretending is never ideal) or even your account in `Threads` and/or 
    `Instagram` might be suspended if you mess up with logining or sending too much requests. 
  * That `Threads` and `Instagram` `APIs` which are used by a library are not provided as public `API` and developed to 
    be used internally (`Meta'`s `back-end` developers for `front-end` developers) without any intention to reveal it. 
    Thus, expect activate development on their side and not stable work of the `APIs` and therefore the library.

## Roadmap

Check what is already done in the table of content above, below placed only things to be done: 

- [ ] Private `API`
  - [ ] Get a user's threads
  - [ ] Get a user's replies
  - [ ] Get a thread's likers
  - [ ] Create a thread
    - [ ] With image
    - [ ] With multiple images
    - [ ] With link attachment
  - [ ] Delete a thread
  - [ ] Embed a thread
  - [ ] Manage auth for accounts with enabled 2FA

## Getting started

### How to install

Install the library with the following command using `pip3`:

```bash
$ pip3 install threads-net
```

### Examples

Find examples of how to use the library in the `examples` folder:

```bash
ls examples
├── private
│   ├── create_thread.py
│   ├── follow_user.py
│   ├── get_user.py
│   ├── get_user_followers.py
│   ├── get_user_following.py
│   └── search_user.py
│   ...
└── public
    ├── get_thread.py
    ├── get_thread_likers.py
    ├── get_user.py
    ├── get_user_replies.py
    └── get_user_threads.py
    ...
```

## API

### Troubleshooting

#### User Identifier

If you use public `API`, you should know that there is one really unstable method — getting a user's identifier 
by a username (`threads.public_api.get_user_id`) because under the hood it does retrieving and parsing a plain `HTML`
instead of regular `GrapQL` or `RESTful API`. The returning `HTML` is inconsistent from time to time as well `API` 
itself is broken not responding with any data at all.

Until the library maintainers find more stable way, you have two options:

* Retrieve a user's identifier manually from a public service like this one — https://commentpicker.com/instagram-user-id.php.
* Use private `API` method (`threads.private_api.get_user_id`) which use much more stable endpoint. You can just fetch
  a user identifier once via it and then pass it to public `API` and it will work.

#### Two-Factor Authentication (2FA)

Currently, it is not possible to use private `API` with two-factor authentication enabled on the account. If you do not
disable it, you might face issues like [#37](https://github.com/dmytrostriletskyi/threads-net/issues/37). So, in order
to use private `API`, you have to disable it first. By the way, there are plans in the roadmap to manage authentication
for such accounts so you don't have to disable it.

### Terminology

There might be a confusion among many `Threads API` clients as well as in both `Threads` an `Instagram` `APIs` according
to the naming of entities. For instance, in `Threads` a publication is called a `thread`, but under the hood in the `API`
of fetching or creating a `thread` it is called a `post`. 

It is done because `Threads` are backed by `Instagram` and `threads` creation is done on `Instagram API` where a 
publication called a post. Library maintainers decided to stick into `Threads` terminology and use the word `thread`.

### Initialization

Import the class responsible for `Threads API` communication and initialize the object. But it depends on if you are
going to use public or private `API`. The differences between public or private `APIs` are:

* Public `API` is `Threads API` which is developed for anonymous access. On other hand, private `API` is `Instagram API`,
  which is developed for access from mobile phone being authorized via `Instagram` username and password.
* Public `API` has only read-only endpoints. On other hand, private `API` has both read and write endpoints such as
  creating a post or follow a user.
* Public `API` much less stable than private `API` (from the library maintainers perspective).
* Public `API` much less risky to get `rate limits` or to have account in `Threads` and/or `Instagram` be suspended.

So, it is a trade-off between less risk, less stability and bugs and more risk, more stability and less bugs.

```python3
>>> from threads import Threads
>>> threads = Threads(username='instagram_username', password='instagram_password')
```

You can leave `username` and `password` parameters unspecified if you have no plans to use private `API`:

```python3
>>> from threads import Threads
>>> threads = Threads()
```

### Public

#### User

##### Get Identifier

`threads.public_api.get_user_id` — getting a user's identifier by their username.

| Parameters |  Type   | Required | Restrictions | Description                                              |
|:----------:|:-------:|:--------:|:------------:|----------------------------------------------------------|
| `username` | String  |   Yes    |      -       | A user's username which goes along with `@` like `zuck`. |

<details>
  <summary>Open example</summary>
  
  ```python3
  >>> user_id = threads.public_api.get_user_id(username='zuck')
  >>> user_id
  314216
  ```
</details>

##### Get By Identifier

`threads.public_api.get_user` — getting a user by their identifier.

| Parameters |  Type   | Required | Restrictions | Description          |
|:----------:|:-------:|:--------:|:------------:|----------------------|
|    `id`    | Integer |   Yes    |     `>0`     | A user's identifier. |

<details>
  <summary>Open example</summary>
  
  ```python3
  >>> user = threads.public_api.get_user(id=314216)
  >>> user
  {
      "data": {
          "userData": {
              "user": {
                  "is_private": false,
                  "profile_pic_url": "https://scontent.cdninstagram.com/v/t51.2885-19/357376107_1330597350674698_8884059223384672080_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=euIj8dtTGIkAX-mW2_l&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfAUZzobOIH6imLnb2Z3iXoWY5H1Fv_kNnyG8T4UGgJegQ&oe=64AED800&_nc_sid=10d13b",
                  "username": "zuck",
                  "hd_profile_pic_versions": [
                      {
                          "height": 320,
                          "url": "https://scontent.cdninstagram.com/v/t51.2885-19/357376107_1330597350674698_8884059223384672080_n.jpg?stp=dst-jpg_s320x320&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=euIj8dtTGIkAX-mW2_l&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfD5z6UgnQH54dihPnMrXgH2L-mLCMGlFsIF9Ug7U4RWdA&oe=64AED800&_nc_sid=10d13b",
                          "width": 320
                      },
                      {
                          "height": 640,
                          "url": "https://scontent.cdninstagram.com/v/t51.2885-19/357376107_1330597350674698_8884059223384672080_n.jpg?stp=dst-jpg_s640x640&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=euIj8dtTGIkAX-mW2_l&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfD4BaVu4cDcX53xPocD-3o_ZbKIESxUZhlU08FBpycCsA&oe=64AED800&_nc_sid=10d13b",
                          "width": 640
                      }
                  ],
                  "is_verified": true,
                  "biography": "",
                  "biography_with_entities": null,
                  "follower_count": 2663947,
                  "profile_context_facepile_users": null,
                  "bio_links": [
                      {
                          "url": ""
                      }
                  ],
                  "pk": "314216",
                  "full_name": "Mark Zuckerberg",
                  "id": null
              }
          }
      },
      "extensions": {
          "is_final": true
      }
  }
  ```
</details>

##### Get Threads

`threads.public_api.get_user_threads` — getting a user's threads by the user's identifier.

| Parameters |  Type   | Required | Restrictions | Description          |
|:----------:|:-------:|:--------:|:------------:|----------------------|
|    `id`    | Integer |   Yes    |     `>0`     | A user's identifier. |

<details>
  <summary>Open example</summary>
  
  ```python3
  >>> user_threads = threads.public_api.get_user_threads(id=314216)
  >>> user_threads
  {
      "instagram": {
          "pk": "314216",
          "username": "zuck",
          "full_name": "Mark Zuckerberg",
          "is_private": false,
          "profile_pic_url": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-19/352224138_1028122805231303_1175896139426286760_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=hbekpcjRfioAX8iYGJv&edm=AKEQFekBAAAA&ccb=7-5&oh=00_AfDf2r6qwujUc84tkzUlYJMfJt66xoWScQ-nsB5bmtYDnw&oe=64B0066A&_nc_sid=29ddf3",
          "profile_pic_url_hd": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-19/352224138_1028122805231303_1175896139426286760_n.jpg?stp=dst-jpg_s320x320&_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=hbekpcjRfioAX8iYGJv&edm=AKEQFekBAAAA&ccb=7-5&oh=00_AfCoPcYmzHdc2evDvduZjZK-IxDS07wGf0x9czecY_TgVQ&oe=64B0066A&_nc_sid=29ddf3",
          "is_verified": true,
          "media_count": 283,
          "follower_count": 11924434,
          "following_count": 523,
          "biography": "",
          "external_url": null,
          "account_type": null,
          "is_business": false,
          "public_email": null,
          "contact_phone_number": null,
          "public_phone_country_code": null,
          "public_phone_number": null,
          "business_contact_method": "UNKNOWN",
          "business_category_name": null,
          "category_name": "Entrepreneur",
          "category": null,
          "address_street": null,
          "city_id": null,
          "city_name": null,
          "latitude": null,
          "longitude": null,
          "zip": null,
          "instagram_location_id": null,
          "interop_messaging_user_fbid": null
      },
      "threads": {
          "data": {
              "userData": {
                  "user": {
                      "is_private": false,
                      "profile_pic_url": "https://scontent.cdninstagram.com/v/t51.2885-19/357376107_1330597350674698_8884059223384672080_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=euIj8dtTGIkAX9JAAZI&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfCdAMkmk0XL_r0GQi2MRD1Aq1kPZKBLfXLby47e_hsZrg&oe=64AED800&_nc_sid=10d13b",
                      "username": "zuck",
                      "hd_profile_pic_versions": [
                          {
                              "height": 320,
                              "url": "https://scontent.cdninstagram.com/v/t51.2885-19/357376107_1330597350674698_8884059223384672080_n.jpg?stp=dst-jpg_s320x320&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=euIj8dtTGIkAX9JAAZI&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfDJeE127_ZFA-eD3qRMM0Fh2NM-jRR4tUFsTywCrMctNA&oe=64AED800&_nc_sid=10d13b",
                              "width": 320
                          },
                          {
                              "height": 640,
                              "url": "https://scontent.cdninstagram.com/v/t51.2885-19/357376107_1330597350674698_8884059223384672080_n.jpg?stp=dst-jpg_s640x640&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=euIj8dtTGIkAX9JAAZI&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfAY-75SdPDasc0ophRu3lgeeHmnb3qPZIE-mCPh8PRRBw&oe=64AED800&_nc_sid=10d13b",
                              "width": 640
                          }
                      ],
                      "is_verified": true,
                      "biography": "",
                      "biography_with_entities": null,
                      "follower_count": 2663588,
                      "profile_context_facepile_users": null,
                      "bio_links": [
                          {
                              "url": ""
                          }
                      ],
                      "pk": "314216",
                      "full_name": "Mark Zuckerberg",
                      "id": null
                  }
              }
          },
          "extensions": {
              "is_final": true
          }
      }
  }
  ```
</details>

##### Get Replies

`threads.public_api.get_user_replies` — getting a user's replies by the user's identifier.

| Parameters |  Type   | Required | Restrictions | Description          |
|:----------:|:-------:|:--------:|:------------:|----------------------|
|    `id`    | Integer |   Yes    |     `>0`     | A user's identifier. |

<details>
  <summary>Open example</summary>
  
  ```python3
  >>> user_replies = threads.public_api.get_user_replies(id=314216)
  >>> user_replies
  {
      "data": {
          "mediaData": {
              "threads": [
                  {
                      "thread_items": [
                          {
                              "post": {
                                  "user": {
                                      "profile_pic_url": "https://scontent.cdninstagram.com/v/t51.2885-19/358196917_1319101762021874_6840458701147612733_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=RYUCB0OzBK8AX-fwWgu&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfAyNgzr1QLbjIdorzFD01h-NpApHx7-0XKdGWOKjS4Xlw&oe=64ABF5FF&_nc_sid=10d13b",
                                      "username": "intense0ne",
                                      "id": null,
                                      "is_verified": true,
                                      "pk": "13455834"
                                  },
                                  "image_versions2": {
                                      "candidates": [
                                          {
                                              "height": 1431,
                                              "url": "https://scontent.cdninstagram.com/v/t51.2885-15/358024814_953839475848219_4275939482568010016_n.jpg?stp=dst-jpg_e35&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=XBVzqlYSSPMAX-rTJuQ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTMwNzMyODM1ODU1NjA4OA%3D%3D.2-ccb7-5&oh=00_AfCUsy68lK2H5iyEGnWnPrQMnd18Dpvl0ZOhGh-iWQpxZA&oe=64ACB5E4&_nc_sid=10d13b",
                                              "width": 1170,
                                              "__typename": "XDTImageCandidate"
                                          },
                                          {
                                              "height": 881,
                                              "url": "https://scontent.cdninstagram.com/v/t51.2885-15/358024814_953839475848219_4275939482568010016_n.jpg?stp=dst-jpg_e35_p720x720&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=XBVzqlYSSPMAX-rTJuQ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTMwNzMyODM1ODU1NjA4OA%3D%3D.2-ccb7-5&oh=00_AfBUyEmnvY6wewYd2xR5RcBUdpwYDQ3-tPOJroowQwDDZA&oe=64ACB5E4&_nc_sid=10d13b",
                                              "width": 720,
                                              "__typename": "XDTImageCandidate"
                                          },
                                          {
                                              "height": 783,
                                              "url": "https://scontent.cdninstagram.com/v/t51.2885-15/358024814_953839475848219_4275939482568010016_n.jpg?stp=dst-jpg_e35_p640x640_sh0.08&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=XBVzqlYSSPMAX-rTJuQ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTMwNzMyODM1ODU1NjA4OA%3D%3D.2-ccb7-5&oh=00_AfCngfqkXR6lMDsTO_3W3ub2wXo6gy8hs9IflxKgVSZ29Q&oe=64ACB5E4&_nc_sid=10d13b",
                                              "width": 640,
                                              "__typename": "XDTImageCandidate"
                                          },
                                          {
                                              "height": 587,
                                              "url": "https://scontent.cdninstagram.com/v/t51.2885-15/358024814_953839475848219_4275939482568010016_n.jpg?stp=dst-jpg_e35_p480x480&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=XBVzqlYSSPMAX-rTJuQ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTMwNzMyODM1ODU1NjA4OA%3D%3D.2-ccb7-5&oh=00_AfDEcZTEK5c-C1M5RO0NLJZ1afo7GGqHClM6SFBH6nVJqQ&oe=64ACB5E4&_nc_sid=10d13b",
                                              "width": 480,
                                              "__typename": "XDTImageCandidate"
                                          },
                                          {
                                              "height": 391,
                                              "url": "https://scontent.cdninstagram.com/v/t51.2885-15/358024814_953839475848219_4275939482568010016_n.jpg?stp=dst-jpg_e35_p320x320&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=XBVzqlYSSPMAX-rTJuQ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTMwNzMyODM1ODU1NjA4OA%3D%3D.2-ccb7-5&oh=00_AfDme7hPMR0v7Uc_Rq5Vl-HA3eUAosNOuznntJ3rwkPVgA&oe=64ACB5E4&_nc_sid=10d13b",
                                              "width": 320,
                                              "__typename": "XDTImageCandidate"
                                          },
                                          {
                                              "height": 294,
                                              "url": "https://scontent.cdninstagram.com/v/t51.2885-15/358024814_953839475848219_4275939482568010016_n.jpg?stp=dst-jpg_e35_p240x240&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=XBVzqlYSSPMAX-rTJuQ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTMwNzMyODM1ODU1NjA4OA%3D%3D.2-ccb7-5&oh=00_AfDKjwryrv-cxfybvuPaa9TbcBqxozsTeOU6I7fRgDaZVw&oe=64ACB5E4&_nc_sid=10d13b",
                                              "width": 240,
                                              "__typename": "XDTImageCandidate"
                                          },
                                          {
                                              "height": 1080,
                                              "url": "https://scontent.cdninstagram.com/v/t51.2885-15/358024814_953839475848219_4275939482568010016_n.jpg?stp=c0.130.1170.1170a_dst-jpg_e35_s1080x1080&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=XBVzqlYSSPMAX-rTJuQ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTMwNzMyODM1ODU1NjA4OA%3D%3D.2-ccb7-5&oh=00_AfAfUg9I6LBwwruVJxP0y7tsa1eILSH3lnERy-GhLvY5tQ&oe=64ACB5E4&_nc_sid=10d13b",
                                              "width": 1080,
                                              "__typename": "XDTImageCandidate"
                                          },
                                          {
                                              "height": 750,
                                              "url": "https://scontent.cdninstagram.com/v/t51.2885-15/358024814_953839475848219_4275939482568010016_n.jpg?stp=c0.130.1170.1170a_dst-jpg_e35_s750x750_sh0.08&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=XBVzqlYSSPMAX-rTJuQ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTMwNzMyODM1ODU1NjA4OA%3D%3D.2-ccb7-5&oh=00_AfC4eDvJfpOFQXP9iDiQccDFa8mH-c-4eHjtoJa1guTIFA&oe=64ACB5E4&_nc_sid=10d13b",
                                              "width": 750,
                                              "__typename": "XDTImageCandidate"
                                          },
                                          {
                                              "height": 640,
                                              "url": "https://scontent.cdninstagram.com/v/t51.2885-15/358024814_953839475848219_4275939482568010016_n.jpg?stp=c0.130.1170.1170a_dst-jpg_e35_s640x640_sh0.08&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=XBVzqlYSSPMAX-rTJuQ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTMwNzMyODM1ODU1NjA4OA%3D%3D.2-ccb7-5&oh=00_AfCz0RbvKHBOKMTsmaHFJTa2NUymRFh9abONGDVhps-3BQ&oe=64ACB5E4&_nc_sid=10d13b",
                                              "width": 640,
                                              "__typename": "XDTImageCandidate"
                                          },
                                          {
                                              "height": 480,
                                              "url": "https://scontent.cdninstagram.com/v/t51.2885-15/358024814_953839475848219_4275939482568010016_n.jpg?stp=c0.130.1170.1170a_dst-jpg_e35_s480x480&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=XBVzqlYSSPMAX-rTJuQ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTMwNzMyODM1ODU1NjA4OA%3D%3D.2-ccb7-5&oh=00_AfCp9r6Se5hjBo-rMHJvLhfDFRJkzbOo7QZu-BkiW-kCew&oe=64ACB5E4&_nc_sid=10d13b",
                                              "width": 480,
                                              "__typename": "XDTImageCandidate"
                                          },
                                          {
                                              "height": 320,
                                              "url": "https://scontent.cdninstagram.com/v/t51.2885-15/358024814_953839475848219_4275939482568010016_n.jpg?stp=c0.130.1170.1170a_dst-jpg_e35_s320x320&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=XBVzqlYSSPMAX-rTJuQ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTMwNzMyODM1ODU1NjA4OA%3D%3D.2-ccb7-5&oh=00_AfCizo3gIxHuMKtgDmK1XNlxXr2NyEwfRbsN8ZLNb6y8GA&oe=64ACB5E4&_nc_sid=10d13b",
                                              "width": 320,
                                              "__typename": "XDTImageCandidate"
                                          },
                                          {
                                              "height": 240,
                                              "url": "https://scontent.cdninstagram.com/v/t51.2885-15/358024814_953839475848219_4275939482568010016_n.jpg?stp=c0.130.1170.1170a_dst-jpg_e35_s240x240&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=XBVzqlYSSPMAX-rTJuQ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTMwNzMyODM1ODU1NjA4OA%3D%3D.2-ccb7-5&oh=00_AfDvAFSgCbR982_ZAUAFSfdyXLWG_7WbXnv-_UZnorY7EA&oe=64ACB5E4&_nc_sid=10d13b",
                                              "width": 240,
                                              "__typename": "XDTImageCandidate"
                                          },
                                          {
                                              "height": 150,
                                              "url": "https://scontent.cdninstagram.com/v/t51.2885-15/358024814_953839475848219_4275939482568010016_n.jpg?stp=c0.130.1170.1170a_dst-jpg_e35_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=XBVzqlYSSPMAX-rTJuQ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTMwNzMyODM1ODU1NjA4OA%3D%3D.2-ccb7-5&oh=00_AfAy_iWsQikPBVk0haExvRIaDHqtPRkh2t-A9DHE4G2HWg&oe=64ACB5E4&_nc_sid=10d13b",
                                              "width": 150,
                                              "__typename": "XDTImageCandidate"
                                          }
                                      ]
                                  },
                                  "original_width": 1170,
                                  "original_height": 1431,
                                  "video_versions": [],
                                  "carousel_media": null,
                                  "carousel_media_count": null,
                                  "pk": "3141307328358556088",
                                  "has_audio": null,
                                  "text_post_app_info": {
                                      "link_preview_attachment": null,
                                      "share_info": {
                                          "quoted_post": null,
                                          "reposted_post": null
                                      },
                                      "reply_to_author": null,
                                      "is_post_unavailable": false
                                  },
                                  "caption": {
                                      "text": "Volk or Yair?? #UFC290\n\nI got Volk!! \ud83d\udc4f\ud83d\udc4f\ud83d\udc4f"
                                  },
                                  "taken_at": 1688693036,
                                  "like_count": 4144,
                                  "code": "CuYKl8tJKG4",
                                  "media_overlay_info": null,
                                  "id": "3141307328358556088_13455834"
                              },
                              "line_type": "squiggle",
                              "view_replies_cta_string": "386 replies",
                              "reply_facepile_users": [
                                  {
                                      "__typename": "XDTUserDict",
                                      "id": null,
                                      "profile_pic_url": "https://scontent.cdninstagram.com/v/t51.2885-19/358513246_834402004938078_3745574617102161833_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=106&_nc_ohc=LtUMjbsa1lgAX83w0Sh&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfDGvGlfVhbbAHunncfE-Gzmbf0rshNG8tlfg4eb5V77iQ&oe=64AD69D4&_nc_sid=10d13b"
                                  },
                                  {
                                      "__typename": "XDTUserDict",
                                      "id": null,
                                      "profile_pic_url": "https://scontent.cdninstagram.com/v/t51.2885-19/358028941_1385051345389996_8437393621281150341_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=104&_nc_ohc=XcGqYzbKhDYAX87Clm7&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfCKDgkhOitXrGIkYQs1V607cQ9rw0cSB9KuZoJTyCIPWQ&oe=64ABFFDC&_nc_sid=10d13b"
                                  },
                                  {
                                      "__typename": "XDTUserDict",
                                      "id": null,
                                      "profile_pic_url": "https://scontent.cdninstagram.com/v/t51.2885-19/358164004_986964552348931_381538637050666409_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=ML6ZsvS6xFsAX_GLu5T&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfBjZQ0RElFZ0DQxOpHmDIw-p2WRX9_NvhArpVy8Fqz0lA&oe=64AC0D96&_nc_sid=10d13b"
                                  }
                              ],
                              "should_show_replies_cta": true,
                              "__typename": "XDTThreadItem"
                          },
                          {
                              "post": {
                                  "user": {
                                      "profile_pic_url": "https://scontent.cdninstagram.com/v/t51.2885-19/357376107_1330597350674698_8884059223384672080_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=9PG1NK-L8OkAX_mdst3&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfAo5WPQy4q_RbWq8Hox7lQS09zUmk8PHdJWXYjU8Tu2yw&oe=64ACDDC0&_nc_sid=10d13b",
                                      "username": "zuck",
                                      "id": null,
                                      "is_verified": true,
                                      "pk": "314216"
                                  },
                                  "image_versions2": {
                                      "candidates": []
                                  },
                                  "original_width": 612,
                                  "original_height": 612,
                                  "video_versions": [],
                                  "carousel_media": null,
                                  "carousel_media_count": null,
                                  "pk": "3141314003249945904",
                                  "has_audio": null,
                                  "text_post_app_info": {
                                      "link_preview_attachment": null,
                                      "share_info": {
                                          "quoted_post": null,
                                          "reposted_post": null
                                      },
                                      "reply_to_author": {
                                          "username": "intense0ne",
                                          "id": null
                                      },
                                      "is_post_unavailable": false
                                  },
                                  "caption": {
                                      "text": "Definitely Volk"
                                  },
                                  "taken_at": 1688693832,
                                  "like_count": 10843,
                                  "code": "CuYMHFLrF0w",
                                  "media_overlay_info": null,
                                  "id": "3141314003249945904_314216"
                              },
                              "line_type": "line",
                              "view_replies_cta_string": "1,114 replies",
                              "reply_facepile_users": [
                                  {
                                      "__typename": "XDTUserDict",
                                      "id": null,
                                      "profile_pic_url": "https://scontent.cdninstagram.com/v/t51.2885-19/357993149_654182843249841_2984126770891448042_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=109&_nc_ohc=-HCIQXYHQlcAX8qkTXo&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfAwsxFT9ZYe71DKt7Wm3tmH4-3SwpA_6ifb74G-bMn8Bg&oe=64AC46A1&_nc_sid=10d13b"
                                  },
                                  {
                                      "__typename": "XDTUserDict",
                                      "id": null,
                                      "profile_pic_url": "https://scontent.cdninstagram.com/v/t51.2885-19/358036814_264065539563777_3872673087942117120_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=109&_nc_ohc=T3x8fyZcDQIAX_FXQ-6&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfDtWBscXjH85fml9eI9IERX2wibGkWU-EQcuSH-b3MvCA&oe=64AD33EE&_nc_sid=10d13b"
                                  },
                                  {
                                      "__typename": "XDTUserDict",
                                      "id": null,
                                      "profile_pic_url": "https://scontent.cdninstagram.com/v/t51.2885-19/358000233_1044681130274316_6742390706661437266_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=100&_nc_ohc=PvpO-62JaD0AX_XMP5_&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfC4ma-opT9ieAnypxLSXNtVUOQkSq5_hbtca5ADqOSHRA&oe=64ACA63A&_nc_sid=10d13b"
                                  }
                              ],
                              "should_show_replies_cta": true,
                              "__typename": "XDTThreadItem"
                          }
                      ],
                      "id": "3141314003249945904"
                  },
                  ...
              ]
          }
      },
      "extensions": {
          "is_final": true
      }
  }
  ```
</details>

#### Thread

##### Get Identifier

`threads.public_api.get_thread_id` — getting a thread's identifier by its `URL` identifier. `URL` identifier is a last 
part of a thread's website `URL`. If the thread's `URL` is `https://threads.net/t/CuXFPIeLLod`, then it would be `CuXFPIeLLod`.

| Parameters |  Type  | Required | Restrictions | Description                  |
|:----------:|:------:|:--------:|:------------:|------------------------------|
|  `url_id`  | String |   Yes    |      -       | A thread's `URL` identifier. |

<details>
  <summary>Open example</summary>
  
  ```python3
  >>> thread_id = threads.public_api.get_thread_id(url_id='CuXFPIeLLod')
  >>> thread_id
  3141002295235099165
  ```
</details>

##### Get By Identifier

`threads.public_api.get_thread` — getting a thread by its identifier.

| Parameters |  Type   | Required | Restrictions | Description            |
|:----------:|:-------:|:--------:|:------------:|------------------------|
|    `id`    | Integer |   Yes    |     `>0`     | A thread's identifier. |

<details>
  <summary>Open example</summary>
  
  ```python3
  >>> thread = threads.public_api.get_thread(id=3141002295235099165)
  >>> thread
  {
      "data": {
          "data": {
              "containing_thread": {
                  "thread_items": [
                      {
                          "post": {
                              "user": {
                                  "profile_pic_url": "https://scontent.cdninstagram.com/v/t51.2885-19/343392897_618515990300243_8088199406170073086_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=1xtR491RY6cAX8Okf3Z&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfDqsZTCRQlz7EaDpgEzBkmXqtqKtTH80Q0r1rIDMJCcpg&oe=64AC2D8D&_nc_sid=10d13b",
                                  "username": "mosseri",
                                  "id": null,
                                  "is_verified": true,
                                  "pk": "95561"
                              },
                              "image_versions2": {
                                  "candidates": []
                              },
                              "original_width": 612,
                              "original_height": 612,
                              "video_versions": [],
                              "carousel_media": null,
                              "carousel_media_count": null,
                              "pk": "3141055616164096839",
                              "has_audio": null,
                              "text_post_app_info": {
                                  "link_preview_attachment": null,
                                  "share_info": {
                                      "quoted_post": null,
                                      "reposted_post": null
                                  },
                                  "reply_to_author": null,
                                  "is_post_unavailable": false,
                                  "direct_reply_count": 2839
                              },
                              "caption": {
                                  "text": "I've been getting some questions about deleting your account. To clarify, you can deactivate your Threads account, which hides your Threads profile and content, you can set your profile to private, and you can delete individual threads posts \u2013 all without deleting your Instagram account. Threads is powered by Instagram, so right now it's just one account, but we're looking into a way to delete your Threads account separately."
                              },
                              "taken_at": 1688663030,
                              "like_count": 29984,
                              "code": "CuXRXDdNOtH",
                              "media_overlay_info": null,
                              "id": "3141055616164096839_95561"
                          },
                          "line_type": "none",
                          "view_replies_cta_string": "2,839 replies",
                          "reply_facepile_users": [],
                          "should_show_replies_cta": true
                      }
                  ],
                  "thread_type": "thread",
                  "header": null,
                  "id": "3141055616164096839"
              },
              "reply_threads": [
                  {
                      "thread_items": [
                          {
                              "post": {
                                  "user": {
                                      "profile_pic_url": "https://scontent.cdninstagram.com/v/t51.2885-19/355424589_948742193018772_4617955233166333765_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=100&_nc_ohc=heQWdfsKG5MAX9mLim0&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfA6TUpLjjegnP6KuducRm8n6uU9iBCXg4O1P33WYSh3mg&oe=64ACDDBA&_nc_sid=10d13b",
                                      "username": "jimmywhotalks",
                                      "id": null,
                                      "is_verified": true,
                                      "pk": "51094265817"
                                  },
                                  "image_versions2": {
                                      "candidates": []
                                  },
                                  "original_width": 612,
                                  "original_height": 612,
                                  "video_versions": [],
                                  "carousel_media": null,
                                  "carousel_media_count": null,
                                  "pk": "3141082664316809193",
                                  "has_audio": null,
                                  "text_post_app_info": {
                                      "link_preview_attachment": null,
                                      "share_info": {
                                          "quoted_post": null,
                                          "reposted_post": null
                                      },
                                      "reply_to_author": {
                                          "username": "mosseri",
                                          "id": null
                                      },
                                      "is_post_unavailable": false
                                  },
                                  "caption": {
                                      "text": "Glad to know, Everyone is worrying for that."
                                  },
                                  "taken_at": 1688666254,
                                  "like_count": 59,
                                  "code": "CuXXgqAva_p",
                                  "media_overlay_info": null,
                                  "id": "3141082664316809193_51094265817"
                              },
                              "line_type": "none",
                              "view_replies_cta_string": null,
                              "reply_facepile_users": [],
                              "should_show_replies_cta": false
                          }
                      ],
                      "thread_type": "thread",
                      "header": null,
                      "id": "3141082664316809193"
                  },
                  ...
              ]
          }
      },
      "extensions": {
          "is_final": true
      }
  }
  ```
</details>

##### Get Likers

`threads.public_api.get_thread_likers` — getting a thread's likers by the thread's identifier.

| Parameters |  Type   | Required | Restrictions | Description            |
|:----------:|:-------:|:--------:|:------------:|------------------------|
|    `id`    | Integer |   Yes    |     `>0`     | A thread's identifier. |

<details>
  <summary>Open example</summary>
  
  ```python3
  >>> thread_likers = threads.public_api.get_thread_likers(id=3141002295235099165)
  >>> thread_likers
  {
      "data": {
          "likers": {
              "users": [
                  {
                      "pk": "32729880576",
                      "full_name": "K 🦋I🦋K🦋I",
                      "profile_pic_url": "https://scontent.cdninstagram.com/19/6007.jpg
                      "follower_count": 51,
                      "is_verified": false,
                      "username": "niyod_couture",
                      "profile_context_facepile_users": null,
                      "id": null
                  },
                  ...
              ]
          }
      },
      "extensions": {
          "is_final": true
      }
  }
  ```
</details>

### Private

#### User

##### Get Identifier

`threads.private_api.get_user_id` — getting a user's identifier by their username.

| Parameters |  Type   | Required | Restrictions | Description                                              |
|:----------:|:-------:|:--------:|:------------:|----------------------------------------------------------|
| `username` | String  |   Yes    |      -       | A user's username which goes along with `@` like `zuck`. |

<details>
  <summary>Open example</summary>
  
  ```python3
  >>> user_id = threads.private_api.get_user_id(username='zuck')
  >>> user_id
  314216
  ```
</details>

##### Get By Identifier

`threads.private_api.get_user` — getting a user by their identifier.

| Parameters |  Type   | Required | Restrictions | Description          |
|:----------:|:-------:|:--------:|:------------:|----------------------|
|    `id`    | Integer |   Yes    |     `>0`     | A user's identifier. |

<details>
  <summary>Open example</summary>
  
  ```python3
  >>> user = threads.private_api.get_user(id=314216)
  >>> user
  {
      "user": {
          "has_anonymous_profile_picture": false,
          "is_supervision_features_enabled": false,
          "follower_count": 2782815,
          "media_count": 283,
          "following_count": 313,
          "following_tag_count": 3,
          "can_use_affiliate_partnership_messaging_as_creator": false,
          "can_use_affiliate_partnership_messaging_as_brand": false,
          "has_collab_collections": false,
          "has_private_collections": true,
          "has_music_on_profile": false,
          "is_potential_business": false,
          "can_use_branded_content_discovery_as_creator": false,
          "can_use_branded_content_discovery_as_brand": false,
          "fan_club_info": {
              "fan_club_id": null,
              "fan_club_name": null,
              "is_fan_club_referral_eligible": null,
              "fan_consideration_page_revamp_eligiblity": null,
              "is_fan_club_gifting_eligible": null,
              "subscriber_count": null,
              "connected_member_count": null,
              "autosave_to_exclusive_highlight": null,
              "has_enough_subscribers_for_ssc": null
          },
          "fbid_v2": "17841401746480004",
          "pronouns": [],
          "is_whatsapp_linked": false,
          "transparency_product_enabled": false,
          "account_category": "",
          "interop_messaging_user_fbid": 119171612803872,
          "bio_links": [
              {
                  "link_id": 17979756671109835,
                  "url": "",
                  "lynx_url": "",
                  "link_type": "external",
                  "title": "",
                  "open_external_url_with_in_app_browser": true
              }
          ],
          "can_add_fb_group_link_on_profile": false,
          "external_url": "",
          "show_shoppable_feed": false,
          "merchant_checkout_style": "none",
          "seller_shoppable_feed_type": "none",
          "creator_shopping_info": {
              "linked_merchant_accounts": []
          },
          "has_guides": false,
          "has_highlight_reels": false,
          "hd_profile_pic_url_info": {
              "url": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-19/357376107_1330597350674698_8884059223384672080_n.jpg?_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=euIj8dtTGIkAX_8Gm2Q&edm=AEF8tYYBAAAA&ccb=7-5&oh=00_AfBs65PPEgj6s58aEAVAZWAUJu9JqhMcsWV8VLubRyzQwQ&oe=64B0D240&_nc_sid=1e20d2",
              "width": 805,
              "height": 805
          },
          "hd_profile_pic_versions": [
              {
                  "width": 320,
                  "height": 320,
                  "url": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-19/357376107_1330597350674698_8884059223384672080_n.jpg?stp=dst-jpg_s320x320&_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=euIj8dtTGIkAX_8Gm2Q&edm=AEF8tYYBAAAA&ccb=7-5&oh=00_AfB7HZGMI4QLDwO-wKkntDBbGavE_-oKHus264KgonCVqg&oe=64B0D240&_nc_sid=1e20d2"
              },
              {
                  "width": 640,
                  "height": 640,
                  "url": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-19/357376107_1330597350674698_8884059223384672080_n.jpg?stp=dst-jpg_s640x640&_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=euIj8dtTGIkAX_8Gm2Q&edm=AEF8tYYBAAAA&ccb=7-5&oh=00_AfBxpkJK3xNM4BLNfbMzrcTyKkza60pitJvggFKtuX4uIA&oe=64B0D240&_nc_sid=1e20d2"
              }
          ],
          "is_interest_account": true,
          "is_favorite": false,
          "is_favorite_for_stories": false,
          "is_favorite_for_igtv": false,
          "is_favorite_for_clips": false,
          "is_favorite_for_highlights": false,
          "broadcast_chat_preference_status": {
              "json_response": "{\"status\":\"ok\",\"status_code\":\"200\",\"is_broadcast_chat_creator\":true,\"notification_setting_type\":2}"
          },
          "live_subscription_status": "default",
          "usertags_count": 43060,
          "total_ar_effects": 1,
          "total_clips_count": 1,
          "has_videos": true,
          "total_igtv_videos": 12,
          "has_igtv_series": false,
          "biography": "",
          "include_direct_blacklist_status": true,
          "biography_with_entities": {
              "raw_text": "",
              "entities": []
          },
          "show_fb_link_on_profile": false,
          "primary_profile_link_type": 0,
          "can_hide_category": true,
          "can_hide_public_contacts": true,
          "should_show_category": false,
          "category_id": 1617,
          "is_category_tappable": false,
          "should_show_public_contacts": false,
          "is_eligible_for_smb_support_flow": true,
          "is_eligible_for_lead_center": false,
          "is_experienced_advertiser": false,
          "lead_details_app_id": "com.bloks.www.ig.smb.lead_gen.subpage",
          "is_business": false,
          "professional_conversion_suggested_account_type": 3,
          "account_type": 3,
          "direct_messaging": "",
          "instagram_location_id": "",
          "address_street": "",
          "business_contact_method": "UNKNOWN",
          "city_id": 0,
          "city_name": "",
          "contact_phone_number": "",
          "is_profile_audio_call_enabled": false,
          "latitude": 0.0,
          "longitude": 0.0,
          "public_email": "",
          "public_phone_country_code": "",
          "public_phone_number": "",
          "zip": "",
          "mutual_followers_count": 0,
          "has_onboarded_to_text_post_app": true,
          "show_text_post_app_badge": true,
          "text_post_app_joiner_number": 1,
          "show_ig_app_switcher_badge": true,
          "show_text_post_app_switcher_badge": true,
          "profile_context": "",
          "profile_context_links_with_user_ids": [],
          "profile_context_facepile_users": [],
          "has_chaining": true,
          "pk": 314216,
          "pk_id": "314216",
          "username": "zuck",
          "full_name": "Mark Zuckerberg",
          "is_private": false,
          "follow_friction_type": 0,
          "is_verified": true,
          "profile_pic_id": "3138909791791822006_314216",
          "profile_pic_url": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-19/357376107_1330597350674698_8884059223384672080_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=euIj8dtTGIkAX_8Gm2Q&edm=AEF8tYYBAAAA&ccb=7-5&oh=00_AfD5zX6BkQpgR-H-iTsZ2PlwDEOXnf7PCbohypiV8Aj10g&oe=64B0D240&_nc_sid=1e20d2",
          "current_catalog_id": null,
          "mini_shop_seller_onboarding_status": null,
          "shopping_post_onboard_nux_type": null,
          "ads_incentive_expiration_date": null,
          "displayed_action_button_partner": null,
          "smb_delivery_partner": null,
          "smb_support_delivery_partner": null,
          "displayed_action_button_type": "",
          "smb_support_partner": null,
          "is_call_to_action_enabled": false,
          "num_of_admined_pages": null,
          "category": "Entrepreneur",
          "account_badges": [],
          "show_account_transparency_details": true,
          "existing_user_age_collection_enabled": true,
          "show_post_insights_entry_point": true,
          "has_public_tab_threads": true,
          "third_party_downloads_enabled": 1,
          "is_regulated_c18": false,
          "is_in_canada": false,
          "profile_type": 0,
          "is_profile_broadcast_sharing_enabled": true,
          "has_exclusive_feed_content": false,
          "has_fan_club_subscriptions": false,
          "is_memorialized": false,
          "open_external_url_with_in_app_browser": true,
          "pinned_channels_info": {
              "pinned_channels_list": [],
              "has_public_channels": false
          },
          "request_contact_enabled": false,
          "robi_feedback_source": null,
          "chaining_results": null,
          "is_bestie": false,
          "remove_message_entrypoint": false,
          "auto_expand_chaining": false,
          "is_new_to_instagram": false,
          "highlight_reshare_disabled": false
      },
      "status": "ok"
  }
  ```
</details>

##### Get Followers

`threads.private_api.get_user_followers` — getting a user's followers by the user's identifier.

| Parameters |  Type   | Required | Restrictions | Description          |
|:----------:|:-------:|:--------:|:------------:|----------------------|
|    `id`    | Integer |   Yes    |     `>0`     | A user's identifier. |

<details>
  <summary>Open example</summary>
  
  ```python3
  >>> user_followers = threads.private_api.get_user_followers(id=314216)
  >>> user_followers
  {
      "users": [
          {
              "has_anonymous_profile_picture": false,
              "fbid_v2": "17841407032091362",
              "has_onboarded_to_text_post_app": true,
              "text_post_app_joiner_number": 100165200,
              "pk": 6970898403,
              "pk_id": "6970898403",
              "username": "ali_moslemi_",
              "full_name": "",
              "is_private": true,
              "is_verified": false,
              "profile_pic_id": "3143675402396969798_6970898403",
              "profile_pic_url": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-19/358504236_795240265474093_1873793041193487951_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=101&_nc_ohc=NDKSnch-bEoAX9bRFSg&edm=APQMUHMBAAAA&ccb=7-5&oh=00_AfBAOL--evGSmg6slpcKO-Bmo1I8rXokvlMygal0yEep5A&oe=64AFB4B0&_nc_sid=6ff7c8",
              "account_badges": [],
              "is_possible_scammer": false,
              "third_party_downloads_enabled": 0,
              "is_possible_bad_actor": {
                  "is_possible_scammer": false,
                  "is_possible_impersonator": {
                      "is_unconnected_impersonator": false
                  }
              },
              "latest_reel_media": 0
          },
          ...
      ],
      "big_list": false,
      "page_size": 200,
      "has_more": false,
      "should_limit_list_of_followers": false,
      "status": "ok"
  }
  ```
</details>

##### Get Following

`threads.private_api.get_user_following` — getting a user's following by the user's identifier.

| Parameters |  Type   | Required | Restrictions | Description          |
|:----------:|:-------:|:--------:|:------------:|----------------------|
|    `id`    | Integer |   Yes    |     `>0`     | A user's identifier. |

<details>
  <summary>Open example</summary>
  
  ```python3
  >>> user_following = threads.private_api.get_user_following(id=314216)
  >>> user_following
  {
      "users": [
          {
              "has_anonymous_profile_picture": false,
              "fbid_v2": "17841400595560228",
              "has_onboarded_to_text_post_app": true,
              "text_post_app_joiner_number": 37063252,
              "pk": 14611852,
              "pk_id": "14611852",
              "username": "mikesego",
              "full_name": "Mike Sego",
              "is_private": false,
              "is_verified": false,
              "profile_pic_id": "3141060757056532902_14611852",
              "profile_pic_url": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-19/358004364_2046926358984696_1656910531495082901_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=100&_nc_ohc=6Hb0M2drxbIAX9eVeGw&edm=ALB854YBAAAA&ccb=7-5&oh=00_AfAeVVBHAjmjJtmatY9YTDLovtOXJwzM-netZTUN_ghOLw&oe=64B028E3&_nc_sid=ce9561",
              "account_badges": [],
              "is_possible_scammer": false,
              "third_party_downloads_enabled": 1,
              "is_possible_bad_actor": {
                  "is_possible_scammer": false,
                  "is_possible_impersonator": {
                      "is_unconnected_impersonator": false
                  }
              },
              "latest_reel_media": 0,
              "is_favorite": false
          },
          ...
      ],
      "big_list": true,
      "page_size": 200,
      "next_max_id": "100",
      "has_more": false,
      "should_limit_list_of_followers": false,
      "status": "ok"
  }
  ```
</details>

##### Search

`threads.private_api.search_user` — search for a user by a query.

| Parameters |  Type  | Required | Restrictions | Description     |
|:----------:|:------:|:--------:|:------------:|-----------------|
|  `query`   | String |   Yes    |      -       | A search query. |

<details>
  <summary>Open example</summary>
  
  ```python3
  >>> found_users = threads.private_api.search_user(query='zuck')
  >>> found_users
  {
      "num_results": 55,
      "users": [
          {
              "has_anonymous_profile_picture": false,
              "follower_count": 2779681,
              "media_count": 283,
              "following_count": 313,
              "following_tag_count": 3,
              "fbid_v2": "17841401746480004",
              "has_onboarded_to_text_post_app": true,
              "show_text_post_app_badge": true,
              "text_post_app_joiner_number": 1,
              "show_ig_app_switcher_badge": true,
              "pk": 314216,
              "pk_id": "314216",
              "username": "zuck",
              "full_name": "Mark Zuckerberg",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3138909791791822006_314216",
              "profile_pic_url": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-19/357376107_1330597350674698_8884059223384672080_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=euIj8dtTGIkAX_8Gm2Q&edm=AM7KJZYBAAAA&ccb=7-5&oh=00_AfBozKxHv4GtcQ5ZwnPSS_eL9ONAYNekI1hhOWPGgNPaxA&oe=64B0D240&_nc_sid=8ec269",
              "has_opt_eligible_shop": false,
              "account_badges": [],
              "third_party_downloads_enabled": 1,
              "unseen_count": 0,
              "friendship_status": {
                  "following": false,
                  "is_private": false,
                  "incoming_request": false,
                  "outgoing_request": false,
                  "text_post_app_pre_following": false,
                  "is_bestie": false,
                  "is_restricted": false,
                  "is_feed_favorite": false
              },
              "latest_reel_media": 0,
              "should_show_category": false
          },
          ...
      ],
      "has_more": false,
      "rank_token": "21af3266-ddec-4166-b00c-091a580a54a8",
      "status": "ok"
  }
  ```
</details>

##### Follow

`threads.private_api.follow_user` — follow a user.

| Parameters |  Type   | Required | Restrictions | Description                        |
|:----------:|:-------:|:--------:|:------------:|------------------------------------|
|    `id`    | Integer |   Yes    |     `>0`     | An identifier of a user to follow. |

<details>
  <summary>Open example</summary>
  
  ```python3
  >>> following = threads.private_api.follow_user(id=314216)
  >>> following
  {
      "friendship_status": {
          "following": true,
          "followed_by": false,
          "blocking": false,
          "muting": false,
          "is_private": false,
          "incoming_request": false,
          "outgoing_request": false,
          "text_post_app_pre_following": false,
          "is_bestie": false,
          "is_restricted": false,
          "is_feed_favorite": false,
          "is_eligible_to_subscribe": false
      },
      "previous_following": false,
      "status": "ok"
  }
  ```
</details>

##### Unfollow

`threads.private_api.unfollow_user` — unfollow a user.

| Parameters |  Type   | Required | Restrictions | Description                          |
|:----------:|:-------:|:--------:|:------------:|--------------------------------------|
|    `id`    | Integer |   Yes    |     `>0`     | An identifier of a user to unfollow. |

<details>
  <summary>Open example</summary>
  
  ```python3
  >>> following = threads.private_api.unfollow_user(id=314216)
  >>> following
  {
      "friendship_status": {
          "following": false,
          "followed_by": false,
          "blocking": false,
          "muting": false,
          "is_private": false,
          "incoming_request": false,
          "outgoing_request": false,
          "text_post_app_pre_following": false,
          "is_bestie": false,
          "is_restricted": false,
          "is_feed_favorite": false,
          "is_eligible_to_subscribe": false
      },
      "status": "ok"
  }
  ```
</details>

#### Thread

##### Get Identifier

`threads.private_api.get_thread_id` — getting a thread's identifier by its `URL` identifier. `URL` identifier is a last 
part of a thread's website `URL`. If the thread's `URL` is `https://threads.net/t/CuXFPIeLLod`, then it would be `CuXFPIeLLod`.

| Parameters |  Type  | Required | Restrictions | Description                  |
|:----------:|:------:|:--------:|:------------:|------------------------------|
|  `url_id`  | String |   Yes    |      -       | A thread's `URL` identifier. |

<details>
  <summary>Open example</summary>
  
  ```python3
  >>> thread_id = threads.private_api.get_thread_id(url_id='CuXFPIeLLod')
  >>> thread_id
  3141002295235099165
  ```
</details>

##### Get By Identifier

`threads.private_api.get_thread` — getting a thread by its identifier.

| Parameters |  Type   | Required | Restrictions | Description            |
|:----------:|:-------:|:--------:|:------------:|------------------------|
|    `id`    | Integer |   Yes    |     `>0`     | A thread's identifier. |

<details>
  <summary>Open example</summary>
  
  ```python3
  >>> thread = threads.private_api.get_thread(id=3141002295235099165)
  >>> thread
  {
      "data": {
          "data": {
              "containing_thread": {
                  "thread_items": [
                      {
                          "post": {
                              "user": {
                                  "profile_pic_url": "https://scontent.cdninstagram.com/v/t51.2885-19/343392897_618515990300243_8088199406170073086_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=1xtR491RY6cAX8Okf3Z&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfDqsZTCRQlz7EaDpgEzBkmXqtqKtTH80Q0r1rIDMJCcpg&oe=64AC2D8D&_nc_sid=10d13b",
                                  "username": "mosseri",
                                  "id": null,
                                  "is_verified": true,
                                  "pk": "95561"
                              },
                              "image_versions2": {
                                  "candidates": []
                              },
                              "original_width": 612,
                              "original_height": 612,
                              "video_versions": [],
                              "carousel_media": null,
                              "carousel_media_count": null,
                              "pk": "3141055616164096839",
                              "has_audio": null,
                              "text_post_app_info": {
                                  "link_preview_attachment": null,
                                  "share_info": {
                                      "quoted_post": null,
                                      "reposted_post": null
                                  },
                                  "reply_to_author": null,
                                  "is_post_unavailable": false,
                                  "direct_reply_count": 2839
                              },
                              "caption": {
                                  "text": "I've been getting some questions about deleting your account. To clarify, you can deactivate your Threads account, which hides your Threads profile and content, you can set your profile to private, and you can delete individual threads posts \u2013 all without deleting your Instagram account. Threads is powered by Instagram, so right now it's just one account, but we're looking into a way to delete your Threads account separately."
                              },
                              "taken_at": 1688663030,
                              "like_count": 29984,
                              "code": "CuXRXDdNOtH",
                              "media_overlay_info": null,
                              "id": "3141055616164096839_95561"
                          },
                          "line_type": "none",
                          "view_replies_cta_string": "2,839 replies",
                          "reply_facepile_users": [],
                          "should_show_replies_cta": true
                      }
                  ],
                  "thread_type": "thread",
                  "header": null,
                  "id": "3141055616164096839"
              },
              "reply_threads": [
                  {
                      "thread_items": [
                          {
                              "post": {
                                  "user": {
                                      "profile_pic_url": "https://scontent.cdninstagram.com/v/t51.2885-19/355424589_948742193018772_4617955233166333765_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=100&_nc_ohc=heQWdfsKG5MAX9mLim0&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfA6TUpLjjegnP6KuducRm8n6uU9iBCXg4O1P33WYSh3mg&oe=64ACDDBA&_nc_sid=10d13b",
                                      "username": "jimmywhotalks",
                                      "id": null,
                                      "is_verified": true,
                                      "pk": "51094265817"
                                  },
                                  "image_versions2": {
                                      "candidates": []
                                  },
                                  "original_width": 612,
                                  "original_height": 612,
                                  "video_versions": [],
                                  "carousel_media": null,
                                  "carousel_media_count": null,
                                  "pk": "3141082664316809193",
                                  "has_audio": null,
                                  "text_post_app_info": {
                                      "link_preview_attachment": null,
                                      "share_info": {
                                          "quoted_post": null,
                                          "reposted_post": null
                                      },
                                      "reply_to_author": {
                                          "username": "mosseri",
                                          "id": null
                                      },
                                      "is_post_unavailable": false
                                  },
                                  "caption": {
                                      "text": "Glad to know, Everyone is worrying for that."
                                  },
                                  "taken_at": 1688666254,
                                  "like_count": 59,
                                  "code": "CuXXgqAva_p",
                                  "media_overlay_info": null,
                                  "id": "3141082664316809193_51094265817"
                              },
                              "line_type": "none",
                              "view_replies_cta_string": null,
                              "reply_facepile_users": [],
                              "should_show_replies_cta": false
                          }
                      ],
                      "thread_type": "thread",
                      "header": null,
                      "id": "3141082664316809193"
                  },
                  ...
              ]
          }
      },
      "extensions": {
          "is_final": true
      }
  }
  ```
</details>

##### Get Likers

`threads.private_api.get_thread_likers` — getting a thread's likers by the thread's identifier.

| Parameters |  Type   | Required | Restrictions | Description            |
|:----------:|:-------:|:--------:|:------------:|------------------------|
|    `id`    | Integer |   Yes    |     `>0`     | A thread's identifier. |

<details>
  <summary>Open example</summary>
  
  ```python3
  >>> thread_likers = threads.private_api.get_thread_likers(id=3141055616164096839)
  >>> thread_likers
  {
      "users": [
          {
              "pk": 54831820289,
              "pk_id": "54831820289",
              "username": "hazrel_syfddn26",
              "full_name": "HAZLER",
              "is_private": false,
              "account_badges": [],
              "is_verified": false,
              "profile_pic_id": "3140964514487728732_54831820289",
              "profile_pic_url": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-19/358165944_6109031802541294_1514688336008099084_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=110&_nc_ohc=V1UF-ylegwMAX_HbWIV&edm=APwHDrQBAAAA&ccb=7-5&oh=00_AfC4W3z1EZ61XFQk6Im82OpgoEvQp_r-JNPd2NmN9cdhUQ&oe=64B23019&_nc_sid=8809c9",
              "has_onboarded_to_text_post_app": true,
              "latest_reel_media": 0
          },
          ...
      ],
      "user_count": 38283,
      "status": "ok"
  }
  ```
</details>

##### Create

`threads.private_api.create_thread` — create a thread. You can create a thread with an attachment link or image (
specifying either `HTTP(S)` `URL` or path to a file). Also, you are able to create a thread as a reply to another
thread. Basically, each thread is either a root or linked to another thread like a graph. You can check 
`https://www.threads.net/@threadstester1` for all the examples of possible threads.

| Parameters  |  Type  | Required | Restrictions | Description                                 |
|:-----------:|:------:|:--------:|:------------:|---------------------------------------------|
|  `caption`  | String |   Yes    |      -       | A thread's caption.                         |
|    `url`    | String |    No    |      -       | A thread's attachment `URL`.                |
| `image_url` | String |    No    |      -       | An image's `HTTP(S)` URL or path to a file. |
| `reply_to`  | String |    No    |      -       | An identifier of a thread to reply to.      |

<details>
  <summary>Open example</summary>
  
  ```python3
  >>> created_thread = threads.private_api.create_thread(
          caption='Hello, world!',
      )
  >>> created_thread = threads.private_api.create_thread(
          caption='Hello, world!',
          url='https://www.youtube.com/watch?v=lc4qU6BakvE'
      )
  >>> created_thread = threads.private_api.create_thread(
          caption='Hello, world!',
          image_url='/Users/dmytrostriletskyi/projects/threads/assets/picture.png',
      )
  >>> created_thread = threads.private_api.create_thread(
          caption='Hello, world!',
          image_url='https://raw.githubusercontent.com/dmytrostriletskyi/threads-net/main/assets/picture.png',
          reply_to=3141055616164096839,
      )
  >>> created_thread
  {
      "media": {
          "taken_at": 1689087793,
          "pk": 3144618785809596584,
          "id": "3144618785809596584_32545771157",
          "device_timestamp": 1689087791,
          "media_type": 1,
          "code": "Cuj7h_yM4Co",
          "client_cache_key": "MzE0NDYxODc4NTgwOTU5NjU4NA==.2",
          "filter_type": 0,
          "can_viewer_reshare": true,
          "caption": {
              "pk": "17986860047032912",
              "user_id": 32545771157,
              "text": "Hello, world!",
              "type": 1,
              "created_at": 1689087793,
              "created_at_utc": 1689087793,
              "content_type": "comment",
              "status": "Active",
              "bit_flags": 0,
              "did_report_as_spam": false,
              "share_enabled": false,
              "user": {
                  "has_anonymous_profile_picture": true,
                  "liked_clips_count": 0,
                  "fan_club_info": {
                      "fan_club_id": null,
                      "fan_club_name": null,
                      "is_fan_club_referral_eligible": null,
                      "fan_consideration_page_revamp_eligiblity": null,
                      "is_fan_club_gifting_eligible": null,
                      "subscriber_count": null,
                      "connected_member_count": null,
                      "autosave_to_exclusive_highlight": null,
                      "has_enough_subscribers_for_ssc": null
                  },
                  "fbid_v2": 17841432494728221,
                  "transparency_product_enabled": false,
                  "text_post_app_take_a_break_setting": 0,
                  "interop_messaging_user_fbid": 17842937552083158,
                  "show_insights_terms": false,
                  "allowed_commenter_type": "any",
                  "is_unpublished": false,
                  "reel_auto_archive": "unset",
                  "can_boost_post": false,
                  "can_see_organic_insights": false,
                  "has_onboarded_to_text_post_app": true,
                  "text_post_app_joiner_number": 68427510,
                  "pk": 32545771157,
                  "pk_id": "32545771157",
                  "username": "dmytro.striletskyi",
                  "full_name": "Dmytro Striletskyi",
                  "is_private": false,
                  "profile_pic_url": "https://scontent-cdg4-1.cdninstagram.com/v/t51.2885-19/44884218_345707102882519_2446069589734326272_n.jpg?_nc_ht=scontent-cdg4-1.cdninstagram.com&_nc_cat=1&_nc_ohc=s7XO4bcYceYAX9jyeT8&edm=AAAAAAABAAAA&ccb=7-5&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.2-ccb7-5&oh=00_AfBhetyTgz8h53kRlSorYqET2tbmZOmYt2jiucME8qI7AQ&oe=64B3528F",
                  "account_badges": [],
                  "feed_post_reshare_disabled": false,
                  "show_account_transparency_details": true,
                  "third_party_downloads_enabled": 0
              },
              "is_covered": false,
              "is_ranked_comment": false,
              "media_id": 3144618785809596584,
              "private_reply_status": 0
          },
          "clips_tab_pinned_user_ids": [],
          "comment_inform_treatment": {
              "should_have_inform_treatment": false,
              "text": "",
              "url": null,
              "action_type": null
          },
          "fundraiser_tag": {
              "has_standalone_fundraiser": false
          },
          "sharing_friction_info": {
              "should_have_sharing_friction": false,
              "bloks_app_url": null,
              "sharing_friction_payload": null
          },
          "xpost_deny_reason": "This post cannot be shared to Facebook.",
          "caption_is_edited": false,
          "original_media_has_visual_reply_media": false,
          "like_and_view_counts_disabled": false,
          "fb_user_tags": {
              "in": []
          },
          "mashup_info": {
              "mashups_allowed": true,
              "can_toggle_mashups_allowed": true,
              "has_been_mashed_up": false,
              "formatted_mashups_count": null,
              "original_media": null,
              "privacy_filtered_mashups_media_count": null,
              "non_privacy_filtered_mashups_media_count": null,
              "mashup_type": null,
              "is_creator_requesting_mashup": false,
              "has_nonmimicable_additional_audio": false,
              "is_pivot_page_available": false
          },
          "can_viewer_save": true,
          "is_in_profile_grid": false,
          "profile_grid_control_enabled": false,
          "featured_products": [],
          "is_comments_gif_composer_enabled": true,
          "product_suggestions": [],
          "user": {
              "has_anonymous_profile_picture": true,
              "liked_clips_count": 0,
              "fan_club_info": {
                  "fan_club_id": null,
                  "fan_club_name": null,
                  "is_fan_club_referral_eligible": null,
                  "fan_consideration_page_revamp_eligiblity": null,
                  "is_fan_club_gifting_eligible": null,
                  "subscriber_count": null,
                  "connected_member_count": null,
                  "autosave_to_exclusive_highlight": null,
                  "has_enough_subscribers_for_ssc": null
              },
              "fbid_v2": 17841432494728221,
              "transparency_product_enabled": false,
              "text_post_app_take_a_break_setting": 0,
              "interop_messaging_user_fbid": 17842937552083158,
              "show_insights_terms": false,
              "allowed_commenter_type": "any",
              "is_unpublished": false,
              "reel_auto_archive": "unset",
              "can_boost_post": false,
              "can_see_organic_insights": false,
              "has_onboarded_to_text_post_app": true,
              "text_post_app_joiner_number": 68427510,
              "pk": 32545771157,
              "pk_id": "32545771157",
              "username": "dmytro.striletskyi",
              "full_name": "Dmytro Striletskyi",
              "is_private": false,
              "profile_pic_url": "https://scontent-cdg4-1.cdninstagram.com/v/t51.2885-19/44884218_345707102882519_2446069589734326272_n.jpg?_nc_ht=scontent-cdg4-1.cdninstagram.com&_nc_cat=1&_nc_ohc=s7XO4bcYceYAX9jyeT8&edm=AAAAAAABAAAA&ccb=7-5&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.2-ccb7-5&oh=00_AfBhetyTgz8h53kRlSorYqET2tbmZOmYt2jiucME8qI7AQ&oe=64B3528F",
              "account_badges": [],
              "feed_post_reshare_disabled": false,
              "show_account_transparency_details": true,
              "third_party_downloads_enabled": 0
          },
          "image_versions2": {
              "candidates": [
                  {
                      "width": 980,
                      "height": 652,
                      "url": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-15/359145974_1454822158673126_2191780209015799278_n.jpg?stp=dst-jpg_e35&_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=8vV5VulJfUwAX-jnGZU&edm=AL_hgCEBAAAA&ccb=7-5&ig_cache_key=MzE0NDYxODc4NTgwOTU5NjU4NA%3D%3D.2-ccb7-5&oh=00_AfB5avonpo72-x_5Te_cXCKf2aM6jJO9dGmmejvdV821zg&oe=64B3067E&_nc_sid=e50d24",
                      "scans_profile": "e35"
                  },
                  {
                      "width": 720,
                      "height": 479,
                      "url": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-15/359145974_1454822158673126_2191780209015799278_n.jpg?stp=dst-jpg_e35_s720x720&_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=8vV5VulJfUwAX-jnGZU&edm=AL_hgCEBAAAA&ccb=7-5&ig_cache_key=MzE0NDYxODc4NTgwOTU5NjU4NA%3D%3D.2-ccb7-5&oh=00_AfBJhcGMT6yd6pECPVoeFAIoTIcgOzTw6zDKxs8ZdZK1CA&oe=64B3067E&_nc_sid=e50d24",
                      "scans_profile": "e35"
                  },
                  {
                      "width": 640,
                      "height": 426,
                      "url": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-15/359145974_1454822158673126_2191780209015799278_n.jpg?stp=dst-jpg_e35_s640x640_sh0.08&_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=8vV5VulJfUwAX-jnGZU&edm=AL_hgCEBAAAA&ccb=7-5&ig_cache_key=MzE0NDYxODc4NTgwOTU5NjU4NA%3D%3D.2-ccb7-5&oh=00_AfBPn-IvLSL4PYxQQoFyFyHFuimEtfKoDq7EoCys3xaMWg&oe=64B3067E&_nc_sid=e50d24",
                      "scans_profile": "e35"
                  },
                  {
                      "width": 480,
                      "height": 319,
                      "url": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-15/359145974_1454822158673126_2191780209015799278_n.jpg?stp=dst-jpg_e35_s480x480&_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=8vV5VulJfUwAX-jnGZU&edm=AL_hgCEBAAAA&ccb=7-5&ig_cache_key=MzE0NDYxODc4NTgwOTU5NjU4NA%3D%3D.2-ccb7-5&oh=00_AfDiPNhb5u_FX3VKC8KZ1rmN7yvmmTMiunWJBK25yuly4A&oe=64B3067E&_nc_sid=e50d24",
                      "scans_profile": "e35"
                  },
                  {
                      "width": 320,
                      "height": 213,
                      "url": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-15/359145974_1454822158673126_2191780209015799278_n.jpg?stp=dst-jpg_e35_s320x320&_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=8vV5VulJfUwAX-jnGZU&edm=AL_hgCEBAAAA&ccb=7-5&ig_cache_key=MzE0NDYxODc4NTgwOTU5NjU4NA%3D%3D.2-ccb7-5&oh=00_AfAy8wZuJneP3N_g6PyDKk-2kiAGLvPO4XPfK1MBwVSSPw&oe=64B3067E&_nc_sid=e50d24",
                      "scans_profile": "e35"
                  },
                  {
                      "width": 240,
                      "height": 160,
                      "url": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-15/359145974_1454822158673126_2191780209015799278_n.jpg?stp=dst-jpg_e35_s240x240&_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=8vV5VulJfUwAX-jnGZU&edm=AL_hgCEBAAAA&ccb=7-5&ig_cache_key=MzE0NDYxODc4NTgwOTU5NjU4NA%3D%3D.2-ccb7-5&oh=00_AfDnUnB202rqbhfPupeNKKd-NRM9e4-FvsnnGD2FsEY_bQ&oe=64B3067E&_nc_sid=e50d24",
                      "scans_profile": "e35"
                  },
                  {
                      "width": 1080,
                      "height": 1080,
                      "url": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-15/359145974_1454822158673126_2191780209015799278_n.jpg?stp=c164.0.652.652a_dst-jpg_e35&_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=8vV5VulJfUwAX-jnGZU&edm=AL_hgCEBAAAA&ccb=7-5&ig_cache_key=MzE0NDYxODc4NTgwOTU5NjU4NA%3D%3D.2-ccb7-5&oh=00_AfDGwvzJe8hIAfBBrRerzo8PCdQAey0_Q9uJSF5eGz1f-w&oe=64B3067E&_nc_sid=e50d24",
                      "scans_profile": "e35"
                  },
                  {
                      "width": 750,
                      "height": 750,
                      "url": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-15/359145974_1454822158673126_2191780209015799278_n.jpg?stp=c164.0.652.652a_dst-jpg_e35_s750x750_sh0.08&_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=8vV5VulJfUwAX-jnGZU&edm=AL_hgCEBAAAA&ccb=7-5&ig_cache_key=MzE0NDYxODc4NTgwOTU5NjU4NA%3D%3D.2-ccb7-5&oh=00_AfD2nnAd_T-Zj3cX0-TUEjajO9jn3EMfKwaUHwLmagBhiA&oe=64B3067E&_nc_sid=e50d24",
                      "scans_profile": "e35"
                  },
                  {
                      "width": 640,
                      "height": 640,
                      "url": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-15/359145974_1454822158673126_2191780209015799278_n.jpg?stp=c164.0.652.652a_dst-jpg_e35_s640x640_sh0.08&_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=8vV5VulJfUwAX-jnGZU&edm=AL_hgCEBAAAA&ccb=7-5&ig_cache_key=MzE0NDYxODc4NTgwOTU5NjU4NA%3D%3D.2-ccb7-5&oh=00_AfB0kVjlsVkk26Rqad6KRlMWTOxs88NzLS1iuHpHYLU1tA&oe=64B3067E&_nc_sid=e50d24",
                      "scans_profile": "e35"
                  },
                  {
                      "width": 480,
                      "height": 480,
                      "url": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-15/359145974_1454822158673126_2191780209015799278_n.jpg?stp=c164.0.652.652a_dst-jpg_e35_s480x480&_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=8vV5VulJfUwAX-jnGZU&edm=AL_hgCEBAAAA&ccb=7-5&ig_cache_key=MzE0NDYxODc4NTgwOTU5NjU4NA%3D%3D.2-ccb7-5&oh=00_AfCo8QoGPw8tlIavEsSbZkMoZOFdey8XM0--RAIABYqxZQ&oe=64B3067E&_nc_sid=e50d24",
                      "scans_profile": "e35"
                  },
                  {
                      "width": 320,
                      "height": 320,
                      "url": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-15/359145974_1454822158673126_2191780209015799278_n.jpg?stp=c164.0.652.652a_dst-jpg_e35_s320x320&_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=8vV5VulJfUwAX-jnGZU&edm=AL_hgCEBAAAA&ccb=7-5&ig_cache_key=MzE0NDYxODc4NTgwOTU5NjU4NA%3D%3D.2-ccb7-5&oh=00_AfAfleZMSb3Ae50Fj1dhDUYc6slUO5zxUKwcKYL0PmHNkA&oe=64B3067E&_nc_sid=e50d24",
                      "scans_profile": "e35"
                  },
                  {
                      "width": 240,
                      "height": 240,
                      "url": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-15/359145974_1454822158673126_2191780209015799278_n.jpg?stp=c164.0.652.652a_dst-jpg_e35_s240x240&_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=8vV5VulJfUwAX-jnGZU&edm=AL_hgCEBAAAA&ccb=7-5&ig_cache_key=MzE0NDYxODc4NTgwOTU5NjU4NA%3D%3D.2-ccb7-5&oh=00_AfAR1f9S-NF_DwhyaSq0qzme6k4rDsGb6RfWkgnw07Tt1A&oe=64B3067E&_nc_sid=e50d24",
                      "scans_profile": "e35"
                  },
                  {
                      "width": 150,
                      "height": 150,
                      "url": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-15/359145974_1454822158673126_2191780209015799278_n.jpg?stp=c164.0.652.652a_dst-jpg_e35_s150x150&_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=8vV5VulJfUwAX-jnGZU&edm=AL_hgCEBAAAA&ccb=7-5&ig_cache_key=MzE0NDYxODc4NTgwOTU5NjU4NA%3D%3D.2-ccb7-5&oh=00_AfAYtetjgt4tQah5PnX8LXRlrUGS0A1uH4kkUrUPNwcr_g&oe=64B3067E&_nc_sid=e50d24",
                      "scans_profile": "e35"
                  }
              ]
          },
          "original_width": 980,
          "original_height": 652,
          "is_reshare_of_text_post_app_media_in_ig": false,
          "comment_threading_enabled": false,
          "max_num_visible_preview_comments": 2,
          "has_more_comments": false,
          "preview_comments": [],
          "comment_count": 0,
          "can_view_more_preview_comments": false,
          "hide_view_all_comment_entrypoint": false,
          "likers": [],
          "shop_routing_user_id": null,
          "can_see_insights_as_brand": false,
          "is_organic_product_tagging_eligible": false,
          "product_type": "feed",
          "is_paid_partnership": false,
          "music_metadata": {
              "music_canonical_id": "0",
              "audio_type": null,
              "music_info": null,
              "original_sound_info": null,
              "pinned_media_ids": null
          },
          "deleted_reason": 0,
          "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjpmYWxzZSwidXVpZCI6IjQxNjBkY2E0ODY1YzQyODY5NThhOWE3M2I2N2UyZWI0MzE0NDYxODc4NTgwOTU5NjU4NCIsInNlcnZlcl90b2tlbiI6IjE2ODkwODc3OTYwOTZ8MzE0NDYxODc4NTgwOTU5NjU4NHwzMjU0NTc3MTE1N3xiY2RkZjliZGNlZjFiMzNlZDIzZTJiZDg4M2E0MjAzZmNlMjQ1ZjI2MjdmYWZiNDgwNTlhNjBiMzgwYjM1MjA3In0sInNpZ25hdHVyZSI6IiJ9",
          "text_post_app_info": {
              "is_post_unavailable": false,
              "is_reply": true,
              "reply_to_author": {
                  "pk": 95561,
                  "pk_id": "95561",
                  "username": "mosseri",
                  "full_name": "Adam Mosseri",
                  "is_private": false,
                  "is_verified": true,
                  "profile_pic_id": "3090458139926225297_95561",
                  "profile_pic_url": "https://instagram.fiev6-1.fna.fbcdn.net/v/t51.2885-19/343392897_618515990300243_8088199406170073086_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fiev6-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=H93HRKonYSQAX9OmlMQ&edm=AL_hgCEBAAAA&ccb=7-5&oh=00_AfC8sdQl6N1YwEs5Xva8HSfc98_zv7l4beWBQVuVBkHxJA&oe=64B21C4D&_nc_sid=e50d24",
                  "has_onboarded_to_text_post_app": true
              },
              "direct_reply_count": 0,
              "self_thread_count": 0,
              "reply_facepile_users": [],
              "link_preview_attachment": null,
              "can_reply": true,
              "reply_control": "everyone",
              "hush_info": null,
              "share_info": {
                  "can_repost": true,
                  "is_reposted_by_viewer": false,
                  "can_quote_post": true
              }
          },
          "integrity_review_decision": "pending",
          "ig_media_sharing_disabled": false,
          "has_shared_to_fb": 0,
          "is_unified_video": false,
          "should_request_ads": false,
          "is_visual_reply_commenter_notice_enabled": true,
          "commerciality_status": "not_commercial",
          "explore_hide_comments": false,
          "has_delayed_metadata": false
      },
      "upload_id": "1689087791",
      "status": "ok"
  }
  ```
</details>

##### Delete

`threads.private_api.delete_thread` — delete a thread.

| Parameters |  Type   | Required | Restrictions | Description                          |
|:----------:|:-------:|:--------:|:------------:|--------------------------------------|
|    `id`    | Integer |   Yes    |     `>0`     | An identifier of a thread to delete. |

<details>
  <summary>Open example</summary>
  
  ```python3
  >>> deletion = threads.private_api.delete_thread(id=3141055616164096839)
  >>> deletion
  {
      "did_delete": true,
      "cxp_deep_deletion_global_response": {},
      "status": "ok"
  }
  ```
</details>

##### Like

`threads.private_api.like_thread` — like a thread.

| Parameters |  Type   | Required | Restrictions | Description                        |
|:----------:|:-------:|:--------:|:------------:|------------------------------------|
|    `id`    | Integer |   Yes    |     `>0`     | An identifier of a thread to like. |

<details>
  <summary>Open example</summary>
  
  ```python3
  >>> liking = threads.private_api.like_thread(id=3141055616164096839)
  >>> liking
  {
      "status": "ok"
  }
  ```
</details>

##### Unlike

`threads.private_api.unlike_thread` — unlike a thread.

| Parameters |  Type   | Required | Restrictions | Description                          |
|:----------:|:-------:|:--------:|:------------:|--------------------------------------|
|    `id`    | Integer |   Yes    |     `>0`     | An identifier of a thread to unlike. |

<details>
  <summary>Open example</summary>
  
  ```python3
  >>> unliking = threads.private_api.unlike_thread(id=3141055616164096839)
  >>> unliking
  {
      "status": "ok"
  }
  ```
</details>
