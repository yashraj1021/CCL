import webapp2

class MainPage(webapp2.RequestHandler) :
    def get(self):
        for i in range (1,6):
            self.response.write("Name: Yashraj Thakur<br>")
            self.response.write("\nSeat Number: 58738<br>")
            self.response.write("\nDept : IT<br>")
            

app = webapp2.WSGIApplication(
    [("/",MainPage)],
    debug=True
)

