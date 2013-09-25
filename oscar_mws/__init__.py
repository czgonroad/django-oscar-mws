__version__ = (0, 1, 0, 'alpha', 1)


MWS_ENDPOINT_CA = 'https://mws.amazonservices.ca'
MWS_ENDPOINT_US = 'https://mws.amazonservices.com'
MWS_ENDPOINT_EU = 'https://mws-eu.amazonservices.com'
MWS_ENDPOINT_IN = 'https://mws.amazonservices.in'
MWS_ENDPOINT_JP = 'https://mws.amazonservices.jp'
MWS_ENDPOINT_CN = 'https://mws.amazonservices.com.cn'

MWS_MARKETPLACE_US = "US"
MWS_MARKETPLACE_CA = "CA"
MWS_MARKETPLACE_DE = "DE"
MWS_MARKETPLACE_ES = "ES"
MWS_MARKETPLACE_FR = "FR"
MWS_MARKETPLACE_IN = "IN"
MWS_MARKETPLACE_IT = "IT"
MWS_MARKETPLACE_UK = "UK"
MWS_MARKETPLACE_JP = "JP"
MWS_MARKETPLACE_CN = "CN"

MWS_MARKETPLACE_ENDPOINTS = {
    MWS_MARKETPLACE_US: MWS_ENDPOINT_US,
    MWS_MARKETPLACE_CA: MWS_ENDPOINT_CA,
    MWS_MARKETPLACE_DE: MWS_ENDPOINT_EU,
    MWS_MARKETPLACE_ES: MWS_ENDPOINT_EU,
    MWS_MARKETPLACE_FR: MWS_ENDPOINT_EU,
    MWS_MARKETPLACE_IN: MWS_ENDPOINT_IN,
    MWS_MARKETPLACE_IT: MWS_ENDPOINT_EU,
    MWS_MARKETPLACE_UK: MWS_ENDPOINT_EU,
    MWS_MARKETPLACE_JP: MWS_ENDPOINT_JP,
    MWS_MARKETPLACE_CN: MWS_ENDPOINT_CN,
}
