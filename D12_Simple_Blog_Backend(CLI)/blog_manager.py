import storage
from datetime import datetime

class BlogManager:
    def __init__(self, file_name="posts.json"):
        self.file_name = file_name
        self.posts = storage.load_post(self.file_name)

    def create_post(self):
        while True:
            post_id = input("Enter post id: ")
            if post_id.isdigit():
                post_id = int(post_id)
                if post_id in self.posts:
                    print("Id already exists")
                else:
                    break
            else:
                print("Post id should be a number")

        while True:
            title = input("Enter post title: ")
            if title.strip() == "":
                print("Title is blank, re-enter the title")
            else:
                break

        while True:
            content = input("Enter post content: ")
            if content.strip() == "":
                print("Content is empty, enter content to post")
            else:
                break

        while True:
            author = input("Enter author name: ")
            if author.strip() == "":
                print("Author cannot be blank")
            else:
                break

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.posts[post_id] = {
            "title": title,
            "content": content,
            "author": author,
            "timestamp": timestamp
        }

        storage.save_post(self.posts, self.file_name)
        print("Post created successfully!\n")

    def view_post(self):
        if not self.posts:
            print("-------Empty---------")
            return
        for post_id, data in self.posts.items():
            print(f"ID: {post_id}")
            print(f"Title: {data['title']}")
            print(f"Content: {data['content']}")
            print(f"Author: {data['author']}")
            print(f"Timestamp: {data['timestamp']}")
            print("-" * 30)

    def search_post(self):
        while True:
            ser_post = input("Enter post id to search: ")
            if ser_post.isdigit():
                ser_post = int(ser_post)
                break
            else:
                print("POST ID must be a number")
        
        if ser_post in self.posts:
            data = self.posts[ser_post]
            print(f"ID: {ser_post}")
            print(f"Title: {data['title']}")
            print(f"Content: {data['content']}")
            print(f"Author: {data['author']}")
            print(f"Timestamp: {data['timestamp']}")
            print("-" * 30)
        else:
            print("Post not found")

    def delete_post(self):
        while True:
            del_post = input("Enter post id to delete: ")
            if del_post.isdigit():
                del_post = int(del_post)
                break
            else:
                print("POST ID must be a number")
        
        if del_post in self.posts:
            data = self.posts[del_post]
            print("Post to be deleted:")
            print(f"ID: {del_post}")
            print(f"Title: {data['title']}")
            print(f"Content: {data['content']}")
            print(f"Author: {data['author']}")
            print(f"Timestamp: {data['timestamp']}")
            print("-" * 30)
            
            while True:
                conf = input("Confirm delete (yes/no): ").lower()
                if conf == "yes":
                    del self.posts[del_post]
                    storage.save_post(self.posts, self.file_name)
                    print("Post deleted successfully!\n")
                    break
                elif conf == "no":
                    print("Post not deleted\n")
                    break
                else:
                    print("Please choose (yes/no)")
        else:
            print("Post not found\n")
