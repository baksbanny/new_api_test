from utils.https_method import Http_methods

url_list_users = "https://reqres.in/api/users?page=2"
url_single_users_not_found = "https://reqres.in/api/users/23"
url_list_resource = "https://reqres.in/api/unknown"
url_single_resource = "https://reqres.in/api/unknown/2"
url_single_resource_not_found = "https://reqres.in/api/unknown/23"
url_users_create = "https://reqres.in/api/users"
url_users_update = "https://reqres.in/api/users/2"
url_register_users = "https://reqres.in/api/register"
url_login_users = "https://reqres.in/api/login"
url_delay = "https://reqres.in/api/users?delay=3"

class Reqres_api():

    @staticmethod
    def list_users():
        result_list_users = Http_methods.get(url_list_users)
        print(result_list_users.text)
        print("Status_code: " + str(result_list_users.status_code))
        assert result_list_users.status_code == 200
        return url_list_users

    @staticmethod
    def single_users():
        result_single_users = Http_methods.get(url_users_update)
        print(result_single_users.text)
        print("Status_code: " + str(result_single_users.status_code))
        assert result_single_users.status_code == 200
        return url_users_update

    @staticmethod
    def single_users_not_fount():
        result_single_users_not_fount = Http_methods.get(url_single_users_not_found)
        print((result_single_users_not_fount.text))
        print("Status_code: " + str(result_single_users_not_fount.status_code))
        assert result_single_users_not_fount.status_code == 404
        return url_single_users_not_found

    @staticmethod
    def list_resource():
        result_list_resource = Http_methods.get(url_list_resource)
        print(result_list_resource.text)
        print("Status_code: " + str(result_list_resource.status_code))
        assert result_list_resource.status_code == 200
        return url_list_resource

    @staticmethod
    def single_resource():
        result_single_resource = Http_methods.get(url_single_resource)
        print(result_single_resource.text)
        print("Status_code: " + str(result_single_resource.status_code))
        assert result_single_resource.status_code == 200
        return  url_single_resource

    @staticmethod
    def single_resource_not_found():
        result_single_resource_not_found = Http_methods.get(url_single_resource_not_found)
        print(result_single_resource_not_found.text)
        print("Status_code: " + str(result_single_resource_not_found.status_code))
        assert result_single_resource_not_found.status_code == 404
        return url_single_resource_not_found

    @staticmethod
    def users():
        data_users = {"name": "morpheus","job": "leader"}
        result_users = Http_methods.post(url_users_create, data_users)
        print(result_users.text)
        print("Status_code: " + str(result_users.status_code))
        assert result_users.status_code == 201
        return url_users_create

    @staticmethod
    def users_update():
        data_users_update = {"name": "morpheus","job": "zion resident"}
        result_users_update = Http_methods.put(url_users_update, data_users_update)
        print(result_users_update.text)
        print("Status_code: " + str(result_users_update.status_code))
        assert result_users_update.status_code == 200
        return url_users_update

    @staticmethod
    def patch_users_update():
        data_patch_users_update = {"name": "morpheus","job": "zion resident"}
        result_patch_users_update = Http_methods.patch(url_users_update, data_patch_users_update)
        print(result_patch_users_update.text)
        print("Status_code: " + str(result_patch_users_update.status_code))
        assert result_patch_users_update.status_code == 200
        return url_users_update

    @staticmethod
    def delete_users():
        result_delete_users = Http_methods.delete(url_users_update)
        print(result_delete_users.text)
        print("Status_code: " + str(result_delete_users.status_code))
        assert result_delete_users.status_code == 204
        return url_users_update

    @staticmethod
    def register_users():
        data_register_users = {"email": "eve.holt@reqres.in","password": "pistol"}
        result_register_users = Http_methods.post(url_register_users, data_register_users)
        print(result_register_users.text)
        print("Status_code: " + str(result_register_users.status_code))
        assert  result_register_users.status_code == 200
        return url_register_users

    @staticmethod
    def register_users_unsuccessful():

        data_register_users_unsuccessful = {"email": "sydney@fife"}
        result_register_users_unsuccessful = Http_methods.post(url_register_users, data_register_users_unsuccessful)
        print(result_register_users_unsuccessful.text)
        print("Status_code: " + str(result_register_users_unsuccessful.status_code))
        assert result_register_users_unsuccessful.status_code == 400
        return url_register_users

    @staticmethod
    def login_users_successful():
        data_login_users_successful = {"email": "eve.holt@reqres.in","password": "cityslicka"}
        result_login_users_successful = Http_methods.post(url_login_users, data_login_users_successful)
        print(result_login_users_successful.text)
        print("Status_code: " + str(result_login_users_successful.status_code))
        assert result_login_users_successful.status_code == 200
        return url_register_users

    @staticmethod
    def login_users_unsuccessful():
        data_login_users_unsuccessful = {"email": "peter@klaven"}
        result_login_users_unsuccessful = Http_methods.post(url_login_users, data_login_users_unsuccessful)
        print(result_login_users_unsuccessful.text)
        print("Status_code: " + str(result_login_users_unsuccessful.status_code))
        assert result_login_users_unsuccessful.status_code == 400
        return url_register_users

    @staticmethod
    def delay():
        result_delay = Http_methods.get(url_delay)
        print(result_delay.text)
        print("Status_code: " + str(result_delay.status_code))
        assert result_delay.status_code == 200
        return url_register_users
