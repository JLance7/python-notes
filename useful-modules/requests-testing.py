import requests
import json


def api_request(url, verify_ssl):
  user = 'username'
  pwd = 'password'

  headers = {"Content-Type":"application/json","Accept":"application/json"}

  if verify_ssl:
      response = requests.get(url, auth=(user, pwd), headers=headers, verify=True)
  else:
      response = requests.get(url, auth=(user, pwd), headers=headers, verify=False)

  data = response.json()
  
  if response.status_code != 200: 
    print(f"Status: {response.status_code} Headers: {response.headers} Error Response: {data}")
    return
  return data


# pokemon = 'clefairy'
# url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
# verify_ssl = False
# data = api_request(url, verify_ssl)
# print(json.dumps(data, indent=2))

def graph_ql_query():
  url = "https://fruits-api.netlify.app/graphql"
  body = """
  {
    fruit(id: 14) {
      scientific_name
      tree_name
    }
  }
  """
  
  response = requests.post(url=url, json={"query": body}, verify=False)
  print("response status code: ", response.status_code)
  if response.status_code == 200:
      print("response : ", response.content)

graph_ql_query()