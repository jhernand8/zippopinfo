from django.core.management.base import BaseCommand, CommandError
from census import censusDataUtils
from census.models import InfoType
from census.models import CensusInfo

class Command(BaseCommand):

  def handle(self, *args, **options):
    zips = ['94010', '94131', '94404'];
    apiKey = os.environ['CENSUS_API_KEY']
    infoTypes = InfoType.objects.all()

    for zip in zips:
      data = censusDataUtils.fetchAndFormCensusInfoForZip(zip, 6, apiKey, infoTypes)

