import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        for i in range (1,11):
            x = 10*i
            self.response.write("10 x %d =" %i)
            self.response.write("%d <br>" %x)

app = webapp2.WSGIApplication(
    [("/", MainPage)],
    debug= True
)