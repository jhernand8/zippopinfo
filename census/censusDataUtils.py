import urllib2
import json
from census.models import CensusInfo
from census.models import InfoType

# Returns a json object of the response for the given url.
def fetch_json(url):
  return json.load(urllib2.urlopen(url))

# Forms a url to get the census data for the given zip and state
# for all the given data keys.
def form_url_for_data(dataKeys, zipCode, state_code, apiKey):
  commaSepDataKeys = ""
  for dataKey in dataKeys:
    commaSepDataKeys += dataKey + ","
  # remove trailing comma
  commaSepDataKeys = commaSepDataKeys[:-1]
  return 
    "https://api.census.gov/data/2010/sf1?get=" + commaSepDataKeys +
    "&for=zip%20code%20tabulation%20area:" + zipCode +
    "&in=state:" + state_code + "&key=" + apiKey;

# For the given zip code and state, request the info in info types
# and form and return CensusInfo objects for them.
def fetchAndFormCensusInfoForZip(zipcode, statecode, apikey, infotypes):
  # form list of data type keys
  dataKeys = []
  for infoType in infotypes:
    dataKeys.append(infoType.census_key

  url = form_url_for_data(dataKeys, zipcode, statecode, apiKey)
  fulljson = fetch_json(url)
  # first is an array of index to the keys
  typetoindex = fulljson.get(0)
  # next is the actual data for the zip code
  datajson = fulljson.get(1)
  
  returnData = []
  # match up the data to the data types we requested
  for idx in typetoindex:
    datakey = typetoindex.get(idx)
    dataInfoType = None
    for infoType in infotypes:
      if infoType.census_key == datakey:
        dataInfoType = infoType
    if dataInfoType not None:
      info = CensusInfo(
          info_type_id = dataInfoType.info_type_id,
          info = datajson.get(idx),
          zipCode = zipcode,
          state_code = statecode)
      returnData.append(info)
  return returnData



