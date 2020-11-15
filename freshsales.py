from client import ApiClient, require_keys


class FSBaseClient(ApiClient):
    def __init__(self, base_url, api_key, timeout):
        super(FSBaseClient, self).__init__(base_url=base_url, timeout=timeout)
        self.config = {
            'base_url': base_url,
            'api_key': api_key
        }

    @property
    def headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f"Token token={self.config.get('api_key')}"
        }


class LeadComponent(FSBaseClient):
    def __init__(self, base_url, api_key, timeout):
        super(LeadComponent, self).__init__(
            base_url=f"{base_url}/leads",
            api_key=api_key,
            timeout=timeout
        )

    def get(self, **kwargs):
        # https://developer.freshsales.io/api/#view_a_lead
        # opcional include
        require_keys(kwargs, 'id')
        id_ = kwargs.get('id')
        return self.get_request(f"/{id_}", params=kwargs, headers=self.headers)

    def create(self, **kwargs):
        # https://developer.freshsales.io/api/#create_lead
        require_keys(kwargs, [
            'first_name',
            'last_name',
            'mobile_number',
            'email',
        ])
        return self.post_request("", data={'lead': kwargs}, headers=self.headers)

    def update(self, **kwargs):
        # https://developer.freshsales.io/api/#update_lead
        require_keys(kwargs, 'id')
        id_ = kwargs.get('id')
        return self.put_request(f"/{id_}", data={'lead': kwargs}, headers=self.headers)


class ContactComponent(FSBaseClient):
    def __init__(self, base_url, api_key, timeout):
        super(ContactComponent, self).__init__(
            base_url=f"{base_url}/contacts",
            api_key=api_key,
            timeout=timeout
        )

    def get(self, **kwargs):
        # https://developer.freshsales.io/api/#view_a_contact
        # opcional include
        require_keys(kwargs, 'id')
        id_ = kwargs.get('id')
        return self.get_request(f"/{id_}", params=kwargs, headers=self.headers)


class FreshsaleClient(FSBaseClient):
    def __init__(self, domain, api_key):
        base_url = f"https://{domain}.freshsales.io/api"
        timeout = 15
        super(FreshsaleClient, self).__init__(base_url=base_url, api_key=api_key, timeout=timeout)
        self.leads = LeadComponent(base_url=base_url, api_key=api_key, timeout=timeout)
        self.contacts = ContactComponent(base_url=base_url, api_key=api_key, timeout=timeout)

    def search(self, query, include=None, page_size=25):
        payload = {
            'q': query,
            'include': include,
            'per_page': page_size,
            'perPage': page_size,
        }
        return self.get_request(endpoint='search', headers=self.headers, params=payload)
