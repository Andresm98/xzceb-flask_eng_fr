import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
# apikey = os.environ['apikey']
# url = os.environ['url']
apikey ="WCxiki5FtesXDccTu25JYPMplpt3Y6GB-5l278sOYSJh"
url = "https://api.us-south.language-translator.watson.cloud.ibm.com/instances/506ccb47-2b3f-4d77-9e70-de1dbb57711e"
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)


def english_to_french(text1):
    # write the code here
    if text1 is None:
        return "Insert data"
    frenchtranslation = language_translator.translate(
        text=text1,
        model_id='en-fr'
    ).get_result()
    return frenchtranslation.get("translations")[0].get("translation")


def french_to_english(text2):
    # write the code here
    if text2 is None:
        return "Insert data"
    englishtranslation = language_translator.translate(
        text=text2,
        model_id='fr-en'
    ).get_result()
    return englishtranslation.get("translations")[0].get("translation")
