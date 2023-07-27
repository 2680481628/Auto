from datetime import tzinfo, timedelta

import requests


class MessagePush:
    @staticmethod
    # ServerChan/PushDeer/PushPlush
    def pushMessage(title, content, token, type):
        if type == 'PushDeer':
            #PushDeer
            url = 'https://api2.pushdeer.com/message/push?pushkey=' + token + '&text=' + title + '&desp=' + content
            resp = requests.post(url)
            if resp.json()["code"] == 0:
                print('PushDeer推送消息提醒成功！')
            else:
                print('PushDeer推送消息提醒失败！')
        elif type == 'PushPlus':
            #PushPlus
            url = 'http://www.pushplus.plus/send?token=' + token + '&title=' + title + '&content=' + content + '&template=html'
            resp = requests.post(url)
            if resp.json()["code"] == 200:
                print('PushPlush推送消息提醒成功！')
            else:
                print('PushPlush推送消息提醒失败！')
        elif type == 'Mail':
            #Mail
            url = 'http://api.lightsky.top/api/mail?content=' + content + '&title=' + title + '&key=3119952303&adress=' + token
            resp = requests.post(url)
            if resp.json()["code"] == 200:
                print('Mail推送消息提醒成功！')
            else:
                print('Mail推送消息提醒失败！')
#        elif type == 'Phone':
#            #phone
#            url = 'https://sms.idcnow.cn/api/index/SmsApi?phone=' + token + '&content=【星诺StarNol】' + content + '&username=name&key=key'
#            resp = requests.post(url)
#            if resp.json()["code"] == 0:
#                print('Phone推送消息提醒成功！')
#            else:
#                print('Phone推送消息提醒失败！')
        else:
            #ServerChan
            url = 'https://sctapi.ftqq.com/' + token + '.send?title=' + title + '&desp=' + content
            resp = requests.post(url)
            if resp.json()["code"] == 0:
                print('ServerChan推送消息提醒成功！')
            else:
                print('ServerChan推送消息提醒失败！')



class UTC(tzinfo):
    """UTC"""

    def __init__(self, offset=0):
        self._offset = offset

    def utcoffset(self, dt):
        return timedelta(hours=self._offset)

    def tzname(self, dt):
        return "UTC +%s" % self._offset

    def dst(self, dt):
        return timedelta(hours=self._offset)

    def timezone(str):
        if str == 'UTC':
            return UTC()
        elif str == 'PRC':
            return UTC(8)
        else:
            return None


SBox = [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B,
        0xFE, 0xD7, 0xAB, 0x76, 0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0,
        0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0, 0xB7, 0xFD, 0x93, 0x26,
        0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
        0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2,
        0xEB, 0x27, 0xB2, 0x75, 0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0,
        0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84, 0x53, 0xD1, 0x00, 0xED,
        0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
        0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F,
        0x50, 0x3C, 0x9F, 0xA8, 0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5,
        0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2, 0xCD, 0x0C, 0x13, 0xEC,
        0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
        0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14,
        0xDE, 0x5E, 0x0B, 0xDB, 0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C,
        0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79, 0xE7, 0xC8, 0x37, 0x6D,
        0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
        0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F,
        0x4B, 0xBD, 0x8B, 0x8A, 0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E,
        0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E, 0xE1, 0xF8, 0x98, 0x11,
        0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
        0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F,
        0xB0, 0x54, 0xBB, 0x16]
SBoxIV = [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e,
          0x81, 0xf3, 0xd7, 0xfb, 0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87,
          0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb, 0x54, 0x7b, 0x94, 0x32,
          0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
          0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49,
          0x6d, 0x8b, 0xd1, 0x25, 0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16,
          0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92, 0x6c, 0x70, 0x48, 0x50,
          0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
          0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05,
          0xb8, 0xb3, 0x45, 0x06, 0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02,
          0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b, 0x3a, 0x91, 0x11, 0x41,
          0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
          0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8,
          0x1c, 0x75, 0xdf, 0x6e, 0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89,
          0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b, 0xfc, 0x56, 0x3e, 0x4b,
          0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
          0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59,
          0x27, 0x80, 0xec, 0x5f, 0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d,
          0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef, 0xa0, 0xe0, 0x3b, 0x4d,
          0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
          0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63,
          0x55, 0x21, 0x0c, 0x7d]


def _gf2_mul(a: int, b: int, poly: int) -> int:
    ans = 0
    digit_1 = poly.bit_length() - 1
    while b:
        if b & 1:
            ans = ans ^ a
        a, b = a << 1, b >> 1
        if a >> digit_1:
            a = a ^ poly
    return ans


class AES:
    def __init__(self, key: bytes):
        self.aes_type = len(key) * 8
        self._key_r = self._generate_key(key)

    def _generate_key(self, key: bytes) -> list:
        """密钥扩展"""
        Rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]  # 轮常数
        Nr, Nk = 10 + (self.aes_type - 128) // 32, self.aes_type // 32  # Nr：轮数，Nk：密钥长度
        w = [0 for _ in range(4 * (Nr + 1))]  # 轮密钥

        for i in range(Nk):
            w[i] = int.from_bytes(key[4 * i:4 * i + 4], 'big')
        for i in range(Nk, 4 * (Nr + 1)):
            temp = w[i - 1]
            if i % Nk == 0:
                temp = self._split_int(temp)  # 拆分成 4x8bit
                temp = [SBox[temp[1]] ^ Rcon[i // Nk - 1], SBox[temp[2]],
                        SBox[temp[3]], SBox[temp[0]]]
                temp = self._joint_int(temp)  # 合并回 32bit
            elif Nk > 6 and i % Nk == 4:
                temp = self._split_int(temp)  # 拆分成 4x8bit
                temp = [SBox[temp[0]], SBox[temp[1]],
                        SBox[temp[2]], SBox[temp[3]]]
                temp = self._joint_int(temp)  # 合并回 32bit
            w[i] = w[i - Nk] ^ temp

        # 将 w 变成 4x4xNr 形式的矩阵
        key_r = [[[[0] for _ in range(4)] for _ in range(4)] for _ in range(Nr + 1)]
        for t in range(Nr + 1):
            for i in range(4):
                temp = self._split_int(w[4 * t + i])
                for j in range(4):
                    key_r[t][j][i] = temp[j]
        return key_r

    @staticmethod
    def _split_int(n: int) -> list:
        """拆分 32bit 成 4x8bit"""
        return [(n >> 24) & 0xFF, (n >> 16) & 0xFF, (n >> 8) & 0xFF, n & 0xFF]

    @staticmethod
    def _joint_int(b: list) -> int:
        """合并 4x8bit 成 32bit"""
        return (b[0] << 24) | (b[1] << 16) | (b[2] << 8) | b[3]

    def encrypt(self, plaintext: bytes) -> bytes:
        """加密"""
        if len(plaintext) % 16 != 0:
            v = 16 - len(plaintext) % 16
            for _ in range(16 - len(plaintext) % 16):
                plaintext += v.to_bytes(1, 'big')
        state = [[plaintext[4 * j + i] for j in range(4)] for i in range(4)]
        Nr = 10 + (self.aes_type - 128) // 32

        state = self._add_key(state, self._key_r[0])
        for t in range(1, Nr):
            state = self._sub_byte(state, iv=False)  # 字节代替
            state = self._shift_row(state, iv=False)  # 行移位
            state = self._mix_col(state, iv=False)  # 列混淆
            state = self._add_key(state, self._key_r[t])  # 轮密钥加
        state = self._sub_byte(state, iv=False)
        state = self._shift_row(state, iv=False)
        state = self._add_key(state, self._key_r[Nr])
        # 将 state 重新排列成一维的形式
        ciphertext = bytearray(16)
        for i in range(4):
            for j in range(4):
                ciphertext[4 * j + i] = state[i][j]
        return bytes(ciphertext)

    def decrypt(self, ciphertext: bytes) -> bytes:
        state = [[ciphertext[4 * j + i] for j in range(4)] for i in range(4)]
        Nr = 10 + (self.aes_type - 128) // 32

        state = self._add_key(state, self._key_r[Nr])
        for t in range(1, Nr):
            state = self._shift_row(state, iv=True)  # 逆行移位
            state = self._sub_byte(state, iv=True)  # 逆字节代替
            state = self._add_key(state, self._key_r[Nr - t])  # 轮密钥加
            state = self._mix_col(state, iv=True)  # 逆列混淆
        state = self._shift_row(state, iv=True)
        state = self._sub_byte(state, iv=True)
        state = self._add_key(state, self._key_r[0])

        plaintext = bytearray(16)
        for i in range(4):
            for j in range(4):
                plaintext[4 * j + i] = state[i][j]
        return bytes(plaintext)

    @staticmethod
    def _add_key(state, k):
        for i in range(4):
            for j in range(4):
                state[i][j] = state[i][j] ^ k[i][j]
        return state

    @staticmethod
    def _shift_row(state, iv):
        if not iv:
            state[1] = [state[1][1], state[1][2], state[1][3], state[1][0]]
            state[2] = [state[2][2], state[2][3], state[2][0], state[2][1]]
            state[3] = [state[3][3], state[3][0], state[3][1], state[3][2]]
        else:
            state[1] = [state[1][3], state[1][0], state[1][1], state[1][2]]
            state[2] = [state[2][2], state[2][3], state[2][0], state[2][1]]
            state[3] = [state[3][1], state[3][2], state[3][3], state[3][0]]
        return state

    @staticmethod
    def _mix_col(state, iv):
        if not iv:
            matrix = [[0x02, 0x03, 0x01, 0x01],
                      [0x01, 0x02, 0x03, 0x01],
                      [0x01, 0x01, 0x02, 0x03],
                      [0x03, 0x01, 0x01, 0x02]]
        else:
            matrix = [[0x0E, 0x0B, 0x0D, 0x09],
                      [0x09, 0x0E, 0x0B, 0x0D],
                      [0x0D, 0x09, 0x0E, 0x0B],
                      [0x0B, 0x0D, 0x09, 0x0E]]
        res = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                temp = 0
                for k in range(4):
                    temp = temp ^ _gf2_mul(matrix[i][k], state[k][j], poly=0x11b)
                res[i][j] = temp
        return res

    @staticmethod
    def _sub_byte(state, iv):
        for i in range(4):
            for j in range(4):
                state[i][j] = SBox[state[i][j]] if not iv else SBoxIV[state[i][j]]
        return state
