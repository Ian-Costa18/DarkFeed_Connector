# DarkFeed_Connector

Connector for the DarkFeed RansoMonitor.

## Installation

To use the script, packages in requirements.txt must be installed.

(Optional) Create a virtual environment and activate it:

Windows:
```
python -m venv .venv
.venv/Scripts/activate
```

Linux:
```
python3 -m venv .venv
.venv/bin/activate
```

Install requirements:
```
pip -r requirements.txt
```

The script can be run standalone to retrieve the latest ransomware posts, or imported using a Python script.

To run standalone:

Windows:
```
python darkfeed_connector.py
```

Linux:
```
python3 darkfeed_connector.py
```

To import into a script:
```
from darkfeed_connector import get_feed

data = get_feed(cookie, feed_url)

for post in data:
    date = datetime.strptime(entry["date"], "%Y-%m-%dT%H:%M:%S")
    link = entry["link"]
    group = entry['title']['rendered']
    victim = entry["excerpt"]["rendered"].replace("<p>", "").replace("</p>", "").strip()

print(f'Group: {group}\n' +
      f'Victim: {victim}\n' +
      f'Date: {str(date)}\n' +
      f'Link: {link}\n'
     )
```

The data provided from the API is formatted like so (JSON):
```
{
    "id": INT,
    "date": STRING, (DateTime formatted "%Y-%m-%dT%H:%M:%S")
    "date_gmt": STRING,
    "guid": {
        "rendered": STRING
    },
    "modified": STRING,
    "modified_gmt": STRING,
    "slug": STRING,
    "status": STRING,
    "type": STRING,
    "link": STRING (Post link),
    "title": {
        "rendered": STRING (Ransomware group name)
    },
    "content": {
        "rendered": STRING,
        "protected": BOOL
    },
    "excerpt": {
        "rendered": STRING, (Victim name, formatted "<p>VICTIM</p>\n")
        "protected": BOOL
    },
    "author": INT,
    "featured_media": INT,
    "comment_status": STRING,
    "ping_status": STRING,
    "sticky": BOOL,
    "template": STRING,
    "format": STRING,
    "meta": {
        "_coblocks_attr": STRING,
        "_coblocks_dimensions": STRING,
        "_coblocks_responsive_height": STRING,
        "_coblocks_accordion_ie_support": STRING,
        "spay_email": STRING,
        "jetpack_anchor_podcast": STRING,
        "jetpack_anchor_episode": STRING,
        "jetpack_anchor_spotify_show": STRING,
        "jetpack_publicize_message": STRING,
        "jetpack_is_tweetstorm": BOOL,
        "jetpack_publicize_feature_enabled": BOOL
    },
    "categories": [
        INT
    ],
    "tags": [
        INT,
        INT,
        INT
    ],
    "yoast_head": STRING,
    "yoast_head_json": {
        "title": STRING,
        "description": STRING,
        "robots": {
            "index": STRING,
            "follow": STRING,
            "max-snippet": STRING,
            "max-image-preview": STRING,
            "max-video-preview": STRING
        },
        "canonical": STRING,
        "og_locale": STRING,
        "og_type": STRING,
        "og_title": STRING,
        "og_description": STRING,
        "og_url": STRING,
        "og_site_name": STRING,
        "article_published_time": STRING,
        "article_modified_time": STRING,
        "og_image": [
            {
                "width": INT,
                "height": INT,
                "url": STRING,
                "type": STRING
            }
        ],
        "twitter_card": STRING,
        "twitter_creator": STRING,
        "twitter_site": STRING,
        "twitter_misc": {
            "Written by": STRING,
            "Est. reading time": STRING
        },
        "schema": {
            "@context": STRING,
            "@graph": [
                {
                    "@type": STRING,
                    "@id": STRING,
                    "url": STRING,
                    "name": STRING,
                    "description": STRING,
                    "potentialAction": [
                        {
                            "@type": STRING,
                            "target": {
                                "@type": STRING,
                                "urlTemplate": STRING
                            },
                            "query-input": STRING
                        }
                    ],
                    "inLanguage": STRING
                },
                {
                    "@type": STRING,
                    "@id": STRING,
                    "inLanguage": STRING,
                    "url": STRING,
                    "contentUrl": STRING,
                    "width": INT,
                    "height": INT
                },
                {
                    "@type": [
                        STRING,
                        STRING
                    ],
                    "@id": STRING,
                    "url": STRING,
                    "name": STRING,
                    "isPartOf": {
                        "@id": STRING
                    },
                    "primaryImageOfPage": {
                        "@id": STRING
                    },
                    "datePublished": STRING,
                    "dateModified": STRING,
                    "author": {
                        "@id": STRING
                    },
                    "description": STRING,
                    "breadcrumb": {
                        "@id": STRING
                    },
                    "inLanguage": STRING,
                    "potentialAction": [
                        {
                            "@type": STRING,
                            "target": [
                                STRING
                            ]
                        }
                    ]
                },
                {
                    "@type": STRING,
                    "@id": STRING,
                    "itemListElement": [
                        {
                            "@type": STRING,
                            "position": INT,
                            "name": STRING,
                            "item": STRING
                        },
                        {
                            "@type": STRING,
                            "position": INT,
                            "name": STRING
                        }
                    ]
                },
                {
                    "@type": STRING,
                    "@id": STRING,
                    "name": STRING,
                    "image": {
                        "@type": STRING,
                        "@id": STRING,
                        "inLanguage": STRING,
                        "url": STRING,
                        "contentUrl": STRING,
                        "caption": STRING
                    }
                }
            ]
        }
    },
    "jetpack_featured_media_url": STRING,
    "jetpack_publicize_connections": [],
    "jetpack_likes_enabled": BOOL,
    "jetpack_sharing_enabled": BOOL,
    "jetpack_shortlink": STRING,
    "amp_enabled": BOOL,
    "_links": {
        "self": [
            {
                "href": STRING
            }
        ],
        "collection": [
            {
                "href": STRING
            }
        ],
        "about": [
            {
                "href": STRING
            }
        ],
        "author": [
            {
                "embeddable": BOOL,
                "href": STRING
            }
        ],
        "replies": [
            {
                "embeddable": BOOL,
                "href": STRING
            }
        ],
        "version-history": [
            {
                "count": INT,
                "href": STRING
            }
        ],
        "predecessor-version": [
            {
                "id": INT,
                "href": STRING
            }
        ],
        "wp:featuredmedia": [
            {
                "embeddable": BOOL,
                "href": STRING
            }
        ],
        "wp:attachment": [
            {
                "href": STRING
            }
        ],
        "wp:term": [
            {
                "taxonomy": STRING,
                "embeddable": BOOL,
                "href": STRING
            },
            {
                "taxonomy": STRING,
                "embeddable": BOOL,
                "href": STRING
            }
        ],
        "curies": [
            {
                "name": STRING,
                "href": STRING,
                "templated": BOOL
            }
        ]
    }
}
```

## Credits

Originally made by DarkFeed (@ido_cohen2), refactored by Ian Costa (@Ian_Costa18)
