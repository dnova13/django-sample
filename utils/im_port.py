import requests
import json
from project import settings
from service.exceptions import ValidationError2, ValidationError3


class ImPort:

    def __init__(self):
        self.get_token_url = 'https://api.iamport.kr/users/getToken'
        self.payment_url = 'https://api.iamport.kr/payments/{}?_token={}'
        self.api_key = settings.IAMPORT_API_KEY
        self.api_secret_key = settings.IAMPORT_API_SECRET_KEY

    def get_token(self):
        """ 
        아임포트 토큰 반환
        """

        response = requests.post(
            url=self.get_token_url,
            data=dict(
                imp_key=self.api_key,
                imp_secret=self.api_secret_key,
            )
        )

        if response.status_code == 200:
            # print(f'token : {response.json()["response"]["access_token"]}')
            return response.json()["response"]["access_token"]
        else:
            return None

    def get_payment_info(self, imp_uid):
        """ 
        결제 정보 얻는 함수
            Args:
                imp_uid(str) : pg사 고유 아이디, @reason : 환불 사유.
        """

        token = self.get_token()
        if token is None:
            return None

        info_response = requests.get(
            url=self.payment_url.format(imp_uid, token)
        )

        if info_response.status_code == 200:
            response_json = info_response.json()
            if response_json['code'] == 0:
                return response_json['response']
            else:
                # 1 인 경우, checksum 유효성 검사 실패(취소가능금액 초과)
                return None
        else:
            return None

    def payment_cancel(self, imp_uid, checksum, amount=0, reason=None):
        """ 
        결제 취소 또는 환불 처리 함수
            Args:
                imp_uid(str) : pg사 고유 아이디, @reason : 환불 사유.
                check_sum(int) : 환불 가능 금액(cancelable_amounts)
                amount(int) : 환불할 금액, 미입력시 전액 환불.
        """

        print('request refund')
        token = self.get_token()

        if token is None:
            return None

        data = dict(imp_uid=imp_uid, ckecksum=checksum,
                    amount=amount, reason=reason)

        if not amount:
            data = dict(imp_uid=imp_uid, checksum=checksum, reason=reason)

        cancel_response = requests.post(
            url=self.payment_url.format('cancel', token),
            data=data,
        )
        # print(cancel_response)
        # print(cancel_response.json())

        if cancel_response.status_code == 200:
            response_json = cancel_response.json()
            result_code = response_json['code']

            # print(result_code)
            # 실제 유효한 imp_uid, token, 금액일 경우 response의 code가 0으로 반환된다.
            if result_code == 0:
                return dict(success=True)
            else:
                return {
                    'success': False,
                    'status': "PG_ERROR",
                    'message': response_json
                }
        return {
            'success': False,
            'status': "PG_ERROR",
            'message': cancel_response.json()
        }  # TODO : 어떤 경우에 iamport API의 리스폰스 내 code가 0이 아닌 다른 값으로 오는지 파악해야한다
