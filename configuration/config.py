from configuration.credentials import basic_auth

medwing_web_config = {
    "qa": {
        "base_url": "https://mdwng.dev/",
        "logged_in_url": "https://my.mdwng.dev/",
        "jobs_url": "https://" + basic_auth["username"] + ":" + basic_auth[
            "password"] + "mdwng.dev/jobs/",
        "recruiting_url": "https://recruiting.mdwng.dev/",
        "registration_flow_a_url": 'https://mdwng.dev/de/de/a/job-finder/job_kind',
        "registration_flow_b_url": 'https://mdwng.dev/de/de/b/job-finder/job_kind'
    },
    "prod": {
        "base_url": "https://medwing.com",
        "logged_in_url": "https://my.medwing.com/",
        "jobs_url": "https://medwing.com/jobs/",
        "recruiting_url": "https://recruiting.medwing.com/",
        "registration_flow_a_url": 'https://medwing.com/de/de/a/job-finder/job_kind',
        "registration_flow_b_url": 'https://medwing.com/de/de/b/job-finder/job_kind'
    }
}
