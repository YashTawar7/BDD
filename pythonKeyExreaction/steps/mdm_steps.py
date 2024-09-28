# steps/mdm_steps.py
import requests
from behave import given, when, then

xml_request = """<?xml version="1.0" encoding="UTF-8"?><TCRMService xmlns="http://www.ibm.com/mdm/schema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.ibm.com/mdm/schema MDMDomains.xsd">
    <RequestControl>
        <requestID>0629</requestID>
        <DWLControl>
            <requesterName>Yash</requesterName>
            <requesterLanguage>100</requesterLanguage>
        </DWLControl>
    </RequestControl>
    <TCRMTx>
        <TCRMTxType>addParty</TCRMTxType>
        <TCRMTxObject>TCRMPersonBObj</TCRMTxObject>
        <TCRMObject>
            <TCRMPersonBObj>
                <PartyType>P</PartyType>
                <ClientStatusType>1</ClientStatusType>
                <TCRMPartyAddressBObj>
                    <AddressUsageType>1</AddressUsageType>
                    <TCRMAddressBObj>
                        <AddressLineOne>123 BDD</AddressLineOne>
                        <City>Philippines</City>
                        <ZipPostalCode>2161</ZipPostalCode>
                        <ProvinceStateType>45</ProvinceStateType>
                        <CountryType>183</CountryType>
                    </TCRMAddressBObj>
                </TCRMPartyAddressBObj>
                <TCRMPartyContactMethodBObj>
                    <ContactMethodUsageType>1</ContactMethodUsageType>
                    <TCRMContactMethodBObj>
                        <ReferenceNumber>989878787</ReferenceNumber>
                        <ContactMethodType>1</ContactMethodType>
                    </TCRMContactMethodBObj>
                </TCRMPartyContactMethodBObj>
                <TCRMPartyContactMethodBObj>
                    <ContactMethodUsageType>5</ContactMethodUsageType>
                    <TCRMContactMethodBObj>
                        <ReferenceNumber>bdd@gmail.com</ReferenceNumber>
                        <ContactMethodType>1</ContactMethodType>
                    </TCRMContactMethodBObj>
                </TCRMPartyContactMethodBObj>
                <TCRMPartyIdentificationBObj>
                    <IdentificationType>1</IdentificationType>
                    <IdentificationNumber>90909</IdentificationNumber>
                </TCRMPartyIdentificationBObj>
                 <TCRMAdminContEquivBObj>
                  <AdminPartyId>Y700</AdminPartyId>
                  <AdminSystemType>4</AdminSystemType>
               </TCRMAdminContEquivBObj>
                <TCRMPersonNameBObj>
                    <NameUsageType>1</NameUsageType>
                    <GivenNameOne>BDD</GivenNameOne>
                    <GivenNameTwo>P</GivenNameTwo>
                    <LastName>Lang</LastName>
                </TCRMPersonNameBObj>
            </TCRMPersonBObj>
        </TCRMObject>
    </TCRMTx>
</TCRMService>"""


@given('I have an XML request')
def step_impl(context):
    context.xml_request = xml_request


@when('I send the XML request to MDM')
def step_impl(context):
    context.response = requests.post('http://10.100.15.32:9081', data=context.xml_request,
                                     headers={'Content-Type': 'application/xml'})


@then('I should receive a valid response')
def step_impl(context):
    assert context.response.status_code == 200
    # Add more validation as needed

