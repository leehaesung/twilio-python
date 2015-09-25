# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class ConnectAppList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the ConnectAppList
        
        :param Version version: Version that contains the resource
        :param account_sid: Contextual account_sid
        
        :returns: ConnectAppList
        :rtype: ConnectAppList
        """
        super(ConnectAppList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
        }
        self._uri = '/Accounts/{account_sid}/ConnectApps.json'.format(**self._kwargs)

    def read(self, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            ConnectAppInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, page_token=None, page_number=None, page_size=None, **kwargs):
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            ConnectAppInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, sid):
        """
        Constructs a ConnectAppContext
        
        :param sid: Contextual sid
        
        :returns: ConnectAppContext
        :rtype: ConnectAppContext
        """
        return ConnectAppContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.ConnectAppList>'


class ConnectAppContext(InstanceContext):

    def __init__(self, version, account_sid, sid):
        super(ConnectAppContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/ConnectApps/{sid}.json'.format(**self._kwargs)

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            ConnectAppInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, authorize_redirect_url=values.unset, company_name=values.unset,
               deauthorize_callback_method=values.unset,
               deauthorize_callback_url=values.unset, description=values.unset,
               friendly_name=values.unset, homepage_url=values.unset,
               permissions=values.unset):
        data = values.of({
            'AuthorizeRedirectUrl': authorize_redirect_url,
            'CompanyName': company_name,
            'DeauthorizeCallbackMethod': deauthorize_callback_method,
            'DeauthorizeCallbackUrl': deauthorize_callback_url,
            'Description': description,
            'FriendlyName': friendly_name,
            'HomepageUrl': homepage_url,
            'Permissions': permissions,
        })
        
        return self._version.update(
            ConnectAppInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )


class ConnectAppInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, sid=None):
        super(ConnectAppInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'authorize_redirect_url': payload['authorize_redirect_url'],
            'company_name': payload['company_name'],
            'deauthorize_callback_method': payload['deauthorize_callback_method'],
            'deauthorize_callback_url': payload['deauthorize_callback_url'],
            'description': payload['description'],
            'friendly_name': payload['friendly_name'],
            'homepage_url': payload['homepage_url'],
            'permissions': payload['permissions'],
            'sid': payload['sid'],
            'uri': payload['uri'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'account_sid': account_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = ConnectAppContext(
                self._version,
                self._context_properties['account_sid'],
                self._context_properties['sid'],
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def authorize_redirect_url(self):
        """ The authorize_redirect_url """
        return self._properties['authorize_redirect_url']

    @property
    def company_name(self):
        """ The company_name """
        return self._properties['company_name']

    @property
    def deauthorize_callback_method(self):
        """ The deauthorize_callback_method """
        return self._properties['deauthorize_callback_method']

    @property
    def deauthorize_callback_url(self):
        """ The deauthorize_callback_url """
        return self._properties['deauthorize_callback_url']

    @property
    def description(self):
        """ The description """
        return self._properties['description']

    @property
    def friendly_name(self):
        """ The friendly_name """
        return self._properties['friendly_name']

    @property
    def homepage_url(self):
        """ The homepage_url """
        return self._properties['homepage_url']

    @property
    def permissions(self):
        """ The permissions """
        return self._properties['permissions']

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def uri(self):
        """ The uri """
        return self._properties['uri']

    def fetch(self):
        self._context.fetch()

    def update(self, authorize_redirect_url=values.unset, company_name=values.unset,
               deauthorize_callback_method=values.unset,
               deauthorize_callback_url=values.unset, description=values.unset,
               friendly_name=values.unset, homepage_url=values.unset,
               permissions=values.unset):
        self._context.update(
            authorize_redirect_url=authorize_redirect_url,
            company_name=company_name,
            deauthorize_callback_method=deauthorize_callback_method,
            deauthorize_callback_url=deauthorize_callback_url,
            description=description,
            friendly_name=friendly_name,
            homepage_url=homepage_url,
            permissions=permissions,
        )