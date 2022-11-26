from requests import Response
from utils.api import Reqres_api


class Test_api_users():

    def test_new_list_users(self):
        print("Method GET")
        result_get_list_users: Response = Reqres_api.list_users()

    def test_new_single_users(self):
        print("Method GET")
        result_get_single_users: Response = Reqres_api.single_users()

    def test_new_single_users_not_fount(self):
        print("Method GET")
        result_get_single_users_not_fount: Response = Reqres_api.single_users_not_fount()

    def test_new_list_resource(self):
        print("Method GET")
        result_get_list_resource: Response = Reqres_api.list_resource()

    def test_new_single_resource(self):
        print("Method GET")
        result_get_single_resource: Response = Reqres_api.single_resource()

    def test_new_single_resource_not_found(self):
        print("Method GET")
        result_get_single_resource_not_found: Response = Reqres_api.single_resource_not_found()

    def test_new_users(self):
        print("Method POST")
        result_post_users: Response = Reqres_api.users()

    def test_new_users_update(self):
        print("Method PUT")
        result_put_users_update: Response = Reqres_api.users_update()

    def test_new_patch_users_update(self):
        print("Method PATCH")
        result_patch_users_update: Response = Reqres_api.patch_users_update()

    def test_new_users_delete(self):
        print("Method DELETE")
        result_delete_users: Response = Reqres_api.delete_users()

    def test_new_register_users(self):
        print("Method POST")
        result_register_users: Response = Reqres_api.register_users()

    def test_new_register_users_unsuccessful(self):
        print("Method POST")
        result_register_users_unsuccessful: Response = Reqres_api.register_users_unsuccessful()

    def test_new_login_users_successful(self):
        print("Method POST")
        result_login_users_successful: Response = Reqres_api.login_users_successful()

    def test_new_login_users_unsuccessful(self):
        print("Method POST")
        result_login_users_unsuccessful: Response = Reqres_api.login_users_unsuccessful()

    def test_new_delay(self):
        print("Method GET")
        result_delay: Response = Reqres_api.delay()
