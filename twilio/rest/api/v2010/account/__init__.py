# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.api.v2010.account.address import AddressList
from twilio.rest.api.v2010.account.application import ApplicationList
from twilio.rest.api.v2010.account.authorized_connect_app import AuthorizedConnectAppList
from twilio.rest.api.v2010.account.available_phone_number import AvailablePhoneNumberCountryList
from twilio.rest.api.v2010.account.call import CallList
from twilio.rest.api.v2010.account.conference import ConferenceList
from twilio.rest.api.v2010.account.connect_app import ConnectAppList
from twilio.rest.api.v2010.account.incoming_phone_number import IncomingPhoneNumberList
from twilio.rest.api.v2010.account.message import MessageList
from twilio.rest.api.v2010.account.notification import NotificationList
from twilio.rest.api.v2010.account.outgoing_caller_id import OutgoingCallerIdList
from twilio.rest.api.v2010.account.queue import QueueList
from twilio.rest.api.v2010.account.recording import RecordingList
from twilio.rest.api.v2010.account.sandbox import SandboxContext
from twilio.rest.api.v2010.account.sip import SipContext
from twilio.rest.api.v2010.account.sms import SmsContext
from twilio.rest.api.v2010.account.token import TokenList
from twilio.rest.api.v2010.account.transcription import TranscriptionList
from twilio.rest.api.v2010.account.usage import UsageContext
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class AccountList(ListResource):

    def __init__(self, version):
        """
        Initialize the AccountList
        
        :param Version version: Version that contains the resource
        
        :returns: AccountList
        :rtype: AccountList
        """
        super(AccountList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {}
        self._uri = '/Accounts.json'.format(**self._kwargs)

    def create(self, friendly_name=values.unset):
        data = values.of({
            'FriendlyName': friendly_name,
        })
        
        return self._version.create(
            AccountInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def read(self, friendly_name=values.unset, status=values.unset, limit=None,
             page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'FriendlyName': friendly_name,
            'Status': status,
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            AccountInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, friendly_name=values.unset, status=values.unset, page_token=None,
             page_number=None, page_size=None, **kwargs):
        params = values.of({
            'FriendlyName': friendly_name,
            'Status': status,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            AccountInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, sid):
        """
        Constructs a AccountContext
        
        :param sid: Contextual sid
        
        :returns: AccountContext
        :rtype: AccountContext
        """
        return AccountContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AccountList>'


class AccountContext(InstanceContext):

    def __init__(self, version, sid):
        super(AccountContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'sid': sid,
        }
        self._uri = '/Accounts/{sid}.json'.format(**self._kwargs)
        
        # Dependents
        self._addresses = None
        self._applications = None
        self._authorized_connect_apps = None
        self._available_phone_numbers = None
        self._calls = None
        self._conferences = None
        self._connect_apps = None
        self._incoming_phone_numbers = None
        self._messages = None
        self._notifications = None
        self._outgoing_caller_ids = None
        self._queues = None
        self._recordings = None
        self._sandbox = None
        self._sip = None
        self._sms = None
        self._tokens = None
        self._transcriptions = None
        self._usage = None

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            AccountInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, friendly_name=values.unset, status=values.unset):
        data = values.of({
            'FriendlyName': friendly_name,
            'Status': status,
        })
        
        return self._version.update(
            AccountInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    @property
    def addresses(self):
        if self._addresses is None:
            self._addresses = AddressList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._addresses

    @property
    def applications(self):
        if self._applications is None:
            self._applications = ApplicationList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._applications

    @property
    def authorized_connect_apps(self):
        if self._authorized_connect_apps is None:
            self._authorized_connect_apps = AuthorizedConnectAppList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._authorized_connect_apps

    @property
    def available_phone_numbers(self):
        if self._available_phone_numbers is None:
            self._available_phone_numbers = AvailablePhoneNumberCountryList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._available_phone_numbers

    @property
    def calls(self):
        if self._calls is None:
            self._calls = CallList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._calls

    @property
    def conferences(self):
        if self._conferences is None:
            self._conferences = ConferenceList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._conferences

    @property
    def connect_apps(self):
        if self._connect_apps is None:
            self._connect_apps = ConnectAppList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._connect_apps

    @property
    def incoming_phone_numbers(self):
        if self._incoming_phone_numbers is None:
            self._incoming_phone_numbers = IncomingPhoneNumberList(
                self._version,
                owner_account_sid=self._kwargs['sid'],
            )
        return self._incoming_phone_numbers

    @property
    def messages(self):
        if self._messages is None:
            self._messages = MessageList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._messages

    @property
    def notifications(self):
        if self._notifications is None:
            self._notifications = NotificationList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._notifications

    @property
    def outgoing_caller_ids(self):
        if self._outgoing_caller_ids is None:
            self._outgoing_caller_ids = OutgoingCallerIdList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._outgoing_caller_ids

    @property
    def queues(self):
        if self._queues is None:
            self._queues = QueueList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._queues

    @property
    def recordings(self):
        if self._recordings is None:
            self._recordings = RecordingList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._recordings

    @property
    def sandbox(self):
        if self._sandbox is None:
            self._sandbox = SandboxContext(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._sandbox

    @property
    def sip(self):
        if self._sip is None:
            self._sip = SipContext(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._sip

    @property
    def sms(self):
        if self._sms is None:
            self._sms = SmsContext(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._sms

    @property
    def tokens(self):
        if self._tokens is None:
            self._tokens = TokenList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._tokens

    @property
    def transcriptions(self):
        if self._transcriptions is None:
            self._transcriptions = TranscriptionList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._transcriptions

    @property
    def usage(self):
        if self._usage is None:
            self._usage = UsageContext(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._usage


class AccountInstance(InstanceResource):

    def __init__(self, version, payload, sid=None):
        super(AccountInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'auth_token': payload['auth_token'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'friendly_name': payload['friendly_name'],
            'owner_account_sid': payload['owner_account_sid'],
            'sid': payload['sid'],
            'status': payload['status'],
            'subresource_uris': payload['subresource_uris'],
            'type': payload['type'],
            'uri': payload['uri'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = AccountContext(
                self._version,
                self._context_properties['sid'],
            )
        return self._lazy_context

    @property
    def auth_token(self):
        """ The auth_token """
        return self._properties['auth_token']

    @property
    def date_created(self):
        """ The date_created """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """ The date_updated """
        return self._properties['date_updated']

    @property
    def friendly_name(self):
        """ The friendly_name """
        return self._properties['friendly_name']

    @property
    def owner_account_sid(self):
        """ The owner_account_sid """
        return self._properties['owner_account_sid']

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def status(self):
        """ The status """
        return self._properties['status']

    @property
    def subresource_uris(self):
        """ The subresource_uris """
        return self._properties['subresource_uris']

    @property
    def type(self):
        """ The type """
        return self._properties['type']

    @property
    def uri(self):
        """ The uri """
        return self._properties['uri']

    def fetch(self):
        self._context.fetch()

    def update(self, friendly_name=values.unset, status=values.unset):
        self._context.update(
            friendly_name=friendly_name,
            status=status,
        )

    @property
    def addresses(self):
        return self._context.addresses

    @property
    def applications(self):
        return self._context.applications

    @property
    def authorized_connect_apps(self):
        return self._context.authorized_connect_apps

    @property
    def available_phone_numbers(self):
        return self._context.available_phone_numbers

    @property
    def calls(self):
        return self._context.calls

    @property
    def conferences(self):
        return self._context.conferences

    @property
    def connect_apps(self):
        return self._context.connect_apps

    @property
    def incoming_phone_numbers(self):
        return self._context.incoming_phone_numbers

    @property
    def messages(self):
        return self._context.messages

    @property
    def notifications(self):
        return self._context.notifications

    @property
    def outgoing_caller_ids(self):
        return self._context.outgoing_caller_ids

    @property
    def queues(self):
        return self._context.queues

    @property
    def recordings(self):
        return self._context.recordings

    @property
    def sandbox(self):
        return self._context.sandbox

    @property
    def sip(self):
        return self._context.sip

    @property
    def sms(self):
        return self._context.sms

    @property
    def tokens(self):
        return self._context.tokens

    @property
    def transcriptions(self):
        return self._context.transcriptions

    @property
    def usage(self):
        return self._context.usage