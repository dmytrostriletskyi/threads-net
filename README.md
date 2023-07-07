Threads (threads.net) Python API wrapper

[![PyPI license](https://img.shields.io/pypi/l/threads-net.svg)](https://pypi.python.org/pypi/threads-net/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/threads-net.svg)](https://pypi.python.org/pypi/threads-net/)

Table of content:

* [Getting started](#getting-started)
  * [How to install](#how-to-install)
  * [Initialization](#initialization)
  * [Examples](#examples)
* [API](#api)
  * [Get User](#get-user)
  * [Get User Threads](#get-user-threads)
  * [Get User Replies](#get-user-replies)
  * [Get Post](#get-post)

## Getting started

### How to install

Install the project with the following command using `pip3`:

```bash
$ pip3 install threads-net
```

### Initialization

Import the class responsible for `Threads API` communication and start using it with the following commands:

```python3
>>> from threads import Threads
>>> threads = Threads()
```

Under the hood, in the constructor (`__init__`), it makes a request to the `Threads API` to fetch a token. It is called 
`lsd` internally and is required for any request. For anonymous users, it is just generated automatically from 
API's back-end and passed to front-end. So, basically, you do not need any `API key` or other credentials to use the library.

### Examples

Find examples of how to use the library functionality in the `examples` folder:

```bash
➜  ls examples
examples
├── __init__.py
├── get_post.py
├── get_user.py
├── get_user_replies.py
└── get_user_threads.py
...
```

## API

### Get User

To get a user, use the following commands:

```python3
>>> user = threads.get_user(id=314216)
>>> user
{
    "data": {
        "userData": {
            "user": {
                "is_private": false,
                "profile_pic_url": "https://scontent.cdninstagram.com/v/t51.2885-19/357376107_1330597350674698_8884059223384672080_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=9PG1NK-L8OkAX-7KBKu&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfANyGvPklT1Hkax6hmmmzvD7QX2vwqYe4XAzZIYo1fGqA&oe=64ACDDC0&_nc_sid=10d13b",
                "username": "zuck",
                "hd_profile_pic_versions": [
                    {
                        "height": 320,
                        "url": "https://scontent.cdninstagram.com/v/t51.2885-19/357376107_1330597350674698_8884059223384672080_n.jpg?stp=dst-jpg_s320x320&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=9PG1NK-L8OkAX-7KBKu&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfCjdM98k9QZZVAr3czL_EjLYje6g__zJ8b_q3ZQi8Uqpw&oe=64ACDDC0&_nc_sid=10d13b",
                        "width": 320
                    },
                    {
                        "height": 640,
                        "url": "https://scontent.cdninstagram.com/v/t51.2885-19/357376107_1330597350674698_8884059223384672080_n.jpg?stp=dst-jpg_s640x640&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=9PG1NK-L8OkAX-7KBKu&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfDA1pVfIGaKNihFuUc80xxx8SnNgnqlpvxSCSq9N_n-mQ&oe=64ACDDC0&_nc_sid=10d13b",
                        "width": 640
                    }
                ],
                "is_verified": true,
                "biography": "",
                "biography_with_entities": null,
                "follower_count": 1988496,
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
    "data": {
        "mediaData": {
            "threads": [
                {
                    "thread_items": [
                        {
                            "post": {
                                "user": {
                                    "profile_pic_url": "https://scontent.cdninstagram.com/v/t51.2885-19/357376107_1330597350674698_8884059223384672080_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=9PG1NK-L8OkAX-q_Nrf&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfDWsSPBghiIhwJnh4_3kO5maVMhDErg9ky_-dhqUHVtRw&oe=64ACDDC0&_nc_sid=10d13b",
                                    "username": "zuck",
                                    "id": null,
                                    "is_verified": true,
                                    "pk": "314216"
                                },
                                "image_versions2": {
                                    "candidates": [
                                        {
                                            "height": 3000,
                                            "url": "https://scontent.cdninstagram.com/v/t51.2885-15/357916630_786901039847062_4398530087245184228_n.jpg?stp=dst-jpg_e35&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=vSLyED13mHsAX-BfOPb&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTAwMjI5NTIzNTA5OTE2NQ%3D%3D.2-ccb7-5&oh=00_AfBVkBmYMO2TozQJYlE6xblN10YDdmKXhzzs0hSHHCfUgQ&oe=64ACBB47&_nc_sid=10d13b",
                                            "width": 4000,
                                            "__typename": "XDTImageCandidate"
                                        },
                                        {
                                            "height": 810,
                                            "url": "https://scontent.cdninstagram.com/v/t51.2885-15/357916630_786901039847062_4398530087245184228_n.jpg?stp=dst-jpg_e35_s1080x1080&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=vSLyED13mHsAX-BfOPb&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTAwMjI5NTIzNTA5OTE2NQ%3D%3D.2-ccb7-5&oh=00_AfCl-OTiAWiST-z8pGT0IHQAcdQiuWxdoI44UQccZrvkdw&oe=64ACBB47&_nc_sid=10d13b",
                                            "width": 1080,
                                            "__typename": "XDTImageCandidate"
                                        },
                                        {
                                            "height": 540,
                                            "url": "https://scontent.cdninstagram.com/v/t51.2885-15/357916630_786901039847062_4398530087245184228_n.jpg?stp=dst-jpg_e35_s720x720&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=vSLyED13mHsAX-BfOPb&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTAwMjI5NTIzNTA5OTE2NQ%3D%3D.2-ccb7-5&oh=00_AfCQ6PZm83pOL4_QMalEvrzu1TTLWqvHWMVK3WercfrQdA&oe=64ACBB47&_nc_sid=10d13b",
                                            "width": 720,
                                            "__typename": "XDTImageCandidate"
                                        },
                                        {
                                            "height": 480,
                                            "url": "https://scontent.cdninstagram.com/v/t51.2885-15/357916630_786901039847062_4398530087245184228_n.jpg?stp=dst-jpg_e35_s640x640_sh0.08&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=vSLyED13mHsAX-BfOPb&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTAwMjI5NTIzNTA5OTE2NQ%3D%3D.2-ccb7-5&oh=00_AfB6A9bQNJLWiNgczI7Kp7q7wII7TC1ifn4oVd5cN8nTBg&oe=64ACBB47&_nc_sid=10d13b",
                                            "width": 640,
                                            "__typename": "XDTImageCandidate"
                                        },
                                        {
                                            "height": 360,
                                            "url": "https://scontent.cdninstagram.com/v/t51.2885-15/357916630_786901039847062_4398530087245184228_n.jpg?stp=dst-jpg_e35_s480x480&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=vSLyED13mHsAX-BfOPb&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTAwMjI5NTIzNTA5OTE2NQ%3D%3D.2-ccb7-5&oh=00_AfAtSvruwFWIjemafFJXaFfb_iag6LMjJL7EFaBmZmyP0Q&oe=64ACBB47&_nc_sid=10d13b",
                                            "width": 480,
                                            "__typename": "XDTImageCandidate"
                                        },
                                        {
                                            "height": 240,
                                            "url": "https://scontent.cdninstagram.com/v/t51.2885-15/357916630_786901039847062_4398530087245184228_n.jpg?stp=dst-jpg_e35_s320x320&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=vSLyED13mHsAX-BfOPb&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTAwMjI5NTIzNTA5OTE2NQ%3D%3D.2-ccb7-5&oh=00_AfCCyzKffNLdsvdSRuyHMdAN-F7sEALSVrc0kM3R2nsrQA&oe=64ACBB47&_nc_sid=10d13b",
                                            "width": 320,
                                            "__typename": "XDTImageCandidate"
                                        },
                                        {
                                            "height": 180,
                                            "url": "https://scontent.cdninstagram.com/v/t51.2885-15/357916630_786901039847062_4398530087245184228_n.jpg?stp=dst-jpg_e35_s240x240&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=vSLyED13mHsAX-BfOPb&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTAwMjI5NTIzNTA5OTE2NQ%3D%3D.2-ccb7-5&oh=00_AfCq8hu-NdtgzUrS_S4MnBrJX4ogGvCiAIhG_gr6xwp5Ag&oe=64ACBB47&_nc_sid=10d13b",
                                            "width": 240,
                                            "__typename": "XDTImageCandidate"
                                        },
                                        {
                                            "height": 1080,
                                            "url": "https://scontent.cdninstagram.com/v/t51.2885-15/357916630_786901039847062_4398530087245184228_n.jpg?stp=c500.0.3000.3000a_dst-jpg_e35_s1080x1080&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=vSLyED13mHsAX-BfOPb&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTAwMjI5NTIzNTA5OTE2NQ%3D%3D.2-ccb7-5&oh=00_AfDWf1VGojZDDWQDCDO1x0l3SU34cgdEOceFGPxK_9EZfA&oe=64ACBB47&_nc_sid=10d13b",
                                            "width": 1080,
                                            "__typename": "XDTImageCandidate"
                                        },
                                        {
                                            "height": 750,
                                            "url": "https://scontent.cdninstagram.com/v/t51.2885-15/357916630_786901039847062_4398530087245184228_n.jpg?stp=c500.0.3000.3000a_dst-jpg_e35_s750x750_sh0.08&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=vSLyED13mHsAX-BfOPb&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTAwMjI5NTIzNTA5OTE2NQ%3D%3D.2-ccb7-5&oh=00_AfA-Kqa9UoMluJGqD_wBNG3qtcbWT63RCkq07fDo88ZVaw&oe=64ACBB47&_nc_sid=10d13b",
                                            "width": 750,
                                            "__typename": "XDTImageCandidate"
                                        },
                                        {
                                            "height": 640,
                                            "url": "https://scontent.cdninstagram.com/v/t51.2885-15/357916630_786901039847062_4398530087245184228_n.jpg?stp=c500.0.3000.3000a_dst-jpg_e35_s640x640_sh0.08&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=vSLyED13mHsAX-BfOPb&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTAwMjI5NTIzNTA5OTE2NQ%3D%3D.2-ccb7-5&oh=00_AfCh7r-VI_5fLBmsPNp_cb-rZSBsDJTYdrn0PnMKBgATlw&oe=64ACBB47&_nc_sid=10d13b",
                                            "width": 640,
                                            "__typename": "XDTImageCandidate"
                                        },
                                        {
                                            "height": 480,
                                            "url": "https://scontent.cdninstagram.com/v/t51.2885-15/357916630_786901039847062_4398530087245184228_n.jpg?stp=c500.0.3000.3000a_dst-jpg_e35_s480x480&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=vSLyED13mHsAX-BfOPb&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTAwMjI5NTIzNTA5OTE2NQ%3D%3D.2-ccb7-5&oh=00_AfBXkMC4qSLcsgFURS0yXTu02CyydoJpInHfOr5L-FP5ww&oe=64ACBB47&_nc_sid=10d13b",
                                            "width": 480,
                                            "__typename": "XDTImageCandidate"
                                        },
                                        {
                                            "height": 320,
                                            "url": "https://scontent.cdninstagram.com/v/t51.2885-15/357916630_786901039847062_4398530087245184228_n.jpg?stp=c500.0.3000.3000a_dst-jpg_e35_s320x320&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=vSLyED13mHsAX-BfOPb&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTAwMjI5NTIzNTA5OTE2NQ%3D%3D.2-ccb7-5&oh=00_AfCwJtku5xDOM0dxwCvfAzmV64T-_kaA4CZLOIl3OTNiJQ&oe=64ACBB47&_nc_sid=10d13b",
                                            "width": 320,
                                            "__typename": "XDTImageCandidate"
                                        },
                                        {
                                            "height": 240,
                                            "url": "https://scontent.cdninstagram.com/v/t51.2885-15/357916630_786901039847062_4398530087245184228_n.jpg?stp=c500.0.3000.3000a_dst-jpg_e35_s240x240&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=vSLyED13mHsAX-BfOPb&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTAwMjI5NTIzNTA5OTE2NQ%3D%3D.2-ccb7-5&oh=00_AfCxaBgqYV7qj0svYLI1KavhteMygChYAfZma84Fe0tZmw&oe=64ACBB47&_nc_sid=10d13b",
                                            "width": 240,
                                            "__typename": "XDTImageCandidate"
                                        },
                                        {
                                            "height": 150,
                                            "url": "https://scontent.cdninstagram.com/v/t51.2885-15/357916630_786901039847062_4398530087245184228_n.jpg?stp=c500.0.3000.3000a_dst-jpg_e35_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=vSLyED13mHsAX-BfOPb&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE0MTAwMjI5NTIzNTA5OTE2NQ%3D%3D.2-ccb7-5&oh=00_AfDwSo36FyoIW052Qvgp7eDCfi-ij8x3NsySfbpfQAlM_Q&oe=64ACBB47&_nc_sid=10d13b",
                                            "width": 150,
                                            "__typename": "XDTImageCandidate"
                                        }
                                    ]
                                },
                                "original_width": 4000,
                                "original_height": 3000,
                                "video_versions": [],
                                "carousel_media": null,
                                "carousel_media_count": null,
                                "pk": "3141002295235099165",
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
                                    "text": "Lots of work on basic capabilities this morning."
                                },
                                "taken_at": 1688656673,
                                "like_count": 184611,
                                "code": "CuXFPIeLLod",
                                "media_overlay_info": null,
                                "id": "3141002295235099165_314216"
                            },
                            "line_type": "line",
                            "view_replies_cta_string": "17,882 replies",
                            "reply_facepile_users": [
                                {
                                    "__typename": "XDTUserDict",
                                    "id": null,
                                    "profile_pic_url": "https://scontent.cdninstagram.com/v/t51.2885-19/358166568_272137218742674_3025287304976949959_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=106&_nc_ohc=Wl0wRGxM7g4AX-cl1FE&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfAaJRzZHv09tlkXbrdFTQC-ZhwW7v2BPih4fIBN3HxdYg&oe=64AC6E7C&_nc_sid=10d13b"
                                },
                                {
                                    "__typename": "XDTUserDict",
                                    "id": null,
                                    "profile_pic_url": "https://scontent.cdninstagram.com/v/t51.2885-19/358337983_581973004113850_7681929282916239696_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=110&_nc_ohc=9xd6QhLrfr0AX_jXvvd&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfD01Al_ukeQOVXysDuudHw82ZUfn4q_PI1KuWE1Swf1Kw&oe=64AC446D&_nc_sid=10d13b"
                                },
                                {
                                    "__typename": "XDTUserDict",
                                    "id": null,
                                    "profile_pic_url": "https://scontent.cdninstagram.com/v/t51.2885-19/358357576_689254799697876_1184079927626851628_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=100&_nc_ohc=95IT8pfSV8MAX8qeB2M&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfBtniKWdsj56GWa3T_UQZG6xEhLv_2ck-q_V9J34Pb4ag&oe=64ADA8C7&_nc_sid=10d13b"
                                }
                            ],
                            "should_show_replies_cta": true,
                            "__typename": "XDTThreadItem"
                        }
                    ],
                    "id": "3141002295235099165"
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

### Get Post

To get a post, use the following commands:

```python3
>>> post = threads.get_post(id=3141055616164096839)
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

