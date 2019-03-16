'''
Program:
    used to analysis the my weichat data.
    Instution : https://itchat.readthedocs.io/zh/latest/
'''


import itchat

class Friends:

    def __init__(self):
        pass

    def get_attr(friends, key):
        # 按照key得到相关list
        return list(map(lambda user: user.get(key), friends))

    @classmethod
    def get_data(self):
        itchat.auto_login(hotReload=True)
        # hotReload参数表示短时间内不需要扫码可登陆
        friends=itchat.get_friends()
        # print(friends[1])
        friends_info=dict(province=self.get_attr(friends,'Province'),
                          city=self.get_attr(friends,'City'),
                          nickname=self.get_attr(friends, "NickName"),
                        sex = self.get_attr(friends, "Sex"),
                        signature = self.get_attr(friends, "Signature"),
                        remarkname = self.get_attr(friends, "RemarkName"),
                        pyquanpin = self.get_attr(friends, "PYQuanPin"),
                        displayname = self.get_attr(friends, "DisplayName"),
                        isowner = self.get_attr(friends, "IsOwner")
                        )
        # print(friends_info['province'])
        return friends_info

if __name__ == '__main__':
    my_friends=Friends
    my_friends.get_data(my_friends)