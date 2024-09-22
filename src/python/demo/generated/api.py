# generated by REST Client Framework for IOP:
#   timestamp: 2024-09-22T00:44:33.686436

from iop_rest.api import BaseClientREST
from uplink.arguments import *
from uplink.commands import *
from uplink.decorators import *
from uplink import returns
from .models import *

@returns.json
@headers({
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Charset": "utf-8",
})
class PetstoreClient(BaseClientREST):
    """
    Swagger Petstore - OpenAPI 3.0
    """

    @json
    @put('pet')
    def update_pet(self, body: Body(type=Pet)) -> Pet: 
        """
        Update an existing pet
        """
        pass

    @json
    @post('pet')
    def add_pet(self, body: Body(type=Pet)) -> Pet:
        """
        Add a new pet to the store
        """
        pass

    @json
    @get('pet/findByStatus')
    def find_pets_by_status(self, status: Query("status", type=str)) -> list[Pet]: 
        """
        Finds Pets by status
        """
        pass

    @json
    @get('pet/findByTags')
    def find_pets_by_tags(self, tags: Query("tags", type=list[str])) -> list[Pet]:
        """
        Finds Pets by tags
        """
        pass

    @json
    @get('pet/{petId}')
    def get_pet_by_id(self, pet_id: Path("petId", type=int)) -> Pet:
        """
        Find pet by ID
        """
        pass

    @json
    @post('pet/{petId}')
    def update_pet_with_form(self, pet_id: Path("petId", type=int), name: Query("name", type=str), status: Query("status", type=str)):
        """
        Updates a pet in the store with form data
        """
        pass

    @json
    @delete('pet/{petId}')
    def delete_pet(self, api_key: Header("api_key", type=str), pet_id: Path("petId", type=int)):
        """
        Deletes a pet
        """
        pass

    @json
    @post('pet/{petId}/uploadImage')
    def upload_file(self, pet_id: Path("petId", type=int), additional_metadata: Query("additionalMetadata", type=str), body: Body(type=str)) -> ApiResponse:
        """
        uploads an image
        """
        pass

    @json
    @get('store/inventory')
    def get_inventory(self) -> dict:
        """
        Returns pet inventories by status
        """
        pass

    @json
    @post('store/order')
    def place_order(self, body: Body(type=Order)) -> Order:
        """
        Place an order for a pet
        """
        pass

    @json
    @get('store/order/{orderId}')
    def get_order_by_id(self, order_id: Path("orderId", type=int)) -> Order:
        """
        Find purchase order by ID
        """
        pass

    @json
    @delete('store/order/{orderId}')
    def delete_order(self, order_id: Path("orderId", type=int)):
        """
        Delete purchase order by ID
        """
        pass

    @json
    @post('user')
    def create_user(self, body: Body(type=User)):
        """
        Create user
        """
        pass

    @json
    @post('user/createWithList')
    def create_users_with_list_input(self, body: Body(type=list[User])) -> User:
        """
        Creates list of users with given input array
        """
        pass

    @json
    @get('user/login')
    def login_user(self, username: Query("username", type=str), password: Query("password", type=str)) -> str:
        """
        Logs user into the system
        """
        pass

    @json
    @get('user/logout')
    def logout_user(self):
        """
        Logs out current logged in user session
        """
        pass

    @json
    @get('user/{username}')
    def get_user_by_name(self, username: Path("username", type=str)) -> User:
        """
        Get user by user name
        """
        pass

    @json
    @put('user/{username}')
    def update_user(self, username: Path("username", type=str), body: Body(type=User)):
        """
        Update user
        """
        pass

    @json
    @delete('user/{username}')
    def delete_user(self, username: Path("username", type=str)):
        """
        Delete user
        """
        pass

