from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs

class Moodify:
    def __init__(self):
        # Song data for different moods
        self.mood_songs = {
            1: [ {'song': 'Chaleya', 'link': 'https://open.spotify.com/track/4nc6XiUze2Yh7wFueGOPv7?si=XJC1K0FASk6Sod-hSCSUKA'},
                 {'song': 'Tum hi ho bandhu','link': 'https://open.spotify.com/track/7H3mfOvtPNA8YDF3EdKy0L?si=5YlGzOrtT5GzBUMICNUVkA'},
                 {'song': 'Love you zindagi','link': 'https://open.spotify.com/track/6k3XXCE1ZzwevQlxf8dNaw?si=zhd8KryjRKqxn4wF6Cfh0w'},
                 {'song': 'Subhanaallah','link': 'https://open.spotify.com/track/0GQngE2rOYvlKwEQjTAsP8?si=cLLV_uJLTkGkN_mvfs-WAA'},
                 {'song': 'Iktara' , 'link':' https://open.spotify.com/track/0RJ7HhnQxJEOpGC5Htmez4?si=IIEVSY0bRTS5izqsdUF1FQ'}
                
                ],
   
            2: [ {'song': 'Roke Na Ruke Naina', 'link': 'https://open.spotify.com/track/0MZe7mevQdrHu25kXAICLA?si=3gWgZlaJS6Kc5V_dfz01zQ'},
                 {'song': 'Tu jaane na','link':'https://open.spotify.com/track/4iFPsNzNV7V9KJgcOX7TEO?si=AgMbq0GWRjCR_ngKh4G15g'},
                 {'song': 'Bekhayali','link':'https://open.spotify.com/track/1feANd8EfcDP5UqSvbheM3?si=RBpHDcefSVycNKYwLStB4A'},
                 {'song': 'Man Bharryaa','link':'https://open.spotify.com/track/3jf5303mzzJ96O8xFTcEn4?si=Bc8e6Bh7S6-7EkG8qnQelA'},
                 {'song': 'Kabhi Alvida na Kehna' , 'link':'https://open.spotify.com/track/4uXShFWajd1PTQzlW3P4jj?si=J8smgEx5QmCFG8YQTWDorQ'}
                
                ],

            3: [ {'song': 'Self Made', 'link': 'https://open.spotify.com/track/5lNQ2M1yJ1HAQGHgUfLlY3?si=AO7GCrfAS6eGSVNLU3rJ4w'},
                 {'song': 'Anjanichya Suta ','link':'https://open.spotify.com/track/2Pu4GmghoLQXB9dRpCGPqT?si=OxYHnh1xSYWOhaiDMRtp5A'},
                 {'song': 'Sarkar','link':'https://open.spotify.com/track/60suOlM8VpTVITPFeqth8r?si=_pkqIBEXTY-9Bb0ZWWQaLQ'},
                 {'song': 'Lehra Do','link':'https://open.spotify.com/track/6EcDkNazXZtD8hMWAa43J6?si=q3BCriDPR5qzAfVTX_bTsg '},
                 {'song': 'Payee Fufata' , 'link':'https://open.spotify.com/track/7AvfiB7Paq388ecxkoq5Mf?si=QkgVozSlToq8sIJNzbrYiQ'}
                
                ],

            4: [
                {'song': 'Teri baaton mein aisa uljha jiya', 'link': 'https://open.spotify.com/track/6IR6mzRO60hnMjNoq8rCPE?si=5SZHVlElSEWmDVA6y9sOSA'},
                {'song': 'Gallan Goodiyan', 'link': 'https://open.spotify.com/track/7hNYvX0qAKrxtVr1jGDmvR?si=59DUlcOWSV-FbCLQ45Ue5Q'},
                {'song': 'Zingaat', 'link': 'https://open.spotify.com/track/3TysRQuZRfhXZ6P8T09YdO?si=ohmRgW96R_WUwQB4YKzGKg'},
                {'song': 'The Jawaani song', 'link': ' https://open.spotify.com/track/7KDFmblffwXCVeLnVE66lu?si=CEXSDDX3TKO0y_PGNqN9rA'},
                {'song': 'Badtameez Dil', 'link': ' https://open.spotify.com/track/4eu27jAU2bbnyHUC3G75U8?si=-72Mpn1US8WRj9hGwIDMRg'}
               ],

               
            5: [ {'song': 'Shivba Raja from sher-shivraj', 'link': 'https://open.spotify.com/track/2nUvk6Q1ZZCugxYci1eMgt?si=pGtVa55YRO-mDHPk4Wprpw'},
                 {'song': 'Soorma Anthem','link':'https://open.spotify.com/wrapped/share/share-ab0b9700d67f4b38a34210f61b9a3c1f?si=CQB42vPXRTedtC9N9XJgIw&track-id=4fzh5t4XkMP7FNLpq8132a&pi=lYLy76tzSZOY'},
                 {'song': 'Kar Har Maidaan Fateh','link':'https://open.spotify.com/wrapped/share/share-4c99c55462c74026a30a7c10d0483aae?si=Dv7CESMARzajP85WPFrcCQ&track-id=3FHl1QYu76zguwjqhqcglX&pi=ZGMOo4VFTomvR'},
                 {'song': 'Zinda','link':'https://open.spotify.com/track/7vZz8oJ5qAqB9MghufRK5k?si=ux-47j1fRxCoIkmY0HqwNA'},
                 {'song': 'Dangal' , 'link':'https://open.spotify.com/track/7AvfiB7Paq388ecxkoq5Mf?si=QkgVozSlToq8sIJNzbrYiQ'}
                
                ] 
        }

    def get_song_recommendations(self, mood_number):
        # Retrieve song recommendations based on the mood number
        if mood_number in self.mood_songs:
            return self.mood_songs[mood_number]
        else:
            return None

class SongRequestHandler(BaseHTTPRequestHandler):
    moodify = Moodify()  # Create an instance of Moodify

    def do_GET(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == '/recommend':
            query = parse_qs(parsed_path.query)
            if 'mood' in query:
                try:
                    mood_number = int(query['mood'][0])
                except (ValueError, KeyError):
                    self.send_response(400)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "Invalid mood number provided."}).encode())
                    return
                
                songs = self.moodify.get_song_recommendations(mood_number)
                if songs:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"mood": mood_number, "songs": songs}).encode())
                else:
                    self.send_response(404)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "No song recommendations found for this mood."}).encode())
            else:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": "No mood parameter provided."}).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Endpoint not found."}).encode())

def run(server_class=HTTPServer, handler_class=SongRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()

