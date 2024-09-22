import os
from bo import PetstoreOperation
from bs import PetstoreService

CLASSES = {
    'dc.demo.bs.PetstoreService': PetstoreService,
    'dc.demo.bo.PetstoreOperation': PetstoreOperation,
}

PRODUCTIONS = [
    {
        'dc.demo.Production': {
            "@Name": "dc.demo.Production",
            "@TestingEnabled": "true",
            "@LogGeneralTraceEvents": "false",
            "Description": "",
            "ActorPoolSize": "2",
            "Item": [
                {
                    "@Name": "PetstoreOperation",
                    "@Category": "",
                    "@ClassName": "dc.demo.bo.PetstoreOperation",
                    "@PoolSize": os.getenv('POOL_SIZE', '1'),
                    "@Enabled": "true",
                    "@Foreground": "false",
                    "@Comment": "",
                    "@LogTraceEvents": "true",
                    "@Schedule": "",
                    "Setting": [
                        {
                            "@Target": "Adapter",
                            "@Name": "HTTPServer",
                            "#text": "petstore3.swagger.io",
                        },
                        {
                            "@Target": "Adapter",
                            "@Name": "HTTPPort",
                            "#text": "443",
                        },
                        {
                            "@Target": "Adapter",
                            "@Name": "URL",
                            "#text": "/api/v3/",
                        },
                        {
                            "@Target": "Adapter",
                            "@Name": "SSLConfig",
                            "#text": "ISC.FeatureTracker.SSL.Config",
                        },
                    ]
                },
                {
                    "@Name": "PetstoreService",
                    "@Category": "",
                    "@ClassName": "dc.demo.bs.PetstoreService",
                    "@PoolSize": os.getenv('POOL_SIZE', '1'),
                    "@Enabled": "true",
                    "@Foreground": "false",
                    "@Comment": "",
                    "@LogTraceEvents": "true",
                    "@Schedule": "",
                    "Setting": [
                        {
                            "@Target": "Adapter",
                            "@Name": "CallInterval",
                            "#text": "300",
                        },
                    ]
                },
            ]
        }
    }
]
