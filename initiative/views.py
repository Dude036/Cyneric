from django.contrib import auth, admin, messages
from django.shortcuts import render
import requests
from .models import InitEntry

# Create your views here.
def index(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    context = {
        'is_admin': user.is_authenticated,
    }
    return render(request, 'initiative_tracker.html', context)


def elastic_search_add(query):
    data_obj = {
        "query": {
            "function_score": {
                "query": {
                    "bool": {
                        "should": [
                            {
                                "match_phrase_prefix": {
                                    "name.sayt": {
                                        "query": query
                                    }
                                }
                            },
                            {
                                "match_phrase_prefix": {
                                    "legacy_name.sayt": {
                                        "query": query
                                    }
                                }
                            },
                            {
                                "match_phrase_prefix": {
                                    "remaster_name.sayt": {
                                        "query": query
                                    }
                                }
                            },
                            {
                                "match_phrase_prefix": {
                                    "text.sayt": {
                                        "query": query,
                                        "boost": 0.1
                                    }
                                }
                            },
                            {
                                "term": {
                                    "name": query
                                }
                            },
                            {
                                "term": {
                                    "legacy_name": query
                                }
                            },
                            {
                                "term": {
                                    "remaster_name": query
                                }
                            },
                            {
                                "bool": {
                                    "must": [
                                        {
                                            "multi_match": {
                                                "query": "{{aon_search}}",
                                                "type": "best_fields",
                                                "fields": [
                                                    "name",
                                                    "legacy_name",
                                                    "remaster_name",
                                                    "text^0.1",
                                                    "trait_raw",
                                                    "type"
                                                ],
                                                "fuzziness": "auto"
                                            }
                                        }
                                    ]
                                }
                            }
                        ],
                        "minimum_should_match": 1,
                        "must_not": [
                            {
                                "term": {
                                    "exclude_from_search": True
                                }
                            },
                            {
                                "exists": {
                                    "field": "remaster_id"
                                }
                            },
                            {
                                "exists": {
                                    "field": "item_child_id"
                                }
                            }
                        ]
                    }
                },
                "boost_mode": "multiply",
                "functions": [
                    {
                        "filter": {
                            "terms": {
                                "type": [
                                    "Ancestry",
                                    "Class",
                                    "Versatile Heritage"
                                ]
                            }
                        },
                        "weight": 1.2
                    },
                    {
                        "filter": {
                            "terms": {
                                "type": [
                                    "Trait"
                                ]
                            }
                        },
                        "weight": 1.05
                    }
                ]
            }
        },
        "size": 1,
        "sort": [
            "_score",
            "_doc"
        ],
        "_source": {
            "excludes": [
                "text"
            ]
        }
    }

    response = requests.request("POST", "https://elasticsearch.aonprd.com/aon/_search", data=data_obj)
    if response.status_code == 200:
        meta_data = response.json()['data']
        if meta_data['_shards']['skipped'] == 1 or meta_data['hits']['failed'] == 1:
            return "No results found."
        if 'creature' in  meta_data['hits']['hits'][0]['_id']:
            return "Result returned is not a creature"
        creature_source = meta_data['hits']['hits'][0]['_source']

        skill_list = ', '.join([k + ' +' + str(v) for k, v in creature_source['skill_mod'].items()])

        return InitEntry(name=creature_source['name'],
                         aon_link='https://2e.aonprd.com/Monsters.aspx?ID=' + creature_source['_id'].replace('creature-', ''),
                         skills=skill_list,
                         ac=creature_source['ac'],
                         hp=creature_source['hp'],
                         will_save=creature_source['will_save'],
                         fortitude_save=creature_source['fortitude_save'],
                         reflex_save=creature_source['reflex_save'],
                         initiative=0,
                         perception=creature_source['perception'],
        )
