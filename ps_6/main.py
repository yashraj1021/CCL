import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        nterms = 8
        n1 = 0
        n2 = 1
        count = 0

        while count<nterms:
            #print(n1)
            self.response.write("%d, " %n1)
            nth = n1+n2
            n1 = n2
            n2 = nth
            count +=1

app = webapp2.WSGIApplication(
    [("/", MainPage)],
    debug = True
)