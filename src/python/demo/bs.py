from iop import BusinessService
from iop_rest.messages import RESTRequest
from generated.models import Pet, Category, Tag
import traceback

class PetstoreService(BusinessService):
    @staticmethod
    def get_adapter_type():
        return "Ens.InboundAdapter"

    def on_process_input(self, message_input):
        try:
            pet = Pet(
                id=1,
                name="Robert",
                category=Category(
                    id=1,
                    name="Doggo",
                ),
                photoUrls=[],
                tags=[
                    Tag(
                        id=1,
                        name="dog",
                    )
                ],
                status="available",
            )
            response: Pet = self.send_request_sync('PetstoreOperation', RESTRequest.create('add_pet', pet))
            # do something with response...
            self.log_info(response.name)
            response = self.send_request_sync('PetstoreOperation', RESTRequest.create('get_pet_by_id', 1))
            self.log_info(response.name)
            # response: list[Pet] = self.send_request_sync('PetstoreOperation', RESTRequest.create('find_pets_by_status'))
        except Exception as e:
            self.log_error("".join(traceback.format_exception(e)))
