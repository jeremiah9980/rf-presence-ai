
rf-presence-ai/
├── README.md
├── LICENSE
├── .env.example
├── docker-compose.yml
├── requirements.txt
│
├── ops/
│   ├── prometheus/
│   │   ├── prometheus.yml
│   │   └── alerts.yml
│   │
│   ├── alertmanager/
│   │   └── alertmanager.yml
│   │
│   └── grafana/
│       ├── datasources.yml
│       └── dashboards/
│           └── grafana_rf_presence_v2.json
│
├── services/
│   ├── correlator/
│   │   ├── correlator.py
│   │   ├── event_matcher.py
│   │   ├── presence_db.py
│   │   ├── ring_client.py
│   │   ├── metrics.py
│   │   ├── alerts_webhook.py
│   │   └── __init__.py
│   │
│   ├── notifier/
│   │   ├── push.py
│   │   ├── sms.py
│   │   └── templates/
│   │
│   └── api/
│       ├── main.py
│       └── routes.py
│
├── ai/
│   ├── clustering.py
│   ├── confidence_boost.py
│   ├── confidence_boost_uwb.py
│   ├── yolo_person.py
│   ├── lpr.py
│   └── models/
│
├── pi-sensor/
│   ├── config.yaml
│   ├── uploader.py
│   ├── wifi_sniffer.py
│   ├── bt_sniffer.py
│   ├── ble_fingerprint.py
│   └── requirements.txt
│
├── esp32-beacon/
│   └── esp32_beacon.ino
│
├── uwb/
│   ├── uwb_interface.py
│   ├── uwb_mqtt.py
│   └── README.md
│
├── home-assistant/
│   ├── config.yaml
│   ├── manifest.json
│   ├── sensor.py
│   ├── services.yaml
│   └── README.md
│
├── mobile-ui/
│   ├── App.js
│   ├── api.md
│   ├── wireframes.md
│   └── README.md
│
├── docker/
│   ├── Dockerfile.correlator
│   ├── Dockerfile.sensor
│   └── Dockerfile.yolo
│
├── proxmox/
│   ├── cloud-init/
│   │   └── user-data.yml
│   └── packer/
│       └── README.md
│
└── docs/
    ├── architecture.md
    ├── rf-detection.md
    ├── ring-integration.md
    ├── triangulation-math.md
    ├── threat-model.md
    ├── compliance.md
    └── roadmap.md
