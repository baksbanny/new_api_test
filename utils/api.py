from utils.https_method import Http_methods

url_list_users = "https://reqres.in/api/users?page=2"
url_single_users = "https://reqres.in/api/users/2"
url_single_users_not_found = "https://reqres.in/api/users/23"
url_list_resource = "https://reqres.in/api/unknown"
url_single_resource = "https://reqres.in/api/unknown/2"
url_single_resource_not_found = "https://reqres.in/api/unknown/23"
url_users_create = "https://reqres.in/api/users"
url_users_update = "https://reqres.in/api/users/2"

class Reqres_api():

    @staticmethod
    def list_users():
        result_list_users = Http_methods.get(url_list_users)
        print(result_list_users.text)
        print(result_list_users.status_code)
        assert  result_list_users.status_code == 200
        return url_list_users

    @staticmethod
    def single_users():
        result_single_users = Http_methods.get(url_single_users)
        print(result_single_users.text)
        print(result_single_users.status_code)
        assert result_single_users.status_code == 200
        return url_single_users

    @staticmethod
    def single_users_not_fount():
        result_single_users_not_fount = Http_methods.get(url_single_users_not_found)
        print((result_single_users_not_fount.text))
        print(result_single_users_not_fount.status_code)
        assert result_single_users_not_fount.status_code == 404
        return url_single_users_not_found

    @staticmethod
    def list_resource():
        result_list_resource = Http_methods.get(url_list_resource)
        print(result_list_resource.text)
        print(result_list_resource.status_code)
        assert result_list_resource.status_code == 200
        return url_list_resource

    @staticmethod
    def single_resource():
        result_single_resource = Http_methods.get(url_single_resource)
        print(result_single_resource.text)
        print(result_single_resource.status_code)
        assert result_single_resource.status_code == 200
        return  url_single_resource

    @staticmethod
    def single_resource_not_found():
        result_single_resource_not_found = Http_methods.get(url_single_resource_not_found)
        print(result_single_resource_not_found.text)
        print(result_single_resource_not_found.status_code)
        assert result_single_resource_not_found.status_code == 404
        return url_single_resource_not_found

    @staticmethod
    def users():
        data_users = {"name": "morpheus","job": "leader"}
        result_users = Http_methods.post(url_users_create, data_users)
        print(result_users.text)
        print(result_users.status_code)
        assert result_users.status_code == 201
        return url_users_create

    @staticmethod
    def users_update():
        data_users_update = {"name": "morpheus","job": "zion resident"}
        result_users_update = Http_methods.put(url_users_update, data_users_update)
        print(result_users_update.text)
        print(result_users_update.status_code)
        assert result_users_update.status_code == 200
        return url_users_update

    @staticmethod
    def patch_users_update():
        data_patch_users_update = {"name": "morpheus","job": "zion resident"}
        result_patch_users_update = Http_methods.patch(url_users_update, data_patch_users_update)
