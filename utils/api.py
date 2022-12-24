import asyncio
import sys
import requests
import riot_auth

def contentuuidconvert(contentuuid):
    content_tiers = requests.get("https://valorant-api.com/v1/contenttiers")
    content_tiers_data = content_tiers.json()
    for row in content_tiers_data["data"]:
        if contentuuid in row["uuid"]:
            return row


async def login(username,password):
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    CREDS = username, password

    auth = riot_auth.RiotAuth()
    await auth.authorize(*CREDS)

    # print(f"Access Token Type: {auth.token_type}\n")
    # print(f"Access Token: {auth.access_token}\n")
    # print(f"Entitlements Token: {auth.entitlements_token}\n")
    # print(f"User ID: {auth.user_id}")

    # Reauth using cookies. Returns a bool indicating whether the reauth attempt was successful.
    #asyncio.run(auth.reauthorize())

    return [auth.access_token, auth.entitlements_token , auth.user_id]

async def check_item_shop(username,password):
    user_data = await login(username, password)
    # print(f"Access Token: {user_data[0]}\n")
    # print(f"Entitlements Token: {user_data[1]}\n")
    # print(f"User ID: {user_data[2]}")
    access_token = user_data[0]
    entitlements_token = user_data[1]
    user_id = user_data[2]
    skin_data =  skins(entitlements_token, access_token, user_id)
    skin_list = [skin_data["skin1_name"], skin_data["skin2_name"], skin_data["skin3_name"], skin_data["skin4_name"], skin_data["SingleItemOffersRemainingDurationInSeconds"]]
    return skin_data
        
def skins(entitlements_token, access_token, user_id):

    headers = {
        'X-Riot-Entitlements-JWT': entitlements_token,
        'Authorization': f'Bearer {access_token}',
    }

    r = requests.get(f'https://pd.AP.a.pvp.net/store/v2/storefront/{user_id}', headers=headers)

    skins_data = r.json()
    #print(skins_data)
    single_skins = skins_data["SkinsPanelLayout"]["SingleItemOffers"]

    bundle_fetch = requests.get(f'https://valorant-api.com/v1/bundles')
    bundle_fetch = bundle_fetch.json()
    weapon_fetch = requests.get(f'https://valorant-api.com/v1/weapons/skinlevels')
    weapon_fetch = weapon_fetch.json()

    # with open("content.txt", "w", encoding="utf-8") as file:
    #     file.write(str(content_data))
    #     file.close()
    # print(content_data)
    # with open("assets.txt", "w") as file:
    #     file.write(str(data))

    all_weapons = requests.get("https://valorant-api.com/v1/weapons")
    data_weapons = all_weapons.json()

    single_skins_images = []
    single_skins_tiers_uuids = []

    # ['12683d76-48d7-84a3-4e09-6985794f0445', 'e046854e-406c-37f4-6607-19a9ba8426fc', '60bca009-4182-7998-dee7-b8a2558dc369', 'e046854e-406c-37f4-6607-19a9ba8426fc']
    # print(contentuuidconvert("e046854e-406c-37f4-6607-19a9ba8426fc"))


    for skin in single_skins:
        for weapons_list in data_weapons['data']:
            for skin1 in weapons_list['skins']:
                if skin in str(skin1):
                    # print(skin1)
                    # if skin1['displayIcon'] != None:
                        # print("test")
                        # for chromas in skin1["chromas"]:
                        # print(skin1["chromas"])
                    if skin1["chromas"][0]["displayIcon"] != None:
                        single_skins_images.append(skin1["chromas"][0]["displayIcon"])
                    else:
                        single_skins_images.append(skin1["chromas"][0]["fullRender"])
                    single_skins_tiers_uuids.append(skin1['contentTierUuid'])
                    # else:
                    #     single_skins_images.append(skin1['displayIcon'])
                    #     single_skins_tiers_uuids.append(skin1['contentTierUuid'])

    # print(single_skins_images)
    headers = {
        'X-Riot-Entitlements-JWT': entitlements_token,
        'Authorization': f'Bearer {access_token}',
        'X-Riot-ClientVersion': getVersion(),
        "X-Riot-ClientPlatform": "ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9"
    }

    data = requests.get(f"https://pd.AP.a.pvp.net/store/v1/offers/", headers=headers)

    offers_data = data.json()

    for row in bundle_fetch["data"]:
        if skins_data["FeaturedBundle"]["Bundle"]["DataAssetID"] == row['uuid']:
            r_bundle_data = requests.get(f"https://valorant-api.com/v1/bundles/{row['uuid']}")
            bundle_data = r_bundle_data.json()
            # print(f"Your featured bundle is {row_small['Name']} - {bundle_data['data']['displayIcon']} - {skins_data['FeaturedBundle']['BundleRemainingDurationInSeconds']}.")
            bundle_name = row['displayName']
            try:
                bundle_image = bundle_data['data']['displayIcon']
            except KeyError:
                bundle_image = "https://notyetinvalorant-api.com"


    daily_reset = skins_data["SkinsPanelLayout"]["SingleItemOffersRemainingDurationInSeconds"]

    skin_counter = 0
    # print("Your daily item shop is: ")

    for skin in single_skins:
        for row in weapon_fetch["data"]:
            if skin == row["uuid"]:
                if skin_counter == 0:
                    skin1_name = row['displayName']
                    skin1_image = row['displayIcon']
                    skin1_price = priceconvert(skin, offers_data)
                elif skin_counter == 1:
                    skin2_name = row['displayName']
                    skin2_image = row['displayIcon']
                    skin2_price = priceconvert(skin, offers_data)
                elif skin_counter == 2:
                    skin3_name = row['displayName']
                    skin3_image = row['displayIcon']
                    skin3_price = priceconvert(skin, offers_data)
                elif skin_counter == 3:
                    skin4_name = row['displayName']
                    skin4_image = row['displayIcon']
                    skin4_price = priceconvert(skin, offers_data)
                skin_counter += 1

    if daily_reset >= 3600:
        daily_reset_in_hr = round(daily_reset / 3600, 0)
        # print(f"Daily shop items resets in {int(daily_reset_in_hr)} hours.")
    else:
        daily_reset_in_minutes = round(daily_reset / 60, 2)
        # print(f"Daily shop items resets in {daily_reset_in_minutes} minutes.")
    skins_list = {
        "bundle_name": bundle_name,
        "bundle_image": bundle_image,
        "skin1_name": skin1_name,
        "skin1_image":skin1_image,
        "skin1_price":skin1_price,
        "skin2_name": skin2_name,
        "skin2_image": skin2_image,
        "skin2_price": skin2_price,
        "skin3_name": skin3_name,
        "skin3_image": skin3_image,
        "skin3_price": skin3_price,
        "skin4_name": skin4_name,
        "skin4_image": skin4_image,
        "skin4_price": skin4_price,
        "SingleItemOffersRemainingDurationInSeconds": daily_reset,
    }

    #print(skins_list)

    return skins_list

def priceconvert(skinUuid, offers_data):
    for row in offers_data["Offers"]:
        if row["OfferID"] == skinUuid:
            # print("a")
            for cost in row["Cost"]:
                # print(cost)
                # print(row)
                # print(row["Cost"][cost])
                return row["Cost"][cost]

def getVersion():
    versionData = requests.get("https://valorant-api.com/v1/version")
    versionDataJson = versionData.json()['data']
    final = f"{versionDataJson['branch']}-shipping-{versionDataJson['buildVersion']}-{versionDataJson['version'][-6:]}"
    return final