import requests
import pandas as pd
import re

# URL and headers setup
url = "https://pladmin.estatesgazette.com/self_service/businesses/6865/leads"
headers = {"cookie": "visid_incap_2703267=2oYDZj4aQ6iSJ+FH+6xJdlweY2YAAAAAQUIPAAAAAABc5dgHvwSYhCzZcRtaIt3X; _gcl_au=1.1.522859.1717771872; _ga=GA1.1.1252106255.1717771873; adobeujs-optin=%7B%22aam%22%3Atrue%2C%22adcloud%22%3Atrue%2C%22aa%22%3Atrue%2C%22campaign%22%3Atrue%2C%22ecid%22%3Atrue%2C%22livefyre%22%3Atrue%2C%22target%22%3Atrue%2C%22mediaaa%22%3Atrue%7D; visid_incap_2703196=78dAs1mPT3G/EFaY1lksNPclY2YAAAAAQUIPAAAAAABqln5yWrsI8PClPKyo4wV/; nlbi_2703267=qmJhNvLM9y3XIXo8U/yCSwAAAABQEzwgZwbhZNj7Zeo97UY7; at_check=true; AMCVS_164E38B352784F380A490D4C%40AdobeOrg=1; s_cc=true; s_gvo_as=logged%20in; _pl_hub_persistent_session=RTZJQzNqY3VQK0pzeHRFaE5zSWZDQTYwM3lod0tsOURydHBqSGw4dzZhUlFLZVVudnFuc3JMVHlCb3I2dGZpdDhyNkhvc1FwZjJ3NHl0TzA0WlFMZ2c9PS0tYUgxTnpqckJrdlpwRHpLcGNnTU9TZz09--9c8a0cfff647cf34b93584c909fd083168f5dbb3; _pl_hub_auth0_session=e21ba9db73211a075304f8932bd7357f; __utmc=149155959; incap_ses_1221_2703196=jhYOK2DY/V1MMtgvH93xEMFnh2YAAAAAhHWND/jQdw7gYSM9hyhHrw==; incap_ses_157_2703267=r+sAayGGoARL0bOxxMYtAkAHjGYAAAAAtHTKjxAaEpKhKfTs7somWg==; incap_ses_157_2703196=CR2oIcXXshavKsSxxMYtAoYejGYAAAAAE/6gnU79xdqb5gQjkbUKOQ==; incap_ses_967_2703267=n/ureMFRKWjg+Bq5d3lrDeMijWYAAAAAOUm4W6ZUrq6lxyLdoTkuPA==; mbox=PC#f4019feadbd841079da230ebc0024711.38_0#1783770343|session#8a7cd88d069744499fd138bd5f4a8e03#1720527402; AMCV_164E38B352784F380A490D4C%40AdobeOrg=-1124106680%7CMCMID%7C77088484519265787371308041984943996299%7CMCAAMLH-1721130342%7C3%7CMCAAMB-1721130342%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1720532742s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0%7CMCIDTS%7C19913%7CMCCIDH%7C1683634888; s_vnum=1804171882639%26vn%3D6; fs_uid=#R8EWC#f59b532f-6a2a-4ee4-9e4d-413ef5d9b6e4:28d6c70c-40b6-4918-b113-987f9050541c:1720525543527::1#/1749307922; s_sq=rbiuk-estatesgazette%3D%2526c.%2526a.%2526activitymap.%2526page%253Deg.com-propertylink%25257Chome%25257Chome%252520page%2526link%253DManage%252520adverts%2526region%253DBODY%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Deg.com-propertylink%25257Chome%25257Chome%252520page%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fpladmin.estatesgazette.com%25252F%2526ot%253DA; incap_ses_967_2703196=7TrTZrBaVid0BRu5d3lrDe0ijWYAAAAAoR3edIxIvhh3dP71Z6S4cg==; __utmz=149155959.1720525553.7.3.utmcsr=propertylink.estatesgazette.com|utmccn=(referral)|utmcmd=referral|utmcct=/; incap_ses_162_2703196=roLyes2RUS31TtLqPYo/AicmjWYAAAAAxBUq884w1iLtVmbBdAE9tg==; _ga_NWH2Z55Z9L=GS1.1.1720551102.9.0.1720551102.0.0.0; nlbi_2703196=XCM3J5uj5G5RTtDQMlzKdAAAAAAUVgq7hBR4GYKLR8Og/Bt5; incap_ses_160_2703196=PtxlWExC/lZ1E4pBRW84Aq/Aj2YAAAAAUTf+LSXzLNWIjmiKqaHyog==; __utma=149155959.1252106255.1717771873.1720525553.1720697008.8; __utmt=1; __utmt_b=1; __utmb=149155959.34.10.1720697008",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "Accept": "application/json",  # Expect JSON response

        "cache-control": "max-age=0",
        "priority": "u=0, i", # type: ignore
        "referer": "https://pladmin.estatesgazette.com/self_service/businesses/6865/leads?advanced%5Bbusiness_ids%5D%5B%5D=6865&advanced%5Benquiry_type%5D=&advanced%5Bterm%5D=&page=79&search%5Bfacets%5D%5Btime%5D%5Bfacets_filter%5D%5Band%5D%5B%5D%5Bterm%5D%5Bbusiness_ids%5D%5B%5D=6865&search%5Bfacets%5D%5Btime%5D%5Brange%5D%5Bfield%5D=created_at&search%5Bfacets%5D%5Btime%5D%5Brange%5D%5Branges%5D%5B%5D%5Bfrom%5D=2024-07-11+00%3A00%3A00+%2B0000&search%5Bfacets%5D%5Btime%5D%5Brange%5D%5Branges%5D%5B%5D%5Bto%5D=2024-07-11+23%3A59%3A59+%2B0000&search%5Bfacets%5D%5Btime%5D%5Brange%5D%5Branges%5D%5B%5D%5Bfrom%5D=2024-07-10+11%3A23%3A27+%2B0000&search%5Bfacets%5D%5Btime%5D%5Brange%5D%5Branges%5D%5B%5D%5Bto%5D=2024-07-11+11%3A23%3A27+%2B0000&search%5Bfacets%5D%5Btime%5D%5Brange%5D%5Branges%5D%5B%5D%5Bfrom%5D=2024-07-04+11%3A23%3A27+%2B0000&search%5Bfacets%5D%5Btime%5D%5Brange%5D%5Branges%5D%5B%5D%5Bto%5D=2024-07-11+11%3A23%3A27+%2B0000&search%5Bfacets%5D%5Btime%5D%5Brange%5D%5Branges%5D%5B%5D%5Bfrom%5D=2024-07-08+00%3A00%3A00+%2B0000&search%5Bfacets%5D%5Btime%5D%5Brange%5D%5Branges%5D%5B%5D%5Bto%5D=2024-07-14+23%3A59%3A59+%2B0000&search%5Bfacets%5D%5Btime%5D%5Brange%5D%5Branges%5D%5B%5D%5Bfrom%5D=2024-07-01+00%3A00%3A00+%2B0000&search%5Bfacets%5D%5Btime%5D%5Brange%5D%5Branges%5D%5B%5D%5Bto%5D=2024-07-31+23%3A59%3A59+%2B0000&search%5Bfacets%5D%5Btime%5D%5Brange%5D%5Branges%5D%5B%5D%5Bfrom%5D=2024-06-01+00%3A00%3A00+%2B0000&search%5Bfacets%5D%5Btime%5D%5Brange%5D%5Branges%5D%5B%5D%5Bto%5D=2024-06-30+23%3A59%3A59+%2B0000&search%5Bfacets%5D%5Btypes%5D%5Bfacets_filter%5D%5Band%5D%5B%5D%5Bterm%5D%5Bbusiness_ids%5D%5B%5D=6865&search%5Bfacets%5D%5Btypes%5D%5Bterms%5D%5Bfield%5D=enquiry_type&search%5Bfacets%5D%5Btypes%5D%5Bterms%5D%5Bsize%5D=50&search%5Bterm%5D=",
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}
# Function to extract comments
def extract_comments(message):
    comment_match = re.search(r'Comments: (.*?)<br>', message, re.S)
    return comment_match.group(1).strip() if comment_match else "No comment found"

# Prepare to store the data
all_data = []

# Start with the first page
page = 1

while True:
    querystring = {
        "advanced[business_ids][]": "6865",
        "page": str(page),
    }
    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code == 200:
        data = response.json()
        items = data.get('items', [])

        # Debugging information
        print(f"Page {page} - Number of items: {len(items)}")

        if not items:
            break  # Exit the loop if no more items are returned

        # Append each item's data to the list
        for item in items:
            all_data.append({
                'First Name': item['first_name'],
                'Last Name': item['last_name'],
                'Telephone': item['telephone'],
                'Email': item['email'],
                'Enquiry Type': item['enquiry_type'],
                'Comments': extract_comments(item['message']),
                'Property URL': item.get('item_url', 'No URL'),
                'Property ID': item['item_id'],
                'Status': item['status'],
                'Created At': item['created_at'],
                'Updated At': item['updated_at']
            })
        
        page += 1  # Move to the next page
    else:
        print(f"Failed to fetch data for page {page}: {response.status_code}")
        break

# Create a DataFrame
df = pd.DataFrame(all_data)

# Verify the number of rows in the DataFrame
print(f"Total rows to write: {len(df)}")

# Write the DataFrame to an Excel file
df.to_excel('output_data.xlsx', index=False)

print("Data has been written to Excel successfully!")