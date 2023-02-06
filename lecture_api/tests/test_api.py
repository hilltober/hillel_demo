import pytest
import requests
import json
import pprint


class TestAPI:
    pp = pprint.PrettyPrinter(depth=4)

    @pytest.mark.get
    def test_list_users(self):
        response = requests.get('https://reqres.in/api/users?page=2')
        assert response.status_code == 200
        parsed = json.loads(response.content)
        # self.pp.pprint(parsed)
        # parsed['data'][0]['first_name'] = ''
        assert all([
            parsed.get('per_page') == 6,
            'contributions' in parsed.get('support').get('text'),
            'support-heading' in parsed.get('support').get('url'),
            len(parsed.get('data')) == 6,
            all([name.get('first_name') for name in [
                record for record in parsed.get('data')]]),
        ])

    @pytest.mark.get
    def test_single_user(self):
        response = requests.get('https://reqres.in/api/users/2')
        assert response.status_code == 200
        parsed = json.loads(response.content)
        data_success = all([x for x in parsed['data'].values()])
        is_first_name_present = parsed.get('data').get('first_name')
        parsed['data']['first_name'] = ''
        is_check_correct = not parsed.get('data').get('first_name')
        is_avatar_present = requests.get(
            parsed.get('data').get('avatar')).status_code == 200
        assert all([
            data_success, is_first_name_present,
            is_check_correct, is_avatar_present])

    @pytest.mark.get
    def test_single_user_not_found(self):
        response = requests.get('https://reqres.in/api/users/23')
        assert response.status_code == 404
        assert not dict(json.loads(response.content))

    @pytest.mark.get
    def test_list_resource(self):
        response = requests.get('https://reqres.in/api/unknown')
        parsed = json.loads(response.content)
        assert response.status_code == 200
        assert len(parsed.get('data')) == parsed.get('per_page')

    @pytest.mark.get
    def test_single_resource(self):
        response = requests.get('https://reqres.in/api/unknown/2')
        parsed = json.loads(response.content)
        assert response.status_code == 200
        assert sorted(
            parsed.get('data').keys()) == sorted(
            ['id', 'name', 'year', 'color', 'pantone_value'])
