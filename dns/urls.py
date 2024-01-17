from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.loadDNSHome, name='dnsHome'),
    url(r'^createNameserver', views.createNameserver, name='createNameserver'),
    url(r'^V2/createNameserverV2', views.createNameserverV2, name='createNameserverV2'),
    url(r'^configureDefaultNameServers$', views.configureDefaultNameServers, name='configureDefaultNameServers'),
    url(r'^V2/configureDefaultNameServersV2$', views.configureDefaultNameServersV2,
        name='configureDefaultNameServersV2'),
    url(r'^createDNSZone', views.createDNSZone, name='createDNSZone'),
    url(r'^V2/createDNSZoneV2', views.createDNSZoneV2, name='createDNSZoneV2'),
    url(r'^addDeleteDNSRecords$', views.addDeleteDNSRecords, name='addDeleteDNSRecords'),
    url(r'^V2/addDeleteDNSRecordsV2$', views.addDeleteDNSRecordsV2, name='addDeleteDNSRecordsV2'),
    url(r'^addDeleteDNSRecordsCloudFlare$', views.addDeleteDNSRecordsCloudFlare, name='addDeleteDNSRecordsCloudFlare'),
    url(r'^V2/addDeleteDNSRecordsCloudFlareV2$', views.addDeleteDNSRecordsCloudFlareV2,
        name='addDeleteDNSRecordsCloudFlareV2'),

    # JS Functions
    url(r'^NSCreation', views.NSCreation, name="NSCreation"),
    url(r'^zoneCreation', views.zoneCreation, name='zoneCreation'),
    url(r'^getCurrentRecordsForDomain$', views.getCurrentRecordsForDomain, name='getCurrentRecordsForDomain'),
    url(r'^addDNSRecord$', views.addDNSRecord, name='addDNSRecord'),
    url(r'^deleteDNSRecord$', views.deleteDNSRecord, name='deleteDNSRecord'),
    url(r'^deleteDNSZone', views.deleteDNSZone, name='deleteDNSZone'),
    url(r'^V2/deleteDNSZoneV2', views.deleteDNSZoneV2, name='deleteDNSZoneV2'),
    url(r'^submitZoneDeletion', views.submitZoneDeletion, name='submitZoneDeletion'),
    url(r'^saveNSConfigurations$', views.saveNSConfigurations, name='saveNSConfigurations'),
    url(r'^saveCFConfigs$', views.saveCFConfigs, name='saveCFConfigs'),
    url(r'^updateRecord$', views.updateRecord, name='updateRecord'),

    url(r'^getCurrentRecordsForDomainCloudFlare$', views.getCurrentRecordsForDomainCloudFlare,
        name='getCurrentRecordsForDomainCloudFlare'),
    url(r'^deleteDNSRecordCloudFlare$', views.deleteDNSRecordCloudFlare, name='deleteDNSRecordCloudFlare'),
    url(r'^addDNSRecordCloudFlare$', views.addDNSRecordCloudFlare, name='addDNSRecordCloudFlare'),
    url(r'^syncCF$', views.syncCF, name='syncCF'),
    url(r'^enableProxy$', views.enableProxy, name='enableProxy')
]
