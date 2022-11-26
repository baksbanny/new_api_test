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