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
  * [Get User Identifier](#get-user-identifier)
  * [Get User By Identifier](#get-user-by-identifier)
  * [Get User Threads](#get-user-threads)
  * [Get User Replies](#get-user-replies)
  * [Get Thread Identifier](#get-thread-identifier)
  * [Get Thread](#get-thread)
  * [Get Thread Likers](#get-thread-likers)
  * [Create Thread](#create-thread)

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

## Roadmap

- [ ] Read public information
  - [x] Get a user's identifier
  - [x] Get a user by an identifier
  - [x] Get a user's threads
  - [x] Get a user's replies
  - [ ] Get a user's followers
  - [ ] Get a user's followings
  - [x] Get a thread's identifier
  - [x] Get a thread
  - [x] Get a thread's likers
- [ ] Read private information
- [ ] Writing capabilities
  - [x] Create a thread with text
  - [ ] Create a thread with media
  - [ ] Reply to an existing thread

## Getting started

### How to install

Install the library with the following command using `pip3`:

```bash
$ pip3 install threads-net
```

### Initialization

Import the class responsible for `Threads API` communication and start using it with the following commands, specifying
`Instagram` username and password:

```python3
>>> from threads import Threads
>>> threads = Threads(username='instagram_username', password='instagram_password')
```

It is taken care of `rate limits`, so those are only used when it is really needed avoiding initialization authentication
(obtaining an `API` token) for each of the library method. Moreover, the `API` token will be cached and fetched only once.

Currently, only this list of methods will perform authentication:

* [Create Thread](#create-thread)

So, if you do not plan to use those method, you can leave them unspecified:

```python3
>>> from threads import Threads
>>> threads = Threads()
```

### Examples

Find examples of how to use the library in the `examples` folder:

```bash
ls examples
├── create_thread.py
├── get_thread.py
├── get_thread_likers.py
├── get_user.py
├── get_user_replies.py
└── get_user_threads.py
```

## API

There might be a confusion among many `Threads API` clients as well as in both `Threads` an `Instagram` `APIs` according
to the naming of entities. For instance, in `Threads` a publication is called a `thread`, but under the hood in the API
of fetching or creating a `thread` it is called a `post`. It is done because `Threads` are backed by `Instagram` and
`threads` creation is done on `Instagram API` where a publication called a post. Library maintainers decided to stick
into `Threads` terminology and use the word `thread`.

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

### Get Thread Identifier

To get a thread's identifier by a URL identifier. For instance, there is the URL — https://www.threads.net/t/CuXFPIeLLod.
The URL's identifier would be `CuXFPIeLLod`. Use the following commands:

```python3
>>> thread_id = threads.get_thread_id(url_id='CuXFPIeLLod')
>>> thread_id
3141002295235099165
```

### Get Thread

To get a thread, use the following commands:

```python3
>>> thread = threads.get_thread(id=3141002295235099165)
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

### Get Thread Likers

To get a thread's likers, use the following commands:

```python3
>>> thread_likers = threads.get_thread_likers(id=3141002295235099165)
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


### Create Thread

To create a thread, use the following commands:

```python3
>>> created_tread = threads.create_thread(caption='Hello, world!')
>>> created_tread
{
    "media": {
        "taken_at": 1688927865,
        "pk": 3143277215847793526,
        "id": "3143277215847793526_32545771157",
        "device_timestamp": 1688927864,
        "media_type": 19,
        "code": "CufKflZL8N2",
        "client_cache_key": "MzE0MzI3NzIxNTg0Nzc5MzUyNg==.2",
        "filter_type": 0,
        "can_viewer_reshare": true,
        "caption": {
            "pk": "18083774509335737",
            "user_id": 32545771157,
            "text": "Hello, world!",
            "type": 1,
            "created_at": 1688927865,
            "created_at_utc": 1688927865,
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
                "profile_pic_url": "https://instagram.fist10-1.fna.fbcdn.net/v/t51.2885-19/44884218_345707102882519_2446069589734326272_n.jpg?_nc_ht=instagram.fist10-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=s7XO4bcYceYAX8idgqz&edm=AEVnrqQBAAAA&ccb=7-5&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.2-ccb7-5&oh=00_AfDFQxQ9GzdvenWWifNYgwTAH9lfhqVzpYkTEyMVYmlfiA&oe=64AF5E0F&_nc_sid=f8b7b3",
                "account_badges": [],
                "feed_post_reshare_disabled": false,
                "show_account_transparency_details": true,
                "third_party_downloads_enabled": 0
            },
            "is_covered": false,
            "is_ranked_comment": false,
            "media_id": 3143277215847793526,
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
            "profile_pic_url": "https://instagram.fist10-1.fna.fbcdn.net/v/t51.2885-19/44884218_345707102882519_2446069589734326272_n.jpg?_nc_ht=instagram.fist10-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=s7XO4bcYceYAX8idgqz&edm=AEVnrqQBAAAA&ccb=7-5&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.2-ccb7-5&oh=00_AfDFQxQ9GzdvenWWifNYgwTAH9lfhqVzpYkTEyMVYmlfiA&oe=64AF5E0F&_nc_sid=f8b7b3",
            "account_badges": [],
            "feed_post_reshare_disabled": false,
            "show_account_transparency_details": true,
            "third_party_downloads_enabled": 0
        },
        "image_versions2": {
            "candidates": []
        },
        "original_width": 612,
        "original_height": 612,
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
        "product_type": "text_post",
        "is_paid_partnership": false,
        "music_metadata": null,
        "deleted_reason": 0,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjpmYWxzZSwidXVpZCI6ImYwZmExMGI0MTQwMzRhZDRhMjgzOWYyYzg0ZWFkYTg1MzE0MzI3NzIxNTg0Nzc5MzUyNiIsInNlcnZlcl90b2tlbiI6IjE2ODg5Mjc4NjczMDd8MzE0MzI3NzIxNTg0Nzc5MzUyNnwzMjU0NTc3MTE1N3wzNzExMTQyZjM2NjZmNjA4YThmMGQwODIyY2RjYmM4MDA5ODcyNDdlM2YzZDg1ZWMyYzhjMzM3MThiMjllMzZhIn0sInNpZ25hdHVyZSI6IiJ9",
        "text_post_app_info": {
            "is_post_unavailable": false,
            "is_reply": false,
            "reply_to_author": null,
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
    "upload_id": "1688927864",
    "status": "ok"
}
```