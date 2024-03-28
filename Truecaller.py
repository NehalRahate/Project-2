#pip install truecallerpy "in TERMINAL"
#truecallerpy login "To login into truecaller account"
#truecallerpy --installationid
# InstallationId will Generate
#truecallerpy -i -r "To Print ID"tr
#truecallerpy -s 1234567890 to search number
#truecallerpy -s 1234567890 --name only
#Similarly, you can use the --email -print only the email associated with number.
#truecallerpy --bs 9912345678,+14051234567,+919987654321 - to search bulk Number
#The Output will be in Json so here is the code to print Names 

import json

# Load the JSON data
json_data = '''
{
  "status_code": 200,
  "data": {
    "data": [
      {
        "key": "828282828282",
        "value": {
          "id": "mgBqgw==",
          "name": "Shahrukh",
          "imId": "4j64vjep"
        }
      },
      {
        "key": "9165652515",
        "value": {
          "id": "5Ul=",
          "name": "Khan Sir",
          "imId": "1jpi9e14ow"
        }
      }
    ]
  }
}
'''

# Parse the JSON string
data = json.loads(json_data)

# Access the list of entries in the 'data' key
entries = data["data"]["data"]

for entry in entries:
    name = entry["value"]["name"]
    print(name)

