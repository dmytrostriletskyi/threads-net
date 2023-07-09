[![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner-direct-single.svg)](https://stand-with-ukraine.pp.ua)

Threads (threads.net) Python API wrapper.

[![Downloads](https://pepy.tech/badge/threads-net)](https://pepy.tech/project/threads-net)
[![PyPI license](https://img.shields.io/pypi/l/threads-net.svg)](https://pypi.python.org/pypi/threads-net/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/threads-net.svg)](https://pypi.python.org/pypi/threads-net/)

Table of content:

* [Disclaimer](#disclaimer)
* [Roadmap](#roadmap)
* [Getting started](#getting-started)
  * [How to install](#how-to-install)
  * [Initialization](#initialization)
  * [Examples](#examples)
* [API](#api)
  * [Login](#login)
  * [Get User Identifier](#get-user-identifier)
  * [Get User By Identifier](#get-user-by-identifier)
  * [Get User Threads](#get-user-threads)
  * [Get User Replies](#get-user-replies)
  * [Get Post Identifier](#get-post-identifier)
  * [Get Post](#get-post)
  * [Get Post Likers](#get-post-likers)

## Disclaimer

* As `Threads` are backed by `Instagram`. It means that `Threads` functionality partially placed in `Instagram API`:
  you do a login to `Threads` application via `Instagram`'s username and password, posting new threads and fetching user
  identifier (for further library usage) too. So expect seeing things related to `Instagram` in this library.
* This project is unofficial and utilize both public and private endpoints of both `Threads` and `Instagram` `APIs`. 
  Utilizing private endpoints means pretending being a mobile phone or web user (via proper `HTTP` headers and other 
  things). Thus you might face `rate limits` (because pretending is never ideal) or even your account in `Threads` and 
  `Instagram` might be suspended if mess up with logining or sending too much requests. So use the project at your own 
  risk until the normal public `ThreadsAPI` is released or this product become more stable for such things.Also,
  utilizing such endpoints mean that they might not be stable (because they are under active development and there is
  no any promise in backward compatibility).
* For all the `Instagram`-related thing other well-know and already stable library called [instagrapi](https://github.com/adw0rd/instagrapi)
  is used in `threads-net`.

## Roadmap

- [ ] Read public information
  - [x] Get a user's identifier
  - [x] Get a user by an identifier
  - [x] Get a user's threads
  - [x] Get a user's replies
  - [ ] Get a user's followers
  - [ ] Get a user's followings
  - [x] Get a post's identifier
  - [x] Get a post
  - [x] Get a post's likers
- [ ] Read private information
- [ ] Writing capabilities
  - [ ] Create a thread with text
  - [ ] Create a thread with media
  - [ ] Reply to an existing thread

## Getting started

### How to install

Install the library with the following command using `pip3`:

```bash
$ pip3 install threads-net
```

### Initialization

Import the class responsible for `Threads API` communication and start using it with the following commands:

```python3
>>> from threads import Threads
>>> threads = Threads()
```

### Examples

Find examples of how to use the library functionality in the `examples` folder:

```bash
➜  ls examples
examples
├── login.py
├── get_post.py
├── get_user.py
├── get_user_replies.py
└── get_user_threads.py
...
```

## API

### Login

In order for `Instagram` to trust you more, you must always login from one device and one IP (or from a subnet), for 
this there is the dump session functionality. So, once you logged in once, store it into a file:

```python3
>>> threads = Threads()
>>> threads.login('INSTAGRAM_USERNAME', 'INSTAGRAM_PASSWORD')
>>> threads.dump_settings('session.json')
```

Next time, just load the session from the file and use it for login with the following commands:

```python3
>>> threads = Threads()
>>> threads.load_settings('session.json')
>>> threads.login(os.environ.get('INSTAGRAM_USERNAME'), os.environ.get('INSTAGRAM_PASSWORD'))
```

The login method might ask for additional username/password entering, confirmation code and other challenges. But if
you reuse the session, those should happen minimum times. For more information, check this out — 
https://adw0rd.github.io/instagrapi/usage-guide/interactions.html

### Get User Identifier

To get a user's identifier by a username, use the following commands:

```python3
>>> user_id = threads.get_user_id(username='zuck')
>>> user_id
314216
```

### Get User by Identifier

To get a user by an identifier, use the following commands:

```python3
>>> user = threads.get_user(id=314216)
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

### Get User Threads

To get a user's threads, use the following commands:

```python3
>>> user_threads = threads.get_user_threads(id=314216)
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

### Get User Replies

To get a user's replies, use the following commands:

```python3
>>> user_replies = threads.get_user_replies(id=314216)
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

### Get Post Identifier

To get a post's identifier by a URL identifier. For instance, there is the URL — https://www.threads.net/t/CuXFPIeLLod.
The URL's identifier would be `CuXFPIeLLod`. Use the following commands:

```python3
>>> post_id = threads.get_post_id(url_id='CuXFPIeLLod')
>>> post_id
3141002295235099165
```

### Get Post

To get a post, use the following commands:

```python3
>>> post = threads.get_post(id=3141002295235099165)
>>> post
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

### Get Post Likers

To get a post's likers, use the following commands:

```python3
>>> post = threads.get_post_likers(id=3141002295235099165)
>>> post_likers
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
