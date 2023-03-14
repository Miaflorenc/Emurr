from .models import Booking


class BookingRepository:

    def all_booking(self):
        return Booking.objects.all()

    def Booking_by_pk(self, pk):
        return Booking.objects.all().filter(client=pk)

    def Delete_Booking(self, pk):
        return Booking.objects.get(id=pk).delete()
