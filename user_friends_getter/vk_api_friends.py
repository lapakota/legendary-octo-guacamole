import vk_api


def get_user_friends(api_vk, user_id):
    friends_list = api_vk.friends.get(user_id=user_id, fields='nickname')
    friends_count = friends_list['count']

    with open(r"friends_list.txt", "w") as file:
        count_output = f'Friends count: {friends_count}'
        file.write(count_output + '\n\n')
        for friend in friends_list['items']:
            output = f"{friend['first_name']} {friend['last_name']} : id={friend['id']}"
            print(output)
            file.write(output + '\n')
        print('\n' + count_output)


def main():
    access_token = ''  # access token
    target_id = int(input('Enter target user id: '))

    api_vk = vk_api.VkApi(token=access_token).get_api()
    get_user_friends(api_vk, target_id)


if __name__ == '__main__':
    main()
