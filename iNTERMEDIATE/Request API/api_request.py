import requests


def fetch_data_from_api(url):
    try:
        # Make a GET request to the API
        response = requests.get(url)

        # Raise an exception if the request was unsuccessful
        response.raise_for_status()

        # Parse the JSON data
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON decoding error: {json_err}")


def process_and_display_data(data):
    if data:
        # Example: Extract specific information
        if 'title' in data and 'body' in data:
            print(f"Title: {data['title']}")
            print(f"Body: {data['body']}")
        else:
            print("Expected data not found in the response.")
    else:
        print("No data to process.")


def main():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    data = fetch_data_from_api(url)
    process_and_display_data(data)


if __name__ == '__main__':
    main()


