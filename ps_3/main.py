import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        for i in range (1,11):
            self.response.write("Seat Number: 58738<br>")
            self.response.write("Dept : IT<br>")

app = webapp2.WSGIApplication(
    [("/", MainPage)],
    debug= True
)