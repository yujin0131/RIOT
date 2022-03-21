from urllib import parse
import json
import time
import requests

riot_key = 'RGAPI-6136e00f-c422-4a59-8fc9-946255bb263f'
print('riot_key : ', end='')
summonerName = input()
#summonerName = parse.quote(summonerName)
name_url = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summonerName + '?api_key=' + riot_key
print('name_url : ' + name_url)

name_res = requests.get(name_url).json()
print('name_res : ', end='')
print(name_res)

encryptedSummonerId = name_res["id"]
print('encryptedSummonerId : ' + encryptedSummonerId)

url = 'https://kr.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/' + encryptedSummonerId + '?api_key=' + riot_key 
#url = 'https://kr.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U?api_key=' + riot_key 
print('url :  ' + url)

res = requests.get(url).json()
print(res)
res_dump = json.dumps(res)
res_data = json.loads(res_dump)

for i in res_data:
    
    championId = i['championId']
    championLevel = i['championLevel']
    championPoints = i['championPoints']
    summonerId = i['summonerId']

    print(championId)
    print(championLevel)
    print(championPoints)
    print(summonerId)
#{"id":"UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U","accountId":"HYquYvl5qcoqqhkntXgey4c0KGbhz1aJefYtpaTxNv2ovls0Bhy_dH5h","puuid":"XQS3FSugR2aEzNY-6jsQz4be1MnHLpmUUZUJV0u24MJic2LG-3rHtQQNxmIduWRQYuy6boiLrVwjBA","name":"광진구뚝배기","profileIconId":4864,"revisionDate":1646451784000,"summonerLevel":134}

#[{'championId': 89, 'championLevel': 7, 'championPoints': 113605, 'lastPlayTime': 1646806595000, 'championPointsSinceLastLevel': 92005, 'championPointsUntilNextLevel': 0, 'chestGranted': True, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 99, 'championLevel': 7, 'championPoints': 104676, 'lastPlayTime': 1646470040000, 'championPointsSinceLastLevel': 83076, 'championPointsUntilNextLevel': 0, 'chestGranted': True, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 58, 'championLevel': 5, 'championPoints': 85672, 'lastPlayTime': 1645802550000, 'championPointsSinceLastLevel': 64072, 'championPointsUntilNextLevel': 0, 'chestGranted': False, 'tokensEarned': 2, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 25, 'championLevel': 7, 'championPoints': 72683, 'lastPlayTime': 1646476980000, 'championPointsSinceLastLevel': 51083, 'championPointsUntilNextLevel': 0, 'chestGranted': True, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 54, 'championLevel': 5, 'championPoints': 56686, 'lastPlayTime': 1646478475000, 'championPointsSinceLastLevel': 35086, 'championPointsUntilNextLevel': 0, 'chestGranted': True, 'tokensEarned': 1, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'},
# {'championId': 53, 'championLevel': 7, 'championPoints': 43540, 'lastPlayTime': 1646814342000, 'championPointsSinceLastLevel': 21940, 'championPointsUntilNextLevel': 0, 'chestGranted': True, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'},
# {'championId': 222, 'championLevel': 6, 'championPoints': 25771, 'lastPlayTime': 1641715147000, 'championPointsSinceLastLevel': 4171, 'championPointsUntilNextLevel': 0, 'chestGranted': True, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'},
# {'championId': 105, 'championLevel': 5, 'championPoints': 24244, 'lastPlayTime': 1645792875000, 'championPointsSinceLastLevel': 2644, 'championPointsUntilNextLevel': 0, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'},
# {'championId': 86, 'championLevel': 4, 'championPoints': 14867, 'lastPlayTime': 1646125288000, 'championPointsSinceLastLevel': 2267, 'championPointsUntilNextLevel': 6733, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'},
# {'championId': 80, 'championLevel': 3, 'championPoints': 11095, 'lastPlayTime': 1645342364000, 'championPointsSinceLastLevel': 5095, 'championPointsUntilNextLevel': 1505, 'chestGranted': True, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 164, 'championLevel': 3, 'championPoints': 8705, 'lastPlayTime': 1604305763000, 'championPointsSinceLastLevel': 2705, 'championPointsUntilNextLevel': 3895, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 51, 'championLevel': 3, 'championPoints': 6083, 'lastPlayTime': 1600356549000, 'championPointsSinceLastLevel': 83, 'championPointsUntilNextLevel': 6517, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 111, 'championLevel': 2, 'championPoints': 5758, 'lastPlayTime': 1635496967000, 'championPointsSinceLastLevel': 3958, 'championPointsUntilNextLevel': 242, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 516, 'championLevel': 2, 'championPoints': 5537, 'lastPlayTime': 1599494335000, 'championPointsSinceLastLevel': 3737, 'championPointsUntilNextLevel': 463, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 81, 'championLevel': 2, 'championPoints': 5033, 'lastPlayTime': 1644925001000, 'championPointsSinceLastLevel': 3233, 'championPointsUntilNextLevel': 967, 'chestGranted': True, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 235, 'championLevel': 2, 'championPoints': 4822, 'lastPlayTime': 1629030955000, 'championPointsSinceLastLevel': 3022, 'championPointsUntilNextLevel': 1178, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 106, 'championLevel': 2, 'championPoints': 4532, 'lastPlayTime': 1596371296000, 'championPointsSinceLastLevel': 2732, 'championPointsUntilNextLevel': 1468, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 145, 'championLevel': 2, 'championPoints': 4351, 'lastPlayTime': 1615858865000, 'championPointsSinceLastLevel': 2551, 'championPointsUntilNextLevel': 1649, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 35, 'championLevel': 2, 'championPoints': 3557, 'lastPlayTime': 1615841120000, 'championPointsSinceLastLevel': 1757, 'championPointsUntilNextLevel': 2443, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 67, 'championLevel': 2, 'championPoints': 2503, 'lastPlayTime': 1646468284000, 'championPointsSinceLastLevel': 703, 'championPointsUntilNextLevel': 3497, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 103, 'championLevel': 2, 'championPoints': 2253, 'lastPlayTime': 1644841974000, 'championPointsSinceLastLevel': 453, 'championPointsUntilNextLevel': 3747, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 84, 'championLevel': 2, 'championPoints': 2193, 'lastPlayTime': 1645800168000, 'championPointsSinceLastLevel': 393, 'championPointsUntilNextLevel': 3807, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 32, 'championLevel': 2, 'championPoints': 2176, 'lastPlayTime': 1646810810000, 'championPointsSinceLastLevel': 376, 'championPointsUntilNextLevel': 3824, 'chestGranted': True, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 117, 'championLevel': 2, 'championPoints': 1891, 'lastPlayTime': 1619873402000, 'championPointsSinceLastLevel': 91, 'championPointsUntilNextLevel': 4109, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 21, 'championLevel': 1, 'championPoints': 1732, 'lastPlayTime': 1572934615000, 'championPointsSinceLastLevel': 1732, 'championPointsUntilNextLevel': 68, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 498, 'championLevel': 1, 'championPoints': 1716, 'lastPlayTime': 1575362969000, 'championPointsSinceLastLevel': 1716, 'championPointsUntilNextLevel': 84, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 221, 'championLevel': 1, 'championPoints': 1633, 'lastPlayTime': 1644930677000, 'championPointsSinceLastLevel': 1633, 'championPointsUntilNextLevel': 167, 'chestGranted': True, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 875, 'championLevel': 1, 'championPoints': 1401, 'lastPlayTime': 1599543372000, 'championPointsSinceLastLevel': 1401, 'championPointsUntilNextLevel': 399, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 34, 'championLevel': 1, 'championPoints': 1401, 'lastPlayTime': 1645454644000, 'championPointsSinceLastLevel': 1401, 'championPointsUntilNextLevel': 399, 'chestGranted': True, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 245, 'championLevel': 1, 'championPoints': 1395, 'lastPlayTime': 1645708538000, 'championPointsSinceLastLevel': 1395, 'championPointsUntilNextLevel': 405, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 12, 'championLevel': 1, 'championPoints': 1379, 'lastPlayTime': 1628261992000, 'championPointsSinceLastLevel': 1379, 'championPointsUntilNextLevel': 421, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 68, 'championLevel': 1, 'championPoints': 1304, 'lastPlayTime': 1638012471000, 'championPointsSinceLastLevel': 1304, 'championPointsUntilNextLevel': 496, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 236, 'championLevel': 1, 'championPoints': 1196, 'lastPlayTime': 1615853277000, 'championPointsSinceLastLevel': 1196, 'championPointsUntilNextLevel': 604, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 22, 'championLevel': 1, 'championPoints': 1151, 'lastPlayTime': 1563619825000, 'championPointsSinceLastLevel': 1151, 'championPointsUntilNextLevel': 649, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 82, 'championLevel': 1, 'championPoints': 1063, 'lastPlayTime': 1582595663000, 'championPointsSinceLastLevel': 1063, 'championPointsUntilNextLevel': 737, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 141, 'championLevel': 1, 'championPoints': 928, 'lastPlayTime': 1615828217000, 'championPointsSinceLastLevel': 928, 'championPointsUntilNextLevel': 872, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 39, 'championLevel': 1, 'championPoints': 896, 'lastPlayTime': 1633802407000, 'championPointsSinceLastLevel': 896, 'championPointsUntilNextLevel': 904, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 91, 'championLevel': 1, 'championPoints': 846, 'lastPlayTime': 1632054873000, 'championPointsSinceLastLevel': 846, 'championPointsUntilNextLevel': 954, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 45, 'championLevel': 1, 'championPoints': 817, 'lastPlayTime': 1646808490000, 'championPointsSinceLastLevel': 817, 'championPointsUntilNextLevel': 983, 'chestGranted': True, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 37, 'championLevel': 1, 'championPoints': 805, 'lastPlayTime': 1597855205000, 'championPointsSinceLastLevel': 805, 'championPointsUntilNextLevel': 995, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 85, 'championLevel': 1, 'championPoints': 801, 'lastPlayTime': 1593188320000, 'championPointsSinceLastLevel': 801, 'championPointsUntilNextLevel': 999, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 350, 'championLevel': 1, 'championPoints': 738, 'lastPlayTime': 1614417903000, 'championPointsSinceLastLevel': 738, 'championPointsUntilNextLevel': 1062, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'},
# {'championId': 92, 'championLevel': 1, 'championPoints': 663, 'lastPlayTime': 1645794961000, 'championPointsSinceLastLevel': 663, 'championPointsUntilNextLevel': 1137, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 18, 'championLevel': 1, 'championPoints': 643, 'lastPlayTime': 1600328897000, 'championPointsSinceLastLevel': 643, 'championPointsUntilNextLevel': 1157, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 412, 'championLevel': 1, 'championPoints': 384, 'lastPlayTime': 1642328072000, 'championPointsSinceLastLevel': 384, 'championPointsUntilNextLevel': 1416, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 429, 'championLevel': 1, 'championPoints': 281, 'lastPlayTime': 1572261220000, 'championPointsSinceLastLevel': 281, 'championPointsUntilNextLevel': 1519, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 150, 'championLevel': 1, 'championPoints': 280, 'lastPlayTime': 1613185616000, 'championPointsSinceLastLevel': 280, 'championPointsUntilNextLevel': 1520, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 101, 'championLevel': 1, 'championPoints': 276, 'lastPlayTime': 1637569669000, 'championPointsSinceLastLevel': 276, 'championPointsUntilNextLevel': 1524, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 3, 'championLevel': 1, 'championPoints': 272, 'lastPlayTime': 1621003990000, 'championPointsSinceLastLevel': 272, 'championPointsUntilNextLevel': 1528, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 133, 'championLevel': 1, 'championPoints': 264, 'lastPlayTime': 1609656911000, 'championPointsSinceLastLevel': 264, 'championPointsUntilNextLevel': 1536, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 36, 'championLevel': 1, 'championPoints': 208, 'lastPlayTime': 1599540521000, 'championPointsSinceLastLevel': 208, 'championPointsUntilNextLevel': 1592, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 147, 'championLevel': 1, 'championPoints': 205, 'lastPlayTime': 1615822530000, 'championPointsSinceLastLevel': 205, 'championPointsUntilNextLevel': 1595, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 7, 'championLevel': 1, 'championPoints': 172, 'lastPlayTime': 1645797949000, 'championPointsSinceLastLevel': 172, 'championPointsUntilNextLevel': 1628, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 161, 'championLevel': 1, 'championPoints': 157, 'lastPlayTime': 1562346225000, 'championPointsSinceLastLevel': 157, 'championPointsUntilNextLevel': 1643, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 267, 'championLevel': 1, 'championPoints': 139, 'lastPlayTime': 1635508099000, 'championPointsSinceLastLevel': 139, 'championPointsUntilNextLevel': 1661, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 555, 'championLevel': 1, 'championPoints': 130, 'lastPlayTime': 1617442837000, 'championPointsSinceLastLevel': 130, 'championPointsUntilNextLevel': 1670, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 30, 'championLevel': 1, 'championPoints': 115, 'lastPlayTime': 1578667428000, 'championPointsSinceLastLevel': 115, 'championPointsUntilNextLevel': 1685, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}, 
# {'championId': 131, 'championLevel': 1, 'championPoints': 92, 'lastPlayTime': 1576952895000, 'championPointsSinceLastLevel': 92, 'championPointsUntilNextLevel': 1708, 'chestGranted': False, 'tokensEarned': 0, 'summonerId': 'UIz6w1kPTTrBq99FIvxhJSyrDlmuNmjdP7xqkdix62kRc4U'}]