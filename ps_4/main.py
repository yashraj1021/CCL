import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        for i in range (1,11):
            num = 5*i
            self.response.write("5 x %d = "%i)
            self.response.write("%d<br>" %num)

app = webapp2.WSGIApplication(
    [("/", MainPage)],
    debug= True
)
