import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# This is a dummy database file name
DB_FILE = 'students.json'

class StudentAPI(BaseHTTPRequestHandler):
    
    def do_GET(self):
        """This function automatically triggers when a GET request hits the server."""
        print("Someone just sent a GET request!")
        
        # 1. We must tell the client the request was successful (HTTP Status 200 OK)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        try:
            with open(DB_FILE, "r") as file:
                file_data = file.read()  # Fixed: Added parentheses ()
                self.wfile.write(file_data.encode('utf-8'))
                
        except FileNotFoundError:
            # Fixed: These lines are now indented 4 spaces inside the except block
            error_message = json.dumps({"message": "File not found"})  # Fixed: Changed dump to dumps
            self.wfile.write(error_message.encode('utf-8'))
    def do_POST(self):
        print("Someone just sent a POST request!")
        
        # 1. Figure out how many bytes of data the client sent
        content_length = int(self.headers['Content-Length'])
        
        # 2. Read those exact bytes from the network stream
        raw_body = self.rfile.read(content_length)
        
        # 3. Translate bytes back to a Python string and parse into a dictionary
        new_student_string = raw_body.decode('utf-8')
        new_student_dict = json.loads(new_student_string)
        
        # ---------------------------------------------------------
        # YOUR MISSION: 
        # 1. Open DB_FILE in read mode, use json.load() to get the current list.
        # 2. Append new_student_dict to that list.
        # 3. Re-open DB_FILE in write mode, use json.dump() to save the updated list.
        # ---------------------------------------------------------
        
        # (Write your JSON file handling code here!)
        with open(DB_FILE, "r") as file:
            student_list = json.load(file)
            student_list.append(new_student_dict)
        with open(DB_FILE, "w") as file:
            json.dump(student_list, file)
        # 4. Tell the client the data was successfully saved (HTTP 201 Created)
        self.send_response(201)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Send a success message back to the client
        success_msg = json.dumps({"message": "Student added successfully!"})
        self.wfile.write(success_msg.encode('utf-8'))


# This block starts the server and keeps it running forever
if __name__ == '__main__':
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, StudentAPI)
    print("Zero-Magic API Server running on http://localhost:8000")
    httpd.serve_forever()