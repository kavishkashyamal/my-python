import json
import datetime

file_path = r"posts.json"
with open(file_path,'r') as posts_list:
    posts = json.load(posts_list)



'''Create a post'''
def create_a_post():
    title = input("Enter your post title : ")
    description = input("Enter post content : ")
    date = datetime.datetime.now().strftime("%Y.%m.%d")
    admin = 'admin'


    with open(file_path, 'r') as f:
        print("✅ Post created successfully!")
    
    posts = view_post_lists()
    posts.append({
        "title": title,
        "description":description,
        "date":date,
        "author":admin
    })
'''Get a list of posts'''
def view_post_lists():
    for post in posts:
        print(f"{post['number']}. {post["title"]}")


while True:

    print("___Admin Menu___")
    print("You can ->")
    print("1. Create a post (1)")
    print("2. Get a list of posts (2)")
    print("Type 'quit' to exit")
    #print("3. View contents (3)")

    admin_input = input("---> ").lower()

    if admin_input == '1':
        create_a_post()
    elif admin_input == '2':
        view_post_lists()
    elif admin_input == 'quit':
        print("Goodbye!")
        break
    else:
        print("❌ Invalid choice. Try again.")


def save_posts(post):
    with open(file_path,'w') as f:
        json.dump(post,f,indent=4)

