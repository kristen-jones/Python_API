#API Constant is a class which contains all the endpoints
#Keep the URLs

class APIConstants(object):

    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    #Concepts
    #Static Method -> Which can be called by w/o the object directly by using class you can call it

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

    #Update, PUT, PATCH, DELETE - bookingID
    def url_patch_put_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)
