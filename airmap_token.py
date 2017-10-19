#!/usr/bin/env python3
"""
Script to generate id_token from an airmap api key
"""
import requests

def get_id_token(api_key, user_id):
    try:
        response = requests.post(
            url="https://api.airmap.com/auth/v1/anonymous/token",
            headers={
                "X-API-Key": api_key
            },
            data={"user_id": user_id}
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
		print(e)

if __name__ == '__main__':
	api_key = input("Enter your airmap api key: ")
	user_id = input("Enter a user id: ")

	get_token(api_key, user_id)